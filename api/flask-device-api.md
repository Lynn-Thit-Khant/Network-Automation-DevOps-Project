# Flask Device API

## Purpose

The Flask API provides a simple interface for managing network device records. It allows the automation workflow to retrieve router details without manually editing the Ansible inventory.

## Supported Operations

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/devices` | Retrieve all device records |
| POST | `/devices` | Add a new device record |
| DELETE | `/devices/<device_ip>` | Remove a device record |

## Example Device Format

```json
{
  "devIP": "192.168.56.101",
  "devName": "CSR1kv-01",
  "devType": "router"
}
```

## Why an API Was Used

Using an API separates the device inventory from the automation logic. This makes it easier to add, remove, or retrieve devices without changing the backup script itself.

## Validation

The API should be validated using:

- Browser access
- Postman
- `curl` commands
- Python requests
