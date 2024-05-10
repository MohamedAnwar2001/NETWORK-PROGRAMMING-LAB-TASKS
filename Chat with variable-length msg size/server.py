import socket
import threading
import ast

# Function to handle each client's connection
def handle_client(client_session, client_address):
    while True:
        try:
            # Receive the size of the incoming message
            size_bytes = client_session.recv(8)
            size = int.from_bytes(size_bytes, 'big')
            
            # Receive the message data
            data = client_session.recv(size).decode('utf-8')
            
            # If no data is received, break the loop
            if not data:
                break
            
            # Print the received message information
            print(f"Received from {client_address}: {data} : with size {size}")

            # Extract the recipient client's address from the message
            recipient_address, message = data.split(':', 1)

            # Find the recipient client's socket
            recipient_socket = None
            for client in clients:
                if client[1] == ast.literal_eval(recipient_address):
                    recipient_socket = client[0]
                    break
            
            # If the recipient socket is found, send the message
            if recipient_socket:
                recipient_socket.send(size_bytes)
                recipient_socket.send(message.encode('utf-8'))
            else:
                print(f"Recipient not found: {recipient_address}")

        except socket.error:
            break

    # Close the client connection
    print(f"Connection closed with {client_address}")
    clients.remove((client_session, client_address))
    client_session.close()

# Function to start the server
def start_server():
    host = 'localhost'
    port = 8000

    # Create a server socket and start listening for connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server started on {host}:{port}")

    # Accept incoming connections and handle them in separate threads
    while True:
        client_session, client_address = server_socket.accept()
        clients.append((client_session, client_address))
        print(f"Connected with {client_address}")
        threading.Thread(target=handle_client, args=(client_session, client_address)).start()

if __name__ == '__main__':
    clients = []
    start_server()
