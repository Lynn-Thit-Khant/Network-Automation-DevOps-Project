# Architecture Overview

## Purpose

This project simulates a network automation backup tool for Cisco routers. The workflow connects a device inventory source, Python automation logic, Ansible configuration management, and Dockerized execution into one repeatable pipeline.

## Main Components

### Device Inventory

Device information is stored in a CSV-backed inventory containing:

- Device IP address
- Device name
- Device type

### Flask REST API

The REST API exposes the device inventory so automation scripts can retrieve, add, and remove network devices without manually editing inventory files.

### Python Automation Script

The Python script retrieves router data from the API, extracts device IP addresses, updates the Ansible inventory, and triggers the backup playbook.

### Ansible Playbook

The Ansible playbook connects to Cisco routers and captures the running configuration using Cisco IOS commands.

### Docker Container

Docker packages Python, Ansible, OpenSSH, and the required scripts into a portable execution environment.

## High-Level Workflow

```text
CSV Device Inventory
        ↓
Flask REST API
        ↓
Python Script
        ↓
Dynamic Ansible Inventory
        ↓
Ansible Backup Playbook
        ↓
Cisco Router Backup Files
        ↓
Dockerized Execution Environment
```
