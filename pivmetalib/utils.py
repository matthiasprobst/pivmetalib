import pathlib

import appdirs
import requests


def get_cache_dir() -> pathlib.Path:
    """Get the cache directory and create it if it does not exist"""
    cache_dir = pathlib.Path(appdirs.user_cache_dir('pivmetalib'))
    if not cache_dir.exists():
        cache_dir.mkdir(parents=True)
    return cache_dir


def download_file(url,
                  dest_filename,
                  known_hash=None,
                  overwrite_existing: bool = False) -> pathlib.Path:
    """Download a file from a URL and check its hash
    
    Parameter
    ---------
    url: str
        The URL of the file to download
    dest_filename: str or pathlib.Path
        The destination filename
    known_hash: str
        The expected hash of the file
    overwrite_existing: bool
        Whether to overwrite an existing file
    
    Returns
    -------
    pathlib.Path
        The path to the downloaded file
    """
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        content = response.content

        # Calculate the hash of the downloaded content
        if known_hash:
            import hashlib
            calculated_hash = hashlib.sha256(content).hexdigest()
            if not calculated_hash == known_hash:
                raise ValueError('File does not match the expected has')

        # Save the content to a file
        dest_filename = pathlib.Path(dest_filename)
        dest_parent = dest_filename.parent
        if not dest_parent.exists():
            dest_parent.mkdir(parents=True)
        if dest_filename.exists() and overwrite_existing:
            dest_filename.unlink()
        elif dest_filename.exists() and not overwrite_existing:
            raise FileExistsError(f'File {dest_filename} already exists and overwrite_existing is set to False.')
        with open(dest_filename, "wb") as f:
            f.write(content)

        return dest_filename
    raise RuntimeError(f'Failed to download the file from {url}')
