<template>
  <q-page>
    <div class="container">
      <h1>
        FRAME: A Findable, Accessible, Interoperable, and Reproducible Protocol
        for Hybrid Hydrological Models
      </h1>

      <h2>1.1. Overview</h2>

      FRAME consists of a set of guidelines for developers of hybrid
      hydrological and ecohydrological models to make their models findable,
      accessible, interoperable, and reproducible (FAIR). Here, hybrid models
      are defined as models which embed a machine learning model within a host
      physics-based model. Specifically, the protocol provides guidelines on
      four different aspects of the model: a) Code and Data standards, b)
      Metadata, c) Ancillary Tools, and d) Documentation (Fig. 1). The current
      version of the protocol provides a <em>minimum</em> set of specifications
      for making a hybrid model FAIR. The current version is based on the first
      protocol design workshop held at the EPFL campus (September 25–26 2024).
      Adopting the protocol will ensure that the hybrid model satisfies the
      requirements of a FAIR research software (FAIR4RS) laid out in
      <a href="https://doi.org/10.1038/s41597-022-01710-x"
        >Barker et al. (2022)</a
      >.

      <h2>1.2 Guidelines</h2>

      <h3>1.2.1. Code and Data Standards</h3>

      <ol>
        <li>
          <strong>Persistent Identifier</strong> – An unique digital object
          identifier (DOI) must be assigned to a) the physics-based model, b)
          the machine learning-based sub-module, and c) the hybrid model as a
          whole (if applicable). As machine learning models are subject to
          higher frequency of updates, not every version of the machine learning
          model needs to have a DOI. Widely used repositories which assign DOIs
          to software such as <a href="https://zenodo.org/">zenodo</a> or
          <a href="https://codeocean.com/">code ocean</a> is suggested.
        </li>
        <li>
          <strong>Licensing</strong> – A hybrid model can be considered FAIR if
          both the physics-based and machine learning-based components of the
          model are <em>open source</em>. Highly permissive licences such as the
          <a href="https://opensource.org/license/bsd-3-clause"
            >Berkeley Source Distribution</a
          >
          (BSD),
          <a href="https://opensource.org/license/mit"
            >Massachusetts Institute of Technology</a
          >
          (MIT), or
          <a href="https://opensource.org/license/apache-2-0">Apache</a> are
          suggested. For a detailed overview of open source licences, the
          developers are referred to
          <a href="https://opensource.org/licenses"
            >https://opensource.org/licenses</a
          >
          or
          <a href="https://spdx.org/licenses/">https://spdx.org/licenses/</a>.
        </li>
        <li>
          <strong>Version control</strong> – Strict version control of both the
          physics-based and machine learning model must be imposed. To achieve
          this, a version control tool such as git is suggested. The model
          should be hosted in an online git platform such as
          <a href="https://github.com/">GitHub</a>,
          <a
            href="https://about.gitlab.com/free-trial/devsecops/?utm_medium=cpc&utm_source=google&utm_campaign=nb_competitors_emea_exact&utm_content=free-trial&utm_term=github&_bt=663185439321&_bk=github&_bm=e&_bn=g&_bg=150558745636&gad_source=1&gclid=CjwKCAjwyfe4BhAWEiwAkIL8sJZ7ibPvV9FjAAuuDKQOMt7j7ZqysUDvdoJA3RysUoBRQHJMLPDJdRoCKdEQAvD_BwE"
            >Gitlab</a
          >
          or similar. For specific versions of the model which will be
          published, these platforms enable seamless communication with
          repositories which assign DOIs such as zenodo.
        </li>
        <li>
          <strong>Input and Output data standard</strong> – All input and output
          data must be in a format which is compatible with FAIR data principles
          (<a href="https://www.nature.com/articles/sdata201618"
            >Wilkinson et al. 2016</a
          >). For this, the
          <a href="https://www.unidata.ucar.edu/software/netcdf/"
            >network Common Data Form</a
          >
          (netCDF) data format is suggested. For both the input and output
          datasets, a set of minimum attributes which adhere to the
          <a href="https://cfconventions.org/">CF metadata standard</a> is
          described in Appendix I. In the future, migration to newer,
          cloud-native formats such as zarr can be explored.
        </li>
        <li>
          <strong>Modularity</strong> – A minimum requirement of modularity is
          imposed. At the most basic level, the physics-based and machine
          learning-based model should be independent of each other i.e., they
          can be run separately. Within the physics-based model, the functions
          representing the main physical processes should be modular i.e. they
          can be run independently of the full model. This involves abstracting
          all the dependent parameters and functions from the main model.
        </li>
        <li>
          <strong>Explainability</strong> – As machine learning models are
          'black box' in nature, some details of the model which enable the
          users to explain the model results are required at a minimum. This
          could be a) explicitly packaging explainable AI (XAI) tools with the
          model such as
          <a href="https://en.wikipedia.org/wiki/Shapley_value"
            >Shapley values</a
          >
          or
          <a
            href="https://www.tensorflow.org/tutorials/interpretability/integrated_gradients"
            >Integrated gradients</a
          >, b) explicitly explaining the physical reasoning or logic behind the
          selection of the predictors in either the model code or metadata, or
          c) metamorphic testing approaches which enable qualitative evaluation
          of hybrid models (<a
            href="https://hess.copernicus.org/articles/28/2505/2024/"
            >Reichert et al. 2024</a
          >).
        </li>
        <li>
          <strong>Interoperability</strong> – In the version of the protocol, no
          requirements on interoperability are imposed. In the long-term,
          interoperability of machine learning models with different
          physics-based models is desirable. However, currently technical
          barriers, primarily due to different programming languages in which
          physics-based and machine learning-based models are written in,
          preclude full interoperability.
        </li>
      </ol>

      <h3>1.2.2. Metadata Specifications</h3>

      <ol>
        <li>
          Detailed metadata specifications which fully describe the
          physics-based and machine learning-based components of the hybrid
          model are required for the hybrid model to be termed FAIR.
        </li>
        <li>
          To ensure that the metadata is both human and machine readable, the
          <a href="https://www.redhat.com/en/topics/automation/what-is-yaml"
            >.yaml format</a
          >
          is suggested.
        </li>
        <li>
          A minimum set of metadata specifications which are needed to
          adequately describe the physics-based and machine learning-based
          components of the hybrid model is provided in the form of a template
          in the
          <a
            href="https://github.com/CHANGE-EPFL/frame-project/blob/main/backend/api/metadata_files/template.yaml"
            >FRAME GitHub repository</a
          >.
        </li>
      </ol>

      <h3>1.2.3. Ancillary Software Tools</h3>

      <ol>
        <li>
          A repository for hybrid models which can host both the physics and
          machine learning-based components.
        </li>
        <li>
          A command line tool to interface with the repository aimed at both the
          model developers and users to upload and download models.
        </li>
      </ol>

      <h3>1.2.4. Documentation</h3>

      <ol>
        <li>
          A detailed documentation of the hybrid model and both its
          physics-based and machine learning-based components are necessary for
          the model to be termed FAIR.
        </li>
        <li>
          The documentation should have a quickstart guide which enables the
          user to install and run a test case of the model.
        </li>
        <li>
          The documentation should have a detailed description of all the
          functions. To facilitate this, automatic documentation generation
          tools similar to docstrings (<a
            href="https://www.geeksforgeeks.org/python-docstrings/"
            >https://www.geeksforgeeks.org/python-docstrings/</a
          >) common in programming languages such as Python are suggested.
        </li>
      </ol>

      <h2 id="references">References</h2>

      <ul>
        <li>
          <a href="https://doi.org/10.1038/s41597-022-01710-x"
            >Barker, M., Chue Hong, N.P., Katz, D.S. et al. Introducing the FAIR
            Principles for research software. Sci Data 9, 622 (2022).</a
          >
        </li>
        <li>
          <a href="https://doi.org/10.5194/hess-28-2505-2024"
            >Reichert, P., Ma, K., Höge, M., et al. Metamorphic testing of
            machine learning and conceptual hydrologic models, Hydrol. Earth
            Syst. Sci. 28, 2505–2529 (2024).</a
          >
        </li>
        <li>
          <a href="https://doi.org/10.1038/sdata.2016.18"
            >Wilkinson, M., Dumontier, M., Aalbersberg, I. et al. The FAIR
            Guiding Principles for scientific data management and stewardship.
            Sci Data 3, 160018 (2016).</a
          >
        </li>
      </ul>

      <h2>
        Appendix I. Minimum set of netCDF metadata for different input and
        output variables (to be updated)
      </h2>
    </div>
  </q-page>
</template>
