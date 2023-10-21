import os
import pandas as pd
import numpy as np
import pickle 

# Objetivo: este programa formata as informações atrociosas que temos em um formato mais palatável...

# Atenção os dados precisam estar no mesmo folder que esse programa, nomeado como 'Data'.
data_folder = 'Data'

# Acho que so funciona em linux esse comando, mas não tem problema, você não deve rodar esse programa em primeiro lugar..
data_files = os.listdir(data_folder)

# Cria um dicionário, então man vão ser varios arrays do numpy com nomes, o nome do arquivo.
data_arrays = {}

def process_file(file_path):
    try:
        # Muda nada aqui não
        df = pd.read_csv(file_path, sep='\t', encoding='latin-1')
        
        df = df.replace(',', '.', regex=True)

        np_array = df.values[1:].astype(float)
        
        # também acho que essa parada so funfa no linux...
        data_arrays[os.path.basename(file_path)] = np_array
        
        print(f"Processed: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Também creio que so funcione no linux assim
for file in data_files:
    file_path = os.path.join(data_folder, file)
    process_file(file_path)

# Salva um arquivo nice, isso funciona tanto em linux quanto em windows
with open('data_files.pkl', 'wb') as f:
    pickle.dump(data_files, f)


with open('data_arrays.pkl', 'wb') as f:
    pickle.dump(data_arrays, f)


# Você pode abrir qualquer array assim:
# data_arrays['Procedimento-1-29-C']

