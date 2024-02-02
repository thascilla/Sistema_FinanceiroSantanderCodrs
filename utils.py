import os
import sys
import time
from datetime import datetime
import pyfiglet
import csv

def limpar_tela():
    """
    Limpa a tela do terminal, detectando automaticamente o sistema operacional
    e usando 'cls' no Windows e 'clear' em sistemas Unix/Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def encerrar_programa():
    """Encerra o programa.
    """
    limpar_tela()
    print("Encerrando o programa...")
    time.sleep(2)
    limpar_tela()
    sys.exit()


def tracos():
    """Imprime uma linha decorativa composta por caracteres '=' e '-', delimitando uma área visual. 
    O comprimento total da linha é 90 caracteres.
    """
    print(f'{"="*85} \n'
          f'{"-"*85} \n'
          f'{"="*85} \n')


def tela_inicial():
    """Exibe a tela inicial e obtém a escolha do usuário.
    """
    #limpar_tela()

    # Exibição do título usando pyfiglet
    f = pyfiglet.Figlet(font='big', justify='center')
    print(f.renderText('ADA  ATM'))

    tracos()

    # Exibição das opções
    print("DIGITE UMA DAS OPÇÕES ABAIXO:\n")
    print("[1] CRIAR UM REGISTRO")
    print("[2] LER UM REGISTRO")
    print("[3] ATUALIZAR UM REGISTRO")
    print("[4] DELETAR UM REGISTRO")
    print("[5] INFORMAÇÕES SOBRE SEUS INVESTIMENTOS")
    print("[6] EXPORTAR RELATÓRIO \n")
    print("[7] SAIR")

    while True:

        operacao = input()

        try:
            if operacao.isdigit() and 1 <= int(operacao) <= 7:
                return int(operacao)
            else:
                tentativas += 1

                if tentativas == 3:
                    print("Você atingiu o número máximo de tentativas.")
                    time.sleep(2)
                    encerrar_programa()
                else:
                    print(
                        f"'{operacao}' Não é uma opção válida. Você tem mais {3 - tentativas} {'tentativa' if tentativas == 2 else 'tentativas'}.")
                    time.sleep(2)
                    limpar_tela()
                    tela_inicial()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")


def limpar_tela():
    """
    Limpa a tela do terminal, detectando automaticamente o sistema operacional
    e usando 'cls' no Windows e 'clear' em sistemas Unix/Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def determina_data():
    """
    Obtem a data de realização do registro
    retornando um tupla no formato (dia, mes, ano) 
    """

    data = datetime.now().date()
    return data.day, data.month, data.year


def valida_digito(mensagem: str, mensagem_erro: str):
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


def valida_data(tempo):
    """ """

    intervalo_valido = {'dia': (0, 32), 'mes': (
        0, 13), 'ano': (2021, datetime.now().year + 1)}

    while True:
        try:
            data = int(
                input(f"Informe o {tempo} do registro que deseja: "))
        except ValueError:
            print("Valor invalido")
            continue
        else:
            if intervalo_valido[tempo][0] < data and data < intervalo_valido[tempo][1]:
                return data
            else:
                print("Data invalida.")

def ler_arquivo(path: str) -> list:
    """Função que recebe o caminho do arquivo csv com os registros salvos 
    e retorna uma lista com os registros salvos caso tal csv exista, 
    caso contrario retorna None"""

    if os.path.exists(path):
            with open(path, 'r', newline='') as file:
                registros = list(csv.reader(file, delimiter=';', lineterminator='\n'))
            return registros
    else:
        return None
