# Author: Anton Mikhaylov
# Created: 16/08/2020

"""
Configuration Module
Defines global object `CONFIGURATION` which contains all settings
"""

import os

CONFIGURATION = None


def _build_config() -> None:
    """
    Function loads parameters from environment of this process and builds CONFIGURATION object
    """

    global CONFIGURATION

    configuration_common = {
        'SERVICE_HOST': os.getenv('SERVICE_HOST', '0.0.0.0'),
        'SERVICE_PORT': os.getenv('SERVICE_PORT', 8080),
        'FILE_NAME': os.getenv('FILE_NAME', 'example'),
    }

    CONFIGURATION = {
        **configuration_common
    }

_build_config()