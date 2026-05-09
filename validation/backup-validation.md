# Backup Validation

## Purpose

Validate that router configuration backups are generated correctly and stored in a predictable location.

## Expected Backup Output

Each router should generate a separate backup file.

Example:

```text
backups/192.168.56.101_running-config.txt
backups/192.168.56.102_running-config.txt
```

## Validation Steps

List backup files:

```bash
ls -l backups/
```

View backup content:

```bash
cat backups/192.168.56.101_running-config.txt
```

## Expected Result

The backup file should contain the Cisco router running configuration.

## Operational Note

A backup workflow is only useful if the output is checked. Backup validation confirms that automation produced usable recovery data.
