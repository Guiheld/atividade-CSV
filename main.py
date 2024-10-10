import logging
import os

import pandas

from operacoes.NetflixOperacoesCSV import comecar_netflix
from operacoes.salariosOperacoesCSV import calcular_media_salarios, calcular_media_experiencia, \
    calcularMediaSalarialCincoAnos, grafico_barra, aumento_decimo, comecar_salarios

# Configure the logging
logging.basicConfig(
    level=logging.DEBUG,  # Nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato das mensagens de log
    datefmt='%Y-%m-%d %H:%M:%S'  # Formato da data e hora
)

NOME_ARQUIVO_CSV_SALARIOS = "Salary_Data.csv"
NOME_ARQUIVO_CSV_NETFLIX = "Netflix TV Shows and Movies.csv"
DIRETORIO_CSV = "ArquivosCSV"

def main():
    if verificar_integridade_arquivos == False:
        logging.critical("Erro ao verificar integridade")
        return 1
    comecar_salarios()
    print("CLIQUE ENTER PARA CARREGAR PROXIMO ARQUIVO")
    input()
    comecar_netflix()

def verificar_integridade_arquivos():
    logging.info("Verificando existencia dos arquivos...")
    try:
        directory = os.path.exists(DIRETORIO_CSV)
        if directory:
            logging.info("Diretorio encontrado")
        else:
            logging.error("Diretorio nao encontrado")
            return False
        arquivoSalarios = os.path.join(DIRETORIO_CSV, NOME_ARQUIVO_CSV_SALARIOS)
        if os.path.exists(arquivoSalarios):
            logging.info("Arquivo Salarios encontrado")
        else:
            logging.error("Arquivo Salarios nao encontrado")
            return False
        arquivoNetflix = os.path.join(DIRETORIO_CSV, NOME_ARQUIVO_CSV_NETFLIX)
        if os.path.exists(arquivoNetflix):
            logging.info("Arquivo Netflix encontrado")
        else:
            logging.error("Arquivo Netflix nao encontrado")
            return False
    except Exception as e:
        logging.critical(e)

def ler_arquivo_csv(arquivoNome):
    try:
        path = os.path.join(DIRETORIO_CSV, arquivoNome)
        logging.info("Convertendo dados em CSV para um DataFrame pandas ...")
        dataFrame = pandas.read_csv(path, header=None, skiprows=1)
        logging.info("Convertendo para numpy ...")
        arrayNumpy = dataFrame.to_numpy()
        if arrayNumpy.size == 0:
            logging.error("Array NumPy vazio ")
        else:
            logging.info("Arquivo " + arquivoNome + " lido com sucesso")
            return arrayNumpy
    except Exception as e:
        logging.critical(e)

if __name__ == "__main__":
    main()
