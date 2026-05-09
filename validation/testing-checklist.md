# Testing Checklist

## API Validation

- [ ] Flask API starts successfully
- [ ] `/devices` endpoint returns device records
- [ ] GET request retrieves devices
- [ ] POST request adds a new device
- [ ] DELETE request removes a device
- [ ] CSV inventory updates correctly

## Python Script Validation

- [ ] Script connects to the API
- [ ] Script retrieves JSON device data
- [ ] Router IPs are extracted correctly
- [ ] Ansible hosts file is updated dynamically
- [ ] Script triggers Ansible playbook execution

## Ansible Validation

- [ ] Ansible connects to Cisco router
- [ ] `show running-config` command runs successfully
- [ ] Backup file is generated
- [ ] Backup file contains router configuration output

## Docker Validation

- [ ] Docker image builds successfully
- [ ] Container can reach Flask API
- [ ] Container can run Python script
- [ ] Container can run Ansible playbook
- [ ] Backup files persist through bind mount
