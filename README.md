## Status

[![Build Status](https://travis-ci.com/whipper-team/morituri-plugin-eaclogger.svg?branch=master)](https://travis-ci.com/whipper-team/morituri-plugin-eaclogger)

## Logger information

This logger provides text reports structured in a way that carefully mimics EAC's generated ones. It is compatible only with morituri.

Eaclogger should be feature complete so future development will consist only of bugfixes.

## Instructions

To use this plugin:

* build it:

    ```bash
    git clone https://travis-ci.com/whipper-team/morituri-plugin-eaclogger.git
    cd morituri-plugin-eaclogger
    python2 setup.py bdist_egg
    ```

* copy it to your plugin directory:

    ```bash
    mkdir -p $HOME/.morituri/plugins
    cp dist/morituri_*egg $HOME/.morituri/plugins
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
