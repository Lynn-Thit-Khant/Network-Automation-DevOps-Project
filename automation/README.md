# Automation Files

This folder contains the core automation files used in the network backup workflow.

## Files

| File | Purpose |
|---|---|
| `update_hosts.py` | Retrieves router details from the REST API, updates Ansible inventory, and starts the backup playbook |
| `backup_playbook.yaml` | Runs Cisco IOS commands and saves router running configurations |
| `ansible.cfg` | Stores Ansible configuration settings for local execution |
| `hosts.example` | Example Ansible inventory with placeholder credentials |

## Security Note

Do not commit real router passwords, SSH keys, or production device IPs. Use placeholder values in public repositories.
