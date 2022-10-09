class Recv:
    def __init__(self, Nome, Senha):
        self.nome_H = Nome
        self.senha = Senha

        self.conn = None
        self.ender = None

        import socket

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = socket.gethostbyname(socket.gethostname())
        server.bind((str(ip), self.senha))

        self.server = server

    def abrir_host(self):
        self.server.listen(1)
        conn, ender = self.server.accept()

        self.conn = conn
        self.ender = ender

    def fechar_conn(self):
        self.conn.close()

    def fechar_server(self):
        self.conn.close()
        self.server.close()

    def enviar_nome(self):
        self.conn.send(str.encode(self.nome_H, 'utf-8'))

    def receber_nome(self):
        global nome

        nome = self.conn.recv(1024)
        nome = nome.decode('utf-8')

        return nome

    def receber_arquivo(self):
        from time import sleep

        try:
            print(f"Esperando {nome} mandar o nome do arquivo...")
        except NameError:
            print("Esperando alguém madar o nome do arquivo...")

        namefile = self.conn.recv(1024)
        namefile = namefile.decode()

        print("Recebendo arquivo...")
        with open(f"Receber/{namefile}", "wb") as file_w:
            fim = False

            while not fim:
                receiving = self.conn.recv(1024)

                while receiving:
                    file_w.write(receiving)
                    receiving = self.conn.recv(1024)

                    fim = True

        sleep(1)
        print(f"\n{namefile} recebido!")


class Env:
    def __init__(self, env_name):
        self.nome = env_name

        import socket

        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente = cliente

    def conectar(self, ip, senha):
        try:
            self.cliente.connect((ip, senha))
            return 'CONECTADO'

        except ConnectionRefusedError:
            return 'ERRO'

        except TimeoutError:
            return 'ERRO'

    def fechar_conn(self):
        self.cliente.close()

    def receber_nome(self):
        global name

        name = self.cliente.recv(1024).decode('utf-8')

        return name

    def enviar_nome(self):
        self.cliente.send(str.encode(self.nome, 'utf-8'))

    def enviar_arquivo(self):
        from os import listdir
        from time import sleep

        env = False

        print("Digite o nome do arquivo abaixo para ser enviado")
        print("(Não esqueça da extenção do arquivo. Exemplo: .txt, .mp3, .mp4)")
        namefile = str(input("Arquivo: "))

        print("\nProcurando o arquivo para ser mandado...")
        sleep(2.5)

        while not env:
            pasta_env = listdir("Enviar")
            arquivos = list()

            for arquivo in pasta_env:
                arquivos.append(arquivo)

            if namefile in arquivos:
                self.cliente.send(str.encode(namefile, 'utf-8'))

                print("\nArquivo encotrado!\nEnviando o arquivo...")
                with open(f"Enviar/{namefile}", "rb") as file_r:
                    file = file_r.read(1024)

                    while file:
                        self.cliente.send(file)
                        file = file_r.read(1024)

                sleep(2.5)
                print(f"\n{namefile} enviado!")

                env = True

            else:
                print("\nArquivo não encontrado\nDigite abaixo o nome do arquivo correto")
                print("(Se o arquivo não estiver na pasta Enviar não podera ser enviado)")

                namefile = str(input("Arquivo: "))
