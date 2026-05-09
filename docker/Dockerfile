FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    openssh-client \
    python3-pip \
    ansible \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install requests

WORKDIR /etc/ansible

COPY ansible.cfg .
COPY hosts .
COPY backup_playbook.yaml .
COPY update_hosts.py .

RUN mkdir -p backups

CMD ["python3", "update_hosts.py"]
