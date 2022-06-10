import glob
import pandas as pd
# import re
import utils
import datetime
import os
import matplotlib.pyplot as plt

path_folder = r'OLD/data'
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
,'p1(W)','p2(W)','p3(W)','pT(W)','q1(var)','q2(var)','q3(var)','qT(var)','s1(Va)','s2(Va)','s3(Va)','sT(Va)'
,'V1_rms_min','V1_rms','V1_rms_max','V2_rms_min','V2_rms','V2_rms_max','V3_rms_min','V3_rms','V3_rms_max','VNE_min','VNE','VNE_max'
,'a1_rms_min','a1_rms','a1_rms_max','a2_rms_min','a2_rms','a2_rms_max','a3_rms_min','a3_rms','a3_rms_max','aN_rms','aN_rms_max'
,'Ep1_(Wh)','Ep2_(Wh)','Ep3_(Wh)','EpT_(Wh)'
,'Eq1_(varh)','Eq2_(varh)','Eq3_(varh)','EqT_(varh)','Es1_(Vah)','Es2_(Vah)','Es3_(Vah)','EsT_(Vah)'
,'pF1','pF2','pF3','pFT'
,'V1_THDr','V2_THDr','V3_THDr','VNE_THDr','a1_THDf','a2_THDf','a3_THDf'
,'pst1','pst2','pst3','plt1','plt2','plt3'
]

sheets_to_import = 'Enregistrement'


path_project_folder=os.path.join(os.path.dirname(__file__), '..')

source_folder_path= path_project_folder + r'\LV_losses_SENELEC\1.Sources\4. Enquete terrain\API_' + str(datetime.datetime.now().date())
print(source_folder_path)
# source_folder_path=path_project_folder + r'\1.Sources\4. Enquete terrain\2022-05-09'

source_liste_postes_path= path_project_folder + r'\LV_losses_SENELEC\1.Sources\4. Enquete terrain'
liste_postes = pd.read_csv(filepath_or_buffer=source_liste_postes_path + r'\liste_postes.txt')['nom poste'].values
# liste_postes=['ZGACB','ZGCB','ZGD','ZGF']   #Modélisation sur un réseau spécifique
# liste_postes=['ZGACB']   #Modélisation sur un réseau spécifique



for nom_poste in liste_postes:  # test de la presence du nom de poste txt dans les noms de poste csv
    source_xlsx_analyseur = path_project_folder + r'\LV_losses_SENELEC\1.Sources\2. Analyseur\8336_190277MMH 1800_Enregistrement_' + nom_poste + '.xlsx'

    #Paths données enquetes
    source_poste_folder_path= source_folder_path +'\\Analyses_individuels\\' + nom_poste
    print(source_poste_folder_path)

    #Récupérationn des csv
    path_poteaux_csv = source_poste_folder_path + r'\Cleaned_files\validated_poteaux.csv'
    path_poste_csv = source_poste_folder_path + r'\Cleaned_files\validated_postes.csv'
    path_clients_csv = source_poste_folder_path + r'\Cleaned_files\validated_clients.csv'

    if not os.path.exists(source_xlsx_analyseur) :
        print(source_xlsx_analyseur + ' does not exist !')
        continue
    if not os.path.exists(path_poste_csv):
        print(path_poste_csv + ' does not exist !')
        continue

    #Récupérationn des csv
    # poteaux_csv = pd.read_csv(path_poteaux_csv, encoding='utf-8', sep=';')
    postes_csv = pd.read_csv(path_poste_csv, encoding='utf-8', sep=';')
    # clients_csv = pd.read_csv(path_clients_csv, encoding='utf-8', sep=';')


    df_data = pd.read_excel(source_xlsx_analyseur, skiprows=[0, 2, 3, 4], header=0,usecols=columns_name_xlsx, sheet_name=sheets_to_import, parse_dates=False)  # Import data
    df_data = utils.timestamp_creation(df_data)
    print('xlsx read')
    # df_data.rename(str.lower.replace(' ','_'), axis='columns',inplace=True)
    df_data.columns = (x.lower().replace(' ', '_').replace('(', '').replace(')', '').replace('é','e').replace('1/2', 'demi') for x in df_data.columns)

    [df_data,s_max_kva,p_max_kw,e_consom_kwh,e_consom_kvah,h_max,k_des,h_total_analyse]=utils.calcul_grandeurs_caracteristiques(df_data)

    postes_csv['s_max_kva']=s_max_kva
    postes_csv['p_max_kw']=p_max_kw
    postes_csv['e_consom_kvah']=e_consom_kvah
    postes_csv['e_consom_kwh']=e_consom_kwh
    postes_csv['h_max']=h_max
    postes_csv['h_max']=h_max

    postes_csv['h_total_analyse']=h_total_analyse

    for name_column in df_data.columns:
        if name_column=='st_va' or name_column=='monotone_s_va':   #Selection
            print(name_column)
            utils.plot_serie_temporelle(df_data,name_column,nom_poste)
            # utils.plot_serie_temporelle(df_data,'PT (W)')
    utils.save_data(df_data,nom_poste)
    postes_csv.to_csv(path_or_buf=path_poste_csv, sep=';', index=False)

print('done !! hura')




#
# df_data['i_moy'] = (df_data['a1_rms'] + df_data['a2_rms'] + df_data['a3_rms']) / 3
# df_data['K_des'] = (df_data['a1_rms'] * df_data['a1_rms'] + df_data['a2_rms'] * df_data['a2_rms'] + df_data[
#     'a3_rms'] * df_data['a3_rms']) / (3 * df_data['i_moy'] * df_data['i_moy'])
