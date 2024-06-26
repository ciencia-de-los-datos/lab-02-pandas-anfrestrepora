"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")



def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """

    # Cargar el archivo TSV en un DataFrame
    df = pd.read_csv('tbl0.tsv', sep='\t')
    # Obtener la cantidad de filas en el DataFrame
    cantidad_filas = len(df)

    return cantidad_filas


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    df = pd.read_csv('tbl0.tsv', sep='\t')

    # Obtener la cantidad de columnas en el DataFrame
    num_columnas = df.shape[1]

    return num_columnas


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """

    df = pd.read_csv('tbl0.tsv', sep='\t')
    # Contar la cantidad de registros por cada letra en la columna _c1
    conteo_por_letra = df['_c1'].value_counts()
    conteo_por_letra_sorted = conteo_por_letra.sort_index()
    print(type(conteo_por_letra_sorted))
    return conteo_por_letra_sorted


def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    df = pd.read_csv('tbl0.tsv', sep='\t')

    # Calcular el promedio de _c2 por cada letra de _c1
    promedio_por_letra = df.groupby('_c1')['_c2'].mean()

    return promedio_por_letra


def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """

    df = pd.read_csv('tbl0.tsv', sep='\t')

    # Calcular el valor máximo de _c2 por cada letra de _c1
    maximo_por_letra = df.groupby('_c1')['_c2'].max()


    return maximo_por_letra


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    df = pd.read_csv('tbl1.tsv', sep='\t')

    # Obtener los valores únicos de la columna _c4, convertidos a mayúsculas y ordenados ascendentemente
    valores_unicos_mayusculas = df['_c4'].str.upper().unique()
    valores_unicos_mayusculas_ordenados = sorted(valores_unicos_mayusculas)


    return valores_unicos_mayusculas_ordenados


def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    df = pd.read_csv('tbl0.tsv', sep='\t')

    # Calcular la suma de _c2 por cada letra de _c1
    suma_por_letra = df.groupby('_c1')['_c2'].sum()


    return suma_por_letra


def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    df = pd.read_csv('tbl0.tsv', sep='\t')

    # Agregar una nueva columna llamada 'suma' con la suma de _c0 y _c2
    df['suma'] = df['_c0'] + df['_c2']


    return df


def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    df = pd.read_csv('tbl0.tsv', sep='\t')
    df['year'] = df['_c3'].str[:4]

    return df


def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c2
      _c1
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    
    """

    df = pd.read_csv('tbl0.tsv', sep='\t')
    
    df_sorted = df.sort_values(by=['_c1', '_c2'], ascending=[True, True])

# Agrupar los valores de la columna _c2 por los valores únicos de la columna _c1
    grouped = df_sorted.groupby('_c1')['_c2'].apply(lambda x: ':'.join(map(str, x))).reset_index()
    grouped.set_index('_c1', inplace=True)




    return grouped



def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    df = pd.read_csv('tbl1.tsv', sep='\t')
  
    df_sorted = df.sort_values(by=['_c0', '_c4'], ascending=[True, True])

    # Agrupar los valores de la columna _c4 por los valores únicos de la columna _c0
    grouped = df_sorted.groupby('_c0')['_c4'].apply(lambda x: ','.join(map(str, x))).reset_index()



    return grouped


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    df = pd.read_csv('tbl2.tsv', sep='\t')
    df_sorted = df.sort_values(by=[ '_c0','_c5a'], ascending=[True,True])
    
    # Convertir las columnas _c5a y _c5b a cadenas
    df_sorted['_c5a'] = df_sorted['_c5a'].astype(str)
    df_sorted['_c5b'] = df_sorted['_c5b'].astype(str)

    # Ordenar alfabéticamente los valores de la columna _c5a y _c5b
    df_sorted['_c5'] = df_sorted.apply(lambda row: ':'.join([row['_c5a'], row['_c5b']]), axis=1)

    # Agrupar los valores de la columna _c5 por los valores únicos de la columna _c0
    grouped = df_sorted.groupby('_c0')['_c5'].apply(lambda x: ','.join(map(str, x))).reset_index()



    return grouped


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """

    tbl0 = pd.read_csv('tbl0.tsv', sep='\t')
    tbl2 = pd.read_csv('tbl2.tsv', sep='\t')

    # Fusionar las tablas en función de la columna _c0
    merged = pd.merge(tbl0, tbl2, on='_c0')

    # Calcular la suma de tbl2._c5b por cada valor en tbl0._c1
    suma_por_c1 = merged.groupby('_c1')['_c5b'].sum()


    return suma_por_c1

def ejemplo():
    a=pd.DataFrame(
            {
                "_c2": [
                    "1:1:2:3:6:7:8:9",
                    "1:3:4:5:6:8:9",
                    "0:5:6:7:9",
                    "1:2:3:5:5:7",
                    "1:1:2:3:3:4:5:5:5:6:7:8:8:9",
                ]
            },
            index=pd.Series(["A", "B", "C", "D", "E"], name="_c1"),
        )

    return a

# print(pregunta_01())
# print(pregunta_02())
# print(pregunta_03())
# print(pregunta_04())
# print(pregunta_05())
# print(pregunta_06())
# print(pregunta_07())
# print(pregunta_08())
# print(pregunta_09())
#print(pregunta_10())
#print(ejemplo())
# print(pregunta_11())
#print(pregunta_12())
#print(pregunta_13())

