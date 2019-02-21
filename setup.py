from setuptools import setup
from eaclogger import __version__ as plugin_version

setup(
    name="morituri-plugin-eaclogger",
    version=plugin_version,
    description="""A plugin for morituri which provides EAC style log reports""",
    author="supermanvelo",
    maintainer="JoeLametta",
    license="ISC License",
    url="https://github.com/whipper-team/morituri-plugin-eaclogger",
    packages=['eaclogger', 'eaclogger.logger'],
    entry_points={
        "morituri.logger": [
            "eac = eaclogger.logger.eac:EacLogger"
        ]
    }
)
