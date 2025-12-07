import socket

# Configurações do Servidor
HOST = 'localhost'  # Endereço IP (localhost = 127.0.0.1)
PORT = 8080         # Porta onde o servidor vai escutar

def iniciar_servidor():
    # 1. Criação do Socket
    # AF_INET = IPv4, SOCK_STREAM = TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Bind (Vincular o socket ao endereço e porta)
    # Setsockopt permite reusar a porta imediatamente caso o servidor seja reiniciado
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    
    # 3. Listen (Colocar em modo de escuta)
    server_socket.listen()
    print(f"Servidor rodando e escutando em http://{HOST}:{PORT} ...")

    while True:
        # 4. Aceitar conexão
        # client_socket é o novo socket para comunicar com este cliente específico
        client_socket, client_address = server_socket.accept()
        
        # 5. Ler a requisição (lê até 1024 bytes)
        request = client_socket.recv(1024).decode('utf-8')
        
        if request:
            # Pega apenas a primeira linha (Ex: GET / HTTP/1.1) conforme solicitado
            primeira_linha = request.split('\r\n')[0]
            print(f"Recebido de {client_address}: {primeira_linha}")

        # 6. Construir a Resposta HTTP Manualmente
        # Estrutura: Linha de Status \r\n Headers \r\n \r\n Corpo
        corpo_resposta = "<html><body><h1>Ola! Servidor HTTP Caseiro Funcionando!</h1></body></html>"
        
        http_response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            f"Content-Length: {len(corpo_resposta)}\r\n"
            "\r\n"
            f"{corpo_resposta}"
        )

        # 7. Enviar resposta e fechar conexão
        client_socket.sendall(http_response.encode('utf-8'))
        client_socket.close()

if __name__ == "__main__":
    try:
        iniciar_servidor()
    except KeyboardInterrupt:
        print("\nServidor parando...")