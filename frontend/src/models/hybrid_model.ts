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
  /**
   * Date when the hybrid was created. (e.g. 2000-12-31).
   */
  created?: string | null;
  /**
   * Summarized description of the hybrid model. Can be formatted with HTML tags.
   */
  description: string;
  /**
   * Indicates whether the hybrid model is hidden within the FRAME library. Hidden models remain accessible if their ID is known.
   */
  hidden?: boolean;
  /**
   * Short name that serves as unique identifier for the hybrid model. Should be all lowercase and contain no spaces (use "_" instead) or special characters.
   */
  id: string;
  /**
   * List of keywords that describe the hybrid model.
   *
   * @minItems 1
   */
  keywords: [string, ...string[]];
  /**
   * Full name of the hybrid model.
   */
  name: string;
  /**
   * List of contributor names.
   *
   * @minItems 1
   */
  contributors: [string, ...string[]];
  /**
   * List of URLs or DOIs for documentation.
   */
  documentation?: string[] | null;
  /**
   * Digital Object Identifier (DOI).
   */
  identifier?: string | null;
  /**
   * License short name.
   */
  license?: string | null;
  /**
   * URL to a Markdown README file.
   */
  readme?: string | null;
  /**
   * Repository URL.
   */
  url: string;
  /**
   * Semantic version.
   */
  version?: string | null;
}
/**
 * Essential metadata fields for hybrid models.
 */
export interface CommonMetadataSummary {
  /**
   * Date when the hybrid was created. (e.g. 2000-12-31).
   */
  created?: string | null;
  /**
   * Summarized description of the hybrid model. Can be formatted with HTML tags.
   */
  description: string;
  /**
   * Indicates whether the hybrid model is hidden within the FRAME library. Hidden models remain accessible if their ID is known.
   */
  hidden?: boolean;
  /**
   * Short name that serves as unique identifier for the hybrid model. Should be all lowercase and contain no spaces (use "_" instead) or special characters.
   */
  id: string;
  /**
   * List of keywords that describe the hybrid model.
   *
   * @minItems 1
   */
  keywords: [string, ...string[]];
  /**
   * Full name of the hybrid model.
   */
  name: string;
}
/**
 * Description of a computational environment.
 */
export interface ComputationalEnvironment {
  /**
   * Type of the computational environment that could be automatically setup after downloading the model.
   */
  type: 'conda' | 'python_requirements' | 'pyproject_toml';
  /**
   * List of file paths that contain the environment description, relative to the repository root.
   */
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
  /**
   * Date when the hybrid was created. (e.g. 2000-12-31).
   */
  created?: string | null;
  /**
   * Summarized description of the hybrid model. Can be formatted with HTML tags.
   */
  description: string;
  /**
   * Indicates whether the hybrid model is hidden within the FRAME library. Hidden models remain accessible if their ID is known.
   */
  hidden?: boolean;
  /**
   * Short name that serves as unique identifier for the hybrid model. Should be all lowercase and contain no spaces (use "_" instead) or special characters.
   */
  id: string;
  /**
   * List of keywords that describe the hybrid model.
   *
   * @minItems 1
   */
  keywords: [string, ...string[]];
  /**
   * Full name of the hybrid model.
   */
  name: string;
  /**
   * List of contributor names.
   *
   * @minItems 1
   */
  contributors: [string, ...string[]];
  /**
   * List of URLs or DOIs for documentation.
   */
  documentation?: string[] | null;
  /**
   * Digital Object Identifier (DOI).
   */
  identifier?: string | null;
  /**
   * License short name.
   */
  license?: string | null;
  /**
   * URL to a Markdown README file.
   */
  readme?: string | null;
  /**
   * Repository URL.
   */
  url: string;
  /**
   * Semantic version.
   */
  version?: string | null;
  ml_process?: string | null;
  host_physics?: string | null;
  latent_variables?: Data[];
  computational_environment?: ComputationalEnvironment[] | null;
  compatible_machine_learning_component_ids: string[];
  compatible_physics_based_component_ids: string[];
  data: DataIO;
  fair_level?: number;
  latest?: boolean;
}
/**
 * Hybrid model.
 */
export interface HybridModelFromFile {
  /**
   * Date when the hybrid was created. (e.g. 2000-12-31).
   */
  created?: string | null;
  /**
   * Summarized description of the hybrid model. Can be formatted with HTML tags.
   */
  description: string;
  /**
   * Indicates whether the hybrid model is hidden within the FRAME library. Hidden models remain accessible if their ID is known.
   */
  hidden?: boolean;
  /**
   * Short name that serves as unique identifier for the hybrid model. Should be all lowercase and contain no spaces (use "_" instead) or special characters.
   */
  id: string;
  /**
   * List of keywords that describe the hybrid model.
   *
   * @minItems 1
   */
  keywords: [string, ...string[]];
  /**
   * Full name of the hybrid model.
   */
  name: string;
  /**
   * List of contributor names.
   *
   * @minItems 1
   */
  contributors: [string, ...string[]];
  /**
   * List of URLs or DOIs for documentation.
   */
  documentation?: string[] | null;
  /**
   * Digital Object Identifier (DOI).
   */
  identifier?: string | null;
  /**
   * License short name.
   */
  license?: string | null;
  /**
   * URL to a Markdown README file.
   */
  readme?: string | null;
  /**
   * Repository URL.
   */
  url: string;
  /**
   * Semantic version.
   */
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
  /**
   * Date when the hybrid was created. (e.g. 2000-12-31).
   */
  created?: string | null;
  /**
   * Summarized description of the hybrid model. Can be formatted with HTML tags.
   */
  description: string;
  /**
   * Indicates whether the hybrid model is hidden within the FRAME library. Hidden models remain accessible if their ID is known.
   */
  hidden?: boolean;
  /**
   * Short name that serves as unique identifier for the hybrid model. Should be all lowercase and contain no spaces (use "_" instead) or special characters.
   */
  id: string;
  /**
   * List of keywords that describe the hybrid model.
   *
   * @minItems 1
   */
  keywords: [string, ...string[]];
  /**
   * Full name of the hybrid model.
   */
  name: string;
}
