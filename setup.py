from setuptools import setup

setup(
    name="morituri-plugin-eaclogger",
    version="0.3.0",
    description="""morituri EAC-style logger""",
    author="superveloman",
    maintainer="JoeLametta",
    packages=[
        'eaclogger',
        'eaclogger.logger'],
    entry_points="""
  [morituri.logger]
  eac = eaclogger.logger.eac:EacLogger
  """)
