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
  contributors?: string[];
  documentation?: string[] | null;
  id: string;
  identifier?: string | null;
  license?: string | null;
  readme?: string | null;
  url?: string | null;
  version?: string | number | null;
}
/**
 * Component of hybrid model.
 */
export interface ComponentFromFile {
  description: string;
  created?: string | null;
  keywords?: string[];
  name: string;
  contributors?: string[];
  documentation?: string[] | null;
  id: string;
  identifier?: string | null;
  license?: string | null;
  readme?: string | null;
  url?: string | null;
  version?: string | number | null;
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
  description: string;
  created?: string | null;
  /**
   * @minItems 1
   */
  keywords: [string, ...string[]];
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
 * Physics-based component.
 */
export interface PhysicsBasedComponent {
  description: string;
  created?: string | null;
  keywords?: string[];
  name: string;
  contributors?: string[];
  documentation?: string[] | null;
  id: string;
  identifier?: string | null;
  license?: string | null;
  readme?: string | null;
  url?: string | null;
  version?: string | number | null;
  type?: string | null;
  fixed_parameters_count?: number | null;
  tunable_parameters_count?: number | null;
  state_variables_count?: number | null;
  temporal_coverage?: string | null;
  spatial_coverage?: string | null;
  spatial_resolution?: string | null;
  temporal_resolution?: string | null;
  vertical_discretization?: VerticalDiscretization | null;
  lateral_flow?: boolean | null;
  related_identifiers?: string[] | null;
  testing_resources?: ComputationalResources | null;
}
/**
 * Vertical discretization of a physics-based component.
 */
export interface VerticalDiscretization {
  soil?: string | null;
  vegetation?: string | null;
}
/**
 * Physics-based component.
 */
export interface PhysicsBasedComponentFromFile {
  description: string;
  created?: string | null;
  keywords?: string[];
  name: string;
  contributors?: string[];
  documentation?: string[] | null;
  id: string;
  identifier?: string | null;
  license?: string | null;
  readme?: string | null;
  url?: string | null;
  version?: string | number | null;
  type?: string | null;
  fixed_parameters_count?: number | null;
  tunable_parameters_count?: number | null;
  state_variables_count?: number | null;
  temporal_coverage?: string | null;
  spatial_coverage?: string | null;
  spatial_resolution?: string | null;
  temporal_resolution?: string | null;
  vertical_discretization?: VerticalDiscretization | null;
  lateral_flow?: boolean | null;
  related_identifiers?: string[] | null;
  testing_resources?: ComputationalResources | null;
}
/**
 * Reference to an existing physics-based component.
 */
export interface PhysicsBasedComponentReference {
  id: string;
}
/**
 * Essential metadata fields for physics-based components.
 */
export interface PhysicsBasedComponentSummary {
  description: string;
  created?: string | null;
  /**
   * @minItems 1
   */
  keywords: [string, ...string[]];
  name: string;
}
