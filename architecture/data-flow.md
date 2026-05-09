# Data Flow

## Data Source

Device records are stored in a CSV-backed device database.

Example record:

```csv
devIP,devName,devType
192.168.56.101,CSR1kv-01,router
```

## API Layer

The Flask API provides device records in JSON format.

Example response:

```json
[
  {
    "devIP": "192.168.56.101",
    "devName": "CSR1kv-01",
    "devType": "router"
  }
]
```

## Automation Layer

The Python script consumes the API response and appends router IP addresses into the Ansible inventory.

## Configuration Management Layer

Ansible reads the inventory and connects to each router to collect running configurations.

## Output Layer

Backup files are created per router.

Example output:

```text
backups/192.168.56.101_running-config.txt
backups/192.168.56.102_running-config.txt
```
