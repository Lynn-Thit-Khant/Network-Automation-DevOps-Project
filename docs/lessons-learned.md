# Lessons Learned

## Infrastructure as Code

Using Ansible shifted the workflow from manual router commands to repeatable configuration management.

## Dynamic Automation

Fetching device details from an API made the backup process more flexible than manually editing router IPs in the inventory.

## Containerisation

Docker simplified dependency management but required careful attention to networking and persistent storage.

## Data Persistence

Containers are temporary by design. Backup files must be stored outside the container using bind mounts or volumes.

## Validation

Automation should always be validated. A successful workflow must prove that devices were discovered, inventories were updated, and backup files were generated correctly.

## Future Improvements

Possible improvements include:

- Error handling and retry logic
- Scheduled backup execution
- Logging failed devices
- Secret management for credentials
- Dashboard for backup status
