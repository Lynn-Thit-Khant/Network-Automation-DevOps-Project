# Container Notes

## Environment Consistency

Docker ensures the automation workflow runs with the same dependencies each time. This avoids setup differences between machines.

## Installed Components

- Python 3
- pip
- Ansible
- OpenSSH client
- Python `requests` library

## Data Persistence

Backup files are written to a bind-mounted host directory so they remain available after the container exits.

## Networking

The container uses host networking to access the local Flask API and network devices.

## Security Note

Do not build container images with hardcoded production credentials.
