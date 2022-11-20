import os  # BIBLIOTECA PARA LIMPAR CONSOLE
import webbrowser  # BIBLIOTECA PARA REDICEIONAR PARA WEB

# declaração de variáveis
login_cpf = []
login_senha = []
login_nome = []
login_telefone = []
regiao = 0
kwh = 0
kwhTotal = 0
valorTotal = 0


objetos = []
consumoObjetos = {}

# PRINTAR A BANDEIRA DE CONSUMO DA REGIÃO


def printBandeira(Bandeira):
    print('A BANDEIRA DESSA REGIÃO É', Bandeira)
    print("="*30)

# ADICIONAR OBJETOS NO DICIONARIO E NA ARRAY


def addObjeto():
    nomeaux = str(input('Qual o nome do objeto? \nresposta: '))
    consumoaux = int(
        input('Qual o consumo em kwh do eletrodomestico? \n resposta:'))

# Adicionando ao array e ao dicionário
    objetos.append(nomeaux)
    consumoObjetos[nomeaux] = consumoaux


# armazenando os objetos em um array e o consumo deles em uma estrutura chamada dicionario(procura no google)
objetos = ['ADICONAR ELETRODOMESTICO', 'FORNO ELETRICO', 'AIR FRYER', 'TELEVISÃO', 'VENTILADOR', 'AR-CONDICIONADO', 'CHUVEIRO ELETRICO', 'FREEZER', 'COMPUTADOR', 'LAMPADA',
    'CARREGADOR', 'CAFETEIRA', 'CHURRASQUEIRA ELETRICA', 'BOMBA DE ÁGUA', 'ASPIRADOR DE PÓ', 'SECADOR DE CABELO', 'FERRO ELETRICO', 'MÁQUINA DE LAVAR ROUPA', 'IMPRESSORA', 'GELADEIRA']
consumoObjetos = {
    'GELADEIRA': 250,
    'FORNO ELETRICO': 6000,
    'AIR FRYER': 1500,
    'TELEVISÃO': 280,
    'VENTILADOR': 100,
    'AR-CONDICIONADO': 1400,
    'CHUVEIRO ELETRICO': 5500,
    'FREEZER': 500,
    'COMPUTADOR': 300,
    'LAMPADA': 12,
    'CARREGADOR': 3,
    'CAFETEIRA': 600,
    'CHURRASQUEIRA ELETRICA': 3000,
    'BOMBA DE ÁGUA': 400,
    'ASPIRADOR DE PÓ': 600,
    'SECADOR DE CABELO': 1000,
    'FERRO ELETRICO': 1000,
    'MÁQUINA DE LAVAR ROUPA': 1000,
    'IMPRESSORA': 45

}

# MOSTRA O MENU INICIAL NO CONSOLE


def mostrarMenu1():
    print('='*25)
    print('\033[36mBEM VINDO AO GREEN ENERGY\033[m')
    print('='*25)

    print('''
    [1] LOGIN
    [2] CADASTRAR
    [3] SAIR''')


opc = 0
while opc != 3:
  mostrarMenu1()

  opc = int(input('Escolha uma opção: '))
  os.system('cls')

# USUARIO COM O LOGIN FEITO ENTRA NO PROGRAMA
  if opc == 1:
    cpf = str(input('DIGITE O SEU CPF: '))
    senha = int(input('DIGITE SUA SENHA:\n(SOMENTE NUMEROS) '))
    if cpf in login_cpf:
      if senha in login_senha:
        os.system('cls')
        print('\033[32mLOGIN EFETUADO COM SUCESSO!\033[m')
        print('BEM VINDO')
        opeletro = 0
        while opeletro != 3:
            print('SELECIONE A OPCAO DESEJADA\n')
            print('''
                [1] ADICIONAR ELETRODOMESTICO
                [2] VERIFICAR CONSUMO TOTAL
                [3] SAIR''')
            opeletro = int(input('\nResposta: '))
            if opeletro == 1:
                os.system('cls')
                if regiao == 1:
                    Bandeira = 1
                    printBandeira(Bandeira)

                    for i in range(1, len(objetos)):
                        print(i, ": ", objetos[i])
                    resp = int(input(
                        '\nAdicone um dos eletrodomesticos da lista ou \033[33mdigite 0 para adicionar um novo: \033[m'))
                    objeto = objetos[resp]

                    if resp == 0:
                        print('\nMENU ADICIONAR OBJETO')
                        addObjeto()
                    else:

                        horas = int(
                            input(f'Quantas horas por dia {objeto.lower()} fica ligado ? '))
                        kwh = ((consumoObjetos[objeto] * 0.003) * horas)
                        kwhTotal += kwh
                        formulaValor = Bandeira * kwh
                        valorTotal += formulaValor
                        os.system('cls')

                # FUNÇAO QUE NAO PERMITE QUE O USUARIO USE + QUE 24 HORAS
                        if horas > 24:
                            print(
                                '\033[31mSELECIONE UMA QUANTIDADE DE HORAS VÁLIDA (DE 0 A 24)\033[m')
                            break

                        print(
                            f'A(o) {objeto.lower()} consumiu {kwh:.4f} kw e custou um total de {formulaValor:.2f} reais')
                elif regiao == 2:
                    Bandeira = 1.41473
                    printBandeira(Bandeira)

                    for i in range(len(objetos)):
                        print(i, ": ", objetos[i])
                    resp = int(input(
                        '\nAdicone um dos eletrodomesticos da lista ou \033[33mdigite 0 para adicionar um novo: \033[m'))
                    objeto = objetos[resp]

                    if resp == 0:
                        print('\nMENU ADICIONAR OBJETO')
                        addObjeto()
                    else:

                        horas = int(
                            input(f'Quantas horas por dia {objeto.lower()} fica ligado ? '))
                        kwh = ((consumoObjetos[objeto] * 0.003) * horas)
                        kwhTotal += kwh
                        formulaValor = Bandeira * kwh
                        valorTotal += formulaValor
                        os.system('cls')

                # FUNÇAO QUE NAO PERMITE QUE O USUARIO USE + QUE 24 HORAS
                        if horas > 24:
                            print(
                                '\033[31mSELECIONE UMA QUANTIDADE DE HORAS VÁLIDA (DE 0 A 24)\033[m')
                            break

                        print(
                            f'A(o) {objeto.lower()} consumiu {kwh:.4f} kw e custou um total de {formulaValor:.2f} reais')
                elif regiao==3:
                    Bandeira=1.3184
                    printBandeira(Bandeira)

                    for i in range(len(objetos)):
                        print(i,": ",objetos[i])
                    resp = int(input(
                        '\nAdicone um dos eletrodomesticos da lista ou \033[33mdigite 0 para adicionar um novo: \033[m'))
                    objeto = objetos[resp]

                    if resp == 0:
                        print('\nMENU ADICIONAR OBJETO')
                        addObjeto()
                    else:

                        horas = int(
                            input(f'Quantas horas por dia {objeto.lower()} fica ligado ? '))
                        kwh = ((consumoObjetos[objeto] * 0.003) * horas)
                        kwhTotal += kwh
                        formulaValor = Bandeira * kwh
                        valorTotal += formulaValor
                        os.system('cls')

                # FUNÇAO QUE NAO PERMITE QUE O USUARIO USE + QUE 24 HORAS
                        if horas > 24:
                            print(
                                '\033[31mSELECIONE UMA QUANTIDADE DE HORAS VÁLIDA (DE 0 A 24)\033[m')
                            break

                        print(
                            f'A(o) {objeto.lower()} consumiu {kwh:.4f} kw e custou um total de {formulaValor:.2f} reais')
                
                elif regiao==4:
                    Bandeira=1.72
                    printBandeira(Bandeira)

                    for i in range(len(objetos)):
                        print(i,": ",objetos[i])
                    resp = int(input(
                        '\nAdicone um dos eletrodomesticos da lista ou \033[33mdigite 0 para adicionar um novo: \033[m'))
                    objeto = objetos[resp]

                    if resp == 0:
                        print('\nMENU ADICIONAR OBJETO')
                        addObjeto()
                    else:

                        horas = int(
                            input(f'Quantas horas por dia {objeto.lower()} fica ligado ? '))
                        kwh = ((consumoObjetos[objeto] * 0.003) * horas)
                        kwhTotal += kwh
                        formulaValor = Bandeira * kwh
                        valorTotal += formulaValor
                        os.system('cls')

                # FUNÇAO QUE NAO PERMITE QUE O USUARIO USE + QUE 24 HORAS
                        if horas > 24:
                            print(
                                '\033[31mSELECIONE UMA QUANTIDADE DE HORAS VÁLIDA (DE 0 A 24)\033[m')
                            break

                        print(
                            f'A(o) {objeto.lower()} consumiu {kwh:.4f} kw e custou um total de {formulaValor:.2f} reais')
                
                
                elif regiao==5:
                    Bandeira=1.40
                    printBandeira(Bandeira)

                    for i in range(len(objetos)):
                        print(i,": ",objetos[i])
                    resp = int(input(
                        '\nAdicone um dos eletrodomesticos da lista ou \033[33mdigite 0 para adicionar um novo: \033[m'))
                    objeto = objetos[resp]

                    if resp == 0:
                        print('\nMENU ADICIONAR OBJETO')
                        addObjeto()
                    else:

                        horas = int(
                            input(f'Quantas horas por dia {objeto.lower()} fica ligado ? '))
                        kwh = ((consumoObjetos[objeto] * 0.003) * horas)
                        kwhTotal += kwh
                        formulaValor = Bandeira * kwh
                        valorTotal += formulaValor
                        os.system('cls')

                # FUNÇAO QUE NAO PERMITE QUE O USUARIO USE + QUE 24 HORAS
                        if horas > 24:
                            print(
                                '\033[31mSELECIONE UMA QUANTIDADE DE HORAS VÁLIDA (DE 0 A 24)\033[m')
                            break

                        print(
                            f'A(o) {objeto.lower()} consumiu {kwh:.4f} kw e custou um total de {formulaValor:.2f} reais')
            
            
            elif opeletro == 2:
                os.system('cls')
                print(f'\033[33mSeu consumo total em kw é\033[m {kwhTotal:.4f} kw e custou um total de {valorTotal:.2f} reais')
                if valorTotal > 430:
                    print('Com o seu consumo atual pode ser interessante o uso de energia solar. ')
                    resp1=int(input('''Você deseja ser redirecionado a realizar um orçamento de energia solar 
                    [1]-\033[32m[SIM]\033[m  
                    [2]-\033[31m[NÃO]\033[m 
                    '''))
                    if resp1==1:
                      webbrowser.open('https://ofertas.starsolenergiasolar.com.br/pedido-de-orcamento')
                    else:
                
                      print('QUE PENA!, O USO DE ENERGIA SOLAR PODE AJUDAR A REDUZIR A SUA CONTA EM ATÉ \033[32m95%\033[m ')
                if valorTotal < 429:
                    print('''\033[32m PARÁBENS, O SEU CONSUMU TEM UMA MEDIA MENOR DO QUE A MEDIA BRASILEIRA\033[m
                    MESMO ASSIM SERIA INTERESSANTE REDUZIR AINDA MAIS ESSE CONSUMO DE ENERGIA''')
                    resp2=int(input('''Você deseja ser redirecionado a dicas de redução de energia ?
                    [1]-\033[32m[SIM]\033[m  
                    [2]-\033[31m[NÃO]\033[m 
                    '''))
                    if resp2==1:
                      webbrowser.open('https://solarprime.com.br/como-reduzir-o-consumo-de-energia/')
                    
            if opeletro == 3:
                print('\033[36m DE VOLTA AO MENU, DESEJA ENCERRAR O PROGRAMA ? \033[m')
                
      else:
        print('\033[31mUsuário ou senha incorreto. Tente novamente.\033[m')
  
  if opc==2:
    nome=str(input('DIGITE SEU NOME: '))
    login_nome.append(nome)

    cpf=str(input('DIGITE O SEU CPF: '))
    login_cpf.append(cpf)

    senha=int(input('DIGITE A SUA SENHA (somente números): '))
    login_senha.append(senha)

    telefone=int(input('DIGITE O SEU TELEFONE: '))
    login_telefone.append(telefone)

    print('QUAL REGIÃO VOCÊ MORA?') 
    print('''
        [1] - NORTE 
        [2] - NORDESTE
        [3] - CETRO-OESTE
        [4] - SUDESTE
        [5] - SUL
        ''') 
    regiao=int(input('INFORME A SUA REGIÃO: '))

    os.system('cls')

    # SALVANDO USUARIO CADASTRADO
    # usuarios=open('dados/usuarios.txt','w+')
    # usuarios.write(nome)
    # usuarios.write(';')
    # usuarios.write(str(senha))
    # usuarios.write('\n')
    
    # usuarios.close()
    print('\033[33mCADASTRO REALIZADO!\033[m')

  if opc==3:
    print("\033[33mVOLTE SEMPRE, LEMBRE-SE ECONOMIZE ENERGIA\033[m")
 
    