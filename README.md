# FRAME: A FAIR protocol for hybrid models and data in hydrology

_Contains the raw metadata files of FAIR hybrid models, as well as the source code of the library website for the ETH ORD Explore project FRAME._


## Adding your own metadata

The existing models' and components' metadata files are all stored in [`backend/api/metadata_files/`](https://github.com/CHANGE-EPFL/frame-project/tree/main/backend/api/metadata_files). To contribute with your own metadata, follow these steps.


### Requirements

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/getting-started/installation/) Python package and project manager
- Make


### Steps

To add new hybrid model or component metadata to the FRAME library, follow these steps:

1. Fork and clone the repository.
2. Setup the development environment. This will enable automatic formatting and validation of metadata files.

```bash
make install
```

3. Add or edit metadata files in the [`backend/api/metadata_files/`](https://github.com/CHANGE-EPFL/frame-project/tree/main/backend/api/metadata_files) directory. The files must follow the provided [`backend/api/metadata_files/schema.json`](https://github.com/CHANGE-EPFL/frame-project/blob/main/backend/api/metadata_files/schema.json). Be sure to add this header on top of your `.yaml` for your text editor to provide you with error checks and hints:

```yaml
# yaml-language-server: $schema=schema.json
```

4. Check the validity of the metadata files.

```bash
make test
```

5. Commit your changes. Metadata files will be re-formatted automatically (line breaks, white spaces...).
6. Push your changes to your fork and create a pull request to the `main` branch of the original repository.


## Deploying the website locally

Follow these instructions to run the FRAME website locally and see your changes before deploying.


### Backend

In one shell, run:

```bash
make install  # Only once
make run-backend
```


### Frontend

In another shell, run:

```bash
make run-frontend
```

The website will be available at [http://localhost:9000](http://localhost:9000).


# Deployment details

The following redirections must be set up in the web server:
- `/schema` → https://raw.githubusercontent.com/CHANGE-EPFL/frame-project/refs/heads/main/backend/api/metadata_files/schema.json
- `/cli-doc*` → https://change-epfl.github.io/frame-project-cli*

For example, in Kubernetes, you can add the following to the `ingress.yaml` file:

```yaml
metadata:
  annotations:
    nginx.ingress.kubernetes.io/server-snippet: |
      location ~* ^/schema(/|$) {
        return 301 https://raw.githubusercontent.com/CHANGE-EPFL/frame-project/refs/heads/main/backend/api/metadata_files/schema.json;
      }
      location ~* ^/cli-doc(.*) {
        return 301 https://change-epfl.github.io/frame-project-cli$1;
      }
```
