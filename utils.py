import datetime

import matplotlib.pyplot as plt
import pandas as pd
import os


def timestamp_creation(df_data):
    df_data['Timestamp'] = pd.to_datetime(df_data['Date:'] + ' ' + df_data['Heure:'], format='%d/%m/%Y %H:%M:%S')
    df_data.drop(['Date:', 'Heure:'], axis=1, inplace=True)  # date = datetime( imported_data['Date:'].values)
    # set Timestamp as index and sort by index
    df_data.set_index("Timestamp", inplace=True)
    df_data.sort_values(by='Timestamp', inplace=True)
    df_data = df_data.apply(pd.to_numeric, errors='coerce')

    return df_data


def plot_serie_temporelle(df, name_column, nom_poste):
    if name_column == 'monotone_s_va':
        df.reset_index(inplace=True)
    plt.clf()
    # print(df[name_column])
    df.plot(y=name_column)
    path_folder = '..//LV_losses_SENELEC//output//'
    if not os.path.exists(path_folder):  # Verification d'existence de ce path
        os.mkdir(path_folder)  # Sinon création du dossier

    if not os.path.exists(path_folder + nom_poste):  # Verification d'existence de ce path
        os.mkdir(path_folder + nom_poste)  # Sinon création du dossier

    path_folder_poste_i = path_folder + nom_poste + '//Courbes Analyseur//'
    if not os.path.exists(path_folder_poste_i):  # Verification d'existence de ce path
        os.mkdir(path_folder_poste_i)  # Sinon création du dossier


    fname = path_folder_poste_i + name_column + '.png'
    plt.savefig(fname=fname, dpi=200)
    plt.show()
    return 'Done'

def calcul_grandeurs_caracteristiques(df_data):

    column_name_dt='st_va'
    column_name_p_total='pt_w'
    point_par_heure=60
    #Monotone
    # df_data['monotone_s_va']= df_data[column_name_dt]
    # df_data['monotone_s_va'] = df_data['monotone_s_va'].apply(lambda x: x.sort_values(ascending=False).values)
    df_data['monotone_s_va'] = df_data.apply(lambda x: x.sort_values(ascending=False).values)[column_name_dt]
    # df_data['monotone_s_va']=df_data['monotone_s_va']/df_max #division par P_max


    s_max_kva=df_data['monotone_s_va'].max()/1000
    p_max_kw=df_data[column_name_p_total].max()/1000

    e_consom_kwh=df_data[column_name_p_total].sum()/point_par_heure/1000
    e_consom_kvah=df_data['monotone_s_va'].sum()/point_par_heure/1000

    h_max=e_consom_kvah/s_max_kva
    h_total_analyse=len(df_data)/60

    #Creation i_moy et k_des
    df_data['i_moy'] = (df_data['a1_rms'] + df_data['a2_rms'] + df_data['a3_rms']) / 3
    df_data['K_des'] = (df_data['a1_rms'] * df_data['a1_rms'] + df_data['a2_rms'] * df_data['a2_rms'] + df_data[
        'a3_rms'] * df_data['a3_rms']) / (3 * df_data['i_moy'] * df_data['i_moy'])

    k_des=df_data['K_des'].mean()

    return df_data,s_max_kva,p_max_kw,e_consom_kwh,e_consom_kvah,h_max,k_des,h_total_analyse

def sauvegarde_variable():

    return 1

def sauvegarde_plot():

    return 1



#df_data['i_moy']=(df_data['A1 rms']+df_data['A2 rms']+df_data['A3 rms'])/3
#df_data['K_des']=(df_data['A1 rms']*df_data['A1 rms']+df_data['A2 rms']*df_data['A2 rms']+df_data['A3 rms']*df_data['A3 rms'])/(3*df_data['i_moy']*df_data['i_moy'])

#A completer proprement en s'inspirante de code fait pour le scada GE
    #
    #
    #
    # #Création de H_max et H_pertes
    #
    # #Calcul de H_max
    # data_sorted_monotone = data_sorted.apply(lambda x: x.sort_values(ascending=False).values) #Le ffil complete le pas horaire different du quart d'heure de l'adms
    # data_sorted_monotone=data_sorted_monotone/df_max #division par P_max
    #
    # data_sorted_monotone=data_sorted_monotone.reset_index(drop=True)
    # # data_sorted_monotone.iloc[:,3].plot()
    # df_H_max=data_sorted_monotone.sum()/point_par_heure
    #
    # #Calcul de H_pertes
    # data_sorted_monotone_carre=data_sorted_monotone.apply(lambda x: x*x)
    # data_sorted_monotone_carre.iloc[:,3].plot()
    # df_H_pertes=data_sorted_monotone_carre.sum()/point_par_heure
    #
    #
    # #Mise en place de la H_max et Hpertes de df_depart
    # #PAS OPTI DU TOUT !!
    # #on pourrait deja rassembler avec Pmax
    # #On pourrait surtout le vectorisé
    #
    # is_in_SCADA = df_depart['ID'].isin(data_sorted.columns).values #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html
    # display(is_in_SCADA)
    #
    # df_depart['H_max']=np.nan
    # df_depart['H_pertes']=np.nan
    # df_depart['Nombre de point horaire disonible']=np.nan
    # df_depart['Energie transite (MWh), Reception']=np.nan
    # df_depart['Energie transite (MWh), Emission']=np.nan
    # df_depart['Puissance à la pointe national 2020']=np.nan
    #
    #
    #
    # for j in range(len(df_depart['ID'])) :
    #     if is_in_SCADA[j]==True :
    #
    #         value_validation=df_depart.iloc[j,df_depart.columns.get_loc('Validite GE ?')] or df_depart.iloc[j,df_depart.columns.get_loc('Validite SE ?')]
    #         ID_j=df_depart.iloc[j,df_depart.columns.get_loc('ID')]
    #         type_j=df_depart.iloc[j,df_depart.columns.get_loc('TYPE')]
    #         #Calcul H_max et Hpertes
    #         H_max=df_H_max[ID_j]
    #         H_pertes=df_H_pertes[ID_j]
    #         P_pointe_national = data_sorted[data_sorted.index == pd.Timestamp('2020-10-20T23')][ID_j]
    #
    #
    #         #Calcul de Energie transité
    #         nb_point_horaire_disponible=len(data_sorted[ID_j].dropna().index)/point_par_heure
    #         energie_transite_emission = data_sorted[ID_j][data_sorted[ID_j]>0].dropna().sum()/point_par_heure
    #         energie_transite_reception = data_sorted[ID_j][data_sorted[ID_j]<0].dropna().sum()/point_par_heure
    #
    #         if value_validation :
    #             if type_j=='feeder_30':
    #                 df_depart.iloc[j,df_depart.columns.get_loc('H_max')]=H_max
    #                 df_depart.iloc[j,df_depart.columns.get_loc('H_pertes')]=H_pertes
    #                 df_depart.iloc[j,df_depart.columns.get_loc('Puissance à la pointe national 2020')]=P_pointe_national
    #
    #
    #
    #             df_depart.iloc[j,df_depart.columns.get_loc('Nombre de point horaire disonible')]=nb_point_horaire_disponible
    #             df_depart.iloc[j,df_depart.columns.get_loc('Energie transite (MWh), Reception')]=energie_transite_reception
    #             df_depart.iloc[j,df_depart.columns.get_loc('Energie transite (MWh), Emission')]=energie_transite_emission
    #
    #
    # df_depart['H_pertes']=df_depart['H_pertes']*8760/df_depart['Nombre de point horaire disonible']
    # df_depart['H_max']=df_depart['H_max']*8760/df_depart['Nombre de point horaire disonible']
    # df_depart['Energie transite (MWh), Reception']=df_depart['Energie transite (MWh), Reception']*8760/df_depart['Nombre de point horaire disonible']
    # df_depart['Energie transite (MWh), Emission']=df_depart['Energie transite (MWh), Emission']*8760/df_depart['Nombre de point horaire disonible']
    #
    #
    # df_depart['a : coefficient de forme'] = (df_depart['H_pertes'] - df_depart['H_max']*df_depart['H_max']/8760 ) / (df_depart['H_max'] - df_depart['H_max']*df_depart['H_max']/8760)
    # display(df_depart)