import sys
import platform

from config import settings


def create_allure_environment_file():
    environment = {
        **settings.model_dump(),
        'os_info': f'{platform.system()}, {platform.release()}',
        'python_version': sys.version,
    }

    properties = '\n'.join(f'{key}={value}' for key, value in environment.items())

    with open(settings.allure_result_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)
