# import pandas as pd



# df = pd.read_csv('data.csv')


# media_geral = df['DOR'].mean()

# valor_individuo_lista = []
# for valor_individuo in df['DOR']:
#     valor_individuo_lista.append(valor_individuo- media_geral)
    
# #soma de dos quadrados
# soma_quadrados_total = 0
# for i in valor_individuo_lista:
#     soma_quadrados_total += i**2

# medias_grupos = df.groupby('GRUPO')['DOR'].mean()
# medias_cont = df.groupby('GRUPO')

# contagem_por_grupo = df.groupby('GRUPO').size()

# soma_quadrados_erro = 0
# for i in range(len(df)):
#     soma_quadrados_erro += (df['DOR'][i] - medias_grupos[df['GRUPO'][i]])**2


# print(f"soma_quadrados_total = {soma_quadrados_total}")
# print(f"soma_quadrados_erro = {soma_quadrados_erro}")

# soma_quadrados_entre_grupos = 0
# #soma de quadrados do grupo
# for i in medias_grupos:
#     soma_quadrados_entre_grupos += (i - media_geral)**2

# soma_quadrados_entre_grupos = 4 * soma_quadrados_entre_grupos

# print(f"soma_quadrados_entre_grupos = {soma_quadrados_entre_grupos}")
# # soma_quadrados_do_grupo = 4 * ()

# grau_libredade_total = len(df) - 1
# print(f"grau_libredade_total = {grau_libredade_total}")
# variancia_total_da_amostra = round(soma_quadrados_total/grau_libredade_total,2)
# print(f"variancia_total_da_amostra = {variancia_total_da_amostra}")

# grau_liberdade_dos_grupos = len(medias_grupos) - 1
# print(f"grau_liberdade_dos_grupos = {grau_liberdade_dos_grupos}")


# grau_libredade_erro = round(len(df) - len(medias_grupos),2)
# print(f"grau_libredade_erro = {grau_libredade_erro}")

# media_quadratica_grupos = round(soma_quadrados_entre_grupos/grau_liberdade_dos_grupos,2)
# print(f"media_quadrados_entre_grupos = {media_quadratica_grupos}")


# media_quadratica_erro = round(soma_quadrados_erro/grau_libredade_erro,2)
# print(f"media_quadrados_erro = {media_quadratica_erro}")

# # media_quadrados_erro = 
# F = round(media_quadratica_grupos/media_quadratica_erro, 2)
# print(f"F = {F}")
#media_ponderada = 0

# contagem_Asp = contagem_por_grupo['Asp']
# contagem_Tyl = contagem_por_grupo['Tyl']
# contagem_Plac = contagem_por_grupo['Plac']
# media_ponderada = (contagem_Asp*(medias_grupos['Asp'] - media_geral)**2 + contagem_Tyl*(medias_grupos['Tyl'] - media_geral)**2 + contagem_Plac*(medias_grupos['Plac'] - media_geral)**2)/(contagem_Asp + contagem_Tyl + contagem_Plac)
# print(f"media_ponderada = {media_ponderada}")
# def ponderada():
#     pass
