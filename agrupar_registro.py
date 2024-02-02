from functools import reduce
import os
import csv
import datetime
import time
import re
from cria_registro import cria_registro
from utils import encerrar_programa
from utils import valida_data
from utils import ler_arquivo
from utils import limpar_tela

# Função de agrupamento usando reduce
def agrupar_registro_por_tipo(registro_lista):
    # Obtém todos os registros da lista
    registro = registro_lista.get_registro()

    # Agrupa os registros por tipo e calcula o total de valores para cada tipo
    agrupamento = reduce(lambda acc, reg: {**acc, reg.tipo: acc.get(reg.tipo, 0) + reg.valor}, registro, {})
    
    return agrupamento

   