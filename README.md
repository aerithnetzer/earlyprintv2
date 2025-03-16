# earlyprintv2

This repository runs development for version 2 of the early print archive.

## Development

### Dependencies

[uv](https://docs.astral.sh/uv/getting-started/installation/)


From the project root directory, run:

`uv venv --python 3.11.6`

and then:

`source .venv/bin/activate`

and then:

`uv pip install -r requirements.txt`

### Starting the development server

While activated in the virtual environment, run:

`uv run manage.py runserver`
