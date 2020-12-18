import argparse
import logging
import logging.config
import sys
from typing import List

import docker

LOGGER = logging.getLogger(__name__)


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--container-name',
        metavar='container_name',
        required=True,
        help='(Partial) name of the container',
        type=str
    )

    args = parser.parse_args(argv)

    try:
        client: docker.DockerClient = docker.from_env()

        containers: List[docker.models.containers.Container] = client.containers.list(
            all=True,
            filters={'name': args.container_name}
        )

        for container in containers:
            res = client.api.inspect_container(container.id)

            # if the container is running, check the health status (if it exists)
            if container.status == 'running':
                if 'Health' in res['State'] and res['State']['Health']['Status'] == 'unhealthy':
                    last_log = res['State']['Health']['Log'][-1]['Output'].strip()
                    LOGGER.error('container "%s" is unhealthy, last log entry: "%s"', container.name, last_log)
            elif container.status != 'running':
                LOGGER.error('container "%s" has status "%s"', container.name, container.status)

        if len(containers) == 0:
            LOGGER.error('no container(s) with name "%s" found', args.container_name)
    except docker.errors.NotFound:
        LOGGER.error('Container "%s" not found', args.container_name)
    except docker.errors.DockerException as exc:
        LOGGER.error('Docker host seems to be down: %s', exc)


if __name__ == '__main__':
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'loggers': {
            '': {
                'level': 'INFO',
            },
        }
    })
    sys.exit(main(sys.argv[1:]))
