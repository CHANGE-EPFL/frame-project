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
      <p>
        <i
          ><u>Requirements</u>:
          <a href="https://docs.astral.sh/uv/">uv</a> Python package and project
          manager.</i
        >
      </p>
      <p>
        Frame CLI relies on <a href="https://docs.astral.sh/uv/">uv</a> to
        manage Python virtual environments. You need to install it first if you
        don't already have it:
      </p>
      <CopyCommand command="wget -qO- https://astral.sh/uv/install.sh | sh" />
      <p>Then, run the following command to install Frame CLI:</p>
      <CopyCommand
        command="uv tool install git+https://github.com/CHANGE-EPFL/frame-project-cli.git"
      />

      <h2>Usage</h2>
      <p>To see the list of available commands, run:</p>
      <CopyCommand command="frame-cli --help" />
      <p>
        Hybrid model and component pages show which command must be run to
        download and setup specific elements.
      </p>
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
