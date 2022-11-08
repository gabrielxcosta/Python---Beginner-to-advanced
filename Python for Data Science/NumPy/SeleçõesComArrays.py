import numpy as np
import pandas as pd

dados = np.array(
    [
        ['Roberto', 'casado', 'masculino'],
        ['Sheila', 'solteira', 'feminino'],
        ['Bruno', 'solteiro', 'masculino'],
        ['Rita', 'casada', 'feminino']
    ]
)

dic_dados = {
    'nomes': dados[:, 0],
    'estado civil' : dados[:, 1],
    'sexo' : dados[:, 2]
    }

print(34 * '-')
print('\t       DATASET:')
print(34 * '-')
df = pd.DataFrame(dic_dados, index=None)
df.index += 1
print(df.head())

print()
print(dados[0::2, :2])