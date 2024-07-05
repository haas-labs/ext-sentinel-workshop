# Integration

## VPN

Please be sure that you have estiblished VPN connection to dev environment

## EXTRACTOR API TOKEN

Create YAML file where you can specify all required environment variables. For example, `.envs/dev.yaml`

```yaml
EXTRACTOR_API_TOKEN: ...
```

## EXTRACTOR API ENDPOINT URL

The endpoint required for registering a monitor schema in the Extractor

```yaml
EXTRACTOR_API_ENDPOINT: https://api.extractor.dev.hacken.cloud
```

## Example of environment file for development environment

`.envs/dev.yaml`

```yaml
EXTRACTOR_API_ENDPOINT: https://extractor.hacken.dev

EXTRACTOR_API_TOKEN: ...
```

## How to specify the path to the file with env variables

```sh
# Bash
export SENTINE_ENV_PROFILE $(pwd)/.envs/dev.yaml

# Fish
set -gx SENTINEL_ENV_PROFILE (pwd)/.envs/dev.yaml
```

