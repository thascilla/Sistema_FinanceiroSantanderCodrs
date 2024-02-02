import csv
from utils import limpar_tela, ler_arquivo
from atualizar_registro import mostrar_opcoes

def deletar_registro():
    """
    """

    flag_mostra_opcao = mostrar_opcoes('DELETAR')

    if flag_mostra_opcao:
        id, operacao = flag_mostra_opcao

        registros_path = {
        '1': '../registros/registros_despesa.csv',
        '2': '../registros/registros_receita.csv',
        '3': '../registros/investimento.csv'}
        
        registros = ler_arquivo(registros_path[operacao])
        
        del registros[id]

        with open(registros_path[operacao],'w') as file:

            escritor = csv.writer(file, delimiter=';', lineterminator='\n')
            escritor.writerows(registros)

        print("\n Registro deletado")
        mensagem = "Pressione Enter para continuar... \n"
        input(mensagem)
        limpar_tela()
        
