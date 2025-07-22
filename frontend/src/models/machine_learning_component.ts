/* tslint:disable */
/* eslint-disable */
/**
/* This file was automatically generated from pydantic models by running pydantic2ts.
/* Do not modify it by hand - just update the pydantic models and then re-run the script
*/

/**
 * Component of hybrid model.
 */
export interface Component {
  /**
   * Summarized description of the unit.
   */
  description: string;
  /**
   * Date when the unit was created. E.g. 2000-12-31. If not provided, will be filled with the associated hybrid model's creation date.
   */
  created?: string | null;
  /**
   * Short name that serves as unique identifier for the unit. Should be all lowercase and contain no spaces(use "_" instead) or special characters.
   */
  id: string;
  /**
   * List of keywords that describe the unit. If not provided, will be filled with the associated hybrid model's keywords.
   */
  keywords?: string[];
  /**
   * Full name of the unit.
   */
  name: string;
  contributors?: string[];
  documentation?: string[] | null;
  identifier?: string | null;
  license?: string | null;
  readme?: string | null;
  url?: string | null;
  version?: string | null;
  latest?: boolean;
}
/**
 * Component of hybrid model.
 */
export interface ComponentFromFile {
  /**
   * Summarized description of the unit.
   */
  description: string;
  /**
   * Date when the unit was created. E.g. 2000-12-31. If not provided, will be filled with the associated hybrid model's creation date.
   */
  created?: string | null;
  /**
   * Short name that serves as unique identifier for the unit. Should be all lowercase and contain no spaces(use "_" instead) or special characters.
   */
  id: string;
  /**
   * List of keywords that describe the unit. If not provided, will be filled with the associated hybrid model's keywords.
   */
  keywords?: string[];
  /**
   * Full name of the unit.
   */
  name: string;
  contributors?: string[];
  documentation?: string[] | null;
  identifier?: string | null;
  license?: string | null;
  readme?: string | null;
  url?: string | null;
  version?: string | null;
}
/**
 * Reference to an existing component of a hybrid model.
 */
export interface ComponentReference {
  id: string;
}
/**
 * Essential metadata fields for hybrid model components.
 */
export interface ComponentSummary {
  /**
   * Summarized description of the unit.
   */
  description: string;
  /**
   * Date when the unit was created. E.g. 2000-12-31.
   */
  created?: string | null;
  /**
   * Short name that serves as unique identifier for the unit. Should be all lowercase and contain no spaces(use "_" instead) or special characters.
   */
  id: string;
  /**
   * List of keywords that describe the unit.
   *
   * @minItems 1
   */
  keywords: [string, ...string[]];
  /**
   * Full name of the unit.
   */
  name: string;
}
/**
 * Computational resources need for a hybrid model or component.
 */
export interface ComputationalResources {
  cpus?: Cpu[];
  gpus?: Gpu[];
  memory?: string | null;
  storage?: string | null;
  software?: string[] | null;
  operating_system?: string | null;
  compute_time?: string | null;
}
/**
 * Central processing unit (CPU) metadata.
 */
export interface Cpu {
  model: string;
  count?: number;
  manufacturer?: string | null;
  cores?: number | null;
  threads?: number | null;
  cache?: string | null;
  clock_speed?: string | null;
}
/**
 * Graphics processing unit (GPU) metadata.
 */
export interface Gpu {
  model: string;
  count?: number;
  manufacturer?: string | null;
  memory?: string | null;
  memory_bandwidth?: string | null;
  clock_speed?: string | null;
  cuda_cores?: number | null;
  tensor_cores?: number | null;
  rt_cores?: number | null;
  ray_tracing?: boolean | null;
}
/**
 * Machine learning component.
 */
export interface MachineLearningComponent {
  /**
   * Summarized description of the unit.
   */
  description: string;
  /**
   * Date when the unit was created. E.g. 2000-12-31. If not provided, will be filled with the associated hybrid model's creation date.
   */
  created?: string | null;
  /**
   * Short name that serves as unique identifier for the unit. Should be all lowercase and contain no spaces(use "_" instead) or special characters.
   */
  id: string;
  /**
   * List of keywords that describe the unit. If not provided, will be filled with the associated hybrid model's keywords.
   */
  keywords?: string[];
  /**
   * Full name of the unit.
   */
  name: string;
  contributors?: string[];
  documentation?: string[] | null;
  identifier?: string | null;
  license?: string | null;
  readme?: string | null;
  url?: string | null;
  version?: string | null;
  ml_process?: string | null;
  neural_networks?: NeuralNetwork[] | null;
  latest?: boolean;
}
/**
 * Neural network metadata.
 */
export interface NeuralNetwork {
  name: string;
  type?: string | null;
  layer_count?: number | null;
  node_count?: number | null;
  batch_size?: number | null;
  learning_rate?: number | null;
  predictor_count?: number | null;
  activation_functions?: string[] | null;
  input_scaling?: string | null;
  initialization?: string | null;
  loss_function?: string | null;
  regularization?: string | null;
  optimization_method?: string | null;
  host_physics_model?: string | null;
  target_variables?: string[] | null;
  training_requirements?: TrainingRequirements | null;
  training_resources?: ComputationalResources | null;
}
/**
 * Training requirements for a machine learning component.
 */
export interface TrainingRequirements {
  gpu?: boolean;
  cpu?: boolean;
}
/**
 * Machine learning component.
 */
export interface MachineLearningComponentFromFile {
  /**
   * Summarized description of the unit.
   */
  description: string;
  /**
   * Date when the unit was created. E.g. 2000-12-31. If not provided, will be filled with the associated hybrid model's creation date.
   */
  created?: string | null;
  /**
   * Short name that serves as unique identifier for the unit. Should be all lowercase and contain no spaces(use "_" instead) or special characters.
   */
  id: string;
  /**
   * List of keywords that describe the unit. If not provided, will be filled with the associated hybrid model's keywords.
   */
  keywords?: string[];
  /**
   * Full name of the unit.
   */
  name: string;
  contributors?: string[];
  documentation?: string[] | null;
  identifier?: string | null;
  license?: string | null;
  readme?: string | null;
  url?: string | null;
  version?: string | null;
  ml_process?: string | null;
  neural_networks?: NeuralNetwork[] | null;
}
/**
 * Reference to an existing machine learning component.
 */
export interface MachineLearningComponentReference {
  id: string;
}
/**
 * Essential metadata fields for machine learning components.
 */
export interface MachineLearningComponentSummary {
  /**
   * Summarized description of the unit.
   */
  description: string;
  /**
   * Date when the unit was created. E.g. 2000-12-31.
   */
  created?: string | null;
  /**
   * Short name that serves as unique identifier for the unit. Should be all lowercase and contain no spaces(use "_" instead) or special characters.
   */
  id: string;
  /**
   * List of keywords that describe the unit.
   *
   * @minItems 1
   */
  keywords: [string, ...string[]];
  /**
   * Full name of the unit.
   */
  name: string;
}
