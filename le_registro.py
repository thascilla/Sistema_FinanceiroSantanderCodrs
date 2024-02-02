from atualizar_registro import mostrar_opcoes
from utils import ler_arquivo
import re
from utils import limpar_tela

def le_registro():
  
    flag_mostra_opcao = mostrar_opcoes('LER')

    if flag_mostra_opcao:
        id, operacao = flag_mostra_opcao

        registros_path = {
        '1': '../registros/registros_despesa.csv',
        '2': '../registros/registros_receita.csv',
        '3': '../registros/investimento.csv'}
    
        registros = ler_arquivo(registros_path[operacao])
        
        valor = registros[id][1]
        data_str = registros[id][2]
        
        def s(data): return re.findall(r'\d+', data)
        data = s(data_str)
        
        if operacao == '1':
        
            print(f"\n O registro escolhido é uma despesa no valor de {-float(valor)} reais na data:{data[0]}/{data[1]}/{data[2]} \n")

            mensagem = "Pressione Enter para continuar..."
            input(mensagem)
            limpar_tela
        
        elif operacao == '2':

            print(f"\n O registro escolhido é uma receita no valor de {valor} reais na data:{data[0]}/{data[1]}/{data[2]} \n")

            mensagem = "Pressione Enter para continuar..."
            input(mensagem)
            limpar_tela

        elif operacao == '3':

            print(f"\n O registro escolhido é um investimento no valor de {valor} reais na data:{data[0]}/{data[1]}/{data[2]},"
                f"do tipo {registros[id][0].capitalize()}, com juros anual de {registros[id][5]} e lucro de {registros[id][5]} reais \n")
            
            mensagem = "Pressione Enter para continuar..."
            input(mensagem)
            limpar_tela
