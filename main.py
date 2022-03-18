import glob
import pandas as pd
# import re
import utils
import datetime
import matplotlib.pyplot as plt

path_folder = r'data'
path_input_files = glob.glob(path_folder + "\\*.xls*")

sheets_to_import = 'Enregistrement'

for file in path_input_files:
    df_data = pd.read_excel(file, skiprows=[0, 2, 3, 4], header=0, sheet_name=sheets_to_import, parse_dates=False)  # Import data
    df_data = utils.timestamp_creation(df_data)

    utils.plot_serie_temporelle(df_data,'PT (W)')
