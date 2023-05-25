import glob
import csv
import os.path

pasta_true = 'fake'
lista_arquivos = glob.glob(pasta_true + '/*')
total_true = len(lista_arquivos)



for item in range(3602):
    caminho = 'fake/'+str(range)+'.txt'

    if not os.path.exists(caminho):
        continue
    with open(caminho, 'r', encoding='utf-8') as file:
        conteudo = file.read()

    # Remover as quebras de linha do conteúdo
    conteudo_sem_quebras = conteudo.replace('\n', '')
    file.close()
    # Salvar o conteúdo modificado em um novo arquivo ou sobrescrever o arquivo original
    with open(caminho, 'w', encoding='utf-8') as file:
        file.write(conteudo_sem_quebras)
    file.close()
# import pandas as pd
#
# caminho_arquivo = 'true/1.txt'
#
# dataframe = pd.read_csv(caminho_arquivo, header=None)
#
# #print(dataframe)
# primeira_linha= dataframe.iloc[0]
# print(primeira_linha)
# import glob
# import csv
# import os.path
#
# pasta_true = 'true'
# lista_arquivos = glob.glob(pasta_true + '/*')
#
# total_true = len(lista_arquivos)

#print(total_true )
#
# dados = [
#     ['Nome', 'Idade', 'Cidade'],
#     ['João', 25, 'São Paulo'],
#     ['Maria', 30, 'Rio de Janeiro'],
#     ['Carlos', 35, 'Curitiba']
# ]
#
# caminho_csv = 'dataset/arquivo.csv'
#
# if not os.path.exists(caminho_csv):
#     os.makedirs(os.path.dirname(caminho_csv), exist_ok=True)
#
# with open(caminho_csv,"w", newline='') as arquivo_csv:
#     writer = csv.writer(arquivo_csv, delimiter=',')
#
#     for linha in dados:
#         writer.writerow(linha)
#
# arquivo_csv.close()
# print("arquivo CSV criado com sucesso.")

# import pandas as pd
#
# # Caminhos dos arquivos TXT
# caminho_arquivo1 = 'true/1.txt'
# caminho_arquivo2 = 'true/2.txt'
# caminho_arquivo3 = 'true/3.txt'
#
# # Ler os arquivos TXT e criar DataFrames
# df1 = pd.read_csv(caminho_arquivo1, delimiter='\t')  # Use delimiter='\t' se o arquivo estiver separado por tabulação
# df2 = pd.read_csv(caminho_arquivo2, delimiter=',')   # Use delimiter=',' se o arquivo estiver separado por vírgula
# df3 = pd.read_csv(caminho_arquivo3, delimiter=';')   # Use delimiter=';' se o arquivo estiver separado por ponto e vírgula
#
# # Concatenar os DataFrames em uma única tabela
# tabela = pd.concat([df1, df2, df3])
#
# # Exibir a tabela
# print(tabela)