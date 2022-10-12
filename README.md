# REA
  REA é um projeto de envio e recebimento de arquivos, usando a biblioteca socket e pyinstaller fizemos um app no qual você pode enviar e receber arquivo de qualquer lugar
  do mundo, apenas é necessária uma conexão com a internet.


# Guia Rápido
  Baixe o zip que contêm os arquivos exe, testado somente no windows, caso queira usar no lixus ou mac baixe o Rea open que provavelmente ira funcionar mas
  será necessário o python instalado (já vem instalado no mac e no lixus, se quiser usar o Rea open no windows precisa instalar o python separadamente).

  Depois de baixado, execute o ENV.exe para enviar um arquivo ou RECV.exe para receber um arquivo. Abaixo está um guia de como usá-los:


## ENV
  #### Username
    Quando abrir ele vai verificar se têm as pastas necessárias e um username salvo caso não tenha você digite um de sua preferencia, e salvará automaticamente,
  se já tiver ele
  mostrará todos os nomes salvos no qual você escolherá usar, ou, se quiser digite outro para salvar um outro nome.

  #### Conectividade
    Depois disso coloque um ip e a port/senha no qual você queira se conectar, se não conseguir conectar vai aparecer opções para tentar novamente, ou, colocar
    um novo ip e senha.

    Quando conectado vai aparacer o username da pessoa que você se conectou, e duas opções: Se quiser continuar conectado, ou, fechar a conexão ali mesmo.
    Se continuar, a função de enviar arquivo ira ser chamada. Para enviar é necessário que o arquivo esteja numa pasta chamada Enviar.
 
## RECV 
  #### Username
    Quando abrir ele vai verificar se têm as pastas necessárias e um username salvo caso não tenha você digite um de sua preferencia, e salvará automaticamente,
    se já tiver ele
    mostrará todos os nomes salvos no qual você escolherá usar, ou, se quiser digite outro para salvar um outro nome.

  #### Conectividade
    Depois disso coloque uma senha com apenas números inteiros, manda o seu ip e a senha para alguém para que ele possa se conectar, para ter a certeza que é
    a pessoa certa o username dele ira ser mostrado na tela, com as opções de continuar conectado ou não.
    Se continuar, a função de receber arquivo ira ser chamada. Quando o arquivo for recebido ele estará na pasta Receber.


# Monetização
  A meneira escolhida de monetizar foi com as doações, caso você gostou do projeto, no fim do ENV.exe e do RECV.exe vai tá lá o endereço de uma carteira bitcoin
  para doações.
  
  Nenhum dado é pego ou salvo (a não ser o username, mas ele é salvo somente no teu pc), caso esteja em dúvida o Rea é open source você mesmo pode ir na pasta
  Rea open que vai tá lá todo o código.
