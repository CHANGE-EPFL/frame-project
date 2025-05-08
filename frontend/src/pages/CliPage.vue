<template>
  <q-page>
    <div class="container">
      <h1>Download the CLI tool</h1>

      <p>
        To download models and components, and to setup environments to run
        those, your can use the dedicated CLI (command-line interface)
        <a href="https://github.com/CHANGE-EPFL/frame-project-cli">tool</a>.
      </p>

      <h2>Installation</h2>

      <h3>Requirements</h3>

      <ul>
        <li>
          <a href="https://docs.astral.sh/uv/">uv</a> Python package and project
          manager
        </li>
        <li><a href="https://git-scm.com/">git</a> version control system</li>
      </ul>

      <p>
        Frame CLI relies on <a href="https://docs.astral.sh/uv/">uv</a> to
        manage Python virtual environments. You need to install it first if you
        don't already have it. Refer to the official
        <a href="https://docs.astral.sh/uv/getting-started/installation/"
          >uv documentation</a
        >.
      </p>
      <p>Then, run the following command to install Frame CLI:</p>
      <CopyCommand command="uv tool install frame-cli" />

      <h2>Usage</h2>
      <p>To see the list of available commands, run:</p>
      <CopyCommand command="frame --help" />
      <p>
        Hybrid model and component pages show which command must be run to
        download and setup specific units.
      </p>

      <p>
        You may want to install autocompletion for easier usage. To do so, run:
      </p>
      <CopyCommand command="frame --install-completion" />

      <h2>Uninstall</h2>
      <p>To remove the CLI tool from your system, run the following command:</p>
      <CopyCommand command="uv tool uninstall frame-cli" />
    </div>
  </q-page>
</template>

<script setup lang="ts">
import CopyCommand from 'src/components/CopyCommand.vue';
</script>

<style>
.code {
  margin: 1em 0;
  padding: 0.7em;
  font-size: 0.9em;
}
</style>
