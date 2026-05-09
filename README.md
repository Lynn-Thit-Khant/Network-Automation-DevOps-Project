# Network Automation & DevOps Project

## Overview

This project demonstrates a network automation workflow for backing up Cisco router configurations. It combines a Flask REST API, CSV-based device inventory, Python scripting, Ansible automation, and Docker containerisation into a repeatable configuration backup pipeline.

The goal is to simulate how network devices can be discovered, added to an automation inventory, and backed up without manually editing device lists.

## Problem Scenario

Manual router backup processes are slow, repetitive, and prone to human error. As the number of devices grows, manually maintaining inventory files and running individual backup commands becomes inefficient.

## Solution

This project automates the workflow by:

- Storing device details in a CSV-backed inventory
- Exposing device records through a Flask REST API
- Using Python to retrieve device IPs from the API
- Dynamically updating the Ansible inventory
- Running an Ansible playbook to back up router configurations
- Packaging the automation workflow in Docker for repeatable execution

## Technologies Used

- Python
- Flask REST API
- Ansible
- Docker
- Cisco CSR1000v
- Cisco IOS
- YAML
- CSV
- Git

## Key Features

- REST API for retrieving, adding, and deleting device records
- CSV-backed device database
- Dynamic Ansible inventory generation
- Automated Cisco running-config backup
- Dockerized execution environment
- Backup output persistence using bind mounts
- Validation across 2 Cisco CSR1000v routers

## Repository Structure

| Folder | Purpose |
|---|---|
| `architecture/` | Workflow design and data flow explanation |
| `api/` | Device API documentation and sample inventory |
| `automation/` | Python script, Ansible playbook, and inventory files |
| `docker/` | Dockerfile and container execution guide |
| `validation/` | Testing, backup validation, and scalability checks |
| `docs/` | Design decisions, troubleshooting, and lessons learned |

## Skills Demonstrated

- Network automation
- Infrastructure as Code
- Python scripting
- REST API integration
- Ansible configuration management
- Docker containerisation
- Cisco router administration
- Technical documentation

## Outcome

The project successfully automated Cisco router configuration backups by retrieving device details from a REST API, updating Ansible inventory dynamically, and generating separate backup files for multiple routers.

## Notes

This repository is structured as a professional project simulation. Credentials, private keys, and environment-specific values have been replaced with placeholders.
