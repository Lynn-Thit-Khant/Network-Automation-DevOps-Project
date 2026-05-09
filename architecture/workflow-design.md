# Workflow Design

## Workflow Summary

The automation pipeline follows a simple operational flow:

1. The device inventory stores router details.
2. The Flask API exposes device data through REST endpoints.
3. The Python script retrieves router IPs from the API.
4. The script updates the Ansible inventory dynamically.
5. Ansible connects to each router and runs `show running-config`.
6. The output is saved as individual backup files.
7. Docker runs the full process in a consistent environment.

## Why This Design Was Used

This design separates responsibilities clearly:

- The API manages device records.
- Python handles data retrieval and orchestration.
- Ansible handles network device automation.
- Docker provides portability and dependency consistency.

This structure makes the workflow easier to troubleshoot, extend, and reuse.

## Operational Benefit

The workflow reduces manual inventory editing and supports repeatable backup execution across multiple network devices.
