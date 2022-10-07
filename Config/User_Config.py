def amazenar_nome(nome, Host, Cliente):
    from os import path

    if path.isfile('Config/user.txt'):
        with open('Config/user.txt', 'r') as file:
            lines = file.readlines()
            itens = len(lines)

        with open('Config/user.txt', 'a') as file:
            if type(Host) != bool or type(Cliente) != bool:
                print('''\033[0;31mERRO: TIPO ERRADO
        A variavel Host e Client precisa ser do tipo booleano\033[m''')

            if Host and not Cliente:
                if itens == 0:
                    file.write('H.' + nome)
                else:
                    file.write('\nH.' + nome)

            if not Host and Cliente:
                if itens == 0:
                    file.write('C.' + nome)
                else:
                    file.write('\nC.' + nome)

            if Host and Cliente:
                if itens == 0:
                    file.write('H.' + nome)
                    file.write('\nC.' + nome)
                else:
                    file.write('\nH.' + nome)
                    file.write('\nC.' + nome)

    else:
        with open('Config/user.txt', 'x') as file:
            if type(Host) != bool or type(Cliente) != bool:
                print('''\033[0;31mERRO: TIPO ERRADO
        A variavel Host e Client precisa ser do tipo booleano\033[m''')

            if Host and not Cliente:
                file.write('H.' + nome)

            if not Host and Cliente:
                file.write('C.' + nome)

            if Host and Cliente:
                file.write('H.' + nome)
                file.write('\nC.' + nome)


def adicionar_nome_na_lista(Host, Cliente):
    lista = list()

    try:
        with open('Config/user.txt', 'r') as file:
            file_name = file.readlines()

        for username in file_name:
            nome = username.replace('\n', '')

            if type(Host) != bool or type(Cliente) != bool:
                print('''\033[0;31mERRO: TIPO ERRADO
                A variavel Host e Client precisa ser do tipo booleano\033[m''')
                break

            if Host:
                if 'H.' in nome[0:2]:
                    lista.append(nome[2:])

            if Cliente:
                if 'C.' in nome[0:2]:
                    lista.append(nome[2:])

            if not Host and not Cliente:
                lista.append(None)
                break

    except FileNotFoundError:
        lista = None
        print("\033[0;31mArquivo user.txt não encontrado\033[m")

    return lista


def verificar_arquivo_user():
    from os import path

    if path.isfile('Config/user.txt'):
        info = True
    else:
        info = False

    return info
