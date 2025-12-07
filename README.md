# Servidor HTTP Simples em Python (Raw Sockets)

Este projeto implementa um servidor web extremamente simples utilizando Python e a biblioteca nativa `socket`. O objetivo é demonstrar como funciona a comunicação HTTP em baixo nível, sem o uso de frameworks web prontos.

## 📝 Funcionamento Básico

### O Protocolo HTTP
O HTTP (Hypertext Transfer Protocol) funciona no modelo cliente-servidor:
1.  **Requisição:** O cliente (navegador) envia um texto pedindo um recurso. A primeira linha contém o método (ex: `GET`), o caminho (ex: `/`) e a versão do protocolo.
2.  **Resposta:** O servidor processa e devolve uma mensagem contendo:
    * **Status Line:** Versão e código de status (ex: `HTTP/1.1 200 OK`).
    * **Headers:** Metadados sobre o conteúdo (ex: `Content-Type`).
    * **Body:** O conteúdo real (HTML, JSON, texto).

### Sockets
O socket é o ponto final de um fluxo de comunicação bidirecional entre dois programas na rede.
1.  **Criação:** Criamos um socket do tipo TCP/IP.
2.  **Bind:** Associamos o socket a um IP (`localhost`) e porta (`8080`).
3.  **Listen:** O servidor fica "ouvindo" por novas conexões.
4.  **Accept & Recv:** Quando o navegador conecta, o servidor aceita a conexão e lê os bytes enviados.
5.  **Send:** O servidor envia a string formatada como HTTP de volta.

## 🚀 Como Executar

### Pré-requisitos
* Python 3.x instalado.

### Passo a passo
1.  Clone este repositório ou baixe o arquivo `redes.py`.
2.  Abra o terminal na pasta do arquivo.
3.  Execute o servidor:
    ```bash
    python redes.py
    ```
4.  Você verá a mensagem: `Servidor rodando e escutando em http://localhost:8080 ...`
5.  Abra seu navegador e acesse: [http://localhost:8080](http://localhost:8080)

Você verá a mensagem HTML sendo renderizada e, no terminal, o log da requisição recebida.
