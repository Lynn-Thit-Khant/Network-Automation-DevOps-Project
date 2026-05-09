# Scalability Test

## Purpose

Validate that the automation workflow can support more than one router without changing the core script or playbook.

## Test Scenario

Two Cisco CSR1000v routers were added to the device inventory.

Example:

```csv
devIP,devName,devType
192.168.56.101,CSR1kv-01,router
192.168.56.102,CSR1kv-02,router
```

## Expected Workflow

1. Python retrieves both router records from the REST API.
2. Both router IPs are added to the Ansible inventory.
3. Ansible runs the backup playbook against both routers.
4. Separate backup files are generated.

## Expected Result

```text
192.168.56.101_running-config.txt
192.168.56.102_running-config.txt
```

## Key Learning

The workflow becomes scalable because the device list is no longer hardcoded into the automation logic.
