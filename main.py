from utils import limpar_tela, tracos, tela_inicial
from cria_registro import cria_registro
from le_registro import le_registro
from deletar_registro import deletar_registro
from atualizar_registro import atualizar_registro
from mostra_features import mostra_features
from exporta_relatorio import exporta_relatorio
from encerrar_programa import encerrar_programa
import time


def main():
    tentativas = 0
    max_tentativas = 3

    operacoes = {
        1: cria_registro,
        2: le_registro,
        3: atualizar_registro,
        4: deletar_registro,
        5: mostra_features,
        6: exporta_relatorio,
        7: encerrar_programa
    }

    while tentativas < max_tentativas:
        try:
            limpar_tela()
            tracos()
            operacao = tela_inicial()

            if operacao in operacoes:
                operacoes[operacao]()
            else:
                tentativas += 1
                print(f"{operacao} não é uma opção válida. "
                      f"Você tem mais {max_tentativas - tentativas} tentativa{'s' if tentativas != max_tentativas - 1 else ''}.")
                time.sleep(10)
 
        except KeyboardInterrupt:
            print("\nOperação interrompida pelo usuário.")
            encerrar_programa()

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            time.sleep(2)

    print("Você atingiu o número máximo de tentativas. Encerrando o programa.")
    time.sleep(2)
    encerrar_programa()



if __name__ == "__main__":
    main()
