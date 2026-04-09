# SimpleScanner

A simple, fast, multithreaded TCP port scanner written in Python. This script allows you to quickly check for open ports on a target IPv4 address by utilizing a separate thread for each scanned port.

## Key Features

* **Single port scanning:** Quickly check a specific service.
* **Range scanning:** Specify a range (e.g., `1-1000`) to scan multiple ports in one go.

## How to Use

Download the repository or just the script file, and run it from your terminal by providing the necessary arguments.

### Available arguments:
* `-ip` : The IPv4 address of the target host (required).
* `-p`, `--port` : A single port or a range of ports separated by a hyphen (required).

### Example
<img width="781" height="220" alt="obraz" src="https://github.com/user-attachments/assets/e07041c7-0028-4282-98c8-cd07199f7c12" />
