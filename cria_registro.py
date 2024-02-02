import csv
import os
from cria_registro_receita import cria_registro_receita
from cria_registro_despesa import cria_registro_despesa
from Investimentos import investimento
from utils import determina_data, valida_digito

def cria_registro(**kwargs):
    """
    Tela inicial com as opçoes de tipos de operacoes
    """

    repeat_question = True

    while repeat_question:

        operacao = input('''Digite a opção que deseja realizar:  \n"
                        
                        [1] CRIAR UM REGISTRO DE DESPESA                             
                        [2] CRIAR UM REGISTRO DE RECEITA                              
                        [3] INVESTIMENTOS                        
                        [4] CANCELAR 
                             
                             insira o número da opção desejada: ''')
        
        if operacao not in ['1','2','3','4']:

            print("Entrada invalida")

        elif operacao == '4':
            
            repeat_question = False
            continue
        
        elif operacao == '1':

            cria_registro_despesa(kwargs)
            repeat_question = False

        elif operacao == '2':
            
            cria_registro_receita(kwargs)
            repeat_question = False


        elif operacao == '3':
            
            investimento(kwargs)
            repeat_question = False


def  executa_investimento():
    """
    Obtem as informacoes referentes a operacao investimento
    e salva o registro com a funcao salva_registro
    """
    
    mensagem = "Informe o valor do Investimento"
    mensagem_erro = "Entrada invalida, informe um valor da numerico"
    investimento = valida_digito(mensagem, mensagem_erro)

    data = determina_data()
    taxa_de_juros = 0.11

    registro = ['investimento', investimento, data, taxa_de_juros]
    salva_registro(registro)

     
def salva_registro(registro:list):
    """
    Recebe uma lista representando o registro com as suas 
    respectivas informações e salva no arquivo registros/registros.csv.
    """

    with open('registros/registros.csv','a') as file:

        registros = csv.writer(file, delimiter=';', lineterminator='\n')
        registros.writerow(registro)
    
    print('Registro salvo')



    

    