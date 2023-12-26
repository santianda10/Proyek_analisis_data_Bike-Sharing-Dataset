import streamlit as st
st.title("Submission Proyek Analisis Data")
# Import Library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
import seaborn as sns
sns.set()
# Memuat tabel penyewaan sepeda per hari
day_df = pd.read_csv('day.csv')
# Memuat tabel penyewaan sepeda per jam
hour_df = pd.read_csv('hour.csv')


# Menyiapkan DataFrame
datetime_columns =["dteday", "dteday"]
day_df.sort_values(by="dteday", inplace=True)
day_df.reset_index(inplace=True)
for column in datetime_columns:
    day_df[column] = pd.to_datetime(day_df[column])



# Membuat komponen Filter
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image('https://www.rodalink.com/pub/media/wysiwyg/landing_page_id/2023/des/id_dewa_sepedabanner.jpg')

    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu Data Penyewa Sepeda Harian', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )


    main_df = day_df[(day_df["dteday"] >= str(start_date))&
                     (day_df["dteday"] <= str(end_date))]





st.subheader('Penyewa sepeda harian')
col1, col2,col3 = st.columns(3)

with col1:
    total_casual = day_df.casual.sum()
    st.metric("Total Casual", value=total_casual)

with col2:
    total_registered = day_df.registered.sum()
    st.metric("Total registered", value=total_registered)
with col3:
    total_cnt = day_df.cnt.sum()
    st.metric("Total cnt", value=total_cnt)

st.subheader('Membuat time series plot  untuk melihat performa jumlah penyewa sepeda tahun 2011 ~ 2012')
# Membuat time series plot  untuk melihat performa jumlah penyewa sepeda
plt.figure(figsize=(12,6))
fig, ax = plt.subplots(figsize=(12, 6))
ax=plt.plot(day_df['dteday'], day_df['cnt'], marker='o', linestyle='-', color='green')
plt.title('Visualisasi jumlah penyewa sepeda per hari dari tahun 2011 (0) ~ 2012(1)')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Penyewaan Sepeda Harian')
st.pyplot(fig)

plt.figure(figsize=(12,6))
fig2, ax = plt.subplots(figsize=(12, 6))
plt.title('Visualisasi jumlah penyewa sepeda per hari menggunakan barplot dari tahun 2011 (0) ~ 2012(1)')
ax=sns.barplot(x='yr', y='cnt',data=day_df)
st.pyplot(fig2)
st.write(
    """
    Permintaan penyewaan sepeda meningkat dari tahun 2011 (0) ke 2012 (1)
    """
)

st.subheader('Melihat korelasi antar parameter')
plt.figure(figsize=(12,6))
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 6))
ax = day_new = day_df[['temp','atemp','hum','windspeed','casual', 'registered','cnt']]
ax = sns.heatmap(day_new.corr(), annot=True, cmap='Greens', linewidths=1)
st.pyplot(fig)
st.write(
    """
    Dapat dilihat bahwa jika nilai parameter mendekati 1 atau sama dengan satu maka parameter saling berkorelasi positif, jika nilai parameter sama dengan nol maka parameter tidak saling berkorelasi, dan jika mendekali -1 atau sama dengan -1 maka parameter saling berkorelasi negatif.

    """
)
st.subheader('Memvisualisasikan parameter-parameter terhadap jumlah pesanan sewa sepeda')


plt.figure(figsize=(12,6))
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
plt.subplot(1,2,1)
plt.title("Hubungan Season terhadap cnt")
ax = sns.barplot(x='season',y='cnt', data=day_df,palette='Paired')
ax.bar_label(ax.containers[0], fmt= '%0.1f', label_type='center' )
plt.subplot(1,2,2)
plt.title("Hubungan Season terhadap cnt, dengan hue yaitu yr")
ax = sns.barplot(x='season',y='cnt', hue='yr', data=day_df,palette='Paired')
st.pyplot(fig)
st.write(
    """
    Pivot di atas 32% dari pemesanan sepeda terjadi pada musim gugur (3) dengan rata-rata lebih dari 5.644,3 pemesanan (selama dua tahun). Diikuti oleh Musim Panas (2) & Musim Dingin (4) dengan 27% & 25% dari total pemesanan. Hal ini menunjukkan bahwa musim dapat digunakan untuk memprediksi jumlah penyewa sepeda lebih lanjut.
    """
)

plt.figure(figsize=(36,12))
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
plt.subplot(1,2,1)
plt.title("Hubungan mnth terhadap cnt")
ax = sns.barplot(x='mnth',y='cnt', data=day_df,palette='Paired')
ax.bar_label(ax.containers[0], fmt= '%0.1f', label_type='center' )
plt.subplot(1,2,2)
plt.title("Hubungan mnth terhadap cnt, dengan hue yaitu yr")
ax = sns.barplot(x='mnth',y='cnt', hue='yr', data=day_df,palette='Paired')
st.pyplot(fig)
st.write(
    """
Pivot di atas menunjukkan cukup bervariasi jumlah pemesanan sewa sepeda dengan rata-rata tertinggi jumlah sewa sepeda pada bulan 6 yaitu 5772,4 unit dan terendah pada bulan ke -1 yaitu 2176,3 unit. Hal ini menujukkan bahwa parameter bulan memiliki tren dan dapat digunakan untuk memprediksi jumlah penyewa sepeda lebih lanjut.
    """
)


plt.figure(figsize=(36,12))
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
plt.subplot(1,2,1)
plt.title("Hubungan weathersit terhadap cnt")
ax = sns.barplot(x='weathersit',y='cnt', data=day_df,palette='Paired')
ax.bar_label(ax.containers[0], fmt= '%0.1f', label_type='center' )
plt.subplot(1,2,2)
plt.title("Hubungan weathersit terhadap cnt, dengan hue yaitu yr")
ax = sns.barplot(x='weathersit',y='cnt', hue='yr', data=day_df,palette='Paired')
st.pyplot(fig)
st.write(
    """
Pivot di atas 46% dari pemesanan sepeda terjadi saat cuaca cerah dengan rata-rata hampir 4876.8 pemesanan (selama dua tahun). Hal ini diikuti oleh cuaca Berawan dengan 37% dari total pemesanan. Hal ini menunjukkan bahwa cuaca memiliki tren dan dapat digunakan untuk memprediksi jumlah penyewa sepeda lebih lanjut.   
    """
)


plt.figure(figsize=(36,12))
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
plt.subplot(1,2,1)
plt.title("Hubungan weekday terhadap cnt")
ax = sns.barplot(x='weekday',y='cnt', data=day_df,palette='Paired')
ax.bar_label(ax.containers[0], fmt= '%0.1f', label_type='center' )
plt.subplot(1,2,2)
plt.title("Hubungan weekday terhadap cnt, dengan hue yaitu yr")
ax = sns.barplot(x='weekday',y='cnt', hue='yr', data=day_df,palette='Paired')
st.pyplot(fig)
st.write(
    """
Pivot di atas  menunjukkan tren yang sangat dekat antara hari ke 0 ~ hari ke 6 dan variabel ini dapat memiliki sedikit atau tidak memiliki pengaruh terhadap jumlah pemesanan sepeda untuk disewa, sehingga diperlukan analisis lebih lanjut apakah variabel ini diperlukan untuk membuat model dalam meningkatkan pesanan jumlah penyewa sepeda.
    """
)


plt.figure(figsize=(36,12))
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
plt.subplot(1,2,1)
plt.title("Hubungan holiday terhadap cnt")
ax = sns.barplot(x='holiday',y='cnt', data=day_df,palette='Paired')
ax.bar_label(ax.containers[0], fmt= '%0.1f', label_type='center' )
plt.subplot(1,2,2)
plt.title("Hubungan holiday terhadap cnt, dengan hue yaitu yr")
ax = sns.barplot(x='holiday',y='cnt', hue='yr', data=day_df,palette='Paired')
st.pyplot(fig)
st.write(
    """
Pivot diatas 55% dari penyewaan sepeda terjadi selama bukan hari liburan (0) yaitu rata-rata sebanyak 4527.1 pemesanan. Hal ini menunjukkan bahwa bukan hari libur memiliki tren dan dapat dipertimbangan digunakan untuk memprediksi jumlah penyewa sepeda lebih lanjut.
   """
)



plt.figure(figsize=(36,12))
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
plt.subplot(1,2,1)
plt.title("Hubungan workingday terhadap cnt")
ax = sns.barplot(x='workingday',y='cnt', data=day_df,palette='Paired')
ax.bar_label(ax.containers[0], fmt= '%0.1f', label_type='center' )
plt.subplot(1,2,2)
plt.title("Hubungan workingday terhadap cnt, dengan hue yaitu yr")
ax = sns.barplot(x='workingday',y='cnt', hue='yr', data=day_df,palette='Paired')
st.pyplot(fig)
st.write(
    """
Pivot di atas 51% dari pemesanan sepeda terjadi pada 'hari kerja' dengan rata-rata 4584.8 pemesanan (selama dua tahun). Hal ini menunjukkan bahwa hari kerja memiliki tren dan dapat dipertimbangan digunakan untuk memprediksi jumlah penyewa sepeda lebih lanjut.
   """
)