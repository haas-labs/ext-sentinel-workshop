# Configuration

For the monitor configuration there are required to create 2 configuration files:

- profile.yaml
- manifest.py

## Manifest (monitor/manifest.py)

contains monitor schema and metadata required for Extractor configuration

## Profile (monitor/profile.yaml)

contains configuration details of monitor: 
- data inputs/outputs
- monitor name, description and classpath to the monitor code

## Predefined configurations

Inputs:
- Kafka Transactions (Ethereum)
- Kafka Monitoring Conditions 

Outputs:
- Kafka Events Outputs

Databases:
- Monitoring Conditions
