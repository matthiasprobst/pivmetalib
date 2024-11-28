from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class PIVMETA(DefinedNamespace):
    # uri = "https://matthiasprobst.github.io/pivmeta#"
    # Generated with pivmetalib
    BackgroundImageGeneration: URIRef  # ['Background Image Generation']
    BackgroundSubtractionMethod: URIRef  # ['Background Subtraction']
    Camera: URIRef  # ['Camera']
    CorrelationMethod: URIRef  # ['Correlation Method']
    DigitalCamera: URIRef  # ['Digital Camera']
    ExperimentalPIVSetup: URIRef  # ['Experimental PIV Setup']
    FlagStatistics: URIRef  # ['Flag Statistics']
    FlagVariable: URIRef  # ['Flag Variable']
    ImageDewarping: URIRef  # ['Image Dewarping']
    ImageFiltering: URIRef  # ['Image Filtering']
    ImageManipulationMethod: URIRef  # ['Image Manipulation Method']
    ImageRotation: URIRef  # ['Image Rotation']
    InterrogationMethod: URIRef  # ['Interrogation Method']
    Laser: URIRef  # ['Laser']
    Lens: URIRef  # ['Lens']
    LensSystem: URIRef  # ['Lens System']
    LightSource: URIRef  # ['Light Source']
    MaskGeneration: URIRef  # ['Mask Generation']
    Multigrid: URIRef  # ['Multigrid']
    Multipass: URIRef  # ['Multipass']
    Objective: URIRef  # ['Objective']
    OpticSensor: URIRef  # ['Optic Sensor']
    OpticalComponent: URIRef  # ['Optical Component']
    OutlierDetectionMethod: URIRef  # ['Outlier Detection Method']
    OutlierReplacementScheme: URIRef  # ['Outlier Replacement Scheme']
    PIVDataset: URIRef  # ['PIV Dataset']
    PIVDistribution: URIRef  # ['PIV Distribution']
    PIVEvaluation: URIRef  # ['PIV Evaluation']
    PIVImageDistribution: URIRef  # ['PIV Image Distribution']
    PIVMaskDistribution: URIRef  # ['PIV Mask Distribution']
    PIVParticle: URIRef  # ['PIV Particle']
    PIVPostProcessing: URIRef  # ['PIV Post Processing']
    PIVPreProcessing: URIRef  # ['Piv Pre processing']
    PIVProcessingStep: URIRef  # ['PIV Processing Step']
    PIVRecording: URIRef  # ['PIV Recording']
    PIVResultDistribution: URIRef  # ['PIV Result Distribution']
    PIVSetup: URIRef  # ['PIV Setup']
    PIVSoftware: URIRef  # ['PIV Software']
    PIVValidation: URIRef  # ['PIV Validation']
    PeakSearchMethod: URIRef  # ['Peak Search Method']
    Singlepass: URIRef  # ['Singlepass']
    SyntheticPIVParticle: URIRef  # ['Synthetic PIV Particle']
    TemporalVariable: URIRef  # ['Temporal Variable']
    VirtualCamera: URIRef  # ['Virtual Camera']
    VirtualLaser: URIRef  # ['Virtual Laser']
    VirtualPIVSetup: URIRef  # ['Virtual PIV Setup']
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
    BlackmanWindow: URIRef  # ['Blackman Window']
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


setattr(PIVMETA, "Background_Image_Generation", PIVMETA.BackgroundImageGeneration)
setattr(PIVMETA, "Background_Subtraction", PIVMETA.BackgroundSubtractionMethod)
setattr(PIVMETA, "Camera", PIVMETA.Camera)
setattr(PIVMETA, "Correlation_Method", PIVMETA.CorrelationMethod)
setattr(PIVMETA, "Digital_Camera", PIVMETA.DigitalCamera)
setattr(PIVMETA, "Experimental_PIV_Setup", PIVMETA.ExperimentalPIVSetup)
setattr(PIVMETA, "Flag_Statistics", PIVMETA.FlagStatistics)
setattr(PIVMETA, "Flag_Variable", PIVMETA.FlagVariable)
setattr(PIVMETA, "Image_Dewarping", PIVMETA.ImageDewarping)
setattr(PIVMETA, "Image_Filtering", PIVMETA.ImageFiltering)
setattr(PIVMETA, "Image_Manipulation_Method", PIVMETA.ImageManipulationMethod)
setattr(PIVMETA, "Image_Rotation", PIVMETA.ImageRotation)
setattr(PIVMETA, "Interrogation_Method", PIVMETA.InterrogationMethod)
setattr(PIVMETA, "Laser", PIVMETA.Laser)
setattr(PIVMETA, "Lens", PIVMETA.Lens)
setattr(PIVMETA, "Lens_System", PIVMETA.LensSystem)
setattr(PIVMETA, "Light_Source", PIVMETA.LightSource)
setattr(PIVMETA, "Mask_Generation", PIVMETA.MaskGeneration)
setattr(PIVMETA, "Multigrid", PIVMETA.Multigrid)
setattr(PIVMETA, "Multipass", PIVMETA.Multipass)
setattr(PIVMETA, "Objective", PIVMETA.Objective)
setattr(PIVMETA, "Optic_Sensor", PIVMETA.OpticSensor)
setattr(PIVMETA, "Optical_Component", PIVMETA.OpticalComponent)
setattr(PIVMETA, "Outlier_Detection_Method", PIVMETA.OutlierDetectionMethod)
setattr(PIVMETA, "Outlier_Replacement_Scheme", PIVMETA.OutlierReplacementScheme)
setattr(PIVMETA, "PIV_Dataset", PIVMETA.PIVDataset)
setattr(PIVMETA, "PIV_Distribution", PIVMETA.PIVDistribution)
setattr(PIVMETA, "PIV_Evaluation", PIVMETA.PIVEvaluation)
setattr(PIVMETA, "PIV_Image_Distribution", PIVMETA.PIVImageDistribution)
setattr(PIVMETA, "PIV_Mask_Distribution", PIVMETA.PIVMaskDistribution)
setattr(PIVMETA, "PIV_Particle", PIVMETA.PIVParticle)
setattr(PIVMETA, "PIV_Post_Processing", PIVMETA.PIVPostProcessing)
setattr(PIVMETA, "Piv_Pre_processing", PIVMETA.PIVPreProcessing)
setattr(PIVMETA, "PIV_Processing_Step", PIVMETA.PIVProcessingStep)
setattr(PIVMETA, "PIV_Recording", PIVMETA.PIVRecording)
setattr(PIVMETA, "PIV_Result_Distribution", PIVMETA.PIVResultDistribution)
setattr(PIVMETA, "PIV_Setup", PIVMETA.PIVSetup)
setattr(PIVMETA, "PIV_Software", PIVMETA.PIVSoftware)
setattr(PIVMETA, "PIV_Validation", PIVMETA.PIVValidation)
setattr(PIVMETA, "Peak_Search_Method", PIVMETA.PeakSearchMethod)
setattr(PIVMETA, "Singlepass", PIVMETA.Singlepass)
setattr(PIVMETA, "Synthetic_PIV_Particle", PIVMETA.SyntheticPIVParticle)
setattr(PIVMETA, "Temporal_Variable", PIVMETA.TemporalVariable)
setattr(PIVMETA, "Virtual_Camera", PIVMETA.VirtualCamera)
setattr(PIVMETA, "Virtual_Laser", PIVMETA.VirtualLaser)
setattr(PIVMETA, "Virtual_PIV_Setup", PIVMETA.VirtualPIVSetup)
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
setattr(PIVMETA, "Blackman_Window", PIVMETA.BlackmanWindow)
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