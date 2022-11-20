import os
import webbrowser
login_cpf=[]
login_senha=[]
login_nome=[]
login_telefone=[]
regiao=0
kwh = 0
kwhTotal = 0
valorTotal = 0

# armazenando os objetos em um array e o consumo deles em uma estrutura chamada dicionario(procura no google)
objetos=['GELADEIRA','FORNO ELETRICO','AIR FRYER','TELEVISÃO','VENTILADOR','AR-CONDICIONADO','CHUVEIRO ELETRICO','FREEZER','COMPUTADOR','LAMPADA','CARREGADOR','CAFETEIRA', 'CHURRASQUEIRA ELETRICA','BOMBA DE ÁGUA', 'ASPIRADOR DE PÓ', 'SECADOR DE CABELO', 'FERRO ELETRICO','MÁQUINA DE LAVAR ROUPA','IMPRESSORA']
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
    'CHURRASQUEIRA ELETRICA':3000,
    'BOMBA DE ÁGUA':400,
    'ASPIRADOR DE PÓ':600,
    'SECADOR DE CABELO':1000,
    'FERRO ELETRICO':1000,
    'MÁQUINA DE LAVAR ROUPA':1000,
    'IMPRESSORA':45
}
#ADICONAR A OPÇÃO (OUTRO), PEDIR NOME, KWH, HORAS LIGADAS E ADICIONAR AO CONSUMO


opc=0
while opc!=3:
  print('='*25)
  print('\033[36mBEM VINDO AO GREEN ENERGY\033[m')
  print('='*25)
  
  print('''
  [1] LOGIN
  [2] CADASTRAR
  [3] SAIR''')

  opc=int(input('Escolha uma opção: '))
  os.system('cls')

  if opc==1:
    cpf=str(input('DIGITE O SEU CPF: '))
    senha=int(input('DIGITE SUA SENHA:\n(SOMENTE NUMEROS) '))
    if cpf in login_cpf:
      if senha in login_senha:
        os.system('cls')
        print('\033[32mLOGIN EFETUADO COM SUCESSO!\033[m')
        print('BEM VINDO')
        #SE A OP 1 FOR DIRETA, PRINTAR UMA MENSAGEM ALERTANDO PARA FAZER O CADASTRO
        opeletro = 0
        while opeletro != 3:
            print('SELECIONE A OPCAO DESEJADA\n')
            print('''
                [1] ADICIONAR ELETRODOMESTICO
                [2] VERIFICAR CONSUMO TOTAL
                [3] SAIR''')
            opeletro=int(input('\nResposta: '))
            if opeletro==1:
                os.system('cls')
                if regiao==1:
                    Bandeira=1
                    print(Bandeira)    
                    print("="*30)
                    
                    for i in range(len(objetos)):
                        print(i,": ",objetos[i])
                    resp=int(input('\nAdicone os eletrodomesticos da lista: '))
                    objeto=objetos[resp]
                    horas = int(input(f'Quantas horas por dia {objeto.lower()} fica ligado ? '))
                    
                    #COLOCAR A FUNÇAO QUE NAO PERMITE HORARIO MAIOR QUE 24
                    
                    kwh = ((consumoObjetos[objeto] * 0.003) * horas)
                    kwhTotal += kwh
                    formulaValor = Bandeira * kwh
                    valorTotal += formulaValor
                    os.system('cls')
                    print(f'A(o) {objeto.lower()} consumiu {kwh:.4f} kw e custou um total de {formulaValor:.2f} reais')
                elif regiao==2:
                    Bandeira=1.41473
                    print(Bandeira)    
                    print("="*30)
                    for i in range(len(objetos)):
                        print(i,": ",objetos[i])
                    resp=int(input('\nAdicone os eletrodomesticos da lista: '))
                    objeto=objetos[resp]
                    horas = int(input(f'Quantas horas por dia {objeto.lower()} fica ligado ? '))

                    kwh = ((consumoObjetos[objeto] * 0.003) * horas)
                    kwhTotal += kwh
                    formulaValor = Bandeira * kwh
                    valorTotal += formulaValor
                    os.system('cls')
                    print(f'A(o) {objeto.lower()} consumiu {kwh:.4f} kw e custou um total de {formulaValor:.2f} reais')
                elif regiao==3:
                    Bandeira=1.3184
                    print(Bandeira)    
                    print("="*30)
                    for i in range(len(objetos)):
                        print(i,": ",objetos[i])
                    resp=int(input('\nAdicone os eletrodomesticos da lista: '))
                    objeto=objetos[resp]
                    horas = int(input(f'Quantas horas por dia {objeto.lower()} fica ligado ? '))

                    kwh = ((consumoObjetos[objeto] * 0.003) * horas)
                    kwhTotal += kwh
                    formulaValor = Bandeira * kwh
                    valorTotal += formulaValor
                    os.system('cls')
                    print(f'A(o) {objeto.lower()} consumiu {kwh:.4f} kw e custou um total de {formulaValor:.2f} reais')
                elif regiao==4:
                    Bandeira=1.72
                    print(Bandeira)    
                    print("="*30)
                    for i in range(len(objetos)):
                        print(i,": ",objetos[i])
                    resp=int(input('\nAdicone os eletrodomesticos da lista: '))
                    objeto=objetos[resp]
                    horas = int(input(f'Quantas horas por dia {objeto.lower()} fica ligado ? '))

                    kwh = ((consumoObjetos[objeto] * 0.003) * horas)
                    kwhTotal += kwh
                    formulaValor = Bandeira * kwh
                    valorTotal += formulaValor
                    os.system('cls')
                    print(f'A(o) {objeto.lower()} consumiu {kwh:.4f} kw e custou um total de {formulaValor:.2f} reais')
                elif regiao==5:
                    Bandeira=1.40
                    print(Bandeira)    
                    print("="*30)
                    for i in range(len(objetos)):
                        print(i,": ",objetos[i])
                    resp=int(input('\nAdicone os eletrodomesticos da lista: '))
                    objeto=objetos[resp]
                    horas = int(input(f'Quantas horas por dia {objeto.lower()} fica ligado ? '))

                    kwh = ((consumoObjetos[objeto] * 0.003) * horas)
                    kwhTotal += kwh
                    formulaValor = Bandeira * kwh
                    valorTotal += formulaValor
                    os.system('cls')
                    print(f'A(o) {objeto.lower()} consumiu {kwh:.4f} kw e custou um total de {formulaValor:.2f} reais')
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
                
                      os.systems('cls')
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
                print('VAMOS LÁ, DE VOLTA AO MENU')
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
    print('\033[33mCADASTRO REALIZADO!\033[m')

  if opc==3:
    print("VOLTE SEMPRE, LEMBRE-SE ECONOMIZE ENERGIA")