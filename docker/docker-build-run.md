# Docker Build and Run Guide

## Purpose

Docker is used to package Python, Ansible, OpenSSH, and the automation files into a repeatable execution environment.

## Build Image

```bash
docker build -t ansible-backup-poc .
```

## Run Container

```bash
docker run -d --rm --network host \
  -v /home/devasc/labs/devnet-src/ansible/ansible-csr1000v/backups:/etc/ansible/backups \
  ansible-backup-poc
```

## Why `--network host` Was Used

The container needs to reach the Flask API running on the host environment. Using `--network host` allows the container to share the host network stack.

## Why a Bind Mount Was Used

Containers are temporary. Without a bind mount, backup files created inside the container may disappear when the container stops. The `-v` option stores backup files directly on the host filesystem.
