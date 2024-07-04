# Installation

## How to configure environment for Sentinel SDK

Since Sentinel Python SDK requires Python 3.10+ installed, first step you need to complete, install Python

Before start, please be sure that `python`
```sh
python3 --version

Python 3.10.12
```
The next steps, the installation of Sentinel SDK.

> IMPORTANT! Strongly recommended to install Sentinel Python SDK in a dedicated virtual environment on all platforms, to avoid conflicting with your system packages.

Virtual environments allow you do not conflict with already-installed Python system packages, which could break some of your system tools and scripts, and still install packages normally with `pip` (without `sudo`).

```sh
python3 -m venv .venv
```

Activation virtual env

```sh
source .venv/bin/activate       # for bash/zsh shell
source .venv/bin/activate.fish  # for fish shell
```
> Please check that you have `(.venv)` in command prompt

Install/Upgrade pip

```sh
python -m pip install --upgrade pip
```

## Getting Sentinel Python SDK

Install Sentinel SDK in your virtual environment

```sh
pip install git+ssh://git@github.com/haas-labs/ext-sentinel-py-sdk.git@v0.5.20
```
Check that Sentinel SDK command line interface is available

```sh
sentinel version --all
{"sentinel-sdk": "0.5.20", "httpx": "0.27.0", "python": "3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]", "platform": "Linux-6.5.0-41-generic-x86_64-with-glibc2.35", "jinja2": "3.1.4", "async_lru": "2.0.4", "aiokafka": "0.10.0", "pydantic": "2.7.4", "web3": "6.19.0", "websockets": "12.0"}
```
