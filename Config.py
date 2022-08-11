class Host:
    def __init__(self, nome_host, senha):
        self.nome_h = nome_host
        self.senha = senha

    def data_exchange(self):
        import socket
        from time import sleep

        # Ligando host e procurando um cliente
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = socket.gethostbyname(socket.gethostname())
        server.bind((f'{ip}', self.senha))
        server.listen(1)
        conn, ender = server.accept()

        # Receber nome do clinte
        while True:
            nome = conn.recv(1024)
            if not nome:
                break
            print("\nCliente encontrado!")
            print(f"Você se conectou com {nome.decode()}\n")
            choice = str(input("Prosseguir?\nSim ou não: "))

            if choice == str("sim"):
                print("Continuando...\n")
                break

            elif choice == str("não"):
                print("Saindo...")
                sleep(3)
                conn.close()
                exit()

        conn.sendall(str.encode(self.nome_h))

        # Troca de menssagens
        print(f"Esperando {nome.decode()} mandar alguma mensagem\n")
        while True:
            mens = conn.recv(1024)
            print(f"{nome.decode()}: {mens.decode()}")

            mens = str(input("Digite: "))

            if mens == str("!receber"):
                conn.sendall(str.encode("quer receber um arquivo"))
                print(f"\nAguardando resposta do {nome.decode()}")
                responce = conn.recv(1024)

                if responce.decode() == str(f"{nome.decode()} atendeu o seu pedido"):
                    print(responce.decode())
                    print("Se preparando para receber o arquivo\n")
                    sleep(3)
                    break
                elif responce.decode() == str(f"{nome.decode()} recusou o seu pedido"):
                    print(responce.decode() + "\n")

            elif mens == "!sair":
                conn.sendall(str.encode("Host se desconectou"))
                sleep(2)
                conn.close()
                print("Saindo...")
                sleep(3)
                exit()

            else:
                conn.sendall(str.encode(mens))

        print(
            "Digite o nome do arquivo que deseja receber\n(não esqueça da extenção Exemplo: .exe, .jpng, .png, .mp4 e .mp3)")
        namefile = input("Arquivo> ")

        conn.send(namefile.encode())

        check = conn.recv(1024)

        if check.decode() == str("ERRO"):
            print("O arquivo que você pediu não existe, fechando conexão...\n")
            sleep(5)
            conn.close()
            print("Fechando app...")
            sleep(3)
            exit()

        elif check.decode() == str("OK"):
            print("O arquivo que você pediu foi encontra e está sendo enviado!")

        with open(f"Receber/{namefile}", "wb") as file_w:
            fim = 0
            while fim == 0:

                receiving = conn.recv(1024)

                while receiving:
                    file_w.write(receiving)
                    receiving = conn.recv(1024)

                    fim = 1

            print(f"{namefile} recebido!\n")

            conn.close()
        print("Fechando app...")
        sleep(4)
        exit()


class Connect:
    def __init__(self, ip_host, nome_client, senha_c):
        self.ip = ip_host
        self.nome_c = nome_client
        self.senha = senha_c

    def data_exchange(self):
        import socket
        from time import sleep

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((self.ip, self.senha))
            print("\nHost encontrado!\nEsperando Host aceitar sua conexão\n")

        except:
            while True:
                print("\nHost pode está desconectado, ou, talvez o ip ou a senha esteja incorretos, tentar de novo?")
                choice = str(input("Sim ou não: "))

                if choice == str("sim"):
                    try:
                        client.connect((self.ip, self.senha))
                        print("Host encontrado!\nEsperando Host aceitar sua conexão\n")
                        break

                    except:
                        pass

                elif choice == str("não"):
                    print("\nSaindo...")
                    sleep(3)
                    exit()

        client.sendall(str.encode(self.nome_c))

        nome = client.recv(1024)
        print("O host aceitou a sua conexão")
        sleep(3)
        print(f"Conectado com {nome.decode()}")
        print("Mande uma mensagem para ele")

        # Troca de menssagens
        while True:
            # escrever menssagem
            mens = str(input("Digite: "))

            if mens == str("!sair"):
                client.sendall(str.encode("Cliente se desconectou"))
                sleep(2)
                client.close()
                print("Saindo...")
                sleep(3)
                exit()

            # mandar menssagem
            client.sendall(str.encode(mens))

            # receber menssagem do host
            mens = client.recv(1024)

            if mens.decode() == str("quer receber um arquivo"):
                print(f"\n{nome.decode()} {mens.decode()}")
                mens = str(input("Atender pedido?\nSim ou não: "))
                if mens == str("sim"):
                    client.sendall(str.encode(f"{self.nome_c} atendeu o seu pedido"))
                    print("\nSe preparando para enviar")
                    sleep(3)
                    print(f"Esperando {nome.decode()} enviar o nome do arquivo que quer receber")
                    print("(Obs: para enviar o arquivo é preciso que o arquivo esteja na pasta Enviar)")
                    break

                elif mens == str("não"):
                    print(f"Você recusou o pedido de {nome.decode()}")
                    client.sendall(str.encode(f"{self.nome_c} recusou o seu pedido"))

            else:
                print(f"{nome.decode()}: {mens.decode()}")

        # receber nome do arquivo que o host quer
        namefile = client.recv(1024)

        import os

        list_file = os.listdir("Enviar")

        if not namefile.decode() in list_file:
            print("O arquivo que o host pediu não existe ou não está na pasta Enviar, fechando conexão...\n")
            sleep(5)
            client.sendall(str.encode("ERRO"))
            client.close()
            print("Fechando app...")
            sleep(3)
            exit()
        else:
            client.sendall(str.encode("OK"))

        # tentar mandar o arquivo
        try:
            print(f"Mandando Arquivo para o host: {nome.decode()}")

            with open(f"Enviar/{namefile.decode()}", "rb") as file:
                file_r = file.read(1024)
                while file_r:
                    client.send(file_r)
                    file_r = file.read(1024)
                client.close()
                print("Arquivo enviado!")

        # se não conseguir faz isso
        except:
            client.sendall(str.encode("ERRO"))
            print("ERRO:")
            print(" Arquivo não encontrado ou erro ao enviar arquivo")
            client.close()
            sleep(4)
