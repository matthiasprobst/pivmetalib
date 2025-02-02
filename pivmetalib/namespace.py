from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class PIVMETA(DefinedNamespace):
    # uri = "https://matthiasprobst.github.io/pivmeta#"
    # Generated with pivmetalib
    BackgroundSubtractionMethod: URIRef  # ['background subtraction method']
    Camera: URIRef  # ['camera']
    CorrelationMethod: URIRef  # ['correlation method']
    DataType: URIRef  # ['piv data type']
    DigitalCamera: URIRef  # ['digital camera']
    ExperimentalPIVSetup: URIRef  # ['experimental PIV setup']
    FlagStatistics: URIRef  # ['flag statistics']
    FlagVariable: URIRef  # ['flag variable']
    ImageManipulationMethod: URIRef  # ['image manipulation method']
    InterrogationMethod: URIRef  # ['interrogation method']
    Laser: URIRef  # ['laser']
    Lens: URIRef  # ['lens']
    LensSystem: URIRef  # ['lens system']
    LightSource: URIRef  # ['light source']
    MinimumIntensityBackgroundSubtractionMethod: URIRef  # ['minimum intensity background subtraction method']
    Multigrid: URIRef  # ['multigrid']
    Multipass: URIRef  # ['multipass']
    Objective: URIRef  # ['objective']
    OpticSensor: URIRef  # ['optic sensor']
    OpticalComponent: URIRef  # ['optical component']
    OutlierDetectionMethod: URIRef  # ['outlier detection method']
    outlierReplacementScheme: URIRef  # ['outlier replacement scheme']
    PIVAnalysis: URIRef  # ['PIV Analysis']
    PIVBackgroundGeneration: URIRef  # ['PIV background generation']
    PIVCalibration: URIRef  # ['PIV calibration']
    PIVDataset: URIRef  # ['PIV dataset']
    PIVDistribution: URIRef  # ['PIV distribution']
    PIVEvaluation: URIRef  # ['PIV evaluation']
    PIVMaskGeneration: URIRef  # ['PIV mask generation']
    PIVParticle: URIRef  # ['PIV particle']
    PIVPostProcessing: URIRef  # ['PIV post processing']
    PIVPreProcessing: URIRef  # ['PIV pre processing']
    PIVProcessingStep: URIRef  # ['PIV Processing step']
    PIVRecording: URIRef  # ['PIV recording']
    PIVSetup: URIRef  # ['PIV setup']
    PIVSoftware: URIRef  # ['PIV software']
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
    hasDataType: URIRef  # ['has PIV data type']
    hasMetric: URIRef  # ['has metric']
    hasWindowWeightingFunction: URIRef  # ['has window weighting function']
    manufacturer: URIRef  # ['manufacturer']
    filenamePattern: URIRef  # ['filename pattern']
    fnumber: URIRef  # ['fnumber']
    hasFlagMeaning: URIRef  # ['has flag meaning']
    hasFlagValue: URIRef  # ['has flag value']
    timeFormat: URIRef  # ['time format']
    BlackmanWindow: URIRef  # ['blackman window']
    DEHS: URIRef  # ['DEHS']
    ExperimentalImage: URIRef  # ['experimental image']
    FlagActive: URIRef  # ['active']
    GaussianWindow: URIRef  # ['Gaussian window']
    HannWindow: URIRef  # ['Hann window']
    ImageDewarping: URIRef  # ['image dewarping']
    ImageFiltering: URIRef  # ['image filtering']
    ImageHorizontalFlip: URIRef  # ['image horizontal flip']
    Interpolation: URIRef  # ['interpolation']
    LeftRightFlip: URIRef  # ['left right flip']
    MilliM_PER_PIXEL: URIRef  # ['millimeter per pixel']
    PER_PIXEL: URIRef  # ['per pixel']
    PIVData: URIRef  # ['PIV data']
    PIVImage: URIRef  # ['PIV image']
    PIVMask: URIRef  # ['PIV mask']
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


setattr(PIVMETA, "background_subtraction_method", PIVMETA.BackgroundSubtractionMethod)
setattr(PIVMETA, "camera", PIVMETA.Camera)
setattr(PIVMETA, "correlation_method", PIVMETA.CorrelationMethod)
setattr(PIVMETA, "piv_data_type", PIVMETA.DataType)
setattr(PIVMETA, "digital_camera", PIVMETA.DigitalCamera)
setattr(PIVMETA, "experimental_PIV_setup", PIVMETA.ExperimentalPIVSetup)
setattr(PIVMETA, "flag_statistics", PIVMETA.FlagStatistics)
setattr(PIVMETA, "flag_variable", PIVMETA.FlagVariable)
setattr(PIVMETA, "image_manipulation_method", PIVMETA.ImageManipulationMethod)
setattr(PIVMETA, "interrogation_method", PIVMETA.InterrogationMethod)
setattr(PIVMETA, "laser", PIVMETA.Laser)
setattr(PIVMETA, "lens", PIVMETA.Lens)
setattr(PIVMETA, "lens_system", PIVMETA.LensSystem)
setattr(PIVMETA, "light_source", PIVMETA.LightSource)
setattr(PIVMETA, "minimum_intensity_background_subtraction_method", PIVMETA.MinimumIntensityBackgroundSubtractionMethod)
setattr(PIVMETA, "multigrid", PIVMETA.Multigrid)
setattr(PIVMETA, "multipass", PIVMETA.Multipass)
setattr(PIVMETA, "objective", PIVMETA.Objective)
setattr(PIVMETA, "optic_sensor", PIVMETA.OpticSensor)
setattr(PIVMETA, "optical_component", PIVMETA.OpticalComponent)
setattr(PIVMETA, "outlier_detection_method", PIVMETA.OutlierDetectionMethod)
setattr(PIVMETA, "outlier_replacement_scheme", PIVMETA.outlierReplacementScheme)
setattr(PIVMETA, "PIV_Analysis", PIVMETA.PIVAnalysis)
setattr(PIVMETA, "PIV_background_generation", PIVMETA.PIVBackgroundGeneration)
setattr(PIVMETA, "PIV_calibration", PIVMETA.PIVCalibration)
setattr(PIVMETA, "PIV_dataset", PIVMETA.PIVDataset)
setattr(PIVMETA, "PIV_distribution", PIVMETA.PIVDistribution)
setattr(PIVMETA, "PIV_evaluation", PIVMETA.PIVEvaluation)
setattr(PIVMETA, "PIV_mask_generation", PIVMETA.PIVMaskGeneration)
setattr(PIVMETA, "PIV_particle", PIVMETA.PIVParticle)
setattr(PIVMETA, "PIV_post_processing", PIVMETA.PIVPostProcessing)
setattr(PIVMETA, "PIV_pre_processing", PIVMETA.PIVPreProcessing)
setattr(PIVMETA, "PIV_Processing_step", PIVMETA.PIVProcessingStep)
setattr(PIVMETA, "PIV_recording", PIVMETA.PIVRecording)
setattr(PIVMETA, "PIV_setup", PIVMETA.PIVSetup)
setattr(PIVMETA, "PIV_software", PIVMETA.PIVSoftware)
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
setattr(PIVMETA, "has_PIV_data_type", PIVMETA.hasDataType)
setattr(PIVMETA, "has_metric", PIVMETA.hasMetric)
setattr(PIVMETA, "has_window_weighting_function", PIVMETA.hasWindowWeightingFunction)
setattr(PIVMETA, "manufacturer", PIVMETA.manufacturer)
setattr(PIVMETA, "filename_pattern", PIVMETA.filenamePattern)
setattr(PIVMETA, "fnumber", PIVMETA.fnumber)
setattr(PIVMETA, "has_flag_meaning", PIVMETA.hasFlagMeaning)
setattr(PIVMETA, "has_flag_value", PIVMETA.hasFlagValue)
setattr(PIVMETA, "time_format", PIVMETA.timeFormat)
setattr(PIVMETA, "blackman_window", PIVMETA.BlackmanWindow)
setattr(PIVMETA, "DEHS", PIVMETA.DEHS)
setattr(PIVMETA, "experimental_image", PIVMETA.ExperimentalImage)
setattr(PIVMETA, "active", PIVMETA.FlagActive)
setattr(PIVMETA, "Gaussian_window", PIVMETA.GaussianWindow)
setattr(PIVMETA, "Hann_window", PIVMETA.HannWindow)
setattr(PIVMETA, "image_dewarping", PIVMETA.ImageDewarping)
setattr(PIVMETA, "image_filtering", PIVMETA.ImageFiltering)
setattr(PIVMETA, "image_horizontal_flip", PIVMETA.ImageHorizontalFlip)
setattr(PIVMETA, "interpolation", PIVMETA.Interpolation)
setattr(PIVMETA, "left_right_flip", PIVMETA.LeftRightFlip)
setattr(PIVMETA, "millimeter_per_pixel", PIVMETA.MilliM_PER_PIXEL)
setattr(PIVMETA, "per_pixel", PIVMETA.PER_PIXEL)
setattr(PIVMETA, "PIV_data", PIVMETA.PIVData)
setattr(PIVMETA, "PIV_image", PIVMETA.PIVImage)
setattr(PIVMETA, "PIV_mask", PIVMETA.PIVMask)
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