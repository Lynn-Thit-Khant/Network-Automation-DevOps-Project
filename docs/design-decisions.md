# Design Decisions

## CSV-Backed Inventory

A CSV-backed device database was used because it is simple, readable, and easy to parse in a proof-of-concept environment.

## REST API Layer

The REST API allows device information to be retrieved programmatically. This separates inventory management from the backup automation logic.

## Python Orchestration

Python was used to connect the API and Ansible workflow. It retrieves device records, updates inventory, and starts backup execution.

## Ansible for Network Automation

Ansible was selected because it is agentless and widely used for configuration management and network automation.

## Docker for Portability

Docker packages dependencies into a consistent environment, making the workflow easier to run across different machines.

## Bind Mounts for Backup Persistence

Bind mounts were used to ensure router backup files remain available on the host after the container exits.
