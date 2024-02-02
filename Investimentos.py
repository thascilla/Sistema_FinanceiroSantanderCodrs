import csv
from datetime import datetime
import os
from utils import limpar_tela

# funcao sera destinada a armazenar registros de investimento e calcular a taxa de investimento.

def investimento(flag_atualiza=None):
    """
    Tela inicial da seleção de investimento
    """

    repeat_question = True

    while repeat_question:

        investimento = input('''informe o tipo de investimento desejado: \n"
                        
                        [1] Tesouro Direto: 10,06% a.a                             
                        [2] CDBs (Certificados de Depósito Bancário): 11,65% a.a                            
                        [3] Poupança: 6,17% a.a 
                        [4] Cancelar
                               
                             insira o número da opção desejada: ''')
                        
        if investimento == '1':
        
            aplicacao_tesouro_direto(flag_atualiza)
            repeat_question = False
            continue
        
        elif investimento == '2':

            aplicacao_cdb(flag_atualiza)
            repeat_question = False
            continue
    
        elif investimento == '3':
    
            aplicacao_poupanca(flag_atualiza)
            repeat_question = False
            continue
        
        elif investimento == '4':

            repeat_question = False
            return

def determina_data():
    data = datetime.now().date()
    return data.day, data.month, data.year

def salva_registro_investimento(tipo_investimento, valor, tempo, lucro:list, juros):
    if not os.path.isdir('../registros'):
        os.makedirs('../registros')

    with open('../registros/investimento.csv', 'a', newline='') as file:
        writer = csv.writer(file,delimiter=';', lineterminator='\n') 
        data = determina_data()
        writer.writerow([tipo_investimento, valor, data, tempo, lucro, juros])
    
    
    print(f"\n O registro do investimento foi salvo e o lucro do seu investimento em {tipo_investimento} será de R$ {lucro:.2f}")
    mensagem = "Pressione Enter para continuar... \n"
    input(mensagem)
    limpar_tela()

def aplicacao_tesouro_direto(flag_atualiza=None):
    valor = float(input("Informe o valor do investimento: "))
    tempo = int(input("Informe quantos meses deseja investir esse valor: "))
    taxa_juros = 10.06 / 100
    lucro = valor * (1 + taxa_juros)**(tempo/12) - valor
    
    if flag_atualiza.get('atualiza'):
        atualiza_registro_investimento("tesouro direto", valor, tempo, lucro, taxa_juros,flag_atualiza['id'], flag_atualiza['operacao'])
    else:
        salva_registro_investimento("tesouro direto", valor, tempo, lucro, taxa_juros)

def aplicacao_cdb(flag_atualiza=None):
    valor = float(input("Informe o valor do investimento: "))
    tempo = int(input("Informe quantos meses deseja investir esse valor: "))
    taxa_juros = 11.65 / 100
    lucro = valor * (1 + taxa_juros)**(tempo/12) - valor
    
    if flag_atualiza.get('atualiza'):
        atualiza_registro_investimento("cbds", valor, tempo, lucro,taxa_juros,flag_atualiza['id'], flag_atualiza['operacao'])
    else:
        salva_registro_investimento("cbds", valor, tempo, lucro, taxa_juros)

def aplicacao_poupanca(flag_atualiza=None):
    valor = float(input("Informe o valor do investimento: "))
    tempo = int(input("Informe quantos meses deseja investir esse valor: "))
    taxa_juros = 6.17 / 100
    lucro = valor * (1 + taxa_juros)**(tempo/12) - valor
    
    if flag_atualiza.get('atualiza'):
        atualiza_registro_investimento("poupanca", valor, tempo, lucro, taxa_juros,flag_atualiza['id'],flag_atualiza['operacao'])
    else:   
        salva_registro_investimento("poupanca", valor, tempo, lucro, taxa_juros)


def atualiza_registro_investimento(tipo_investimento, valor, tempo, lucro:list, taxa_juros, id, operacao):
    
    data = determina_data()
    registro = [tipo_investimento, valor, data, tempo, lucro,taxa_juros]

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

    with open('../registros/investimento.csv','a') as file:

        escritor = csv.writer(file, delimiter=';', lineterminator='\n')
        escritor.writerow(registro)

    print('Registro atualizado')
    mensagem = "\n Pressione Enter para continuar... \n"
    input(mensagem)
    limpar_tela()