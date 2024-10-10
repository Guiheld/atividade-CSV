import logging

import numpy
import pandas
from matplotlib import pyplot as plt


def comecar_netflix():
    import main
    arrayNumpyNetflix = main.ler_arquivo_csv(main.NOME_ARQUIVO_CSV_NETFLIX)
    dataFrameNetflix = pandas.DataFrame(arrayNumpyNetflix)

    logging.info("Começando processamento de dados ...")
    primeiros10FilmesNetflix = listar_primeiros_10_filmes(dataFrameNetflix)
    ultimos10FilmesNetflix = listar_ultimos_10_filmes(dataFrameNetflix)
    melhorFilme = melhor_filme(dataFrameNetflix)
    piorFilme = pior_filme(dataFrameNetflix)
    mediaDuracao = media_duracao_geral(dataFrameNetflix)
    filmeMaisLongo = filme_mais_longo(dataFrameNetflix)
    showMaisLongo = show_mais_longo(dataFrameNetflix)
    anoMaisAvaliado = achar_ano_mais_avaliado_filme(dataFrameNetflix)
    quantidade_por_categoria = achar_categorias_filmes_por_certificacao(dataFrameNetflix)

    gerar_graficos(dataFrameNetflix)

def listar_primeiros_10_filmes(dataFrameNetflix):
    try:
        logging.info("Começando processo para listar os primeiros 10 filmes ...")
        primeirosFilmesNetflix = dataFrameNetflix.head(10)
        logging.info("Primeiros 10 filmes listados com sucesso")
        return primeirosFilmesNetflix
    except Exception as e:
        logging.error(e)

def listar_ultimos_10_filmes(dataFrameNetflix):
    try:
        logging.info("Começando processo para listar os ultimos 10 filmes ...")
        ultimosFilmesNetflix = dataFrameNetflix.tail(10)
        logging.info("Ultimos 10 filmes listados com sucesso")
        return ultimosFilmesNetflix
    except Exception as e:
        logging.error(e)

def melhor_filme(dataFrameNetflix):
    try:
        logging.info("Começando processo para buscar o filme melhor avaliado ...")
        melhorFilme = dataFrameNetflix.iloc[dataFrameNetflix.iloc[:, 9].idxmax()]
        logging.info("Filme melhor avaliado encontrado com sucesso")
        return melhorFilme
    except Exception as e:
        logging.error(e)

def pior_filme(dataFrameNetflix):
    try:
        logging.info("Começando processo para buscar o filme pior avaliado ...")
        piorFilme = dataFrameNetflix.iloc[dataFrameNetflix.iloc[:, 9].idxmin()]
        logging.info("Filme pior avaliado encontrado com sucesso")
        return piorFilme
    except Exception as e:
        logging.error(e)

def media_duracao_geral(dataFrameNetflix):
    try:
        logging.info("Começando processo para calculara media de duracao dos titulos ...")
        numpyNetflix = dataFrameNetflix.toNumpy()
        duracao = numpyNetflix[:, 7].astype(float)
        media = numpy.mean(duracao)
        logging.info("Media calculada com sucesso")
        return media
    except Exception as e:
        logging.error(e)

def filme_mais_longo(dataFrameNetflix):
    try:
        logging.info("Começando processo para achar o filme mais longo")
        filmes = dataFrameNetflix[dataFrameNetflix.iloc[:, 3] == 'MOVIE']
        filmeMaisLongo = filmes.loc[filmes.iloc[:, 7].idxmax()]
        logging.info("Filme mais longo encontrado com sucesso")
        return filmeMaisLongo
    except Exception as e:
        logging.error(e)

def show_mais_longo(dataFrameNetflix):
    try:
        logging.info("Começando processo para achar o show mais longo")
        show = dataFrameNetflix[dataFrameNetflix.iloc[:, 3] == 'SHOW']
        showMaisLongo = show.loc[show.iloc[:, 7].idxmax()]
        logging.info("Show mais longo encontrado com sucesso")
        return showMaisLongo
    except Exception as e:
        logging.error(e)

def achar_ano_mais_avaliado_filme(dataFrameNetflix):
    try:
        logging.info("Começando processo para achar o ano com filmes mais avaliados ...")
        logging.info("Puxando todos os filmes ...")
        filmes = dataFrameNetflix[dataFrameNetflix.iloc[:, 3] == 'MOVIE']
        logging.info("Agrupar os filmes pelo ano de lançamento e criar uma lista de filmes avaliados por ano")
        filmesPorAno = filmes.groupby(filmes.iloc[:, 5]).apply(lambda x: list(x.iloc[:, 2])).reset_index()
        logging.info("Achar qual ano tem mais filmes avaliados")
        anoMaisAvaliado = filmesPorAno.idxmax()
        logging.info("Ano com mais filmes avaliados encontrado com sucesso")
        return anoMaisAvaliado
    except Exception as e:
        logging.error(e)

def achar_categorias_filmes_por_certificacao(dataFrameNetflix):
    try:
        logging.info("Começando processo para achar as categorias de certificação e a quantidade de filmes de cada ...")
        logging.info("Puxando todos os filmes ...")
        filmes = dataFrameNetflix[dataFrameNetflix.iloc[:, 3] == 'MOVIE']
        logging.info("Agrupar os filmes pela categoria de age_certification e contar a quantidade de filmes")
        quantidade_por_categoria = filmes.iloc[:, 6].value_counts().reset_index()
        quantidade_por_categoria.columns = ['age_certification', 'count'] # Renomear as colunas para melhor visualização
        logging.info("Categorias de age_certification e suas respectivas contagens encontradas")
        return quantidade_por_categoria
    except Exception as e:
        logging.error(e)

def achar_campos_vazios(dataFrameNetflix):
    try:
        logging.info("Começando processo para achar campos vazios ...")
        campos_vazios = dataFrameNetflix.isna().sum()
        colunas_com_campos_vazios = campos_vazios[campos_vazios > 0]
        logging.info("Colunas com campos vazios e a quantidade de campos vazios em cada coluna encontradas")
        return colunas_com_campos_vazios
    except Exception as e:
        logging.error(e)

def gerar_graficos(dataFrameNetflix):
    logging.info("Começando o processo de gerar um grafico para os dados da Netflix ...")
    try:
        logging.info("Filtrando os dados para Movies e Shows ...")
        filmes = dataFrameNetflix[dataFrameNetflix.iloc[:, 3] == 'MOVIE']
        shows = dataFrameNetflix[dataFrameNetflix.iloc[:, 3] == 'SHOW']

        logging.info("Calculando a média de scores de IMDb ao longo dos anos para filmes ...")
        releaseYearFilme = filmes.iloc[:, 5]
        imdbNotaFilme = filmes.iloc[:, 9]
        filmes_avg_scores = filmes.groupby(releaseYearFilme)[imdbNotaFilme.name].mean().dropna()
        logging.info("Média de scores de IMDb para filmes ao longo dos anos calculada com sucesso")

        logging.info("Calculando a média de scores de IMDb ao longo dos anos para shows ...")
        releaseYearshows = shows.iloc[:, 5]
        imdbNotashows = shows.iloc[:, 9]
        shows_avg_scores = shows.groupby(releaseYearshows)[imdbNotashows.name].mean().dropna()
        logging.info("Média de scores de IMDb para shows ao longo dos anos calculada com sucesso!")

        logging.info("Criando gráfico de média de scores ao longo dos anos para filmes e shows ...")
        plt.figure(figsize=(14, 7))
        plt.subplot(1, 2, 1)
        filmes_avg_scores.plot(kind='line', marker='o', label='Movies', color='blue')
        shows_avg_scores.plot(kind='line', marker='o', label='TV Shows', color='green')
        plt.title('Média de Scores de IMDb ao Longo dos Anos')
        plt.xlabel('Ano de Lançamento')
        plt.ylabel('Média de IMDb Score')
        plt.legend()

        logging.info("Calculando a soma dos votos de IMDb para filmes e shows ...")
        votantes_filmes = filmes.iloc[:, 10].sum()
        votantes_shows = shows.iloc[:, 10].sum()

        logging.info("Criando gráfico da proporção de votantes para filmes e shows ...")
        plt.subplot(1, 2, 2)
        plt.pie([votantes_filmes, votantes_shows], labels=['Movies', 'TV Shows'], autopct='%1.1f%%', startangle=90,
                colors=['blue', 'green'])
        plt.title('Proporção de Votantes por Tipo')
        plt.tight_layout()

        logging.info("Grafico gerado com sucesso!")
        plt.show()
    except Exception as e:
        logging.error(e)