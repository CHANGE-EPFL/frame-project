/* tslint:disable */
/* eslint-disable */
/**
/* This file was automatically generated from pydantic models by running pydantic2ts.
/* Do not modify it by hand - just update the pydantic models and then re-run the script
*/

/**
 * Common metadata fields for hybrid models.
 */
export interface CommonMetadata {
  description: string;
  created?: string | null;
  id: string;
  /**
   * @minItems 1
   */
  keywords: [string, ...string[]];
  name: string;
  /**
   * @minItems 1
   */
  contributors: [string, ...string[]];
  documentation?: string[] | null;
  identifier?: string | null;
  license?: string | null;
  readme?: string | null;
  url?: string | null;
  version?: string | null;
}
/**
 * Essential metadata fields for hybrid models.
 */
export interface CommonMetadataSummary {
  description: string;
  created?: string | null;
  id: string;
  /**
   * @minItems 1
   */
  keywords: [string, ...string[]];
  name: string;
}
/**
 * Description of a computational environment.
 */
export interface ComputationalEnvironment {
  type: "conda" | "python_requirements" | "pyproject_toml";
  file_paths: string[];
}
/**
 * Data structure for input and output data.
 */
export interface Data {
  name: string;
  encoding_format?: string | null;
  identifier?: string | null;
  url?: string | null;
  quality?: number | string | null;
  units?: string | null;
  precision?: string | null;
  scale?: number | null;
  offset?: number | null;
  description?: string | null;
  min_value?: number | null;
  max_value?: number | null;
  temporal_coverage?: string | null;
  spatial_coverage?: string | null;
  spatial_resolution?: string | null;
  temporal_resolution?: string | null;
}
/**
 * Collection of input and output data for a hybrid model.
 */
export interface DataIO {
  inputs?: Data[];
  outputs?: Data[];
}
/**
 * Hybrid model.
 */
export interface HybridModel {
  description: string;
  created?: string | null;
  id: string;
  /**
   * @minItems 1
   */
  keywords: [string, ...string[]];
  name: string;
  /**
   * @minItems 1
   */
  contributors: [string, ...string[]];
  documentation?: string[] | null;
  identifier?: string | null;
  license?: string | null;
  readme?: string | null;
  url?: string | null;
  version?: string | null;
  ml_process?: string | null;
  host_physics?: string | null;
  latent_variables?: Data[];
  computational_environment?: ComputationalEnvironment[] | null;
  compatible_machine_learning_component_ids: string[];
  compatible_physics_based_component_ids: string[];
  data: DataIO;
  latest?: boolean;
}
/**
 * Hybrid model.
 */
export interface HybridModelFromFile {
  description: string;
  created?: string | null;
  id: string;
  /**
   * @minItems 1
   */
  keywords: [string, ...string[]];
  name: string;
  /**
   * @minItems 1
   */
  contributors: [string, ...string[]];
  documentation?: string[] | null;
  identifier?: string | null;
  license?: string | null;
  readme?: string | null;
  url?: string | null;
  version?: string | null;
  ml_process?: string | null;
  host_physics?: string | null;
  latent_variables?: Data[];
  computational_environment?: ComputationalEnvironment[] | null;
}
/**
 * Contains essential metadata fields for hybrid models.
 */
export interface HybridModelSummary {
  description: string;
  created?: string | null;
  id: string;
  /**
   * @minItems 1
   */
  keywords: [string, ...string[]];
  name: string;
}
