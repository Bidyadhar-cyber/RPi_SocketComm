# RPi_SocketComm
RPi_SocketComm is a Python package designed for Raspberry Pi-based RFID systems to handle socket communication with RFID readers like **IDENTIUM** and **SECUREYE**. It supports both server-mode and client-mode communication and provides convenient parsing of RFID tag data from raw bytes.
---
## 🚀 Features

- TCP server for IDENTIUM RFID readers
- TCP client for SECUREYE RFID readers
- Byte-to-hex data conversion
- Error-handling for common socket issues
- Designed for Raspberry Pi and embedded systems

---
## 📦 Installation

Clone the repository and install using `pip`:

```bash
git clone https://github.com/yourusername/RPi_SocketComm.git
cd RPi_SocketComm
pip install .

**🧠 Method Overview**

        Method            |              Description
--------------------------+---------------------------------------------------
start_identium_server()   | Starts a server to receive data from IDENTIUM
parse_identium_data()     | Parses and extracts RFID tag from IDENTIUM bytes
start_secureye_client()   | Connects to SECUREYE and receives data
parse_secureye_data()     | Parses SECUREYE RFID hex if valid
