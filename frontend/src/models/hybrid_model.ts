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
  url?: string | null;
  version?: string | number | null;
}
/**
 * Essential metadata fields for hybrid models.
 */
export interface CommonMetadataSummary {
  description: string;
  created?: string | null;
  /**
   * @minItems 1
   */
  keywords: [string, ...string[]];
  name: string;
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
  /**
   * @minItems 1
   */
  keywords: [string, ...string[]];
  name: string;
  id: number;
  short_name: string;
  /**
   * @minItems 1
   */
  contributors: [string, ...string[]];
  documentation?: string[] | null;
  identifier?: string | null;
  license?: string | null;
  url?: string | null;
  version?: string | number | null;
  ml_process?: string | null;
  host_physics?: string | null;
  latent_variables?: Data[];
  compatible_machine_learning_component_ids: number[];
  compatible_physical_based_component_ids: number[];
  data: DataIO;
}
/**
 * Hybrid model, without assigned id.
 */
export interface HybridModelFromFile {
  description: string;
  created?: string | null;
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
  url?: string | null;
  version?: string | number | null;
  ml_process?: string | null;
  host_physics?: string | null;
  latent_variables?: Data[];
}
/**
 * Contains essential metadata fields for hybrid models.
 */
export interface HybridModelSummary {
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
