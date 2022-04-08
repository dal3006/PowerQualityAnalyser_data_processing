import glob
import pandas as pd
# import re
import utils
import datetime
import matplotlib.pyplot as plt

path_folder = r'data'
path_input_files = glob.glob(path_folder + "\\*.xls*")
columns_name_xlsx = ['Date:', 'Heure:'
,'P1 (W)', 'P2 (W)', 'P3 (W)', 'PT (W)', 'Q1 (var)', 'Q2 (var)', 'Q3 (var)', 'QT (var)', 'S1 (VA)', 'S2 (VA)', 'S3 (VA)', 'ST (VA)'
,'V1 rms MIN 1/2 période', 'V1 rms', 'V1 rms MAX 1/2 période', 'V2 rms MIN 1/2 période', 'V2 rms', 'V2 rms MAX 1/2 période', 'V3 rms MIN 1/2 période', 'V3 rms', 'V3 rms MAX 1/2 période', 'VNE MIN 1/2 période', 'VNE', 'VNE MAX 1/2 période'
,'A1 rms MIN 1/2 période', 'A1 rms', 'A1 rms MAX 1/2 période', 'A2 rms MIN 1/2 période', 'A2 rms', 'A2 rms MAX 1/2 période', 'A3 rms MIN 1/2 période', 'A3 rms', 'A3 rms MAX 1/2 période', 'AN rms', 'AN rms MAX 1/2 période'
,'Ep1 (Wh)', 'Ep2 (Wh)', 'Ep3 (Wh)', 'EpT (Wh)'
,'Eq1 (varh)', 'Eq2 (varh)', 'Eq3 (varh)', 'EqT (varh)', 'Es1 (VAh)', 'Es2 (VAh)', 'Es3 (VAh)', 'EsT (VAh)'
,'PF1', 'PF2', 'PF3', 'PFT'
,'V1 THDr', 'V2 THDr', 'V3 THDr', 'VNE THDr', 'A1 THDf', 'A2 THDf', 'A3 THDf'
,'Pst1', 'Pst2', 'Pst3', 'Plt1', 'Plt2', 'Plt3'
]
columns_name = ['Date:','Heure:'
,'p1_(W)','p2_(W)','p3_(W)','pT_(W)','q1_(var)','q2_(var)','q3_(var)','qT_(var)','s1_(Va)','s2_(Va)','s3_(Va)','sT_(Va)'
,'V1_rms_min','V1_rms','V1_rms_max','V2_rms_min','V2_rms','V2_rms_max','V3_rms_min','V3_rms','V3_rms_max','VNE_min','VNE','VNE_max'
,'a1_rms_min','a1_rms','a1_rms_max','a2_rms_min','a2_rms','a2_rms_max','a3_rms_min','a3_rms','a3_rms_max','aN_rms','aN_rms_max'
,'Ep1_(Wh)','Ep2_(Wh)','Ep3_(Wh)','EpT_(Wh)'
,'Eq1_(varh)','Eq2_(varh)','Eq3_(varh)','EqT_(varh)','Es1_(Vah)','Es2_(Vah)','Es3_(Vah)','EsT_(Vah)'
,'pF1','pF2','pF3','pFT'
,'V1_THDr','V2_THDr','V3_THDr','VNE_THDr','a1_THDf','a2_THDf','a3_THDf'
,'pst1','pst2','pst3','plt1','plt2','plt3'
]

sheets_to_import = 'Enregistrement'

for file in path_input_files:
    df_data = pd.read_excel(file, skiprows=[0, 2, 3, 4], header=0,usecols=columns_name_xlsx, sheet_name=sheets_to_import, parse_dates=False)  # Import data
    df_data.columns=columns_name
    df_data = utils.timestamp_creation(df_data)
    for name_column in df_data.columns:
        print(name_column)
        utils.plot_serie_temporelle(df_data,name_column)
        # utils.plot_serie_temporelle(df_data,'PT (W)')
