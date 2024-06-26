import socket
import threading

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 7000))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            message = client.recv(1024).decode('ascii')
            
            # If the server requests nickname, send the chosen nickname
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                # Print messages from other clients
                print(message)
        except:
            # Close Connection When Error
            print("An error occurred!")
            client.close()
            break
        
# Sending Messages To Server
def write():
    while True:
        # Constructing message with nickname
        message = '{}: {}'.format(nickname, input(''))
        
        # Send message to server
        client.send(message.encode('ascii'))
        
# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
