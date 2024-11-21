from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class PIVMETA(DefinedNamespace):
    # uri = "https://matthiasprobst.github.io/pivmeta#"
    # Generated with pivmetalib
    BackgroundImageGeneration: URIRef  # ['background image generation']
    BackgroundSubtractionMethod: URIRef  # ['background subtraction']
    Camera: URIRef  # ['Camera']
    CorrelationMethod: URIRef  # ['Correlation Method']
    DigitalCamera: URIRef  # ['Digital Camera']
    FlagCount: URIRef  # ['Flag Count']
    FlagVariable: URIRef  # ['Flag Variable']
    ImageDewarp: URIRef  # ['image dewarp']
    ImageFilter: URIRef  # ['image filter']
    ImageManipulationMethod: URIRef  # ['Image Manipulation Method']
    ImageRotation: URIRef  # ['image rotation']
    ImageType: URIRef  # ['Image Type']
    InterrogationMethod: URIRef  # ['Interrogation Method']
    Laser: URIRef  # ['Laser']
    LightSource: URIRef  # ['Light Source']
    MaskGeneration: URIRef  # ['mask generation']
    Multigrid: URIRef  # ['Multigrid']
    Multipass: URIRef  # ['Multipass']
    OpticSensor: URIRef  # ['Optic Sensor']
    OutlierDetectionMethod: URIRef  # ['Outlier Detection Method']
    OutlierReplacementScheme: URIRef  # ['Outlier Replacement Scheme']
    PIVEvaluation: URIRef  # ['piv evaluation']
    PIVHardware: URIRef  # ['PIV Hardware']
    PIVParticle: URIRef  # ['PIV Particle']
    PIVSoftware: URIRef  # ['Piv Software']
    PeakSearchMethod: URIRef  # ['Peak Search Method']
    PivDistribution: URIRef  # ['piv distribution']
    PivImageDistribution: URIRef  # ['piv image distribution']
    PivMaskDistribution: URIRef  # ['piv mask distribution']
    PivPostProcessing: URIRef  # ['piv post processing']
    PivPreProcessing: URIRef  # ['piv pre processing']
    PivProcessingStep: URIRef  # ['piv processing step']
    PivResultDistribution: URIRef  # ['piv result distribution']
    PivValidation: URIRef  # ['piv validation']
    Singlepass: URIRef  # ['Singlepass']
    Substance: URIRef  # ['Substance']
    SyntheticPIVParticle: URIRef  # ['Synthetic Particle']
    TemporalVariable: URIRef  # ['Temporal Variable']
    VirtualCamera: URIRef  # ['Virtual Camera']
    VirtualLaser: URIRef  # ['Virtual Laser']
    VirtualTool: URIRef  # ['Virtual Tool']
    WindowWeightingFunction: URIRef  # ['Window Weighting Function']
    flag: URIRef  # ['flag']
    flagIn: URIRef  # ['flag in']
    hasStandardName: URIRef  # ['has standard name']
    outlierReplacementScheme: URIRef  # ['outlier replacement scheme']
    pivImageType: URIRef  # ['piv image type']
    windowWeightingFunction: URIRef  # ['window weighting function']
    filenamePattern: URIRef  # ['filename pattern']
    fnumber: URIRef  # ['fnumber']
    hasFlagMeaning: URIRef  # ['has flag meaning']
    hasFlagValue: URIRef  # ['has flag value']
    numberOfRecords: URIRef  # ['number of records']
    timeFormat: URIRef  # ['time format']
    DEHS: URIRef  # ['DEHS']
    ExperimentalImage: URIRef  # ['experimental image']
    FlagActive: URIRef  # ['active']
    GaussianWindow: URIRef  # ['Gaussian Window']
    HammingWindow: URIRef  # ['Hamming Window']
    HannWindow: URIRef  # ['Hann Window']
    Interpolation: URIRef  # ['Interpolation']
    LeftRightFlip: URIRef  # ['left right flip']
    MilliM_PER_PIXEL: URIRef  # ['millimeter per pixel']
    PER_PIXEL: URIRef  # ['per pixel']
    PIVData: URIRef  # ['PIV data']
    PIVImageAAA: URIRef  # ['PIV image']
    ParticleImageVelocimetry: URIRef  # ['Particle Image Velocimetry']
    ParticleTrackingVelocimetry: URIRef  # ['Particle Tracking Velocimetry']
    ReEvaluateWithLargerSample: URIRef  # ['re-evaluate with larger sample']
    SpatialResolution: URIRef  # ['spatial resolution']
    SplitImage: URIRef  # ['split image']
    SquareWindow: URIRef  # ['Square Window']
    SyntheticImage: URIRef  # ['synthetic image']
    TopBottomFlip: URIRef  # ['top bottom flip']
    TryLowerOrderPeaks: URIRef  # ['try lower order peaks']
    TukeyWindow: URIRef  # ['Tukey Window']
    microPIV: URIRef  # ['Micro PIV']

    _NS = Namespace("https://matthiasprobst.github.io/pivmeta#")


setattr(PIVMETA, "background_image_generation", PIVMETA.BackgroundImageGeneration)
setattr(PIVMETA, "background_subtraction", PIVMETA.BackgroundSubtractionMethod)
setattr(PIVMETA, "Camera", PIVMETA.Camera)
setattr(PIVMETA, "Correlation_Method", PIVMETA.CorrelationMethod)
setattr(PIVMETA, "Digital_Camera", PIVMETA.DigitalCamera)
setattr(PIVMETA, "Flag_Count", PIVMETA.FlagCount)
setattr(PIVMETA, "Flag_Variable", PIVMETA.FlagVariable)
setattr(PIVMETA, "image_dewarp", PIVMETA.ImageDewarp)
setattr(PIVMETA, "image_filter", PIVMETA.ImageFilter)
setattr(PIVMETA, "Image_Manipulation_Method", PIVMETA.ImageManipulationMethod)
setattr(PIVMETA, "image_rotation", PIVMETA.ImageRotation)
setattr(PIVMETA, "Image_Type", PIVMETA.ImageType)
setattr(PIVMETA, "Interrogation_Method", PIVMETA.InterrogationMethod)
setattr(PIVMETA, "Laser", PIVMETA.Laser)
setattr(PIVMETA, "Light_Source", PIVMETA.LightSource)
setattr(PIVMETA, "mask_generation", PIVMETA.MaskGeneration)
setattr(PIVMETA, "Multigrid", PIVMETA.Multigrid)
setattr(PIVMETA, "Multipass", PIVMETA.Multipass)
setattr(PIVMETA, "Optic_Sensor", PIVMETA.OpticSensor)
setattr(PIVMETA, "Outlier_Detection_Method", PIVMETA.OutlierDetectionMethod)
setattr(PIVMETA, "Outlier_Replacement_Scheme", PIVMETA.OutlierReplacementScheme)
setattr(PIVMETA, "piv_evaluation", PIVMETA.PIVEvaluation)
setattr(PIVMETA, "PIV_Hardware", PIVMETA.PIVHardware)
setattr(PIVMETA, "PIV_Particle", PIVMETA.PIVParticle)
setattr(PIVMETA, "Piv_Software", PIVMETA.PIVSoftware)
setattr(PIVMETA, "Peak_Search_Method", PIVMETA.PeakSearchMethod)
setattr(PIVMETA, "piv_distribution", PIVMETA.PivDistribution)
setattr(PIVMETA, "piv_image_distribution", PIVMETA.PivImageDistribution)
setattr(PIVMETA, "piv_mask_distribution", PIVMETA.PivMaskDistribution)
setattr(PIVMETA, "piv_post_processing", PIVMETA.PivPostProcessing)
setattr(PIVMETA, "piv_pre_processing", PIVMETA.PivPreProcessing)
setattr(PIVMETA, "piv_processing_step", PIVMETA.PivProcessingStep)
setattr(PIVMETA, "piv_result_distribution", PIVMETA.PivResultDistribution)
setattr(PIVMETA, "piv_validation", PIVMETA.PivValidation)
setattr(PIVMETA, "Singlepass", PIVMETA.Singlepass)
setattr(PIVMETA, "Substance", PIVMETA.Substance)
setattr(PIVMETA, "Synthetic_Particle", PIVMETA.SyntheticPIVParticle)
setattr(PIVMETA, "Temporal_Variable", PIVMETA.TemporalVariable)
setattr(PIVMETA, "Virtual_Camera", PIVMETA.VirtualCamera)
setattr(PIVMETA, "Virtual_Laser", PIVMETA.VirtualLaser)
setattr(PIVMETA, "Virtual_Tool", PIVMETA.VirtualTool)
setattr(PIVMETA, "Window_Weighting_Function", PIVMETA.WindowWeightingFunction)
setattr(PIVMETA, "flag", PIVMETA.flag)
setattr(PIVMETA, "flag_in", PIVMETA.flagIn)
setattr(PIVMETA, "has_standard_name", PIVMETA.hasStandardName)
setattr(PIVMETA, "outlier_replacement_scheme", PIVMETA.outlierReplacementScheme)
setattr(PIVMETA, "piv_image_type", PIVMETA.pivImageType)
setattr(PIVMETA, "window_weighting_function", PIVMETA.windowWeightingFunction)
setattr(PIVMETA, "filename_pattern", PIVMETA.filenamePattern)
setattr(PIVMETA, "fnumber", PIVMETA.fnumber)
setattr(PIVMETA, "has_flag_meaning", PIVMETA.hasFlagMeaning)
setattr(PIVMETA, "has_flag_value", PIVMETA.hasFlagValue)
setattr(PIVMETA, "number_of_records", PIVMETA.numberOfRecords)
setattr(PIVMETA, "time_format", PIVMETA.timeFormat)
setattr(PIVMETA, "DEHS", PIVMETA.DEHS)
setattr(PIVMETA, "experimental_image", PIVMETA.ExperimentalImage)
setattr(PIVMETA, "active", PIVMETA.FlagActive)
setattr(PIVMETA, "Gaussian_Window", PIVMETA.GaussianWindow)
setattr(PIVMETA, "Hamming_Window", PIVMETA.HammingWindow)
setattr(PIVMETA, "Hann_Window", PIVMETA.HannWindow)
setattr(PIVMETA, "Interpolation", PIVMETA.Interpolation)
setattr(PIVMETA, "left_right_flip", PIVMETA.LeftRightFlip)
setattr(PIVMETA, "millimeter_per_pixel", PIVMETA.MilliM_PER_PIXEL)
setattr(PIVMETA, "per_pixel", PIVMETA.PER_PIXEL)
setattr(PIVMETA, "PIV_data", PIVMETA.PIVData)
setattr(PIVMETA, "PIV_image", PIVMETA.PIVImageAAA)
setattr(PIVMETA, "Particle_Image_Velocimetry", PIVMETA.ParticleImageVelocimetry)
setattr(PIVMETA, "Particle_Tracking_Velocimetry", PIVMETA.ParticleTrackingVelocimetry)
setattr(PIVMETA, "re-evaluate_with_larger_sample", PIVMETA.ReEvaluateWithLargerSample)
setattr(PIVMETA, "spatial_resolution", PIVMETA.SpatialResolution)
setattr(PIVMETA, "split_image", PIVMETA.SplitImage)
setattr(PIVMETA, "Square_Window", PIVMETA.SquareWindow)
setattr(PIVMETA, "synthetic_image", PIVMETA.SyntheticImage)
setattr(PIVMETA, "top_bottom_flip", PIVMETA.TopBottomFlip)
setattr(PIVMETA, "try_lower_order_peaks", PIVMETA.TryLowerOrderPeaks)
setattr(PIVMETA, "Tukey_Window", PIVMETA.TukeyWindow)
setattr(PIVMETA, "Micro_PIV", PIVMETA.microPIV)