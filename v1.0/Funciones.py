""""
Created on 09-01-2019

@author: Aitor Diaz Medina

Generación de vistas temporales del csv importado
"""


import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np
import os

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option("display.max_columns", 10)


def leer_archivo(input_file):
    df = pd.read_csv(input_file)
    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')
    df['Hora'] = pd.to_datetime(df['Hora'], format='%H:%M:%S')
    return df


def escribir_csv(df, nombre_archivo):
    df.to_csv(nombre_archivo, encoding='utf-8')
    print('Fichero CSV creado: ' + nombre_archivo)


def escribir_excel(df, nombre_archivo, nombre_hoja):
    print(nombre_archivo, nombre_hoja)
    excel = nombre_archivo + ".xlsx"
    if not os.path.isfile(excel):
        with pd.ExcelWriter(excel, date_format='dd mmm yyyy', datetime_format='dd mmm yyyy hh:mm:ss') as writer:
            df.to_excel(writer, sheet_name=nombre_hoja)
    else:
        with pd.ExcelWriter(excel, date_format='DD-MM-YYYY', datetime_format='DD-MM-YYYY HH:MM:SS', mode='a') as writer:
            df.to_excel(writer, sheet_name=nombre_hoja)
    print('Fichero Excel creado: ', excel)


def distribucion_dias_semana(input_file, export_file):
    df = leer_archivo(input_file)
    # ordenar dataframe
    sorted_df = df.sort_values(by='Fecha').set_index("Mensaje", drop=False)
    sorted_df['Día'] = pd.Categorical(sorted_df['Día'],
                                      ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
    # agrupar por día
    df_dias = sorted_df.groupby('Día')
    df_def = df_dias.size().reset_index(name='Total')
    # print(df_def)

    # Gráfico
    # plt.figure()
    # print(df_def.plot(kind='bar', rot=45, fontsize=10))
    # plt.show(block=True)

    # Generar csv
    # df_def.to_csv('export/dias_semana.csv', index=False)
    escribir_excel(df_def, export_file, 'Temporal días')
    return df_def


def distribucion_fechas(input_file, export_file):
    df = leer_archivo(input_file)

    sorted_df = df.sort_values(by='Fecha')
    df_fechas = sorted_df.set_index(["Fecha", "Mensaje"]).count(level="Fecha")

    index = pd.date_range(sorted_df['Fecha'].min(), sorted_df['Fecha'].max(), freq='D')
    # reindex the DataFrame
    df_reindexed = df_fechas.reindex(index)
    df_def = df_reindexed.loc[:, 'Foro']
    df_def2 = df_def.to_frame()
    # cambiar nombre de la columna del dataframe
    df_def2.columns = ['Total']
    # cambiar NaN por 0 y pasar a tipo integer
    df_def2 = df_def2.fillna(0)
    df_def2['Total'] = df_def2['Total'].astype(np.int64)
    # poner la fecha de indice del dataframe
    df_def2.index.names = ['Fecha']
    # print(df_def2)

    # Gráfico
    # plt.figure()
    # print(df_def2.plot(kind='bar', fontsize=4))
    # plt.show(block=True)

    # Generar el csv
    # escribir_csv(df_def2, 'export/fechas.csv')
    escribir_excel(df_def2, export_file, 'Temporal fechas')
    return df_def2


def distribucion_rango_horas(input_file, export_file):
    df = leer_archivo(input_file)
    # sorted_df = df.sort_values(by='Fecha')
    # index = pd.date_range(sorted_df['Fecha'].min(), sorted_df['Fecha'].max(), freq='D')

    df_rango_horas = df.groupby([df.Fecha, df.Día, pd.Grouper(key='Hora', freq='4H')]).size()

    # df_reindexed = df_rango_horas.reindex(index)
    # print(df_reindexed)

    df_rango_horas_def = df_rango_horas.unstack()
    df_rango_horas_def.columns = ['de 0:00 a 4:00', 'de 4:00 a 8:00', 'de 8:00 a 12:00', 'de 12:00 a 16:00', 'de 16:00 a 20:00', 'de 20:00 a 24:00']
    df_rango_horas_def = df_rango_horas_def.fillna(0)
    df_rango_horas_def = df_rango_horas_def.astype(np.int64)

    # print(df_rango_horas_def)

    # escribir_csv(df_rango_horas_def, 'export/rango_horas.csv')
    escribir_excel(df_rango_horas_def, export_file, 'Rango horas')
    return df_rango_horas_def


def distribucion_personas_dias(input_file, export_file):
    df = leer_archivo(input_file)
    # ordenar por fecha y los dias de la semana
    sorted_df = df.sort_values(by='Fecha').set_index("Mensaje", drop=False)
    sorted_df['Día'] = pd.Categorical(sorted_df['Día'],
                                      ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
    # agrupar por remitente y dia de la semana
    df_rango_semanas = sorted_df.groupby([sorted_df.Autor, sorted_df.Remitente, sorted_df.Día]).size()  # .reset_index(name='count')
    df_rango_semanas_def = df_rango_semanas.unstack()

    # cambiar a integer y NaN por 0s
    df_rango_semanas_def = df_rango_semanas_def.fillna(0)
    df_rango_semanas_def = df_rango_semanas_def.astype(np.int64)


    # print(df_rango_semanas_def)
    # escribir_csv(df_rango_semanas_def, 'export/personas_dias_semana.csv')
    # escribir_excel(df_rango_semanas_def, export_file, 'Personas días')
    return df_rango_semanas_def


def distribucion_personas_horas(input_file, export_file):
    df = leer_archivo(input_file)
    # agrupar por remitente y rango de horas
    df_personas_rango_horas = df.groupby([df.Autor, df.Remitente, pd.Grouper(key='Hora', freq='4H')]).size()  # .reset_index(name='count')
    df_def = df_personas_rango_horas.unstack()
    df_def.columns = ['de 0:00 a 4:00', 'de 4:00 a 8:00', 'de 8:00 a 12:00', 'de 12:00 a 16:00', 'de 16:00 a 20:00', 'de 20:00 a 24:00']

    # cambiar a integer y NaN por 0s
    df_def = df_def.fillna(0)
    df_def = df_def.astype(np.int64)

    # print(df_def)
    # escribir_csv(df_def, 'export/personas_horas.csv')
    # escribir_excel(df_def, export_file, 'Personas horas')
    return df_def


def distribucion_personas_dias_horas(input_file, export_file):
    df_personas_dias = distribucion_personas_dias(input_file, export_file)
    df_personas_horas = distribucion_personas_horas(input_file, export_file)

    # print(df_personas_dias)
    # print(df_personas_horas)
    # print(df_personas_dias.info(), df_personas_horas.info())
    df = pd.merge(df_personas_horas, df_personas_dias, on=['Remitente', 'Autor'])
    # print(df)
    # escribir_csv(df, 'export/personas_horas_dias.csv')
    escribir_excel(df_personas_dias, export_file, 'Personas dias')
    escribir_excel(df_personas_horas, export_file, 'Personas horas')
    escribir_excel(df, export_file, 'Personas horas días')
    return df


def distribucion_hilos_horas(input_file, export_file):
    df = leer_archivo(input_file)
    # agrupar por hilos y rango de horas
    # print(df.info())
    df = df.replace(np.nan, '', regex=True)
    df1 = df[df['Responde a'] == '']
    df_hilos_rango_horas = df1.groupby([pd.Grouper(key='Hora', freq='4H')], ).size()
    # print(df_hilos_rango_horas)
    # print(df_hilos_rango_horas.to_frame().info())
    df_def = df_hilos_rango_horas.to_frame()
    df_def.columns = [['Total']]
    # print(df_def)
    # Generar el csv
    # escribir_csv(df_def, 'export/hilos_horas.csv')
    escribir_excel(df_def, export_file, 'Hilos horas')
    return df_def


def distribucion_personas_semanas(input_file, export_file):
    df = leer_archivo(input_file)

    df_personas_semanas = df.groupby([df.Autor, df.Remitente, pd.Grouper(key='Fecha', freq='W-MON')]).size()
    # print(df_personas_semanas)
    df_def = df_personas_semanas.unstack()
    df_def = df_def.fillna(0)
    df_def = df_def.astype(np.int64)
    # print(df_def)

    # Generar el csv
    # escribir_csv(df_def2, 'export/personas_semanas.csv')
    # ruta_excel = os.path.splitext(input_file)[0]
    escribir_excel(df_def, export_file, 'Personas semanas')
    return df_def


def generar_archivos_cuerpo(input_file):
    df = leer_archivo(input_file)
    eleccion = ""
    while eleccion != '1' and eleccion != '2' and eleccion != '3':
        print('Opciones: ')
        print('1. Separar por foros.')
        print('2. Separar por hilos.')
        print('3. No separar.')

        eleccion = input()

    raiz = 'asig' + str(df.loc[0, 'Asignatura'])
    if not os.path.exists(raiz):
        os.makedirs(raiz)

    if eleccion == '1':
        for index, row in df.iterrows():
            hilo = str(row['Hilo'])
            directory = raiz + '/' + hilo
            if not os.path.exists(directory):
                os.makedirs(directory)
            with open(directory + "/" + row['Mensaje'] + ".txt", "w") as text_file:
                print(f"" + row['Texto mensaje'], file=text_file)
    elif eleccion == '2':
        for index, row in df.iterrows():
            foro = str(row['Foro'])
            hilo = str(row['Hilo'])
            directory = raiz + '/' + foro + '/' + hilo
            if not os.path.exists(directory):
                os.makedirs(directory)
            with open(directory + "/" + row['Mensaje'] + ".txt", "w") as text_file:
                print(f"" + row['Texto mensaje'], file=text_file)
    else:
        for index, row in df.iterrows():
            directory = raiz
            if not os.path.exists(directory):
                os.makedirs(directory)
            with open(directory + "/" + row['Mensaje'] + ".txt", "w") as text_file:
                print(f"" + row['Texto mensaje'], file=text_file)

    print('Creados ficheros en carpeta ' + raiz)


def ejecutarFunciones(nombrearchivo):
    csv = nombrearchivo + ".csv"
    distribucion_dias_semana(csv, nombrearchivo)
    distribucion_fechas(csv, nombrearchivo)
    distribucion_rango_horas(csv, nombrearchivo)
    distribucion_personas_dias(csv, nombrearchivo)
    distribucion_personas_horas(csv, nombrearchivo)
    distribucion_personas_dias_horas(csv, nombrearchivo)
    distribucion_hilos_horas(csv, nombrearchivo)
    distribucion_personas_semanas(csv, nombrearchivo)

