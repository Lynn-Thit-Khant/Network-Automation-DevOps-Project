# Troubleshooting

## Flask API is not reachable

Check whether the Flask server is running:

```bash
curl http://localhost:5000/devices
```

If running inside Docker, confirm the container can reach the host network.

## Docker container cannot reach API

Use host networking when the API runs on the host system:

```bash
docker run --network host ansible-backup-poc
```

## Ansible cannot connect to router

Check:

- Router IP address
- Router credentials
- Network connectivity
- Ansible inventory format
- Cisco IOS SSH access

## Backup file does not appear

Check:

- `backups/` directory exists
- Bind mount path is correct
- Ansible playbook completed successfully
- File permissions allow writing

## Python script fails

Check:

- API URL is correct
- `requests` library is installed
- JSON response format matches expected device fields
- Ansible files are in the correct directory
