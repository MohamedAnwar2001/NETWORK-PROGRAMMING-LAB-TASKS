import socket
import threading

def receive_messages(sock):
    while True:
        try:
            # Receive the size of the incoming message
            size_bytes = sock.recv(8)
            size = int.from_bytes(size_bytes, 'big')

            # Receive the message itself
            data = sock.recv(size).decode('utf-8')

            # Print the received message
            print(data)
        except socket.error:
            break

def send_message(sock):
    while True:
        # Input message from the user
        message = input("Enter your message: ")
        recipient = input("Enter recipient address (host:port): ")
        data = f"{recipient}:{message}"

        # Send the size of the message followed by the message itself
        sock.send(len(data).to_bytes(8,'big'))
        sock.send(data.encode('utf-8'))

def start_chat():
    host = 'localhost'
    port = 8000

    # Connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    # Start a thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    receive_thread.start()

    # Start a thread to send messages
    send_thread = threading.Thread(target=send_message, args=(sock,))
    send_thread.start()

if __name__ == '__main__':
    start_chat()
