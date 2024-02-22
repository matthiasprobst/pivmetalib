import appdirs
import pathlib
import requests


def get_cache_dir() -> pathlib.Path:
    """Get the cache directory and create it if it does not exist"""
    cache_dir = pathlib.Path(appdirs.user_cache_dir('pivmetalib'))
    if not cache_dir.exists():
        cache_dir.mkdir(parents=True)
    return cache_dir


def download_file(url,
                  dest_filename=None,
                  known_hash=None,
                  overwrite_existing: bool = False,
                  show_pbar: bool = False) -> pathlib.Path:
    """Download a file from a URL and check its hash
    
    Parameter
    ---------
    url: str
        The URL of the file to download
    dest_filename: str or pathlib.Path =None
        The destination filename. If None, the filename is taken from the URL
    known_hash: str
        The expected hash of the file
    overwrite_existing: bool
        Whether to overwrite an existing file
    show_pbar: bool
        Whether to show a progress bar
    
    Returns
    -------
    pathlib.Path
        The path to the downloaded file

    Raises
    ------
    HTTPError if the request is not successful
    ValueError if the hash of the downloaded file does not match the expected hash
    """
    response = requests.get(url, stream=True)
    if not response.ok:
        response.raise_for_status()

    content = response.content

    # Calculate the hash of the downloaded content
    if known_hash:
        import hashlib
        calculated_hash = hashlib.sha256(content).hexdigest()
        if not calculated_hash == known_hash:
            raise ValueError('File does not match the expected has')

    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024

    # Save the content to a file
    if dest_filename is None:
        from uuid import uuid4
        dest_filename = pathlib.Path(f"{uuid4()}.tmp")
    else:
        dest_filename = pathlib.Path(dest_filename)
    dest_parent = dest_filename.parent
    if not dest_parent.exists():
        dest_parent.mkdir(parents=True)
    if dest_filename.exists() and overwrite_existing:
        dest_filename.unlink()
    elif dest_filename.exists() and not overwrite_existing:
        raise FileExistsError(f'File {dest_filename} already exists and overwrite_existing is set to False.')

    if show_pbar:
        try:
            from tqdm import tqdm
        except ImportError:
            raise ImportError('tqdm is required to show progress bar. Please install it or set show_pbar to False.')
        with tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
            with open(dest_filename, "wb") as f:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    f.write(data)
    else:
        with open(dest_filename, "wb") as f:
            f.write(content)

    return dest_filename
