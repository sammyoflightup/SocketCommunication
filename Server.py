import socket

def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define host and port
    host = 'localhost'
    port = 5000
    
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    
    # Put the socket into listening mode
    server_socket.listen(5)  # The argument specifies the maximum number of queued connections
    
    print(f'Server listening on {host}:{port}')
    
    # Wait for a connection
    while True:
        # Establish a connection with the client
        client_socket, addr = server_socket.accept()
        print(f'Got connection from {addr}')
        
        # Send a thank you message to the client
        client_socket.send(b'Thank you for connecting')
        
        # Close the connection with the client
        client_socket.close()

if __name__ == '__main__':
    main()
