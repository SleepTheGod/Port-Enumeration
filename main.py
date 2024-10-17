import socket
import errno

def enumerate_active_ports():
    print("lulz: Enumerating active ports on the machine:")
    
    for port in range(1, 65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind(('', port))  # Bind to all interfaces on the specified port
        except OSError as e:
            if e.errno == errno.EADDRINUSE:
                print(f"Port {port} is active.")
        finally:
            sock.close()  # Ensure the socket is closed whether binding succeeds or fails

    print("lulz: Port enumeration completed.")

if __name__ == "__main__":
    enumerate_active_ports()
