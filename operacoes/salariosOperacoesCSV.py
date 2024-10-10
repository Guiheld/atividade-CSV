import csv
import logging
import os.path
from array import array

import pandas as pd
import matplotlib.pyplot as plt
import numpy as numpy

def comecar_salarios():
    import main
    logging.info("Começando o processo de leitura do arquivo " + main.NOME_ARQUIVO_CSV_SALARIOS)
    arrayNumpySalarios = main.ler_arquivo_csv(main.NOME_ARQUIVO_CSV_SALARIOS)
    logging.info("Fim do processo de leitura do arquivo " + main.NOME_ARQUIVO_CSV_SALARIOS)

    mediaSalarios = calcular_media_salarios(arrayNumpySalarios)
    mediaExperiencia = calcular_media_experiencia(arrayNumpySalarios)
    mediaSalarioCincoAnos = calcularMediaSalarialCincoAnos(arrayNumpySalarios)
    aumento = aumento_decimo(arrayNumpySalarios)

    logging.info("Gerando grafico para os salarios em relacao ao tempo de experiencia")
    grafico_barra(arrayNumpySalarios)
    print("============================== Dados gerados =============================")
    print("Media salarios: " + str(mediaSalarios))
    print("Media experiencia: " + str(mediaExperiencia))
    print("Media salario dos funcionarios com mais de 5 anos de experiencia: " + str(mediaSalarioCincoAnos))
    print("Salarios caso um aumento de 10% ocorra:")
    print(aumento)
    print("==========================================================================")

def calcular_media_salarios(arrayNumpy):
    logging.info("Calculando a media de salarios ...")
    try:
        logging.info("Puxando a segunda coluna dos salarios para calcular media de salarios")
        salarios = arrayNumpy[:, 1].astype(float)
        logging.info("Calculando a media dos salarios ...")
        media = numpy.mean(salarios)
        return media
    except Exception as e:
        logging.error(e)

def calcular_media_experiencia(arrayNumpy):
    logging.info("Calculando a media de experiencia dos funcionarios ... ")
    try:
        logging.info("Puxando a primeira coluna dos salarios para calcular media de experiencia")
        experiencia = arrayNumpy[:, 0].astype(float)
        logging.info("Calculando a media de experiencia dos empregados...")
        media = numpy.mean(experiencia)
        return media
    except Exception as e:
        logging.error(e)

def calcularMediaSalarialCincoAnos(arrayNumpy):
    logging.info("Calculando a media de salario dos funcionarios com mais de cinco anos de experiencia ...")
    try:
        logging.info("Puxando a primeira coluna dos salarios para calcular media de salario dos funcionarios com mais de cinco anos de experiencia")
        experiencia = arrayNumpy[:, 0].astype(float)
        logging.info("Puxando a segunda coluna dos salarios para calcular media de salario dos funcionarios com mais de cinco anos de experiencia")
        salarios = arrayNumpy[:, 1].astype(float)
        logging.info("Filtrando salarios com mais de 5 anos de experiencia")
        salariosCincoAnos = salarios[experiencia > 5]
        logging.info("Calculando a media dos salarios dos funcionarios com mais de 5 anos de experiencia")
        media = numpy.mean(salariosCincoAnos)
        return media
    except Exception as e:
        logging.error(e)

def aumento_decimo(arrayNumpy):
    logging.info("Calculando salarios caso um aumento de 10% ocorra")
    try:
        logging.info("Puxando a primeira coluna dos salarios para calcular salarios com aumento de 10%")
        salarios = arrayNumpy[:, 1].astype(float)
        logging.info("Calculando salarios com aumento de 10%")
        salariosNovoAumento = salarios * 1.1
        return salariosNovoAumento
    except Exception as e:
        logging.error(e)

def grafico_barra(arrayNumpy):
    logging.getLogger('matplotlib').setLevel(logging.INFO)  # tirar um pouco de log desnecessario
    colunas = ['experiencia', 'salario']
    # Converter o array NumPy para DataFrame do pandas
    df = pd.DataFrame(data=arrayNumpy, columns=colunas)
    plt.figure(figsize=(10, 6))
    plt.bar(df['experiencia'], df['salario'], color='blue')

    plt.title('Salários em relação ao tempo de serviço')
    plt.xlabel('Tempo de Serviço (anos)')
    plt.ylabel('Salário')

    # Exiba o gráfico
    plt.show()


