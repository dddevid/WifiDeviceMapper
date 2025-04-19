# Connected Devices on Router

This project allows you to visualize devices connected to the local network through an ARP scan. It uses Flask for the backend and an interactive visualization with D3.js for the frontend.
[https://github.com/dddevid/WifiDeviceMapper/blob/main/Images/image(3).png?raw=true]()


## Features
- Detects the IP and MAC address of the network gateway (router).
- Scans the local network to identify connected devices.
- Displays connected devices in an interactive visualization.
- Supports light and dark mode.

## Demo
A live demo (fully functional but simulated) is available at: [WifiDeviceMapper Demo](https://dddevid.github.io/WifiDeviceMapper/)

## Requirements
Before running the project, make sure you have the following installed:
- Python 3
- pip
- Scapy (for ARP scanning)
- Flask
- netifaces
- [Npcap](https://npcap.com/) (required for packet capturing on Windows)

## Installation

### Cloning the Repository
Before proceeding with the installation, clone the repository using:
```sh
git clone https://github.com/dddevid/WifiDeviceMapper.git
cd WifiDeviceMapper
```

### Steps for Windows
1. **Install Python**: If you don’t have Python installed, download it from [python.org](https://www.python.org/downloads/) and make sure to add it to the PATH.
2. **Install Npcap**: Download and install [Npcap](https://npcap.com/).
3. **Open the terminal (cmd or PowerShell)** and navigate to the project folder:
   ```sh
   cd path/to/folder
   ```
4. **Install dependencies** by running:
   ```sh
   pip install flask scapy netifaces
   ```
5. **Start the application**:
   ```sh
   python app.py
   ```
6. **Access the web interface** by opening your browser and going to:
   ```
   http://127.0.0.1:5000/
   ```

### Steps for macOS
1. **Install Homebrew** (if not already installed):
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. **Install Python and dependencies**:
   ```sh
   brew install python3
   pip3 install flask scapy netifaces
   ```
3. **Start the application**:
   ```sh
   python3 app.py
   ```
4. **Access the web interface**:
   ```
   http://127.0.0.1:5000/
   ```

### Steps for Linux
#### Ubuntu-based distributions
1. **Update package lists and install dependencies**:
   ```sh
   sudo apt update && sudo apt install python3 python3-pip
   pip3 install flask scapy netifaces
   ```
2. **Start the application**:
   ```sh
   python3 app.py
   ```
3. **Access the web interface**:
   ```
   http://127.0.0.1:5000/
   ```

#### Arch-based distributions
1. **Update package lists and install dependencies**:
   ```sh
   sudo pacman -Syu python python-pip
   pip install flask scapy netifaces
   ```
2. **Start the application**:
   ```sh
   python app.py
   ```
3. **Access the web interface**:
   ```
   http://127.0.0.1:5000/
   ```

## How It Works
- The Python backend uses Flask to serve an HTML page and provide JSON data with information about connected devices.
- The `scan_devices()` function performs an ARP scan to detect devices on the local network.
- The frontend uses D3.js to visually represent connected devices and the gateway.

## Notes
- To perform an ARP scan, the program must be run with administrator privileges.
- The scan may take a few seconds to gather all the data.
- If Scapy is not installed, an error message will be displayed.

## Support
If you find this project useful and want to support my work, you can buy me a coffee at: [buymeacoffee.com/devidd](https://buymeacoffee.com/devidd)

## Author
Project developed by **Devid**.

