import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
from scipy.optimize import curve_fit

# Esse arquivo está para te ajudar a usar os dados


# Não mexe
with open('data_files.pkl', 'rb') as f:
    data_files = pickle.load(f)

# Não mexe
with open('data_arrays.pkl', 'rb') as f:
    data_arrays = pickle.load(f)

# Para ter acesso aos arrays basta acessar o dicionario 'data_arrays'
# Bem para isso voce precisa escrever o nome dos arquivos, se quiser ver o nome dos arquivos
# Vai na pasta Data ou roda 
#for file in data_files:
#   print(file)
# Ou cheque no final do arquivo
# Vamos supor que você quer acessar um array, 
# Primeiro acha o nome do arquivo que quer, exemplo : Procedimento-2-181C-10nA
# Para acessar basta escrever :P2 = data_arrays['Procedimento-2-181C-10nA'] 
# P2 sera dividido em dois arrays P2[:, 0] e P2[:, 1]. igual nos arquivos


# Funções
# Essa função aqui é para achar os pontos de pico, 'dh' é a diferença de altura que daremos para aceitar um pico, assim:
# se a diferença de dois pontos for maior que 'dh' é pico
def find_peaks(data, dh):
    return np.where(np.diff(data)>= dh)[0]+1

# Essa função tem proposito de checar como é o arquivo original e se estamos pegando os picos corretos.
# e quais partes dessa função desejamos cortar... 
# dh tem o mesmo proposito que antes,
# data_array é nosso dicionário,
# name_data é o nome da data, lembre de colocar entre parenteses ''
# Title é auto explicativo
def graph_of_w_peaks(data_array, name_data, title, dh):
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel('Tensão de aceleração /2')
    ax.set_ylabel('Tensão de desaceleração')

    x = data_array[name_data][:, 0]
    y = data_array[name_data][:, 1]

    peaks = find_peaks(y, dh)

    px = data_array[name_data][peaks, 0]
    py = data_array[name_data][peaks, 1]

    ax.plot(x, y)

    ax.scatter(px, py)
    
    plt.show()


# Esta pega o grafico, porem sem os picos que é o que queremos, contudo, as vezes apenas eliminar os 
# picos não basta, alguns graficos tiveram avalanches e para cortar elas do grafico usamos a e b
# a é o limite de baixo e b o limite de cima, então o grafico agora vai de 'a' a 'b'.
def graph_of_wn_peaks(data_array, name_data, title, dh, a, b):
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel('Tensão de aceleração /2')
    ax.set_ylabel('Tensão de desacerelação')

    peaks = find_peaks(data_array[name_data][:, 1], dh)
    
    x = np.delete(data_array[name_data][:, 0], peaks)
    y = np.delete(data_array[name_data][:, 1], peaks)
    d = np.where((x<=a)|(x>=b))
    x = np.delete(x, d)
    y = np.delete(y, d)

    ax.plot(x, y)
    
    plt.show()




# Exemplo... Lembre de fechar o grafico para ver o proximo

dh = 0.1
titulo = 'Procedimento-2-159C-10nA'
procedimento = 'Procedimento-2-159C-10nA'
a = 0
b = 10.7

#graph_of_w_peaks(data_arrays , procedimento, titulo, dh)
#graph_of_wn_peaks(data_arrays, procedimento, titulo, dh, a, b)




# Nome dos arquivos para você copiar e colar



# 1: Procedimento-2-181C-10nA 
# 
# 2: Procedimento-3.3-175,5C-10nA-1.5V 
# 
# 3: Procedimento-2-205C-1nA 
# 
# 4: Procedimento-2-194C-1nA 
# 
# 5: Procedimento-3.3-175,5C-10nA-0V 
# 
# 6: Procedimento-3.3-175,0C-10nA-0;1V 
# 
# 7: Procedimento-2-171C-10nA 
# 
# 8: Procedimento-3.3-175,5C-10nA-1V 
# 
# 9: Procedimento-3.3-175,5C-10nA-2.5V 
# 
# 10: Procedimento-3.3-175,5C-10nA-0.5V 
# 
# 11: Procedimento-2-205C-1nA-2 
# 
# 12: Procedimento-3.3-175,5C-10nA-3V 
# 
# 13: Procedimento-2-184C-1nA 
# 
# 14: Procedimento-1-29-C 
# 
# 15: Procedimento-3.3-175,5C-10nA-2V 
# 
# 16: Procedimento-2-159C-10nA 

























