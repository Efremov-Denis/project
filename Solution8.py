import threading
import socket
import json

def load_configs():
    return {
        'ACTION': 'action',
        'TIME': 'time',
        'ACCOUNT_NAME': 'account_name',
        'EXIT': 'exit',
        'PRESENCE': 'presence',
        'USER': 'user',
        'MESSAGE': 'message',
        'MESSAGE_TEXT': 'message_text'
    }

# Определение конфигурации
configs = load_configs()

def create_transport(server_address):
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect(server_address)  # Устанавливаем соединение с сервером
    return transport

def get_user_message(transport, configs):
    return input("Введите ваше сообщение: ")

def handle_server_message(message, configs):
    # Просто выводим полученное сообщение
    print("Received message from server:", message)

def get_message(transport, configs):
    # Получаем сообщение от сервера
    message = transport.recv(1024).decode('utf-8')
    # Подтверждаем получение сообщения обратной отправкой подтверждения
    confirm_message = "Message received"
    transport.send(confirm_message.encode('utf-8'))
    return message

def send_message(transport, message, configs):
    try:
        message_json = json.dumps(message)
        transport.send(message_json.encode('utf-8'))
    except (OSError, json.JSONDecodeError) as e:
        print(f"Error while sending message: {e}")

def listen_for_messages(transport, configs):
    while True:
        try:
            message_bytes = transport.recv(1024)  # Принимаем сообщение
            if message_bytes:
                message = json.loads(message_bytes.decode('utf-8'))  # Декодируем и разбираем сообщение
                handle_server_message(message, configs)  # Обрабатываем полученное сообщение
        except (OSError, json.JSONDecodeError) as e:
            print(f"Error while listening for messages: {e}")

def start_client(server_address):
    transport = create_transport(server_address)
    send_thread = threading.Thread(target=send_message, args=(transport, get_user_message(transport, configs), configs))
    listen_thread = threading.Thread(target=handle_server_message, args=(get_message(transport, configs), configs))

    send_thread.start()
    listen_thread.start()

    send_thread.join()
    listen_thread.join()

def main():
    server_address = 'адрес_сервера_и_порт'
    start_client(server_address)

if __name__ == '__main__':
    main()