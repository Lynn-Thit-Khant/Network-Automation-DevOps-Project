import requests
import subprocess
from pathlib import Path

API_URL = "http://mytest.demo.local:5000/devices"
HOSTS_FILE = Path("hosts")
PLAYBOOK_FILE = "backup_playbook.yaml"


def fetch_devices():
    """Retrieve device records from the Flask REST API."""
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    return response.json()


def update_ansible_hosts(devices):
    """Append router IP addresses from the API response into the Ansible hosts file."""
    existing_content = HOSTS_FILE.read_text(encoding="utf-8") if HOSTS_FILE.exists() else ""

    with HOSTS_FILE.open("a", encoding="utf-8") as hosts:
        for device in devices:
            dev_ip = device.get("devIP")
            dev_type = device.get("devType")

            if dev_type == "router" and dev_ip and dev_ip not in existing_content:
                hosts.write(f"{dev_ip}\n")
                print(f"Added router to Ansible inventory: {dev_ip}")


def run_ansible_backup():
    """Run the Ansible playbook to back up router configurations."""
    subprocess.run(["ansible-playbook", PLAYBOOK_FILE], check=True)


if __name__ == "__main__":
    devices = fetch_devices()
    update_ansible_hosts(devices)
    run_ansible_backup()
