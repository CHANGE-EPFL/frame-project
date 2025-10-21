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
   * Date when the hybrid model was created. (e.g. 2000-12-31).
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
   * Date when the hybrid model was created. (e.g. 2000-12-31).
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
   * Type of computational environment that can be automatically setup after downloading the model.
   */
  type: string;
  /**
   * List of file paths that contain the target environment description, relative to the repository root. E.g., for 'conda', it could be ['environment.yml'].
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
   * Date when the hybrid model was created. (e.g. 2000-12-31).
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
  computational_environment?:
    | (
        | CondaComputationalEnvironment
        | PythonComputationalEnvironment
        | JuliaComputationalEnvironment
        | ComputationalEnvironment
      )[]
    | null;
  compatible_machine_learning_component_ids: string[];
  compatible_physics_based_component_ids: string[];
  data: DataIO;
  fair_level?: number;
  latest?: boolean;
}
/**
 * Conda computational environment.
 */
export interface CondaComputationalEnvironment {
  /**
   * Conda computational environment that can be automatically setup after downloading the model.
   */
  type: string;
  /**
   * List of file paths that contain the conda environment description, relative to the repository root. E.g., 'environment.yml'.
   */
  file_paths: string[];
}
/**
 * Python computational environment.
 */
export interface PythonComputationalEnvironment {
  /**
   * Python computational environment that can be automatically setup after downloading the model.
   */
  type: string;
  /**
   * List of file paths that contain the python environment description, relative to the repository root. E.g., 'requirements.txt', 'pyproject.toml'.
   */
  file_paths: string[];
}
/**
 * Julia computational environment.
 */
export interface JuliaComputationalEnvironment {
  /**
   * Julia computational environment that can be automatically setup after downloading the model.
   */
  type: string;
  /**
   * List of file paths that contain the julia environment description, relative to the repository root. E.g., 'Project.toml', 'Manifest.toml'.
   */
  file_paths: string[];
}
/**
 * Hybrid model.
 */
export interface HybridModelFromFile {
  /**
   * Date when the hybrid model was created. (e.g. 2000-12-31).
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
  computational_environment?:
    | (
        | CondaComputationalEnvironment
        | PythonComputationalEnvironment
        | JuliaComputationalEnvironment
        | ComputationalEnvironment
      )[]
    | null;
}
/**
 * Contains essential metadata fields for hybrid models.
 */
export interface HybridModelSummary {
  /**
   * Date when the hybrid model was created. (e.g. 2000-12-31).
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
