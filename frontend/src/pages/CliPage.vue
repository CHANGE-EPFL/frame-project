<template>
  <q-page>
    <div class="container">
      <h1>Download the CLI tool</h1>

      <p>
        To download models and components, and to setup environments to run
        those, your can use the dedicated CLI (command-line interface) tool.
      </p>

      <h2>Installation</h2>
      <p>
        <i><u>Requirements</u>: Python 3.10 or higher.</i>
      </p>
      <p>
        We recommend you install the FRAME CLI inside a Python virtual
        environment, for example using
        <a href="https://github.com/astral-sh/uv">uv</a> or
        <a
          href="https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html"
          >conda</a
        >. To install, run the following command in your terminal:
      </p>
      <q-card class="code" dark>
        <code
          >pip install
          git+https://gitlab.com/CHANGE-EPFL/frame-project-cli.git</code
        >
      </q-card>

      <h2>Usage</h2>
      <p>To get hints on how to use the CLI tool, run:</p>
      <q-card class="code" dark>
        <code>frame-cli --help</code>
      </q-card>
      <p>
        Hybrid model and component pages show which command must be run to
        download and setup specific elements.
      </p>
    </div>
  </q-page>
</template>

<style>
.code {
  margin: 1em 0;
  padding: 0.7em;
  font-size: 0.9em;
}
</style>
