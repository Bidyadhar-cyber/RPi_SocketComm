import socket
import time


class SocketCommunication:
    """Handles socket-based communication for RFID readers."""

    def __init__(self, ip_address, port_number, data_length):
        self.ip_address = str(ip_address)
        self.port_number = int(port_number)
        self.data_length = int(data_length)
        self.server_socket = None
        self.client_socket = None

    # =======================
    # IDENTIUM SOCKET SERVER
    # =======================

    def start_identium_server(self):
        """Starts IDENTIUM RFID socket server and reads data from the client."""
        try:
            self.server_socket = self._create_server_socket()
            self.client_socket, _ = self.server_socket.accept()
            data = self.client_socket.recv(self.data_length)
            return data

        except socket.timeout:
            return "False"

        except socket.error as err:
            return self._handle_socket_error(err)

        except Exception:
            return "E-5"

        finally:
            self._close_sockets()

    def parse_identium_data(self, data):
        """Converts raw IDENTIUM byte data to hex and extracts RFID tag."""
        try:
            hex_data = self._bytes_to_hex(data)
            return hex_data[36:60] if hex_data else False
        except Exception:
            return None

    # =======================
    # SECUREYE SOCKET CLIENT
    # =======================

    def start_secureye_client(self):
        """Connects to SECUREYE RFID socket server and reads data."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(60)
                s.connect((self.ip_address, self.port_number))
                return s.recv(self.data_length)

        except socket.timeout:
            return "False"

        except socket.error as err:
            return self._handle_socket_error(err, client=True)

        except Exception:
            return "E-3"

    def parse_secureye_data(self, data):
        """Converts raw SECUREYE byte data to hex if length is valid."""
        try:
            hex_data = self._bytes_to_hex(data)
            return hex_data if len(hex_data) == 36 else False
        except Exception:
            return None

    # =======================
    # HELPER METHODS
    # =======================

    def _create_server_socket(self):
        """Creates and configures a server socket."""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.ip_address, self.port_number))
        s.listen(1)
        return s

    def _bytes_to_hex(self, data):
        """Converts byte data to a hexadecimal string."""
        return ''.join(f"{byte:02x}" for byte in data).strip()

    def _handle_socket_error(self, error, client=False):
        """Handles known socket errors."""
        errno = error.errno
        if errno == 98:
            time.sleep(1)
            return "E-1"
        elif errno == 104:
            return "E-2" if not client else "E-1"
        elif errno == 9:
            return "E-3"
        return "E-4" if not client else "E-2"

    def _close_sockets(self):
        """Closes server and client sockets if open."""
        if self.client_socket:
            try:
                self.client_socket.close()
            except:
                pass
        if self.server_socket:
            try:
                self.server_socket.close()
            except:
                pass
