# docker-monitor
Simple docker container monitor informing about non-running and unhealthy containers.

Checks the status of containers containing a given name for their status. Reports containers that are not running or running but unhealthy.
Nothing will be reported if everything is fine to make it compatible with calling the script using a cronjob (`cron` will not send out emails on empty output).

## How to call
`docker-monitor` makes use of the [Docker SDK for Python](https://github.com/docker/docker-py) to access information from the Docker Engine API.

You therefore need to install the `docker` Python library. It is best to use a virtual environment, for example, using `venv`:

1. `python3.8 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements/base.txt`
4. `python monitor.py --container-name <nameOfContainer>`

## Development

### How to set up development environment

1. `python3.8 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements/development.txt`

Linting with `flake8` and type checking with `mypy` is used. The configuration is located in `setup.cfg`. The project contains settings for `vscode` where these are enabled. However, they can also be executed from the project root as follows.

* Linting with `flake8`: Execute `flake8`
* Static type checking with `mypy`: Execute `mypy`

### How to update dependencies

This project makes use of [pip-upgrader](https://github.com/simion/pip-upgrader) to update the requirements files to the latest versions of dependencies.

1. Run `pip-upgrade` to update the desired dependencies
1. Verify that everything still works
1. Commit the updates to the requirements file(s)
