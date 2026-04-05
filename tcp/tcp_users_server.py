import socket


def server():
    messages = []
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(10)
    print("Сервер запущен и ждет подключений....")

    while True:
        client_socket, client_address = server_socket.accept()
        server_address = client_address[0]
        print(f"Пользователь с адресом: {server_address} подключился к серверу")

        try:
            data = client_socket.recv(1024).decode()
            if data:
                print(f"Пользователь с адресом: {server_address} отправил сообщение: {data}")
                messages.append(data)
                client_socket.send('\n'.join(messages).encode())
        finally:
            client_socket.close()


if __name__ == '__main__':
    server()