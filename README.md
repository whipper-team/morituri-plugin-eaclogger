## Status

[![License](https://img.shields.io/github/license/whipper-team/morituri-plugin-eaclogger.svg)](https://github.com/whipper-team/morituri-plugin-eaclogger/blob/master/LICENSE)
[![Build Status](https://travis-ci.com/whipper-team/morituri-plugin-eaclogger.svg?branch=master)](https://travis-ci.com/whipper-team/morituri-plugin-eaclogger)
[![GitHub (pre-)release](https://img.shields.io/github/release/whipper-team/morituri-plugin-eaclogger/all.svg)](https://github.com/whipper-team/morituri-plugin-eaclogger/releases/latest)

**NOTICE: UNMAINTAINED**

## Logger information

This logger plugin for morituri provides text reports structured in a way that
carefully mimics EAC's generated ones (except for the checksum).

The logger should be feature complete so future development will consist
mainly of bugfixes.

If you're looking for the analogous [whipper](https://github.com/whipper-team/whipper) plugin,
it can be found [here](https://github.com/whipper-team/whipper-plugin-eaclogger).

## License

Licensed under the [ISC license](https://github.com/whipper-team/morituri-plugin-eaclogger/blob/master/LICENSE).

## Instructions

To use this plugin:

* build it:

    ```bash
    git clone https://github.com/whipper-team/morituri-plugin-eaclogger.git
    cd morituri-plugin-eaclogger
    python2 setup.py bdist_egg
    ```

* copy it to your plugin directory:

    ```bash
    mkdir -p "$HOME/.morituri/plugins"
    cp dist/morituri_*egg "$HOME/.morituri/plugins"
    ```

* verify that it gets recognized:

    ```bash
    rip cd rip --help
    ```

  You should see `eac` as a possible logger.

* use it:

    ```bash
    rip cd rip --logger=eac
    ```

## Developers

To use the plugin while developing uninstalled:

```bash
python2 setup.py develop --install-dir=path/to/checkout/of/morituri
```
