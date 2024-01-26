from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class PIVMETA(DefinedNamespace):
    # uri = "https://w3id.org/nfdi4ing/metadata4ing#"
    # Generated with h5rdmtoolbox.data.m4i.generate_namespace_file()
    time: URIRef  # ['time']
    BackgroundSubtractionMethod: URIRef  # ['background subtraction']
    CorrelationAlgorithm: URIRef  # ['CorrelationAlgorithm']
    ImageDewarp: URIRef  # ['image dewarp']
    ImageFilter: URIRef  # ['image filter']
    InterrogationMethod: URIRef  # ['Interrogation Method']
    Multigrid: URIRef  # ['Multigrid']
    Multipass: URIRef  # ['Multipass']
    OutlierDetectionMethod: URIRef  # ['Outlier Detection Method']
    PIVEvaluation: URIRef  # ['piv evaluation']
    PivImageDistribution: URIRef  # ['piv image distribution']
    PivPostProcessing: URIRef  # ['piv post processing']
    PivPreProcessing: URIRef  # ['piv pre processing']
    PivProcessingStep: URIRef  # ['piv processing step']
    PivResultDistribution: URIRef  # ['piv result distribution']
    Singlepass: URIRef  # ['Singlepass']
    SubPixelPeakFitMethod: URIRef  # ['Sub Pixel Peak Fit Method']
    hasStandardName: URIRef  # ['has standard name']
    pivImageType: URIRef  # ['piv image type']
    usesCorrelationAlgorithm: URIRef  # ['correlation algorithm']
    ExperimentalImage: URIRef  # ['experimental image']
    LeftRightFlip: URIRef  # ['left right flip']
    SplitImage: URIRef  # ['split image']
    SyntheticImage: URIRef  # ['synthetic image']
    TopBottomFlip: URIRef  # ['top bottom flip']
    micro_piv: URIRef  # ['micro piv']
    piv: URIRef  # ['piv']
    piv_first_peak_correlation_coefficient: URIRef  # ['piv_first_peak_correlation_coefficient']
    ptv: URIRef  # ['ptv']
    piv_correlation_coefficient: URIRef  # ['piv_correlation_coefficient']
    piv_second_peak_correlation_coefficient: URIRef  # ['piv_second_peak_correlation_coefficient']
    piv_third_peak_correlation_coefficient: URIRef  # ['piv_third_peak_correlation_coefficient']
    first_peak_x_displacement: URIRef  # ['first_peak_x_displacement']
    first_peak_y_displacement: URIRef  # ['first_peak_y_displacement']
    piv_flag: URIRef  # ['piv_flag']
    image_particle_density: URIRef  # ['image_particle_density']
    image_particle_diameter: URIRef  # ['image_particle_diameter']
    piv_image_index: URIRef  # ['piv_image_index']
    inplane_velocity: URIRef  # ['inplane_velocity']
    laser_sheet_thickness: URIRef  # ['laser_sheet_thickness']
    mean_seeding_particle_size: URIRef  # ['mean_seeding_particle_size']
    number_of_particles: URIRef  # ['number_of_particles']
    laser_pulse_delay: URIRef  # ['laser_pulse_delay']
    saturated_pixel_number: URIRef  # ['saturated_pixel_number']
    second_peak_x_displacement: URIRef  # ['second_peak_x_displacement']
    second_peak_y_displacement: URIRef  # ['second_peak_y_displacement']
    seeding_material: URIRef  # ['seeding_material']
    standard_deviation_of_image_particle_diameter: URIRef  # ['standard_deviation_of_image_particle_diameter']
    third_peak_x_displacement: URIRef  # ['third_peak_x_displacement']
    third_peak_y_displacement: URIRef  # ['third_peak_y_displacement']
    relative_time: URIRef  # ['relative_time']
    velocity: URIRef  # ['velocity']
    displacement: URIRef  # ['displacement']
    x_final_interrogation_window_overlap_size: URIRef  # ['x_final_interrogation_window_overlap_size']
    x_final_interrogation_window_size: URIRef  # ['x_final_interrogation_window_size']
    x_initial_interrogation_window_size: URIRef  # ['x_initial_interrogation_window_size']
    x_pixel_coordinate: URIRef  # ['x_pixel_coordinate']
    y_final_interrogation_window_overlap_size: URIRef  # ['y_final_interrogation_window_overlap_size']
    y_final_interrogation_window_size: URIRef  # ['y_final_interrogation_window_size']
    y_initial_interrogation_window_size: URIRef  # ['y_initial_interrogation_window_size']
    y_pixel_coordinate: URIRef  # ['y_pixel_coordinate']
    pixel_origin: URIRef  # ['pixel_origin']
    coordinate: URIRef  # ['coordinate']
    signal_to_noise_ratio: URIRef  # ['signal_to_noise_ratio']
    least_square_residual_of_z_displacement_reconstruction: URIRef  # ['least_square_residual_of_z_displacement_reconstruction']
    piv_scaling_factor: URIRef  # ['piv_scaling_factor']
    image_filter_kernel_size: URIRef  # ['image_filter_kernel_size']

    _NS = Namespace("https://matthiasprobst.github.io/pivmeta#")


setattr(PIVMETA, "time", PIVMETA.time)
setattr(PIVMETA, "background_subtraction", PIVMETA.BackgroundSubtractionMethod)
setattr(PIVMETA, "CorrelationAlgorithm", PIVMETA.CorrelationAlgorithm)
setattr(PIVMETA, "image_dewarp", PIVMETA.ImageDewarp)
setattr(PIVMETA, "image_filter", PIVMETA.ImageFilter)
setattr(PIVMETA, "Interrogation_Method", PIVMETA.InterrogationMethod)
setattr(PIVMETA, "Multigrid", PIVMETA.Multigrid)
setattr(PIVMETA, "Multipass", PIVMETA.Multipass)
setattr(PIVMETA, "Outlier_Detection_Method", PIVMETA.OutlierDetectionMethod)
setattr(PIVMETA, "piv_evaluation", PIVMETA.PIVEvaluation)
setattr(PIVMETA, "piv_image_distribution", PIVMETA.PivImageDistribution)
setattr(PIVMETA, "piv_post_processing", PIVMETA.PivPostProcessing)
setattr(PIVMETA, "piv_pre_processing", PIVMETA.PivPreProcessing)
setattr(PIVMETA, "piv_processing_step", PIVMETA.PivProcessingStep)
setattr(PIVMETA, "piv_result_distribution", PIVMETA.PivResultDistribution)
setattr(PIVMETA, "Singlepass", PIVMETA.Singlepass)
setattr(PIVMETA, "Sub_Pixel_Peak_Fit_Method", PIVMETA.SubPixelPeakFitMethod)
setattr(PIVMETA, "has_standard_name", PIVMETA.hasStandardName)
setattr(PIVMETA, "piv_image_type", PIVMETA.pivImageType)
setattr(PIVMETA, "correlation_algorithm", PIVMETA.usesCorrelationAlgorithm)
setattr(PIVMETA, "experimental_image", PIVMETA.ExperimentalImage)
setattr(PIVMETA, "left_right_flip", PIVMETA.LeftRightFlip)
setattr(PIVMETA, "split_image", PIVMETA.SplitImage)
setattr(PIVMETA, "synthetic_image", PIVMETA.SyntheticImage)
setattr(PIVMETA, "top_bottom_flip", PIVMETA.TopBottomFlip)
setattr(PIVMETA, "micro_piv", PIVMETA.micro_piv)
setattr(PIVMETA, "piv", PIVMETA.piv)
setattr(PIVMETA, "piv_first_peak_correlation_coefficient", PIVMETA.piv_first_peak_correlation_coefficient)
setattr(PIVMETA, "ptv", PIVMETA.ptv)
setattr(PIVMETA, "piv_correlation_coefficient", PIVMETA.piv_correlation_coefficient)
setattr(PIVMETA, "piv_second_peak_correlation_coefficient", PIVMETA.piv_second_peak_correlation_coefficient)
setattr(PIVMETA, "piv_third_peak_correlation_coefficient", PIVMETA.piv_third_peak_correlation_coefficient)
setattr(PIVMETA, "first_peak_x_displacement", PIVMETA.first_peak_x_displacement)
setattr(PIVMETA, "first_peak_y_displacement", PIVMETA.first_peak_y_displacement)
setattr(PIVMETA, "piv_flag", PIVMETA.piv_flag)
setattr(PIVMETA, "image_particle_density", PIVMETA.image_particle_density)
setattr(PIVMETA, "image_particle_diameter", PIVMETA.image_particle_diameter)
setattr(PIVMETA, "piv_image_index", PIVMETA.piv_image_index)
setattr(PIVMETA, "inplane_velocity", PIVMETA.inplane_velocity)
setattr(PIVMETA, "laser_sheet_thickness", PIVMETA.laser_sheet_thickness)
setattr(PIVMETA, "mean_seeding_particle_size", PIVMETA.mean_seeding_particle_size)
setattr(PIVMETA, "number_of_particles", PIVMETA.number_of_particles)
setattr(PIVMETA, "laser_pulse_delay", PIVMETA.laser_pulse_delay)
setattr(PIVMETA, "saturated_pixel_number", PIVMETA.saturated_pixel_number)
setattr(PIVMETA, "second_peak_x_displacement", PIVMETA.second_peak_x_displacement)
setattr(PIVMETA, "second_peak_y_displacement", PIVMETA.second_peak_y_displacement)
setattr(PIVMETA, "seeding_material", PIVMETA.seeding_material)
setattr(PIVMETA, "standard_deviation_of_image_particle_diameter", PIVMETA.standard_deviation_of_image_particle_diameter)
setattr(PIVMETA, "third_peak_x_displacement", PIVMETA.third_peak_x_displacement)
setattr(PIVMETA, "third_peak_y_displacement", PIVMETA.third_peak_y_displacement)
setattr(PIVMETA, "relative_time", PIVMETA.relative_time)
setattr(PIVMETA, "velocity", PIVMETA.velocity)
setattr(PIVMETA, "displacement", PIVMETA.displacement)
setattr(PIVMETA, "x_final_interrogation_window_overlap_size", PIVMETA.x_final_interrogation_window_overlap_size)
setattr(PIVMETA, "x_final_interrogation_window_size", PIVMETA.x_final_interrogation_window_size)
setattr(PIVMETA, "x_initial_interrogation_window_size", PIVMETA.x_initial_interrogation_window_size)
setattr(PIVMETA, "x_pixel_coordinate", PIVMETA.x_pixel_coordinate)
setattr(PIVMETA, "y_final_interrogation_window_overlap_size", PIVMETA.y_final_interrogation_window_overlap_size)
setattr(PIVMETA, "y_final_interrogation_window_size", PIVMETA.y_final_interrogation_window_size)
setattr(PIVMETA, "y_initial_interrogation_window_size", PIVMETA.y_initial_interrogation_window_size)
setattr(PIVMETA, "y_pixel_coordinate", PIVMETA.y_pixel_coordinate)
setattr(PIVMETA, "pixel_origin", PIVMETA.pixel_origin)
setattr(PIVMETA, "coordinate", PIVMETA.coordinate)
setattr(PIVMETA, "signal_to_noise_ratio", PIVMETA.signal_to_noise_ratio)
setattr(PIVMETA, "least_square_residual_of_z_displacement_reconstruction", PIVMETA.least_square_residual_of_z_displacement_reconstruction)
setattr(PIVMETA, "piv_scaling_factor", PIVMETA.piv_scaling_factor)
setattr(PIVMETA, "image_filter_kernel_size", PIVMETA.image_filter_kernel_size)