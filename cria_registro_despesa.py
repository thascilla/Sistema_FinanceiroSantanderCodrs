import csv
from datetime import datetime
import os
from utils import limpar_tela

#funcao sera destinada para armazenar apenas os registros de despesa em um CSV na pasta registros.

def cria_registro_despesa(flag_atualiza=None):
    mensagem = "informe o valor da despesa: "
    mensagem_erro = "entrada inválida, informe um valor numérico"

    despesa = valida_digito(mensagem, mensagem_erro)
    data = determina_data()
    
    registro = ['despesa', -despesa, data]
    
    if flag_atualiza.get('atualiza'):
        atualiza_registro_despesa(registro, flag_atualiza['id'], flag_atualiza['operacao'])
    else:
        salva_registro(registro)

def valida_digito(mensagem:str, mensagem_erro:str):

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
                print("valor deve ser maior que zero.")

def determina_data():
    data = datetime.now().date()
    return data.day, data.month, data.year

def salva_registro(registro:list):
    if not os.path.isdir('../registros'):
        os.makedirs('../registros')

    if not os.path.isfile('../registros/registros_despesa.csv'):
        with open('../registros/registros_despesa.csv', 'w') as file:
             pass
        
    with open('../registros/registros_despesa.csv','a') as file:
        registros_despesa = csv.writer(file, delimiter=';', lineterminator='\n')
        registros_despesa.writerow(registro)

    print ('Registro de despesa salvo')
    mensagem = "Pressione Enter para continuar... \n"
    input(mensagem)
    limpar_tela()

def atualiza_registro_despesa(registro, id, operacao):
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

    with open('../registros/registros_despesa.csv','a') as file:

        escritor = csv.writer(file, delimiter=';', lineterminator='\n')
        escritor.writerow(registro)

    print('Registro atualizado')
    mensagem = "Pressione Enter para continuar... \n"
    input(mensagem)
    limpar_tela()