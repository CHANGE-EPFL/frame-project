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
  description: string;
  created?: string | null;
  keywords?: string[];
  name: string;
  id: number;
  short_name: string;
  contributors?: string[];
  documentation?: string[] | null;
  identifier?: string | null;
  license?: string | null;
  readme?: string | null;
  url?: string | null;
  version?: string | number | null;
}
/**
 * Component of hybrid model, without assigned id.
 */
export interface ComponentFromFile {
  description: string;
  created?: string | null;
  keywords?: string[];
  name: string;
  contributors?: string[];
  documentation?: string[] | null;
  identifier?: string | null;
  license?: string | null;
  readme?: string | null;
  url?: string | null;
  version?: string | number | null;
  short_name?: string | null;
}
/**
 * Essential metadata fields for hybrid model components.
 */
export interface ComponentSummary {
  description: string;
  created?: string | null;
  /**
   * @minItems 1
   */
  keywords: [string, ...string[]];
  name: string;
  id: number;
  short_name: string;
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
  description: string;
  created?: string | null;
  keywords?: string[];
  name: string;
  id: number;
  short_name: string;
  contributors?: string[];
  documentation?: string[] | null;
  identifier?: string | null;
  license?: string | null;
  readme?: string | null;
  url?: string | null;
  version?: string | number | null;
  ml_process?: string | null;
  neural_networks?: NeuralNetwork[] | null;
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
 * Machine learning component, without assigned id.
 */
export interface MachineLearningComponentFromFile {
  description: string;
  created?: string | null;
  keywords?: string[];
  name: string;
  contributors?: string[];
  documentation?: string[] | null;
  identifier?: string | null;
  license?: string | null;
  readme?: string | null;
  url?: string | null;
  version?: string | number | null;
  short_name?: string | null;
  ml_process?: string | null;
  neural_networks?: NeuralNetwork[] | null;
}
/**
 * Essential metadata fields for machine learning components.
 */
export interface MachineLearningComponentSummary {
  description: string;
  created?: string | null;
  /**
   * @minItems 1
   */
  keywords: [string, ...string[]];
  name: string;
  id: number;
  short_name: string;
}
