# Explanation
Socket Creation We create a socket using socket.socket(socket.AF_INET, socket.SOCK_STREAM) to indicate we are using IPv4 and TCP.

# Port Loop 
We loop through ports from 1 to 65535.

# Binding to Port 
We attempt to bind to each port using sock.bind(('', port)), which binds to all available network interfaces.

# Error Handling 
If binding fails due to the port being in use, we check if the error is an address already in use (errno.EADDRINUSE) and print the port number.

# Socket Closure 
The socket is closed after each iteration, regardless of whether the binding was successful or not.

# Installing The Script
```bash
git clone https://github.com/SleepTheGod/Port-Enumeration/
cd Port-Enumeration
python main.py
```
