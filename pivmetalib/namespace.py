from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class PIVMETA(DefinedNamespace):
    # uri = "https://matthiasprobst.github.io/pivmeta#"
    # Generated with pivmetalib
    BackgroundImageGeneration: URIRef  # ['background image generation']
    BackgroundSubtractionMethod: URIRef  # ['background subtraction']
    Camera: URIRef  # ['camera']
    CorrelationMethod: URIRef  # ['correlation method']
    DigitalCamera: URIRef  # ['digital camera']
    ExperimentalPIVSetup: URIRef  # ['experimental PIV setup']
    FlagStatistics: URIRef  # ['flag statistics']
    FlagVariable: URIRef  # ['flag variable']
    ImageDewarping: URIRef  # ['image dewarping']
    ImageFiltering: URIRef  # ['image filtering']
    ImageManipulationMethod: URIRef  # ['image manipulation method']
    ImageRotation: URIRef  # ['image rotation']
    InterrogationMethod: URIRef  # ['interrogation method']
    Laser: URIRef  # ['laser']
    Lens: URIRef  # ['lens']
    LensSystem: URIRef  # ['lens system']
    LightSource: URIRef  # ['light source']
    MaskGeneration: URIRef  # ['mask generation']
    Multigrid: URIRef  # ['multigrid']
    Multipass: URIRef  # ['multipass']
    Objective: URIRef  # ['objective']
    OpticSensor: URIRef  # ['optic sensor']
    OpticalComponent: URIRef  # ['optical component']
    OutlierDetectionMethod: URIRef  # ['outlier detection method']
    outlierReplacementScheme: URIRef  # ['outlier replacement scheme']
    PIVAnalysis: URIRef  # ['PIV analysis']
    PIVDataset: URIRef  # ['PIV dataset']
    PIVDistribution: URIRef  # ['PIV distribution']
    PIVEvaluation: URIRef  # ['PIV evaluation']
    PIVImageDistribution: URIRef  # ['PIV image distribution']
    PIVMaskDistribution: URIRef  # ['PIV mask distribution']
    PIVParticle: URIRef  # ['PIV particle']
    PIVPostProcessing: URIRef  # ['PIV post processing']
    PIVPreProcessing: URIRef  # ['Piv pre processing']
    PIVRecording: URIRef  # ['PIV recording']
    PIVResultDistribution: URIRef  # ['PIV result distribution']
    PIVSetup: URIRef  # ['PIV setup']
    PIVSoftware: URIRef  # ['PIV software']
    PIVValidation: URIRef  # ['PIV validation']
    PeakSearchMethod: URIRef  # ['peak search method']
    Singlepass: URIRef  # ['singlepass']
    SyntheticPIVParticle: URIRef  # ['synthetic PIV particle']
    TemporalVariable: URIRef  # ['temporal variable']
    VirtualCamera: URIRef  # ['virtual camera']
    VirtualLaser: URIRef  # ['virtual laser']
    VirtualPIVSetup: URIRef  # ['virtual PIV experiment']
    VirtualTool: URIRef  # ['virtual tool']
    WindowWeightingFunction: URIRef  # ['window weighting function']
    flag: URIRef  # ['flag']
    flagIn: URIRef  # ['flag in']
    hasWindowWeightingFunction: URIRef  # ['has window weighting function']
    manufacturer: URIRef  # ['manufacturer']
    pivImageType: URIRef  # ['piv image type']
    filenamePattern: URIRef  # ['filename pattern']
    fnumber: URIRef  # ['fnumber']
    hasFlagMeaning: URIRef  # ['has flag meaning']
    hasFlagValue: URIRef  # ['has flag value']
    imageBitDepth: URIRef  # ['bit depth']
    numberOfRecords: URIRef  # ['number of records']
    timeFormat: URIRef  # ['time format']
    BlackmanWindow: URIRef  # ['blackman window']
    DEHS: URIRef  # ['DEHS']
    ExperimentalImage: URIRef  # ['experimental image']
    FlagActive: URIRef  # ['active']
    GaussianWindow: URIRef  # ['Gaussian window']
    HannWindow: URIRef  # ['Hann window']
    Interpolation: URIRef  # ['interpolation']
    LeftRightFlip: URIRef  # ['left right flip']
    MilliM_PER_PIXEL: URIRef  # ['millimeter per pixel']
    PER_PIXEL: URIRef  # ['per pixel']
    PIVData: URIRef  # ['PIV data']
    PIVImage: URIRef  # ['PIV image']
    ParticleImageVelocimetry: URIRef  # ['Particle Image Velocimetry']
    ParticleTrackingVelocimetry: URIRef  # ['Particle Tracking Velocimetry']
    ReEvaluateWithLargerSample: URIRef  # ['re-evaluate with larger sample']
    SpatialResolution: URIRef  # ['spatial resolution']
    SplitImage: URIRef  # ['split image']
    SquareWindow: URIRef  # ['square window']
    SyntheticImage: URIRef  # ['synthetic image']
    TopBottomFlip: URIRef  # ['top bottom flip']
    TryLowerOrderPeaks: URIRef  # ['try lower order peaks']
    TukeyWindow: URIRef  # ['Tukey window']
    microPIV: URIRef  # ['Micro PIV']

    _NS = Namespace("https://matthiasprobst.github.io/pivmeta#")


setattr(PIVMETA, "background_image_generation", PIVMETA.BackgroundImageGeneration)
setattr(PIVMETA, "background_subtraction", PIVMETA.BackgroundSubtractionMethod)
setattr(PIVMETA, "camera", PIVMETA.Camera)
setattr(PIVMETA, "correlation_method", PIVMETA.CorrelationMethod)
setattr(PIVMETA, "digital_camera", PIVMETA.DigitalCamera)
setattr(PIVMETA, "experimental_PIV_setup", PIVMETA.ExperimentalPIVSetup)
setattr(PIVMETA, "flag_statistics", PIVMETA.FlagStatistics)
setattr(PIVMETA, "flag_variable", PIVMETA.FlagVariable)
setattr(PIVMETA, "image_dewarping", PIVMETA.ImageDewarping)
setattr(PIVMETA, "image_filtering", PIVMETA.ImageFiltering)
setattr(PIVMETA, "image_manipulation_method", PIVMETA.ImageManipulationMethod)
setattr(PIVMETA, "image_rotation", PIVMETA.ImageRotation)
setattr(PIVMETA, "interrogation_method", PIVMETA.InterrogationMethod)
setattr(PIVMETA, "laser", PIVMETA.Laser)
setattr(PIVMETA, "lens", PIVMETA.Lens)
setattr(PIVMETA, "lens_system", PIVMETA.LensSystem)
setattr(PIVMETA, "light_source", PIVMETA.LightSource)
setattr(PIVMETA, "mask_generation", PIVMETA.MaskGeneration)
setattr(PIVMETA, "multigrid", PIVMETA.Multigrid)
setattr(PIVMETA, "multipass", PIVMETA.Multipass)
setattr(PIVMETA, "objective", PIVMETA.Objective)
setattr(PIVMETA, "optic_sensor", PIVMETA.OpticSensor)
setattr(PIVMETA, "optical_component", PIVMETA.OpticalComponent)
setattr(PIVMETA, "outlier_detection_method", PIVMETA.OutlierDetectionMethod)
setattr(PIVMETA, "outlier_replacement_scheme", PIVMETA.outlierReplacementScheme)
setattr(PIVMETA, "PIV_analysis", PIVMETA.PIVAnalysis)
setattr(PIVMETA, "PIV_dataset", PIVMETA.PIVDataset)
setattr(PIVMETA, "PIV_distribution", PIVMETA.PIVDistribution)
setattr(PIVMETA, "PIV_evaluation", PIVMETA.PIVEvaluation)
setattr(PIVMETA, "PIV_image_distribution", PIVMETA.PIVImageDistribution)
setattr(PIVMETA, "PIV_mask_distribution", PIVMETA.PIVMaskDistribution)
setattr(PIVMETA, "PIV_particle", PIVMETA.PIVParticle)
setattr(PIVMETA, "PIV_post_processing", PIVMETA.PIVPostProcessing)
setattr(PIVMETA, "Piv_pre_processing", PIVMETA.PIVPreProcessing)
setattr(PIVMETA, "PIV_recording", PIVMETA.PIVRecording)
setattr(PIVMETA, "PIV_result_distribution", PIVMETA.PIVResultDistribution)
setattr(PIVMETA, "PIV_setup", PIVMETA.PIVSetup)
setattr(PIVMETA, "PIV_software", PIVMETA.PIVSoftware)
setattr(PIVMETA, "PIV_validation", PIVMETA.PIVValidation)
setattr(PIVMETA, "peak_search_method", PIVMETA.PeakSearchMethod)
setattr(PIVMETA, "singlepass", PIVMETA.Singlepass)
setattr(PIVMETA, "synthetic_PIV_particle", PIVMETA.SyntheticPIVParticle)
setattr(PIVMETA, "temporal_variable", PIVMETA.TemporalVariable)
setattr(PIVMETA, "virtual_camera", PIVMETA.VirtualCamera)
setattr(PIVMETA, "virtual_laser", PIVMETA.VirtualLaser)
setattr(PIVMETA, "virtual_PIV_experiment", PIVMETA.VirtualPIVSetup)
setattr(PIVMETA, "virtual_tool", PIVMETA.VirtualTool)
setattr(PIVMETA, "window_weighting_function", PIVMETA.WindowWeightingFunction)
setattr(PIVMETA, "flag", PIVMETA.flag)
setattr(PIVMETA, "flag_in", PIVMETA.flagIn)
setattr(PIVMETA, "has_window_weighting_function", PIVMETA.hasWindowWeightingFunction)
setattr(PIVMETA, "manufacturer", PIVMETA.manufacturer)
setattr(PIVMETA, "piv_image_type", PIVMETA.pivImageType)
setattr(PIVMETA, "filename_pattern", PIVMETA.filenamePattern)
setattr(PIVMETA, "fnumber", PIVMETA.fnumber)
setattr(PIVMETA, "has_flag_meaning", PIVMETA.hasFlagMeaning)
setattr(PIVMETA, "has_flag_value", PIVMETA.hasFlagValue)
setattr(PIVMETA, "bit_depth", PIVMETA.imageBitDepth)
setattr(PIVMETA, "number_of_records", PIVMETA.numberOfRecords)
setattr(PIVMETA, "time_format", PIVMETA.timeFormat)
setattr(PIVMETA, "blackman_window", PIVMETA.BlackmanWindow)
setattr(PIVMETA, "DEHS", PIVMETA.DEHS)
setattr(PIVMETA, "experimental_image", PIVMETA.ExperimentalImage)
setattr(PIVMETA, "active", PIVMETA.FlagActive)
setattr(PIVMETA, "Gaussian_window", PIVMETA.GaussianWindow)
setattr(PIVMETA, "Hann_window", PIVMETA.HannWindow)
setattr(PIVMETA, "interpolation", PIVMETA.Interpolation)
setattr(PIVMETA, "left_right_flip", PIVMETA.LeftRightFlip)
setattr(PIVMETA, "millimeter_per_pixel", PIVMETA.MilliM_PER_PIXEL)
setattr(PIVMETA, "per_pixel", PIVMETA.PER_PIXEL)
setattr(PIVMETA, "PIV_data", PIVMETA.PIVData)
setattr(PIVMETA, "PIV_image", PIVMETA.PIVImage)
setattr(PIVMETA, "Particle_Image_Velocimetry", PIVMETA.ParticleImageVelocimetry)
setattr(PIVMETA, "Particle_Tracking_Velocimetry", PIVMETA.ParticleTrackingVelocimetry)
setattr(PIVMETA, "re-evaluate_with_larger_sample", PIVMETA.ReEvaluateWithLargerSample)
setattr(PIVMETA, "spatial_resolution", PIVMETA.SpatialResolution)
setattr(PIVMETA, "split_image", PIVMETA.SplitImage)
setattr(PIVMETA, "square_window", PIVMETA.SquareWindow)
setattr(PIVMETA, "synthetic_image", PIVMETA.SyntheticImage)
setattr(PIVMETA, "top_bottom_flip", PIVMETA.TopBottomFlip)
setattr(PIVMETA, "try_lower_order_peaks", PIVMETA.TryLowerOrderPeaks)
setattr(PIVMETA, "Tukey_window", PIVMETA.TukeyWindow)
setattr(PIVMETA, "Micro_PIV", PIVMETA.microPIV)