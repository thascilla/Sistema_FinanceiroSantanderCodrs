import csv
import datetime
import re

REGISTROS_DESPESA_PATH = '../registros/registros_despesa.csv'
REGISTROS_RECEITA_PATH = '../registros/registros_receita.csv'
REGISTROS_INVESTIMENTO_PATH = '../registros/investimento.csv'
RELATORIO_EXPORTADO_PATH = '../registros/relatorio_exportado.csv'

def ler_arquivo_csv(caminho):
    try:
        with open(caminho, 'r', newline='') as arquivo:
            leitor_csv = list(csv.reader(arquivo, delimiter=';'))
            return leitor_csv
    except FileNotFoundError:
        print(f"Arquivo {caminho} não encontrado.")
        return []

def extrair_data(registro):
    string_data = registro[2]
    lista_data = re.findall(r'\d+', string_data)
    if len(lista_data) >= 3:
        return datetime.date(int(lista_data[2]), int(lista_data[1]), int(lista_data[0]))
    return None

def tracos():
    print('-' * 50)

def exporta_relatorio():
    registros_despesa = ler_arquivo_csv(REGISTROS_DESPESA_PATH)
    registros_receita = ler_arquivo_csv(REGISTROS_RECEITA_PATH)
    registros_investimento = ler_arquivo_csv(REGISTROS_INVESTIMENTO_PATH)

    registros_despesa = [registro for registro in registros_despesa if extrair_data(registro) is not None]
    registros_receita = [registro for registro in registros_receita if extrair_data(registro) is not None]
    registros_investimento = [registro for registro in registros_investimento if extrair_data(registro) is not None]

    registros_despesa = sorted(registros_despesa, key=lambda reg: extrair_data(reg))
    registros_receita = sorted(registros_receita, key=lambda reg: extrair_data(reg))
    registros_investimento = sorted(registros_investimento, key=lambda reg: extrair_data(reg))

    print("Despesas:")
    soma_despesas = 0
    for registro in registros_despesa:
        tipo, valor, data = registro[0], float(registro[1]), registro[2]
        print(f"Tipo: {tipo}, Valor: {valor}, Data: {data}")
        tracos()
        soma_despesas += valor

    print(f"Soma total de despesas: {soma_despesas:.2f}")
    tracos()

    print("Receitas:")
    soma_receitas = 0
    for registro in registros_receita:
        tipo, valor, data = registro[0], float(registro[1]), registro[2]

        print(f"Tipo: {tipo}, Valor: {valor}, Data: {data}")
        tracos()
        soma_receitas += valor

    print(f"Soma total de receitas: {soma_receitas:.2f}")
    tracos()

    print("Investimentos:")
    soma_tesouro_direto = 0
    soma_poupanca = 0
    soma_cdb = 0

    for registro in registros_investimento:
        tipo, valor, data, _, _, _ = registro
        print(f"Tipo: {tipo}, Valor: {valor}, Data: {data}")
        tracos()

    tracos()

    with open(RELATORIO_EXPORTADO_PATH, 'w', newline='') as relatorio:
        escritor_csv = csv.writer(relatorio, delimiter=',')
        escritor_csv.writerow(['Tipo', 'Valor', 'Data'])
        escritor_csv.writerows(registros_despesa + registros_receita + registros_investimento)

    print(f"Relatório exportado para {RELATORIO_EXPORTADO_PATH} com sucesso!")