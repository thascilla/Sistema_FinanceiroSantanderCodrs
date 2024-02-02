import csv
from datetime import datetime
import os
from utils import limpar_tela

#função será destinada para armazenar apenas os registros de receita.

def cria_registro_receita(flag_atualiza=None):
    """
    Obtem as informacoes referentes a operacao receita
    e salva o registro com a funcao salva_registro
    """
    
    mensagem = "Informe o valor da receita: "
    mensagem_erro = "Entrada invalida, informe um valor da numerico"
    receita = valida_digito(mensagem, mensagem_erro)

    data = determina_data()

    registro = ['receita', receita, data]
    
    if flag_atualiza.get('atualiza'):
        atualiza_registro_receita(registro, flag_atualiza['id'], flag_atualiza['operacao'])
    else:
        salva_registro(registro)

def valida_digito(mensagem:str, mensagem_erro:str):
    """
    Faz a validacao do valor informado pelo usuario, caso nao seja
    um numero a conversao para float ira gerar um erro, que faz a função
    requisitar novamente o valor numerico. Caso o valor nao seja maior que zero
    a função  requisitara novamente o valor numerico
    """

    while True:
        try:
            despesa = float(input(mensagem))   
        except ValueError:
            print(mensagem_erro)
            continue
        else:
            if despesa > 0:
                return despesa 
            else:
                print("O valor deve ser maior que zero.")

def determina_data():
    """
    Obtem a data de realização do registro
    retornando um tupla no formato (dia, mes, ano) 
    """

    data = datetime.now().date()
    return data.day, data.month, data.year

def salva_registro(registro:list):
    """
    Recebe uma lista representando o registro com as suas 
    respectivas informações e salva no arquivo ../registros/registros_receita.csv.
    """

    if not os.path.isdir('../registros'):
        os.makedirs('../registros')

    if not os.path.isfile('../registros/registros_receita.csv'):
        with open('../registros/registros_receita.csv', 'w') as file:
            pass

    with open('../registros/registros_receita.csv','a') as file:
        registros_receita = csv.writer(file, delimiter=';', lineterminator='\n')
        registros_receita.writerow(registro)
    
    print('Registro de receita salvo ')
    mensagem = "Pressione Enter para continuar... \n"
    input(mensagem)
    limpar_tela()

def atualiza_registro_receita(registro, id, operacao):
    """
    Recebe uma lista representando o registro com as suas 
    respectivas informações e salva no arquivo registros/registros.csv.
    """

    registros_path = {
        '1': '../registros/registros_despesa.csv',
        '2': '../registros/registros_receita.csv',
        '3': '../registros/investimento.csv'}

    with open(registros_path[operacao],'r') as file:

        registros = list(csv.reader(file, delimiter=';', lineterminator='\n'))
        
    del registros[id] 

    with open(registros_path[operacao],'w') as file:

        escritor = csv.writer(file, delimiter=';', lineterminator='\n')
        escritor.writerows(registros)

    with open('../registros/registros_receita.csv','a') as file:

        escritor = csv.writer(file, delimiter=';', lineterminator='\n')
        escritor.writerow(registro)

    print('\n Registro atualizado \n')
    mensagem = "\n Pressione Enter para continuar... \n"
    input(mensagem)
    limpar_tela()
