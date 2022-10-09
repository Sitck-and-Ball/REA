import Gerenciador as Gc
from time import sleep

# Verificar arquivos nessarias para o funcionamento do sistema
print("Verificando pastas...")
check_folder = Gc.Pasta_Config.verificar_pastas()
check_user = Gc.User_Config.verificar_arquivo_user()
sleep(1.5)

if False in check_folder:
    print("Criando pastas...")
    Gc.Pasta_Config.criar_pastas()
    sleep(2.5)
    print("Pastas criadas")

else:
    print("Pastas ok!")
    sleep(2)

if check_user:
    print('\nProurando nomes salvos...')
    lista_nomes = Gc.User_Config.adicionar_nome_na_lista(Host=False, Cliente=True)
    qtd_nomes = len(lista_nomes)
    sleep(2.5)

    if qtd_nomes == 0:
        print("\nNenhum nome encontrado")
        nome = str(input("Digite um nome de sua escolha: "))
        nome = nome.strip()

        print("\nSalvando nome...\nNome selecionado!")
        Gc.User_Config.amazenar_nome(nome, Host=False, Cliente=True)

    else:
        print("\nNomes encontrados!")
        print("Carregando nomes...\n")

        for nome in lista_nomes:
            sleep(1)
            print(nome)

        # Selecionar algum nome mostrado acima, senão quiser nenhum nome acima criar outro nome (ou usuario)
        escolha = str(input("\nDigite uns dos nomes acima ou digite novo para criar um novo nome\nNome: "))
        escolha = escolha.strip()
        if escolha in lista_nomes:
            pass
        else:
            escolha = escolha.upper()

        if escolha == 'NOVO':
            # Código para salvar um novo nome
            salvar_nome = str(input("\nDigite um novo nome: "))
            salvar_nome = salvar_nome.strip()

            print('Salvando nome...')
            Gc.User_Config.amazenar_nome(nome=salvar_nome, Host=False, Cliente=True)
            sleep(2.5)
            print("Nome salvo!\nNome selecionado!")
            nome = salvar_nome
            sleep(1.5)

        else:
            # Verificar se o nome selecionado existe, senão criar nome ou selecionar outro
            if escolha in lista_nomes:
                nome = escolha
                print('\nNome selecionado!')

            else:
                while True:
                    print("\nNome não encontrado, digite 'outro' para selecionar outro nome, ou, digite 'novo' para criar um novo nome")
                    escolha = str(input("Digite: "))
                    escolha = escolha.strip()
                    escolha = escolha.upper()

                    if escolha == 'NOVO':
                        salvar_nome = str(input("\nDigite um novo nome: "))
                        salvar_nome = salvar_nome.strip()
                        Gc.User_Config.amazenar_nome(salvar_nome, Host=False, Cliente=True)

                        nome = salvar_nome
                        break

                    elif escolha == 'OUTRO':
                        qtd_nomes = len(lista_nomes)
                        qtd_nomes = qtd_nomes - 1
                        mostrados = 0

                        for _ in lista_nomes:
                            if mostrados == 0 and mostrados == qtd_nomes:
                                print('\n' + lista_nomes[mostrados] + '\n')

                            elif mostrados == 0:
                                print('\n' + lista_nomes[mostrados])

                            elif mostrados == qtd_nomes:
                                print(lista_nomes[mostrados] + '\n')

                            else:
                                print(lista_nomes[mostrados])
                            mostrados += 1

                        escolha = str(input("Digite uns dos nomes mostrados acima: "))

                        if escolha in lista_nomes:
                            print("\nNome selecionado!")
                            nome = escolha
                            break

                        else:
                            print("\nNome não encontrado")

else:
    print("\nNomes não encotrados, digite um nome abaixo para prosseguir")
    nome = str(input("Digite: "))
    nome = nome.strip()

    print("\nSalvando nome...")
    Gc.User_Config.amazenar_nome(nome=nome, Host=False, Cliente=True)
    sleep(2.5)
    print("Nome salvo!")
    sleep(1.5)

Env = Gc.Connection.Env(env_name=nome)

ip_connection = str(input("\nDigite o ip no qual deseja se conectar: "))
senha = int(input("Digite a senha: "))

print("\nTentando estabelecer uma conexão")

conexao = Env.conectar(ip_connection, senha)

if conexao == 'ERRO':
    while conexao != 'CONECTADO':
        print(
            "\nErro ao conectar, digite 'conectar' para tentar se conectar de novo ou digite 'outro' para se conectar em outro usuario")
        escolha = str(input("Digite: "))
        escolha = escolha.strip()
        escolha = escolha.upper()

        if escolha == 'CONECTAR':
            conexao = Env.conectar(ip_connection, senha)

        elif escolha == 'OUTRO':
            ip_connection = str(input("\nDigite um outro ip: "))
            senha = int(input("Digite a senha: "))

            conexao = Env.conectar(ip_connection, senha)

if conexao == 'CONECTADO':
    pass

else:
    print("Algo inesperado aconteceu, fechando app...")
    sleep(3)
    exit()

print("Conexão estabelecida!\n")

Env.enviar_nome()
host_name = Env.receber_nome()

print(f"Você está conectado com {host_name} Prosseguir?")
escolha = str(input("Sim ou não: "))
escolha = escolha.upper()
escolha = escolha.strip()

if escolha == 'SIM':
    print("\nProsseguindo com a conexão")
    print("Abrindo configuração de envio de arquivo...\n")
    sleep(2.5)
else:
    print("\nFehando app...")
    sleep(3)
    Env.fechar_conn()
    exit()

try:
    Env.enviar_arquivo()

except ConnectionAbortedError:
    print(f"\n{host_name} fechou a conexão")
    print("Fechando app...")
    sleep(4)
    Env.fechar_conn()
    exit()

print("\nFechando conexão...")
Env.fechar_conn()
sleep(3)

print("\nGostou do REA beta?")
print("Então ajude o prejeto mandando alguns satoshis")
print("bc1qaaxa5m95wgycjwnhxyrtrm75qr9525gn4whevf")
sleep(5)

input("\nAperte enter para fechar o app")

Env.fechar_conn()
print("Fechando app...")
sleep(1.5)
exit()
