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
    print("Pastas criadas\n")

else:
    print("Pastas ok!\n")
    sleep(2)

if check_user:
    print('Prourando nomes salvos...')
    lista_nomes = Gc.User_Config.adicionar_nome_na_lista(Host=True, Cliente=False)
    qtd_nomes = len(lista_nomes)
    sleep(2.5)

    if qtd_nomes == 0:
        print("\nNenhum nome encontrado")
        nome = str(input("Digite um nome de sua escolha: "))
        nome = nome.strip()

        print("\nSalvando nome...\n")
        Gc.User_Config.amazenar_nome(nome, True, False)

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
            Gc.User_Config.amazenar_nome(nome=salvar_nome, Host=True, Cliente=False)
            sleep(2.5)
            print("Nome salvo!\nNome selecionado!\n")
            nome = salvar_nome
            sleep(1.5)

        else:
            # Verificar se o nome selecionado existe, senão criar nome ou selecionar outro
            if escolha in lista_nomes:
                nome = escolha
                print('\nNome selecionado!\n')

            else:
                while True:
                    print("\nNome não encontrado, digite 'outro' para selecionar outro nome, ou, digite 'novo' para criar um novo nome")
                    escolha = str(input("Digite: "))
                    escolha = escolha.strip()
                    escolha = escolha.upper()

                    if escolha == 'NOVO':
                        salvar_nome = str(input("\nDigite um novo nome: "))
                        salvar_nome = salvar_nome.strip()
                        Gc.User_Config.amazenar_nome(salvar_nome, Host=True, Cliente=False)

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
                            print("\nNome selecionado!\n")
                            nome = escolha
                            break

                        else:
                            print("\nNome não encontrado")

else:
    print("Nomes não encotrados, digite um nome abaixo para prosseguir")
    nome = str(input("Digite: "))
    nome = nome.strip()

    print("\nSalvando nome...")
    Gc.User_Config.amazenar_nome(nome=nome, Host=True, Cliente=False)
    sleep(2.5)
    print("Nome salvo!")
    sleep(1.5)

senha = None

print("Agora digte uma senha para o seu HOST")
while type(senha) != int:
    try:
        senha = int(input('Digite uma senha com apenas números: '))

    except ValueError:
        print("\nPor favor digite apenas números")

Recv = Gc.Connection.Recv(Nome=nome, Senha=senha)

print("\nAbrindo host...")
sleep(1.5)
print("Esperando alguém se conectar...\n")
Recv.abrir_host()

cliente_name = Recv.receber_nome()
Recv.enviar_nome()

print(f"Você está conectado com {cliente_name} Prosseguir?")
escolha = str(input("Sim ou não: "))
escolha = escolha.upper()
escolha = escolha.strip()

if escolha == 'SIM':
    print("\nProsseguindo com a conexão")
    print("Abrindo configuração de recebimento de arquivo...\n")
    sleep(2.5)

else:
    print("\nFechando app...")
    sleep(3)
    Recv.fechar_server()
    exit()

try:
    Recv.receber_arquivo()

except ConnectionAbortedError:
    print(f"\n{cliente_name} fechou a conexão")
    print("Fechando app...")
    sleep(3)
    Recv.fechar_server()
    exit()

print("\nFechando conexão...")
Recv.fechar_server()
sleep(3)

print("\nGostou do REA beta?")
print("Então ajude o prejeto mandando alguns satoshis")
print("bc1qaaxa5m95wgycjwnhxyrtrm75qr9525gn4whevf")
sleep(5)

input("\nAperte enter para fechar o app")

print("Fechando app...")
sleep(1.5)
exit()
