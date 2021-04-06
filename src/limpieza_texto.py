import pandas as pd
import numpy as np
import limpieza_texto as lt
import re
import seaborn as sns


def echo(x):
    return str(x)

def say_hello():
    print('hello')

# 1

def get_subset(df, lst):
    '''Subset con las columnas de la lista lst'''
    return df[lst]

def new_values_species(row):
    '''Función para agrupar valores en Species'''
    pattern1 = r'.*[Gg]alapagos.*'
    pattern2 = r'.*[Bb]ull.*'
    pattern3 = r'.*(([sS]and)|([Gg]rey.[Nn]urse)).*'
    pattern4 = r'.*[Ll]emon.*'
    pattern5 = r'.*[Rr]aggedtooth.*'
    pattern6 = r'.*[Ww]hite.*'
    pattern7 = r'.*[Bb]lacktip.*'
    pattern8 = r'.*[Tt]iger.*'
    pattern9 = r'.*[Bb]lue.*'
    pattern10 = r'.*[Dd]og.*'
    pattern11 = r'.*[Bb]rown.*'
    pattern12 = r'.*[Gg]rey.[Rr]eef.*'
    pattern13 = r'.*[Hh]ammerhead.*'
    pattern14 = r'.*[Zz]ambe.*'
    pattern15 = r'.*[Dd]usky.*'
    pattern16 = r'.*[Bb]onze.*'
    pattern17 = r'.*[Gg]ray.*'
    pattern18 = r'.*[Bb]roadnose.*'
    pattern19 = r'.*[Cc]aribbean.*'
    pattern20 = r'.*[Cc]arpet.*'
    pattern21 = r'.*[Gg]oblin.*'
    pattern22 = r'.*[Mm]ako.*'
    pattern23 = r'.*[Nn]urse.*'
    pattern24 = r'.*[Pp]orbeagle.*'
    pattern25 = r'.*[Ss]evengill.*'
    pattern26 = r'.*[Ss]hovelnose.*'
    pattern27 = r'.*[Ss]pinner.*'
    pattern28 = r'.*[Ww]hale.*'
    pattern29 = r'.*[Ww]obbegong.*'

    sequence = row['Species ']

    if re.match(pattern1, sequence):
        return 'Galapagos'
    if re.match(pattern2, sequence):
        return 'Bull'
    if re.match(pattern3, sequence):
        return 'Sandtiger'
    if re.match(pattern4, sequence):
        return 'Lemon'
    if re.match(pattern5, sequence):
        return 'Raggedtooth'
    if re.match(pattern6, sequence):
        return 'White'
    if re.match(pattern7, sequence):
        return 'Blacktip reef'
    if re.match(pattern8, sequence):
        return 'Tiger'
    if re.match(pattern9, sequence):
        return 'Blue'
    if re.match(pattern10, sequence):
        return 'Dog'
    if re.match(pattern11, sequence):
        return 'Brown'
    if re.match(pattern12, sequence):
        return 'Gray reef'
    if re.match(pattern13, sequence):
        return 'Hammerhead'
    if re.match(pattern14, sequence):
        return 'Zambezi'
    if re.match(pattern15, sequence):
        return 'dusky'
    if re.match(pattern16, sequence):
        return 'Bronze whaler'
    if re.match(pattern17, sequence):
        return 'Gray'
    if re.match(pattern18, sequence):
        return 'Broadnose sevengill'
    if re.match(pattern19, sequence):
        return 'Caribbean reef'
    if re.match(pattern20, sequence):
        return 'Carpet'
    if re.match(pattern21, sequence):
        return 'Goblin'
    if re.match(pattern22, sequence):
        return 'Mako'
    if re.match(pattern23, sequence):
        return 'Nurse'
    if re.match(pattern24, sequence):
        return 'Porbeagle'
    if re.match(pattern25, sequence):
        return 'Sevengill'
    if re.match(pattern26, sequence):
        return 'Shovelnose'
    if re.match(pattern27, sequence):
        return 'Spinner'
    if re.match(pattern28, sequence):
        return 'Whale'
    if re.match(pattern28, sequence):
        return 'Wobbegong'

    return 'Other Species'

def apply_filters(df):
    return df.apply(new_values_species, axis=1)

def drop_column(df, column):
   '''Eliminar columna'''
   return df.drop([column], axis = 1)

def _missing_values_fatal(row):
    '''Función para identificar los missing_values de la columna Fatal (Y/N)'''
    if row['Fatal (Y/N)'] == 'N' or row['Fatal (Y/N)'] == 'Y':
        return False
    return True
  
def apply_missing_fatal(df):
    '''Filtrar como True los missing_values'''
    return df.apply(_missing_values_fatal, axis=1)

def drop_true_rows_by_column(df, column):
    '''Eliminar las filas cuyo valor sea True en la columna delete_missing_values_fatal'''
    cpy = df.copy()
    cpy.drop(cpy[cpy[column] == True].index, inplace = True)
    return cpy

# 2

# 
def new_values_time(row):
    '''Función para agrupar valores en Time'''
    pattern1 = r'(0[0-9]|1[01])h'
    pattern2 = r'1[2-9]h'
    pattern3 = r'2[0-3]h'
    sequence = row['Time']

    if re.match(pattern1, sequence):
        return 'Morning'
    if re.match(pattern2, sequence):
        return 'Afternoon'
    if re.match(pattern3, sequence):
        return 'Night'

    if row['Time'] in ['Shortly before 12h00', '9h00', 'Morning ', '0830', 'Midday', 'Before 07h00', 'Early morning',
                        '"Just before 11h00"', '>08h00', 'Early Morning',  'Late morning', 'P.M.', 'Noon', 'A.M.', '>06h45',
                        'Between 06h00 & 07h20', '06j00', 'Mid-morning', 'Daytime', 'Before 10h30', 'Morning']:
        return 'Morning'

    if row['Time'] in ['Late afternoon', 'After noon', '1600', 'Early afternoon',
                        'Lunchtime', '15j45', 'Dusk', 'Just before sundown', 'Just after 12h00', 'Sunset', 'P.M.', 'Shortly before 13h00',
                        ' 14h00', 'Dark', 'Dawn', '"After dark"', '1500', '>14h30', 'After dusk', 'Late afternon', 'Late Afternoon', 'Afternoon']:
        return 'Afternoon'

    if row['Time'] in ['Night', 'Midnight', 'Evening', '"Evening"', 'Shortly after midnight', '8:04 pm',  '"Night"', 'Late night', 'Night']:
        return 'Night'

    return '--'

def apply_time_correction(df):
    '''Crear nueva columna para indicar lel resultado de new_values_time'''
    return df.apply(new_values_time, axis=1)

def drop_dashed_rows_by_column(df, column):
    '''Eliminar las filas cuyo valor sea '--' en la columna Day period'''
    cpy = df.copy()
    cpy.drop(cpy[cpy[column] == '--'].index, inplace = True)
    return cpy

def missing_values_fatal(row):
    '''Función para identificar los missing_values de la columna Fatal (Y/N)'''
    if row['Fatal (Y/N)'] == 'M' or row['Fatal (Y/N)'] == 'UNKNOWN' or row['Fatal (Y/N)'] == '2017':
        return True
    else:
        return False


# 3

def remove_na(df, column):
    '''Eliminar los valores nulos'''
    return df[df[column].notna()]

def replace_countries(dt):
  '''Función para sustituir string en las celdas'''
  new_dt = dt.copy()

  new_dt.loc[new_dt['Country'] == 'EGYPT / ISRAEL', 'Country'] = 'EGYPT'
  new_dt.loc[new_dt['Country'] == 'EGYPT ', 'Country'] = 'EGYPT'
  new_dt.loc[new_dt['Country'] == 'INDIAN OCEAN', 'Country'] = 'INDIA'
  new_dt.loc[new_dt['Country'] == 'ITALY / CROATIA', 'Country'] = 'ITALY'
  new_dt.loc[new_dt['Country'] == 'ST. MAARTIN', 'Country'] = 'ST. MARTIN'
  new_dt.loc[(new_dt['Country'].str.find('?') >= 0),
             'Country'] = new_dt['Country'].str.replace('?', '')
  return new_dt

def remove_non_countries(df):
    '''Función para eliminar filas cuyas variables no son paises'''
    return df[df.Country.str.contains("OCEAN") == False]


def count_dataframe(df, column, count_name):
    '''Función para añadir columna con el value_count de Country'''
    df = df.value_counts().rename_axis(column).reset_index(name=count_name)
    return df
