import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(page_title="EDA Data PNS Jabar", layout="wide")
dataset_path = st.secrets.path_configuration.dataset_path
df = pd.read_csv(f"{dataset_path}pns_jabar.csv")
df.drop(["kode_provinsi", "nama_provinsi", "satuan"], axis=1, inplace=True)
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["All", "2015", "2017", "2018", "2019", "2020", "2021", "2022", "2023"])
with tab1:
    st.dataframe(df, hide_index=True, use_container_width=True)
    groupby_tahun = df.groupby("tahun", as_index=False)["jumlah_pns"].sum(numeric_only=True)
    st.line_chart(groupby_tahun, x="tahun", y="jumlah_pns")
    groupby_tahun2 = df.groupby(["jenis_kelamin", "tahun"], as_index=False)["jumlah_pns"].sum(numeric_only=True)
    st.line_chart(groupby_tahun2, x="tahun", y="jumlah_pns", color="jenis_kelamin")
with tab2:
    data = df[df['tahun']==2015]
    st.dataframe(data, hide_index=True, use_container_width=True)
    col_1, col_2 = st.columns([6, 6])
    with col_1:
        groupby_perangkat = data.groupby("perangkat_daerah", as_index=False)["jumlah_pns"].sum(numeric_only=True)
        st.bar_chart(groupby_perangkat, x="perangkat_daerah", y="jumlah_pns")
    with col_2:
        groupby_jkel = data.groupby("jenis_kelamin", as_index=False)["jumlah_pns"].sum(numeric_only=True)
        st.bar_chart(groupby_jkel, x="jenis_kelamin", y="jumlah_pns")
with tab3:
    data = df[df['tahun']==2017]
    st.dataframe(data, hide_index=True, use_container_width=True)
    col_1, col_2 = st.columns([6, 6])
    with col_1:
        groupby_perangkat = data.groupby("perangkat_daerah", as_index=False)["jumlah_pns"].sum(numeric_only=True)
        st.bar_chart(groupby_perangkat, x="perangkat_daerah", y="jumlah_pns")
    with col_2:
        groupby_jkel = data.groupby("jenis_kelamin", as_index=False)["jumlah_pns"].sum(numeric_only=True)
        st.bar_chart(groupby_jkel, x="jenis_kelamin", y="jumlah_pns")
with tab4:
    data = df[df['tahun']==2018]
    st.dataframe(data, hide_index=True, use_container_width=True)
    col_1, col_2 = st.columns([6, 6])
    with col_1:
        groupby_perangkat = data.groupby("perangkat_daerah", as_index=False)["jumlah_pns"].sum(numeric_only=True)
        st.bar_chart(groupby_perangkat, x="perangkat_daerah", y="jumlah_pns")
    with col_2:
        groupby_jkel = data.groupby("jenis_kelamin", as_index=False)["jumlah_pns"].sum(numeric_only=True)
        st.bar_chart(groupby_jkel, x="jenis_kelamin", y="jumlah_pns")
with tab5:
    data = df[df['tahun']==2019]
    st.dataframe(data, hide_index=True, use_container_width=True)
    col_1, col_2 = st.columns([6, 6])
    with col_1:
        groupby_perangkat = data.groupby("perangkat_daerah", as_index=False)["jumlah_pns"].sum(numeric_only=True)
        st.bar_chart(groupby_perangkat, x="perangkat_daerah", y="jumlah_pns")
    with col_2:
        groupby_jkel = data.groupby("jenis_kelamin", as_index=False)["jumlah_pns"].sum(numeric_only=True)
        st.bar_chart(groupby_jkel, x="jenis_kelamin", y="jumlah_pns")
with tab6:
    data = df[df['tahun']==2020]
    st.dataframe(data, hide_index=True, use_container_width=True)
    col_1, col_2 = st.columns([6, 6])
    with col_1:
        groupby_perangkat = data.groupby("perangkat_daerah", as_index=False)["jumlah_pns"].sum(numeric_only=True)
        st.bar_chart(groupby_perangkat, x="perangkat_daerah", y="jumlah_pns")
    with col_2:
        groupby_jkel = data.groupby("jenis_kelamin", as_index=False)["jumlah_pns"].sum(numeric_only=True)
        st.bar_chart(groupby_jkel, x="jenis_kelamin", y="jumlah_pns")
with tab7:
    data = df[df['tahun']==2021]
    st.dataframe(data, hide_index=True, use_container_width=True)
    col_1, col_2 = st.columns([6, 6])
    with col_1:
        groupby_perangkat = data.groupby("perangkat_daerah", as_index=False)["jumlah_pns"].sum(numeric_only=True)
        st.bar_chart(groupby_perangkat, x="perangkat_daerah", y="jumlah_pns")
    with col_2:
        groupby_jkel = data.groupby("jenis_kelamin", as_index=False)["jumlah_pns"].sum(numeric_only=True)
        st.bar_chart(groupby_jkel, x="jenis_kelamin", y="jumlah_pns")
with tab8:
    data = df[df['tahun']==2022]
    st.dataframe(data, hide_index=True, use_container_width=True)
    col_1, col_2 = st.columns([6, 6])
    with col_1:
        groupby_perangkat = data.groupby("perangkat_daerah", as_index=False)["jumlah_pns"].sum(numeric_only=True)
        st.bar_chart(groupby_perangkat, x="perangkat_daerah", y="jumlah_pns")
    with col_2:
        groupby_jkel = data.groupby("jenis_kelamin", as_index=False)["jumlah_pns"].sum(numeric_only=True)
        st.bar_chart(groupby_jkel, x="jenis_kelamin", y="jumlah_pns")
with tab9:
    data = df[df['tahun']==2023]
    st.dataframe(data, hide_index=True, use_container_width=True)
    col_1, col_2 = st.columns([6, 6])
    with col_1:
        groupby_perangkat = data.groupby("perangkat_daerah", as_index=False)["jumlah_pns"].sum(numeric_only=True)
        st.bar_chart(groupby_perangkat, x="perangkat_daerah", y="jumlah_pns")
    with col_2:
        groupby_jkel = data.groupby("jenis_kelamin", as_index=False)["jumlah_pns"].sum(numeric_only=True)
        st.bar_chart(groupby_jkel, x="jenis_kelamin", y="jumlah_pns")