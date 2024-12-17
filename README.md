# FRAME: A FAIR protocol for hybrid models and data in hydrology

_Contains the raw metadata files of FAIR hybrid models, as well as the source code of the library website for the ETH ORD Explore project FRAME._


## Contributing

### Requirements

- Python 3.10 or higher
- [Poetry](https://python-poetry.org/) (`pip install poetry`)
- Make


### Steps

To add a new hybrid model or component to the FRAME library, follow these steps:

1. Fork and clone the repository.
2. Setup the development environment. This will enable automatic formatting and validation of metadata files.

```bash
make install
```

3. Add or edit metadata files in the `backend/api/metadata_files/` directory.
4. Check the validity of the metadata files.

```bash
make test
```

5. Commit your changes. Metadata files will be formatted automatically.
6. Push your changes to your fork and create a pull request to the `main` branch of the original repository.


## Deploying the website locally

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
