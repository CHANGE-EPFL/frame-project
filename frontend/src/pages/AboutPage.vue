<template>
  <q-page>
    <div class="container">
      <h1>About</h1>
      <h2 id="fair-level">FAIR level</h2>
      <h3>What are FAIR principles for research software?</h3>

      <p>
        FAIR stands for Findable, Accessible, Interoperable, and Reusable. These
        set of principles were originally devised for qualifying
        <a href="http://dx.doi.org/10.1038/sdata.2016.18">scientific data</a>,
        to ensure that it is properly managed and reusable by others. They have
        been adapted for
        <a href="https://doi.org/10.1038/s41597-022-01710-x"
          >research software</a
        >
        with the branding FAIR4RS. The summarized principles are:
      </p>
      <q-list>
        <q-item>
          <q-item-section>
            <q-item-label><strong>F: Findable</strong></q-item-label>
            <q-item-label
              >Software, and its associated metadata, is easy for both humans
              and machines to find.</q-item-label
            >
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label><strong>A: Accessible</strong></q-item-label>
            <q-item-label
              >Software, and its metadata, is retrievable via standardised
              protocols.</q-item-label
            >
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label><strong>I: Interoperable</strong></q-item-label>
            <q-item-label
              >Software interoperates with other software by exchanging data
              and/or metadata, and/or through interaction via application
              programming interfaces (APIs), described through
              standards.</q-item-label
            >
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label><strong>R: Reusable</strong></q-item-label>
            <q-item-label
              >Software is both usable (can be executed) and reusable (can be
              understood, modified, built upon, or incorporated into other
              software).</q-item-label
            >
          </q-item-section>
        </q-item>
      </q-list>

      <h3>How is the FAIR level computed?</h3>
      <!-- Match to FAIR_LEVEL_PROPERTIES in backend/api/services/metadata.py -->
      <p>
        The FAIR level is computed based on the presence of specific metadata
        fields in the FRAME metadata file for each hybrid model. The FAIR level
        ranges from 1 to 5, with each level requiring the presence of certain
        metadata fields as outlined below.
      </p>
      <h4>Level 1</h4>
      <q-list>
        <q-item>
          <q-item-section>
            <q-item-label
              ><q-chip dense class="level-chip">metadata</q-chip></q-item-label
            >
            <q-item-label caption
              >Have a valid
              <router-link to="/contribute">FRAME metadata file</router-link
              >.</q-item-label
            >
          </q-item-section>
        </q-item>
      </q-list>

      <h4>Level 2</h4>
      <q-list>
        <q-item>
          <q-item-section>
            <q-item-label
              ><q-chip dense class="level-chip">created</q-chip></q-item-label
            >
            <q-item-label caption
              >Date when the hybrid model was created.</q-item-label
            >
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label
              ><q-chip dense class="level-chip"
                >description</q-chip
              ></q-item-label
            >
            <q-item-label caption
              >Summarized description of the hybrid model.</q-item-label
            >
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label
              ><q-chip dense class="level-chip"
                >identifier</q-chip
              ></q-item-label
            >
            <q-item-label caption
              >Digital Object Identifier (DOI).</q-item-label
            >
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label
              ><q-chip dense class="level-chip">license</q-chip></q-item-label
            >
            <q-item-label caption>License short name.</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label
              ><q-chip dense class="level-chip">url</q-chip></q-item-label
            >
            <q-item-label caption>Repository URL.</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>

      <h4>Level 3</h4>
      <q-list>
        <q-item>
          <q-item-section>
            <q-item-label
              ><q-chip dense class="level-chip"
                >host_physics</q-chip
              ></q-item-label
            >
            <q-item-label caption
              >Host physics description for the hybrid model.</q-item-label
            >
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label
              ><q-chip dense class="level-chip"
                >latent_variables</q-chip
              ></q-item-label
            >
            <q-item-label caption
              >List of latent variables and their properties.</q-item-label
            >
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label
              ><q-chip dense class="level-chip"
                >ml_process</q-chip
              ></q-item-label
            >
            <q-item-label caption
              >Description of the machine learning process.</q-item-label
            >
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label
              ><q-chip dense class="level-chip">readme</q-chip></q-item-label
            >
            <q-item-label caption>URL to a Markdown README file.</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>

      <h4>Level 4</h4>
      <q-list>
        <q-item>
          <q-item-section>
            <q-item-label
              ><q-chip dense class="level-chip"
                >computational_environment</q-chip
              ></q-item-label
            >
            <q-item-label caption
              >Description of the computational environment(s) required to run
              the model.</q-item-label
            >
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label
              ><q-chip dense class="level-chip"
                >data.inputs</q-chip
              ></q-item-label
            >
            <q-item-label caption
              >List of input data fields and their properties.</q-item-label
            >
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label
              ><q-chip dense class="level-chip"
                >data.outputs</q-chip
              ></q-item-label
            >
            <q-item-label caption
              >List of output data fields and their properties.</q-item-label
            >
          </q-item-section>
        </q-item>
      </q-list>

      <h4>Level 5</h4>
      <q-list>
        <q-item>
          <q-item-section>
            <q-item-label
              ><q-chip dense class="level-chip"
                >documentation</q-chip
              ></q-item-label
            >
            <q-item-label caption
              >List of URLs or DOIs for documentation.</q-item-label
            >
          </q-item-section>
        </q-item>
      </q-list>
    </div>
  </q-page>
</template>

<style scoped>
.level-chip {
  font-family: 'Fira Mono', 'Menlo', 'Consolas', monospace;
  font-size: 0.85em;
  display: inline-block;
  transform: translateY(-0.2em);
}
</style>
