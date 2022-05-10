import streamlit as st
import datetime
from PIL import Image
import pandas as pd
import os
import sqlite3
import webbrowser
#st.set_page_config(layout='wide')

conn = sqlite3.connect("discrepancy_v11.db")

def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv(sep='\t').encode('utf-8')

def open_browser():
    webbrowser.open_new('http://localhost:8501')

st.set_page_config(
        page_title="Discrepancy Check",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded")

header = st.container()
dataset = st.container()
rf_bar = st.container()
c1 = st.sidebar
modelTraining = st.container()
interactive = st.container()
mapping = st.container()

with header:
    image = Image.open("road_7.png")
    st.image(image,use_column_width=True)
    st.title("")

with c1:
     st.sidebar.title("Navigation")
     selected_page = st.sidebar.radio("Which tech would you like to go to", options=["Overall", "2G", "3G", "4G"])

     #selected_page = st.selectbox("Which page would you like to go to?", options=["Resume", "Telecommunication", "Data Science", "Map Visualization", "Computer Vision"])
     #st.sidebar.title("Operator Selection")
     #operator = st.selectbox("Which operator do you want to analyze ",options=["O2 (UK)","T-Mobile UK"])
     #st.sidebar.title("Period Selection")
     #period=st.sidebar.radio("Which period do you want to analyze", options=['PreTest','PostTest'])
     #st.sidebar.title("Technology Selection")
     #tech_data=st.sidebar.radio("Which type of tech do you want to analyze", options=['4G','4G/3G','3G', '2G'])
     #type_fail =st.sidebar.radio("Which type of test do you want to analize",options=['Data','Voice','Coverage'])

if selected_page == 'Overall':
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2 :
        image = Image.open("summary_table_v2.png")
        st.image(image,use_column_width=True)

elif selected_page == '4G':
    st.sidebar.title("Category")
    selected_page_2 = st.sidebar.radio("Which discrepancy would you like to go to", options=["4G Summary", "Neighbor Relations","EARFCN Definition Check", "PCI clash", "RSI clash", "TAC-LAC Mapping","Tilt Discrepancies","256QAM Switch Check","eNodeB ID Duplication","External Definition Discrepancies"])
    if selected_page_2 == '4G Summary':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2 :
            image = Image.open("summary_4g_v2.png")
            st.image(image,use_column_width=True)
    elif selected_page_2 == 'EARFCN Definition Check':
        col1, col2, col3 = st.columns([1, 5, 1])
        with col2:
            st.title("EARFCN Definition Check")
            st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item indicates cases where the defined EARFCN and bandwidth of the cells are incompatible with the operator strategy."
                        "</p>", unsafe_allow_html=True)
            st.title("There is no case")
    elif selected_page_2 == 'Neighbor Relations':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2 :
            selected_page_3 = st.selectbox("Which discrepancy would you like to go to", options=['Missing Co-site Same EARFCN Neighbours','Cells_Without_Any_IRAT_3G_neighbor_relationship','4G Cells without neighbours', '4G Cells without any incoming neighbours','LTE-3G CoSite Missing Neighbor Relations','LTE-3G Invalid Neighbor Relations', 'LTE-3G Redundant Frequency', 'LTE-2G Unidirectional neighboring relationship check in LTE','LTE-3G Unidirectional neighboring relationship check in LTE','LTE-LTE Unidirectional Intra neighboring relationship check in LTE','LTE-LTE Unidirectional Inter neighboring relationship check in LTE'])
        if selected_page_3 == 'Missing Co-site Same EARFCN Neighbours' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("Missing Co-site Same EARFCN Neighbours")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows missing neighbor relationships between LTE cells that are part of the same site and have the same EARFCN value"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/Missing Co-site Same EARFCN Neighbours.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-4'""", con=conn, index_col=None)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='Missing Co-site Same EARFCN Neighbours.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'Cells_Without_Any_IRAT_3G_neighbor_relationship' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("Cells Without Any IRAT 3G neighbor relationship")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows LTE Cells that do not have a defined neighbor relationship with any 3G cell that would allow the LTE Cell to perform IRAT handover"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/Cells_Without_Any_IRAT_3G_neighbor_relationship.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-5'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='Cells_Without_Any_IRAT_3G_neighbor_relationship.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '4G Cells without neighbours' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("4G Cells without neighbours")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows LTE Cells that do not have any neighbor cells."
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/4G Cells without neighbours.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-6'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='4G Cells without neighbours.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '4G Cells without any incoming neighbours' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("4G Cells without any incoming neighbours")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows LTE Cells that do not have any incoming neighboring relationships."
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/4G Cells without any incoming neighbours.png")
                st.image(image,use_column_width=True)
                st.title("There is no case")
        elif selected_page_3 == 'LTE-3G CoSite Missing Neighbor Relations' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("LTE-3G CoSite Missing Neighbor Relations")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows missing neighbor relationships from a LTE cell to a 3G cell that are both in the same site"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/LTE-3G CoSite Missing Neighbor Relations.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-8'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='LTE-3G CoSite Missing Neighbor Relations.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'LTE-3G Invalid Neighbor Relations' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("LTE-3G Invalid Neighbor Relations")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-9'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='LTE-3G Invalid Neighbor Relations.xls',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'LTE-3G Redundant Frequency' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("LTE-3G Redundant Frequency")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-10'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='LTE-3G Redundant Frequency',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'LTE-2G Unidirectional neighboring relationship check in LTE' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("LTE-2G Unidirectional neighboring relationship check in LTE")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "If cell B on the LTE side is configured as a neighboring cell of cell A on the GSM side but cell A is not configured as a neighboring cell of cell B, cell B is a unidirectional neighboring cell. In this case, the handover depends on the ANR function on the LTE network. The handover success rate may be lower than that when neighbor relationships are manually configured. The matching identity for the neighboring GSM cell on the LTE network is LOCALCELLID(local LTE cell)+MCC+MNC+GERANCELLID+LAC(peer GSM cell)."
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/LTE-2G Unidirectional neighboring relationship check in LTE.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-11'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='LTE-2G Unidirectional neighboring relationship check in LTE.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'LTE-3G Unidirectional neighboring relationship check in LTE' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("LTE-3G Unidirectional neighboring relationship check in LTE")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "If cell B on the LTE side is configured as a neighboring cell of cell A on the UMTS side but cell A is not configured as a neighboring cell of cell B, cell B is a unidirectional neighboring cell. In this case, the handover depends on the ANR function on the LTE network. The handover success rate may be lower than that when neighbor relationships are manually configured. The matching identity for the neighboring UMTS cell on the LTE network is versions earlier than SRAN8.0: LOCALCELLID(local LTE cell)+RNCID+UTRANCELLID(peer UMTS cell) SRAN8.0 and later versions:  LOCALCELLID(local LTE cell)+RNCID+CELLID(peer UMTS cell)"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/LTE-3G Unidirectional neighboring relationship check in LTE.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-12'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='LTE-3G Unidirectional neighboring relationship check in LTE.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'LTE-LTE Unidirectional Intra neighboring relationship check in LTE' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("LTE-LTE Unidirectional Intra neighboring relationship check in LTE")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "If cell A is an intra-frequency neighboring cell of cell B but cell B is not a neighboring cell of cell A, cell A is the unidirectional intra neighboring cell of cell B. In this case, the handover depends on the ANR function on the LTE network. The handover success rate may be lower than that when neighbor relationships are manually configured. The matching identity for the neighboring LTE cell on the LTE network is LOCALCELLID(local LTE cell)+MCC+MNC+ENODEBID+CELLID(peer LTE cell)."
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/LTE-LTE Unidirectional Intra neighboring relationship check in LTE.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-13'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='LTE-LTE Unidirectional Intra neighboring relationship check in LTE.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'LTE-LTE Unidirectional Inter neighboring relationship check in LTE' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("LTE-LTE Unidirectional Inter neighboring relationship check in LTE")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "If cell A is an inter-frequency neighboring cell of cell B but cell B is not a neighboring cell of cell A, cell A is the unidirectional inter neighboring cell of cell B. In this case, the handover depends on the ANR function on the LTE network. The handover success rate may be lower than that when neighbor relationships are manually configured. The matching identity for the neighboring LTE cell on the LTE network is LOCALCELLID(local LTE cell)+MCC+MNC+ENODEBID+CELLID(peer LTE cell)."
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/LTE-LTE Unidirectional Inter neighboring relationship check in LTE.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-14'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='LTE-LTE Unidirectional Inter neighboring relationship check in LTE.csv',
                     mime='text/csv',
                 )
    elif selected_page_2 == 'PCI clash':
        col1, col2, col3 = st.columns([1, 5, 1])
        with col2:
            st.title("PCI clash")
            st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows LTE Cells whose PCI value is the same with another LTE cell within a distance less than 5 km"
                        "</p>", unsafe_allow_html=True)
            image = Image.open("item_png/PCI clash.png")
            st.image(image,use_column_width=True)
            st.title("RESULTS")
            df = pd.read_sql("""select * from 'ITEM-2'""", con=conn)
            df.drop('index', inplace=True, axis=1)
            st.dataframe(df)
            csv = convert_df(df)
            st.download_button(
                 label="Download data as CSV",
                 data=csv,
                 file_name='PCI clash.csv',
                 mime='text/csv',
             )
    elif selected_page_2 == 'RSI clash':
        col1, col2, col3 = st.columns([1, 5, 1])
        with col2:
            st.title("RSI clash")
            st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows LTE Cells whose RSI value is the same with another LTE cell within a distance less than 5 km "
                        "</p>", unsafe_allow_html=True)
            st.title("RESULTS")
            df = pd.read_sql("""select * from 'ITEM-3'""", con=conn)
            df.drop('index', inplace=True, axis=1)
            st.dataframe(df)
            csv = convert_df(df)
            st.download_button(
                 label="Download data as CSV",
                 data=csv,
                 file_name='RSI clash.csv',
                 mime='text/csv',
             )
    elif selected_page_2 == '256QAM Switch Check':
        col1, col2, col3 = st.columns([1, 5, 1])
        with col2:
            st.title("256QAM Switch Check")
            st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows cells that do not have 256 QAM switches turned on."
                        "</p>", unsafe_allow_html=True)
            st.title("RESULTS")
            df = pd.read_sql("""select * from 'ITEM-20'""", con=conn)
            df.drop('index', inplace=True, axis=1)
            st.dataframe(df)
            csv = convert_df(df)
            st.download_button(
                 label="Download data as CSV",
                 data=csv,
                 file_name='256QAM Switch Check.csv',
                 mime='text/csv'
             )
    elif selected_page_2 == 'eNodeB ID Duplication':
        col1, col2, col3 = st.columns([1, 5, 1])
        with col2:
            st.title("eNodeB ID Duplication")
            st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows eNodeB ID values that are assigned to more than one cells in the network"
                        "</p>", unsafe_allow_html=True)
            st.title("RESULTS")
            df = pd.read_sql("""select * from 'ITEM-21'""", con=conn)
            df.drop('index', inplace=True, axis=1)
            st.dataframe(df)
            csv = convert_df(df)
            st.download_button(
                 label="Download data as CSV",
                 data=csv,
                 file_name='eNodeB ID Duplication.csv',
                 mime='text/csv',
             )
    elif selected_page_2 == 'External Definition Discrepancies':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2 :
            selected_page_3 = st.selectbox("Which discrepancy would you like to go to", options=['External Definitions Check (BSIC/BCCH)  - (4G to 2G)', 'External Definitions Check (LAC/PSC/DLUARFCN) - (4G to 3G)', 'External Definitions Check (PCI/TAC/DLEARFCN)  - (4G to 4G)', 'External Definition Check (Redundant Cells) -  (4G to 3G)'])
        if selected_page_3 == 'External Definitions Check (BSIC/BCCH)  - (4G to 2G)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("External Definitions Check (BSIC/BCCH) - (4G to 2G)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-22'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='External Definitions Check (BSIC/BCCH)-(4G to 2G).csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'External Definitions Check (LAC/PSC/DLUARFCN) - (4G to 3G)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("External Definitions Check (LAC/PSC/DLUARFCN) - (4G to 3G)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-23'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='External Definitions Check (LAC/PSC/DLUARFCN) - (4G to 3G).csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'External Definitions Check (PCI/TAC/DLEARFCN)  - (4G to 4G)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("External Definitions Check (PCI/TAC/DLEARFCN) - (4G to 4G)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-24'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='External Definitions Check (PCI/TAC/DLEARFCN) - (4G to 4G).csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'External Definition Check (Redundant Cells) -  (4G to 3G)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("External Definition Check (Redundant Cells) -  (4G to 3G)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-25'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='External Definition Check (Redundant Cells) -  (4G to 3G).csv',
                     mime='text/csv',
                 )

elif selected_page == '3G':
    st.sidebar.title("Category")
    selected_page_2 = st.sidebar.radio("Which discrepancy would you like to go to", options=["3G Summary", "PSC Clash","Neighbor Relation Discrepancies","Duplicate_3G_LAC-CI","Co-Sector Chip Rate (Tcell) Check","Tilt Discrepancies","Power InConsistencies","64QAM Switch Check","External Definitions Check", "Radio Data Consistency"])
    if selected_page_2 == '3G Summary':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2 :
            image = Image.open("summary_3g_v2.png")
            st.image(image,use_column_width=True)
    elif selected_page_2 == 'PSC Clash':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2 :
            selected_page_3 = st.selectbox("Which discrepancy would you like to go to", options=["Same PSC Pairs within 3 km","3G Same PSC in Source and Tier Neighbour","3G Same PSC in Source and Neighbours of Neighbour"])
        if selected_page_3 == 'Same PSC Pairs within 3 km' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("Same PSC Pairs within 3 km")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 3G Cells whose PSC value is the same with another 3G cell within a distance less than 3 km "
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/PSC_clash.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-28'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='PSC_clash.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '3G Same PSC in Source and Tier Neighbour' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("3G Same PSC in Source and Tier Neighbour")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/PSC_clash.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-29'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='PSC_clash.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '3G Same PSC in Source and Neighbours of Neighbour' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("3G Same PSC in Source and Neighbours of Neighbour")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 3G Cells whose PSC value is shared by another 3G neighbor of one of the neighbors of the source cell. In other words, when a 3G Cell 'A' with PSC = XX has a neighbor 'B' with PSC=YY, and Cell 'B' has another neighbor cell 'C' with also PSC=XX"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/psc_n_of_n.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-30'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='PSC_clash.csv',
                     mime='text/csv',
                 )
    elif selected_page_2 == 'Neighbor Relation Discrepancies':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2 :
            selected_page_3 = st.selectbox("Which discrepancy would you like to go to", options=["Missing Co-Site same UARFCN Neighbours","3G Cells without neighbours","3G Cells without any incoming neighbours","3G-LTE CoSite Missing Neighbor Relations","3G-3G CoSite Missing Neighbor Relations","3G-2G CoSite Missing Neighbor Relations","3G-3G Multi Carrier Neighbor Cells","3G-2G Multi Carrier Neighbor Cells","3G Invalid Neighbor Relations","3G-3G unidirectional Intra neighboring relationship check in UMTS","3G-3G unidirectional Inter neighboring relationship check in UMTS","3G-2G unidirectional neighboring relationship check in UMTS","3G-LTE unidirectional neighboring relationship check in UMTS"])
        if selected_page_3 == 'Missing Co-Site same UARFCN Neighbours' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("Missing Co-Site same UARFCN Neighbours")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows missing neighbor relationships between 3G cells that are part of the same site and have the same UARFCN value"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/Missing Co-Site same UARFCN Neighbours.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-31'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='Missing Co-Site same UARFCN Neighbours.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '3G Cells without neighbours' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("3G Cells without neighbours")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 3G Cells that do not have any neighbor cells/relationships"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/3G Cells without neighbours.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-32'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='3G Cells without neighbours.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '3G Cells without any incoming neighbours' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("3G Cells without any incoming neighbours")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 3G Cells that do not have any incoming neighboring relationships. Incoming indicates a handover from another cell to the mentioned cell."
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/3G Cells without any incoming neighbours.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-33'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='3G Cells without any incoming neighbours.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '3G-LTE CoSite Missing Neighbor Relations' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("3G-LTE CoSite Missing Neighbor Relations")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows missing neighbor relationships from a 3G cell to a LTE cell that are both present in the same site"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/3G-LTE CoSite Missing Neighbor Relations.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-35'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='3G-LTE CoSite Missing Neighbor Relations.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '3G-3G CoSite Missing Neighbor Relations' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("3G-3G CoSite Missing Neighbor Relations")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows missing neighbor relationships from a 3G cell to another 3G cell that are both present in the same site"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/3G-3G CoSite Missing Neighbor Relations.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-36'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='3G-3G CoSite Missing Neighbor Relations.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '3G-2G CoSite Missing Neighbor Relations' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("3G-2G CoSite Missing Neighbor Relations")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows missing neighbor relationships from a 3G cell to a 2G cell that are both present in the same site"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/3G-2G CoSite Missing Neighbor Relations.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-37'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='3G-2G CoSite Missing Neighbor Relations.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '3G-3G Multi Carrier Neighbor Cells' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("3G-3G Multi Carrier Neighbor Cells")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 3G cell pairs that are neighors with each other and both have multiple carriers"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/3G-2G CoSite Missing Neighbor Relations.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-38'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='3G-3G Multi Carrier Neighbor Cells.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '3G-2G Multi Carrier Neighbor Cells' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("3G-2G Multi Carrier Neighbor Cells")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 3G-2G cell pairs that are neighors with each other and both have multiple carriers"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/3G-2G CoSite Missing Neighbor Relations.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-39'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='3G-2G Multi Carrier Neighbor Cells.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '3G Invalid Neighbor Relations' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("3G Invalid Neighbor Relations")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/3G-2G CoSite Missing Neighbor Relations.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-40'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='3G Invalid Neighbor Relations.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '3G-3G unidirectional Intra neighboring relationship check in UMTS' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("3G-3G unidirectional Intra neighboring relationship check in UMTS")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 3G-3G cell pairs (same EARFCN) where a handover is defined from one of them to the other but not vice versa."
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/3G-3G unidirectional Intra neighboring relationship check in UMTS.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-41'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='3G-3G unidirectional Intra neighboring relationship check in UMTS.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '3G-3G unidirectional Inter neighboring relationship check in UMTS' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("3G-3G unidirectional Inter neighboring relationship check in UMTS")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 3G-3G cell pairs (different UARFCN) where a handover is defined from one of them to the other but not vice versa."
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/3G-3G unidirectional Inter neighboring relationship check in UMTS.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-42'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='3G-3G unidirectional Inter neighboring relationship check in UMTS.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '3G-2G unidirectional neighboring relationship check in UMTS' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("3G-2G unidirectional neighboring relationship check in UMTS")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 3G-2G cell pairs where a handover from 2G to 3G is defined but not vice versa."
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/3G-2G unidirectional neighboring relationship check in UMTS.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-43'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='3G-2G unidirectional neighboring relationship check in UMTS.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '3G-LTE unidirectional neighboring relationship check in UMTS' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("3G-LTE unidirectional neighboring relationship check in UMTS")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 3G-LTE cell pairs where a handover from LTE to 3G is defined but not vice versa."
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/3G-LTE unidirectional neighboring relationship check in UMTS.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-44'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='3G-LTE unidirectional neighboring relationship check in UMTS.csv',
                     mime='text/csv',
                 )
    elif selected_page_2 == 'Duplicate_3G_LAC-CI':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2 :
            st.title("Duplicate_3G_LAC-CI")
            st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows duplicated LAC-CI value pairs (assigned to more than one cell in the same network)"
                        "</p>", unsafe_allow_html=True)
            st.title("There is no case")
    elif selected_page_2 == 'Co-Sector Chip Rate (Tcell) Check':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2 :
            st.title("Co-Sector Chip Rate (Tcell) Check")
            st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows cells in the same sector that have different chip rate (chip rate = symbol rate X spreading factor)"
                        "</p>", unsafe_allow_html=True)
            st.title("RESULTS")
            df = pd.read_sql("""select * from 'ITEM-46'""", con=conn)
            df.drop('index', inplace=True, axis=1)
            st.dataframe(df)
            csv = convert_df(df)
            st.download_button(
                 label="Download data as CSV",
                 data=csv,
                 file_name='Co-Sector Chip Rate (Tcell) Check.csv',
                 mime='text/csv',
             )
    elif selected_page_2 == 'Power InConsistencies':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2 :
            selected_page_3 = st.selectbox("Which discrepancy would you like to go to", options=["Non-Standard CPICH Power Setting (CPICH Power/ Total Power <%5)", "Non-Standard CPICH Power Setting (CPICH Power/Total Power  >%15)", "maxpwr > maxtxpower  (power mismatch between nodeb &rnc)", "maxpwr < maxtxpower (power mismatch between nodeb &rnc)"])
        if selected_page_3 == 'Non-Standard CPICH Power Setting (CPICH Power/ Total Power <%5)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("Non-Standard CPICH Power Setting (CPICH Power/ Total Power <%5)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 3G cells whose CPICH power is less than 5% of the total power"
                        "</p>", unsafe_allow_html=True)

                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-48'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='Non-Standard CPICH Power Setting (CPICH Power/ Total Power <%5).csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'Non-Standard CPICH Power Setting (CPICH Power/Total Power  >%15)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("Non-Standard CPICH Power Setting (CPICH Power/Total Power  >%15)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 3G cells whose CPICH power is more than 15% of the total power"
                        "</p>", unsafe_allow_html=True)

                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-49'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='Non-Standard CPICH Power Setting (CPICH Power/Total Power  >%15).csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'maxpwr > maxtxpower  (power mismatch between nodeb &rnc)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("maxpwr > maxtxpower  (power mismatch between nodeb &rnc)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                        "</p>", unsafe_allow_html=True)

                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-50'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='maxpwr > maxtxpower  (power mismatch between nodeb &rnc).csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'maxpwr < maxtxpower (power mismatch between nodeb &rnc)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("maxpwr < maxtxpower (power mismatch between nodeb &rnc)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                        "</p>", unsafe_allow_html=True)

                st.title("There is no case")
    elif selected_page_2 == '64QAM Switch Check':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2 :
            st.title("64QAM Switch Check")
            st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows cells that do not have 256 QAM switches turned on."
                        "</p>", unsafe_allow_html=True)
            st.title("RESULTS")
            df = pd.read_sql("""select * from 'ITEM-53'""", con=conn)
            df.drop('index', inplace=True, axis=1)
            st.dataframe(df)
            csv = convert_df(df)
            st.download_button(
                 label="Download data as CSV",
                 data=csv,
                 file_name='64QAM Switch Check.csv',
                 mime='text/csv',
             )
    elif selected_page_2 == 'External Definitions Check':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2 :
            selected_page_3 = st.selectbox("Which discrepancy would you like to go to", options=["External Definitions Check (BSIC/BCCH) - (3G to 2G)","External Definitions Check (LAC/PSC/DLUARFCN) - (3G to 3G)","External Definitions Check (PCI/TAC/DLEARFCN) - (3G to 4G)","External Definition Check (Redundant Cells) -  (3G to 3G)","External Definition Check (Redundant Cells) -  (3G to 4G)","External Definition Check (Redundant Cells) -  (3G to 2G)"])
        if selected_page_3 == 'External Definitions Check (BSIC/BCCH) - (3G to 2G)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("External Definitions Check (BSIC/BCCH) - (3G to 2G)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-54'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='External Definitions Check (BSIC/BCCH) - (3G to 2G).csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'External Definitions Check (LAC/PSC/DLUARFCN) - (3G to 3G)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("External Definitions Check (LAC/PSC/DLUARFCN) - (3G to 3G)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-55'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='External Definitions Check (LAC/PSC/DLUARFCN) - (3G to 3G).csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'External Definitions Check (PCI/TAC/DLEARFCN) - (3G to 4G)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("External Definitions Check (PCI/TAC/DLEARFCN) - (3G to 4G)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-56'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='External Definitions Check (PCI/TAC/DLEARFCN) - (3G to 4G).csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'External Definition Check (Redundant Cells) -  (3G to 3G)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("External Definition Check (Redundant Cells) -  (3G to 3G)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-57'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='External Definition Check (Redundant Cells) -  (3G to 3G).csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'External Definition Check (Redundant Cells) -  (3G to 4G)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("External Definition Check (Redundant Cells) -  (3G to 4G)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-58'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='External Definition Check (Redundant Cells) -  (3G to 4G).csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'External Definition Check (Redundant Cells) -  (3G to 2G)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("External Definition Check (Redundant Cells) -  (3G to 2G)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-59'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='External Definition Check (Redundant Cells) -  (3G to 2G).csv',
                     mime='text/csv',
                 )
    elif selected_page_2 == 'Radio Data Consistency':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2 :
            st.title("Check Consistency of LOCELL")
            st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows cells that do not have 256 QAM switches turned on."
                        "</p>", unsafe_allow_html=True)
            st.title("RESULTS")
            df = pd.read_sql("""select * from 'ITEM-60'""", con=conn)
            df.drop('index', inplace=True, axis=1)
            st.dataframe(df)
            csv = convert_df(df)
            st.download_button(
                 label="Download data as CSV",
                 data=csv,
                 file_name='Check Consistency of LOCELL.csv',
                 mime='text/csv',
             )
elif selected_page == '2G':
    st.sidebar.title("Category")
    selected_page_2 = st.sidebar.radio("Which discrepancy would you like to go to", options=["2G Summary", "BSIC-BCCH Inconsistency", "Neighbor Relation Discrepancies", "Power Inconsistency", "Cell Frequency not in MA and BA list", "External Definition Check"])
    if selected_page_2 == '2G Summary':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2 :
            image = Image.open("summary_2g_v2.png")
            st.image(image,use_column_width=True)
    elif selected_page_2 == 'BSIC-BCCH Inconsistency':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2 :
            selected_page_3 = st.selectbox("Which discrepancy would you like to go to", options=["Same BCCH Pairs Within 2 km", "Same BSIC-BCCH Pairs within 5 km"])
        if selected_page_3 == 'Same BCCH Pairs Within 2 km' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("Same BCCH Pairs Within 2 km")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 2G cell pairs that have the same BCCH value within a 2 km distance"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/Same BCCH Pairs Within 2 km.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-61'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='Same BCCH Pairs Within 2 km.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'Same BSIC-BCCH Pairs within 5 km' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("Same BSIC-BCCH Pairs within 5 km")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 2G cell pairs that have the same BCCH-BSIC value pair within a 5 km distance"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/Same BSIC-BCCH Pairs within 5 km.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-62'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='Same BSIC-BCCH Pairs within 5 km.csv',
                     mime='text/csv',
                 )
    elif selected_page_2 == 'Neighbor Relation Discrepancies':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2 :
            selected_page_3 = st.selectbox("Which discrepancy would you like to go to", options=["Missing Co-Site IntraBand 2G Neighbours","2G Cells without neighbours","2G Cells without any incoming neighbours","Same BCCH in Source and Neighbors","Same BCCH-BSIC in Source and Neighbors","Same BCCH-BSIC Pairs in source Cells' Neighbours","2G-LTE CoSite Missing Neighbor Relations","2G-3G CoSite Missing Neighbor Relations","2G-2G CoSite Missing Neighbor Relations","2G-2G unidirectional neighboring relationship check in GSM","2G-3G unidirectional neighboring relationship check in GSM","2G-LTE unidirectional neighboring relationship check in GSM"])
        if selected_page_3 == 'Missing Co-Site IntraBand 2G Neighbours' :
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.title("Missing Co-Site IntraBand 2G Neighbours")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows missing neighbor relationships between 2G cells that are part of the same site and have the same ARFCN value"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/Missing Co-Site IntraBand 2G Neighbours.png")
                st.image(image,use_column_width=True)
                st.title("There is no case")
        elif selected_page_3 == '2G Cells without neighbours' :
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.title("2G Cells without neighbours")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 2G Cells that do not have any neighbor cells/relationships"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/2G Cells without neighbours.png")
                st.image(image,use_column_width=True)
                st.title("There is no case")
        elif selected_page_3 == '2G Cells without any incoming neighbours' :
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.title("2G Cells without any incoming neighbour")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 2G Cells that do not have any incoming neighboring relationships. Incoming indicates a handover from another cell to the mentioned cell."
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/2G Cells without any incoming neighbour.png")
                st.image(image,use_column_width=True)
                st.title("There is no case")
        elif selected_page_3 == 'Same BCCH in Source and Neighbors' :
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.title("Same BCCH in Source and Neighbors")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/Same BCCH in Source and Neighbors.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-66'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='Same BCCH in Source and Neighbors.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == "Same BCCH-BSIC Pairs in source Cells' Neighbours" :
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.title("Same BCCH-BSIC Pairs in source Cells' Neighbours")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "BCCH and BSIC pair together can cause co BCCH/BSIC clash and Ghost RACH but independently two same BSIC’s do not harm the network. Same BCCH causes interference with the same BSIC the system cannot recognize which cell it is."
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/Same BCCH-BSIC Pairs in source Cells' Neighbours.png")
                st.image(image,use_column_width=True)
                st.title("There is no case")
        elif selected_page_3 == '2G-LTE CoSite Missing Neighbor Relations' :
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.title("2G-LTE CoSite Missing Neighbor Relations")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows missing neighbor relationships from a 2G cell to a LTE cell that are both present in the same site"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/2G-LTE CoSite Missing Neighbor Relations.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-69'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='2G-LTE CoSite Missing Neighbor Relations.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '2G-3G CoSite Missing Neighbor Relations' :
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.title("2G-3G CoSite Missing Neighbor Relations")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows missing neighbor relationships from a 2G cell to another 3G cell that are both present in the same site"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/2G-3G CoSite Missing Neighbor Relations.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-70'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='2G-3G CoSite Missing Neighbor Relations.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '2G-2G CoSite Missing Neighbor Relations' :
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.title("2G-2G CoSite Missing Neighbor Relations")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows missing neighbor relationships from a 2G cell to a 2G cell that are both present in the same site"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/2G-2G CoSite Missing Neighbor Relations.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-71'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='2G-2G CoSite Missing Neighbor Relations.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '2G-2G unidirectional neighboring relationship check in GSM' :
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.title("2G-2G unidirectional neighboring relationship check in GSM")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "Check and modify the GSM unidirectional neighboring cells. If cell A is a neighboring cell of cell B but cell B is not a neighboring cell of cell A, cell A is the unidirectional neighboring cell of cell B. MSs can be handed over only from cell B to cell A but not from cell A to cell B. Too many abnormal unidirectional neighboring cells deteriorate MS handover quality."
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/2G-2G unidirectional neighboring relationship check in GSM.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-72'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='2G-2G unidirectional neighboring relationship check in GSM.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '2G-3G unidirectional neighboring relationship check in GSM' :
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.title("2G-3G unidirectional neighboring relationship check in GSM")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 3G-2G cell pairs where a handover from 3G to 2G is defined but not vice versa."
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/2G-3G unidirectional neighboring relationship check in GSM.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-73'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='2G-3G unidirectional neighboring relationship check in GSM.csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == '2G-LTE unidirectional neighboring relationship check in GSM' :
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.title("2G-LTE unidirectional neighboring relationship check in GSM")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "This item shows 4G-2G cell pairs where a handover from LTE to 2G is defined but not vice versa."
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/2G-LTE unidirectional neighboring relationship check in GSM.png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-74'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='2G-LTE unidirectional neighboring relationship check in GSM.csv',
                     mime='text/csv',
                 )
    elif selected_page_2 == 'Power Inconsistency':
        col1, col2, col3 = st.columns([1, 5, 1])
        with col2:
            st.title("Check GSMCELL Trx Power Consistency")
            st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                    "Check whether the transmit power on the top of a cabinet is consistent between all TRXs within a cell. The call completion rate of MSs is reduced and power is wasted when the transmit power on the top of a cabinet is inconsistent between the BCCH TRX and TCH TRX."
                    "</p>", unsafe_allow_html=True)
            image = Image.open("item_png/Check GSMCELL Trx Power Consistency.png")
            st.image(image,use_column_width=True)
            st.title("RESULTS")
            df = pd.read_sql("""select * from 'ITEM-75'""", con=conn)
            df.drop('index', inplace=True, axis=1)
            st.dataframe(df)
            csv = convert_df(df)
            st.download_button(
                 label="Download data as CSV",
                 data=csv,
                 file_name='Check GSMCELL Trx Power Consistency.csv',
                 mime='text/csv',
             )
    elif selected_page_2 == 'Cell Frequency not in MA list':
        col1, col2, col3 = st.columns([1, 5, 1])
        with col2:
            st.title("Cell Frequency not in MA list")
            st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                    "Check whether the frequencies of a cell exist in the MA group. The frequencies that do not exist in the MA group are wasted."
                    "</p>", unsafe_allow_html=True)
            st.title("RESULTS")
            df = pd.read_sql("""select * from 'ITEM-28'""", con=conn)
            df.drop('index', inplace=True, axis=1)
            st.dataframe(df)
            csv = convert_df(df)
            st.download_button(
                 label="Download data as CSV",
                 data=csv,
                 file_name='Cell Frequency not in MA list.csv',
                 mime='text/csv',)
    elif selected_page_2 == 'Cell Frequency not in BA list':
        col1, col2, col3 = st.columns([1, 5, 1])
        with col2:
            st.title("Cell Frequency not in BA list")
            st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                    "Check whether the BCCH frequency of a cell exists in the BA table. If the BCCH frequency of a cell does not exist in the BA table, MSs cannot be handed over to the cell"
                    "</p>", unsafe_allow_html=True)
            st.title("There is no case")
    elif selected_page_2 == 'External Definition Check':
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2 :
            selected_page_3 = st.selectbox("Which discrepancy would you like to go to", options=["External Definitions Check (BSIC/BCCH) - (2G to 2G)","External Definitions Check (LAC/PSC/DLUARFCN) - (2G to 3G)","External Definitions Check (PCI/TAC/DLEARFCN) - (2G to 4G)","External Definition Check (Redundant Cells) -  (2G to 2G)","External Definition Check (Redundant Cells) -  (2G to 4G)","External Definition Check (Redundant Cells) -  (2G to 3G)"])
        if selected_page_3 == 'External Definitions Check (BSIC/BCCH) - (2G to 2G)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("External Definitions Check (BSIC/BCCH) - (2G to 2G)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "Check parameter consistency between an LTE source cell on an external M2000 and an LTE external cell on the local M2000. The cells are identified by Cell Name (CELLNAME). The parameters to be checked are as follows: MCC, MNC, CI, Cell TAC (TAC), EARFCN (FREQ), Physical Cell ID (PCID), and EUTRAN Cell Type (EUTRANTYPE)."
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/External Definitions Check (BSIC/BCCH) - (2G to 2G).png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-28'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='External Definitions Check (BSIC/BCCH) - (2G to 2G).csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'External Definitions Check (LAC/PSC/DLUARFCN) - (2G to 3G)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("External Definitions Check (LAC/PSC/DLUARFCN) - (2G to 3G)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/External Definitions Check (LAC/PSC/DLUARFCN) - (2G to 3G).png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-28'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='External Definitions Check (LAC/PSC/DLUARFCN) - (2G to 3G).csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'External Definitions Check (PCI/TAC/DLEARFCN) - (2G to 4G)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("External Definitions Check (PCI/TAC/DLEARFCN) - (2G to 4G)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/External Definitions Check (PCI/TAC/DLEARFCN) - (2G to 4G).png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-28'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='External Definitions Check (PCI/TAC/DLEARFCN) - (2G to 4G).csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'External Definition Check (Redundant Cells) -  (2G to 2G)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("External Definition Check (Redundant Cells) -  (2G to 2G)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/External Definition Check (Redundant Cells) -  (2G to 2G).png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-28'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='External Definition Check (Redundant Cells) -  (2G to 2G).csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'External Definition Check (Redundant Cells) -  (2G to 4G)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("External Definition Check (Redundant Cells) -  (2G to 4G)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/External Definition Check (Redundant Cells) -  (2G to 4G).png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-28'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='External Definition Check (Redundant Cells) -  (2G to 4G).csv',
                     mime='text/csv',
                 )
        elif selected_page_3 == 'External Definition Check (Redundant Cells) -  (2G to 3G)' :
            col1, col2, col3 = st.columns([1, 5, 1])
            with col2:
                st.title("External Definition Check (Redundant Cells) -  (2G to 3G)")
                st.markdown("<p style='text-align: center; color: black; font-size:25px'>"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
                        "</p>", unsafe_allow_html=True)
                image = Image.open("item_png/External Definition Check (Redundant Cells) -  (2G to 3G).png")
                st.image(image,use_column_width=True)
                st.title("RESULTS")
                df = pd.read_sql("""select * from 'ITEM-28'""", con=conn)
                df.drop('index', inplace=True, axis=1)
                st.dataframe(df)
                csv = convert_df(df)
                st.download_button(
                     label="Download data as CSV",
                     data=csv,
                     file_name='External Definition Check (Redundant Cells) -  (2G to 3G).csv',
                     mime='text/csv',
                 )


#summary_table_2g.png
#os.system(os.system("streamlit run C:/Users/hasan.acar/PycharmProjects/Discrepancy_check_streamlit/main.py"))
#exit("main.py")

