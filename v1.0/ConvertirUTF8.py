""""
Created on 09-01-2019

@author: Aitor Diaz Medina

"""

import io
import sys
import os


def convertir_utf8(path):
    ruta2 = os.path.splitext(path)[0] + 'utf8.txt'
    with io.open(path, 'r', encoding='iso-8859-1') as f:
        text = f.read()
    # process iso-8859-1 text
    with io.open(ruta2, 'w', encoding='utf8') as f:
        f.write(text)
    print(ruta2)
    return ruta2


if __name__ == '__main__':
    convertir_utf8(sys.argv[1])


# convertir_utf8(ruta_fichero_plano)


