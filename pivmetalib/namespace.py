from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class PIV(DefinedNamespace):
    # uri = "https://matthiasprobst.github.io/pivmeta#"
    # Generated with pivmetalib
    BackgroundSubtractionMethod: URIRef  # ['background subtraction method']
    Camera: URIRef  # ['camera']
    CorrelationMethod: URIRef  # ['correlation method']
    DigitalCamera: URIRef  # ['digital camera']
    ExperimentalSetup: URIRef  # ['experimental setup']
    FlagStatistics: URIRef  # ['flag statistics']
    FlagVariable: URIRef  # ['flag variable']
    ImageManipulationMethod: URIRef  # ['image manipulation method']
    ImageVelocimetryDataset: URIRef  # ['Image Velocimetry Dataset']
    ImageVelocimetryDistribution: URIRef  # ['Image Velocimetry Distribution']
    ImageVelocimetryMethod: URIRef  # ['image velocimetry method']
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
    OutlierDetectionMethod: URIRef  # ['Outlier detection method']
    OutlierReplacementScheme: URIRef  # ['Outlier replacement scheme']
    PIVAnalysis: URIRef  # ['PIV Analysis']
    PIVBackgroundGeneration: URIRef  # ['PIV background generation']
    PIVCalibration: URIRef  # ['PIV calibration']
    PIVDataType: URIRef  # ['PIV data type']
    PIVDataset: URIRef  # ['PIV dataset']
    PIVEvaluation: URIRef  # ['PIV evaluation']
    PIVMaskGeneration: URIRef  # ['PIV mask generation']
    PIVParticle: URIRef  # ['PIV particle']
    PIVPostProcessing: URIRef  # ['PIV post processing']
    PIVPreProcessing: URIRef  # ['PIV pre processing']
    PIVProcessingStep: URIRef  # ['PIV Processing step']
    PIVRecording: URIRef  # ['PIV recording']
    PIVSoftware: URIRef  # ['PIV software']
    PTVDataset: URIRef  # ['PTV dataset']
    PeakSearchMethod: URIRef  # ['peak search method']
    Setup: URIRef  # ['Setup']
    Singlepass: URIRef  # ['singlepass']
    SyntheticPIVParticle: URIRef  # ['synthetic PIV particle']
    TemporalVariable: URIRef  # ['temporal variable']
    VirtualCamera: URIRef  # ['virtual camera']
    VirtualLaser: URIRef  # ['virtual laser']
    VirtualSetup: URIRef  # ['virtual setup']
    VirtualTool: URIRef  # ['virtual tool']
    WindowWeightingFunction: URIRef  # ['window weighting function']
    flag: URIRef  # ['flag']
    flagIn: URIRef  # ['flag in']
    hasMetric: URIRef  # ['has metric']
    hasPIVDataType: URIRef  # ['has PIV data type']
    hasSetup: URIRef  # ['has setup']
    hasWindowWeightingFunction: URIRef  # ['has window weighting function']
    isSetupFor: URIRef  # ['is setup for']
    manufacturer: URIRef  # ['manufacturer']
    outlierReplacementScheme: URIRef  # ['outlier replacement scheme']
    usesAcquisitionSoftware: URIRef  # ['uses acquisition software']
    usesAnalysisSoftware: URIRef  # ['uses analysis software']
    usesSoftware: URIRef  # ['uses software']
    filenamePattern: URIRef  # ['filename pattern']
    fnumber: URIRef  # ['fnumber']
    hasFlagMeaning: URIRef  # ['has flag meaning']
    hasFlagValue: URIRef  # ['has flag value']
    timeValue: URIRef  # ['time value']
    BlackmanWindow: URIRef  # ['blackman window']
    DEHS: URIRef  # ['DEHS']
    ExperimentalImage: URIRef  # ['experimental image']
    FlagActive: URIRef  # ['active']
    FlagDisabled: URIRef  # ['disabled']
    FlagFiltered: URIRef  # ['filtered']
    FlagInactive: URIRef  # ['inactive']
    FlagInterpolated: URIRef  # ['interpolated']
    FlagManualEdit: URIRef  # ['manualedit']
    FlagMasked: URIRef  # ['masked']
    FlagNoResult: URIRef  # ['noresult']
    FlagReplaced: URIRef  # ['replaced']
    GaussianWindow: URIRef  # ['Gaussian window']
    HannWindow: URIRef  # ['Hann window']
    Image: URIRef  # ['image']
    ImageDewarping: URIRef  # ['image dewarping']
    ImageFiltering: URIRef  # ['image filtering']
    ImageHorizontalFlip: URIRef  # ['image horizontal flip']
    Interpolation: URIRef  # ['interpolation']
    LeftRightFlip: URIRef  # ['left right flip']
    Mask: URIRef  # ['mask']
    MilliM_PER_PIXEL: URIRef  # ['millimeter per pixel']
    PER_PIXEL: URIRef  # ['per pixel']
    PIV: URIRef  # ['Particle Image Velocimetry']
    PTV: URIRef  # ['Particle Tracking Velocimetry']
    ProcessedImage: URIRef  # ['processed image']
    ReEvaluateWithLargerSample: URIRef  # ['re-evaluate with larger sample']
    ResultData: URIRef  # ['result data']
    SpatialResolution: URIRef  # ['spatial resolution']
    SplitImage: URIRef  # ['split image']
    SquareWindow: URIRef  # ['square window']
    SyntheticImage: URIRef  # ['synthetic image']
    TopBottomFlip: URIRef  # ['top bottom flip']
    TryLowerOrderPeaks: URIRef  # ['try lower order peaks']
    TukeyWindow: URIRef  # ['Tukey window']
    microPIV: URIRef  # ['Micro Particle Image Velocimetry']

    _NS = Namespace("https://matthiasprobst.github.io/pivmeta#")


setattr(PIV, "background_subtraction_method", PIV.BackgroundSubtractionMethod)
setattr(PIV, "camera", PIV.Camera)
setattr(PIV, "correlation_method", PIV.CorrelationMethod)
setattr(PIV, "digital_camera", PIV.DigitalCamera)
setattr(PIV, "experimental_setup", PIV.ExperimentalSetup)
setattr(PIV, "flag_statistics", PIV.FlagStatistics)
setattr(PIV, "flag_variable", PIV.FlagVariable)
setattr(PIV, "image_manipulation_method", PIV.ImageManipulationMethod)
setattr(PIV, "Image_Velocimetry_Dataset", PIV.ImageVelocimetryDataset)
setattr(PIV, "Image_Velocimetry_Distribution", PIV.ImageVelocimetryDistribution)
setattr(PIV, "image_velocimetry_method", PIV.ImageVelocimetryMethod)
setattr(PIV, "interrogation_method", PIV.InterrogationMethod)
setattr(PIV, "laser", PIV.Laser)
setattr(PIV, "lens", PIV.Lens)
setattr(PIV, "lens_system", PIV.LensSystem)
setattr(PIV, "light_source", PIV.LightSource)
setattr(PIV, "minimum_intensity_background_subtraction_method", PIV.MinimumIntensityBackgroundSubtractionMethod)
setattr(PIV, "multigrid", PIV.Multigrid)
setattr(PIV, "multipass", PIV.Multipass)
setattr(PIV, "objective", PIV.Objective)
setattr(PIV, "optic_sensor", PIV.OpticSensor)
setattr(PIV, "optical_component", PIV.OpticalComponent)
setattr(PIV, "Outlier_detection_method", PIV.OutlierDetectionMethod)
setattr(PIV, "Outlier_replacement_scheme", PIV.OutlierReplacementScheme)
setattr(PIV, "PIV_Analysis", PIV.PIVAnalysis)
setattr(PIV, "PIV_background_generation", PIV.PIVBackgroundGeneration)
setattr(PIV, "PIV_calibration", PIV.PIVCalibration)
setattr(PIV, "PIV_data_type", PIV.PIVDataType)
setattr(PIV, "PIV_dataset", PIV.PIVDataset)
setattr(PIV, "PIV_evaluation", PIV.PIVEvaluation)
setattr(PIV, "PIV_mask_generation", PIV.PIVMaskGeneration)
setattr(PIV, "PIV_particle", PIV.PIVParticle)
setattr(PIV, "PIV_post_processing", PIV.PIVPostProcessing)
setattr(PIV, "PIV_pre_processing", PIV.PIVPreProcessing)
setattr(PIV, "PIV_Processing_step", PIV.PIVProcessingStep)
setattr(PIV, "PIV_recording", PIV.PIVRecording)
setattr(PIV, "PIV_software", PIV.PIVSoftware)
setattr(PIV, "PTV_dataset", PIV.PTVDataset)
setattr(PIV, "peak_search_method", PIV.PeakSearchMethod)
setattr(PIV, "Setup", PIV.Setup)
setattr(PIV, "singlepass", PIV.Singlepass)
setattr(PIV, "synthetic_PIV_particle", PIV.SyntheticPIVParticle)
setattr(PIV, "temporal_variable", PIV.TemporalVariable)
setattr(PIV, "virtual_camera", PIV.VirtualCamera)
setattr(PIV, "virtual_laser", PIV.VirtualLaser)
setattr(PIV, "virtual_setup", PIV.VirtualSetup)
setattr(PIV, "virtual_tool", PIV.VirtualTool)
setattr(PIV, "window_weighting_function", PIV.WindowWeightingFunction)
setattr(PIV, "flag", PIV.flag)
setattr(PIV, "flag_in", PIV.flagIn)
setattr(PIV, "has_metric", PIV.hasMetric)
setattr(PIV, "has_PIV_data_type", PIV.hasPIVDataType)
setattr(PIV, "has_setup", PIV.hasSetup)
setattr(PIV, "has_window_weighting_function", PIV.hasWindowWeightingFunction)
setattr(PIV, "is_setup_for", PIV.isSetupFor)
setattr(PIV, "manufacturer", PIV.manufacturer)
setattr(PIV, "outlier_replacement_scheme", PIV.outlierReplacementScheme)
setattr(PIV, "uses_acquisition_software", PIV.usesAcquisitionSoftware)
setattr(PIV, "uses_analysis_software", PIV.usesAnalysisSoftware)
setattr(PIV, "uses_software", PIV.usesSoftware)
setattr(PIV, "filename_pattern", PIV.filenamePattern)
setattr(PIV, "fnumber", PIV.fnumber)
setattr(PIV, "has_flag_meaning", PIV.hasFlagMeaning)
setattr(PIV, "has_flag_value", PIV.hasFlagValue)
setattr(PIV, "time_value", PIV.timeValue)
setattr(PIV, "blackman_window", PIV.BlackmanWindow)
setattr(PIV, "DEHS", PIV.DEHS)
setattr(PIV, "experimental_image", PIV.ExperimentalImage)
setattr(PIV, "active", PIV.FlagActive)
setattr(PIV, "disabled", PIV.FlagDisabled)
setattr(PIV, "filtered", PIV.FlagFiltered)
setattr(PIV, "inactive", PIV.FlagInactive)
setattr(PIV, "interpolated", PIV.FlagInterpolated)
setattr(PIV, "manualedit", PIV.FlagManualEdit)
setattr(PIV, "masked", PIV.FlagMasked)
setattr(PIV, "noresult", PIV.FlagNoResult)
setattr(PIV, "replaced", PIV.FlagReplaced)
setattr(PIV, "Gaussian_window", PIV.GaussianWindow)
setattr(PIV, "Hann_window", PIV.HannWindow)
setattr(PIV, "image", PIV.Image)
setattr(PIV, "image_dewarping", PIV.ImageDewarping)
setattr(PIV, "image_filtering", PIV.ImageFiltering)
setattr(PIV, "image_horizontal_flip", PIV.ImageHorizontalFlip)
setattr(PIV, "interpolation", PIV.Interpolation)
setattr(PIV, "left_right_flip", PIV.LeftRightFlip)
setattr(PIV, "mask", PIV.Mask)
setattr(PIV, "millimeter_per_pixel", PIV.MilliM_PER_PIXEL)
setattr(PIV, "per_pixel", PIV.PER_PIXEL)
setattr(PIV, "Particle_Image_Velocimetry", PIV.PIV)
setattr(PIV, "Particle_Tracking_Velocimetry", PIV.PTV)
setattr(PIV, "processed_image", PIV.ProcessedImage)
setattr(PIV, "re-evaluate_with_larger_sample", PIV.ReEvaluateWithLargerSample)
setattr(PIV, "result_data", PIV.ResultData)
setattr(PIV, "spatial_resolution", PIV.SpatialResolution)
setattr(PIV, "split_image", PIV.SplitImage)
setattr(PIV, "square_window", PIV.SquareWindow)
setattr(PIV, "synthetic_image", PIV.SyntheticImage)
setattr(PIV, "top_bottom_flip", PIV.TopBottomFlip)
setattr(PIV, "try_lower_order_peaks", PIV.TryLowerOrderPeaks)
setattr(PIV, "Tukey_window", PIV.TukeyWindow)
setattr(PIV, "Micro_Particle_Image_Velocimetry", PIV.microPIV)