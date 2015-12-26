# datapackage-bigquery-py

[![Travis](https://img.shields.io/travis/okfn/datapackage-bigquery-py.svg)](https://travis-ci.org/okfn/datapackage-bigquery-py)
[![Coveralls](http://img.shields.io/coveralls/okfn/datapackage-bigquery-py.svg?branch=master)](https://coveralls.io/r/okfn/datapackage-bigquery-py?branch=master)

Generate and load BigQuery tables based on Data Package.

## Usage

This section is intended to be used by end-users of the library.

> See section below how to get authentificated service.

Package represents Data Package stored as Big Query dataset:

```python
from dpbq import Package

package = Package(<service>, 'project_id', 'dataset_id')

package.create('path/to/descriptor.json')
package.get_resources()

package.export('path/to/descriptor.json')
```

Dataset represents a native Big Query dataset:

```python
from dpbq import Dataset

dataset = Dataset(<service>, 'project_id', 'dataset_id')

dataset.create()
dataset.get_tables()
```

### Authentificated service

To start using Google BigQuery service:
- Create a new project - [link](https://console.developers.google.com/home/dashboard)
- Create a service key - [link](https://console.developers.google.com/apis/credentials)
- Download json credentials and set `GOOGLE_APPLICATION_CREDENTIALS` environment variable

For example:

```python
import os
from apiclient.discovery import build
from oauth2client.client import GoogleCredentials

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '.credentials.json'
credentials = GoogleCredentials.get_application_default()
service = build('bigquery', 'v2', credentials=credentials)
```

### Design Overview

#### Entities

- Dataset

    Table is a native BigQuery dataset. Dataset can contain tables.

- Package

    Package is a Data Package stored as Dataset on BigQuery. Resources
    are stored as tables with directory separator `/` replaced by `__` (2 underscores).
    Data Package structure can be restored from BigQuery dataset without
    any knowledge about initial `datapackage.json`.

> Package is a Data Package facade to Dataset (BigQuery) backend.

Dataset and Package are geteways by their nature. It means user can initiate
Dataset without real BigQuery dataset creation then call `create` or `delete` to
delete the real datable without instance destruction.

#### Mappings

```
datapackage.json -> *not stored*
datapackage.json resources -> BigQuery dataset's tables
data/data.csv schema -> BigQuery talbe schema
data/data.csv data -> BigQuery talbe data
```

#### Drivers

Default Google BigQuery client is used as part of `jsontableschema-bigquery-py` package - [docs](https://developers.google.com/resources/api-libraries/documentation/bigquery/v2/python/latest/).

## Development

This section is intended to be used by tech users collaborating
on this project.

### Getting Started

To activate virtual environment, install
dependencies, add pre-commit hook to review and test code
and get `run` command as unified developer interface:

```
$ source activate.sh
```

### Reviewing

The project follow the next style guides:
- [Open Knowledge Coding Standards and Style Guide](https://github.com/okfn/coding-standards)
- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

To check the project against Python style guide:

```
$ run review
```

### Testing

To run tests with coverage check:

```
$ run test
```

Coverage data will be in the `.coverage` file.
