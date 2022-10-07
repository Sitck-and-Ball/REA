def verificar_pastas():
    from os import path

    if path.exists('Enviar'):
        pasta_env = True
    else:
        pasta_env = False

    if path.exists('Receber'):
        pasta_rec = True
    else:
        pasta_rec = False

    return pasta_env, pasta_rec


def criar_pastas():
    from os import makedirs, path

    if not path.exists('Enviar'):
        makedirs('Enviar')

    if not path.exists('Receber'):
        makedirs('Receber')
