import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carga el archivo CSV "database_titanic.csv" en un DataFrame de pandas.
df = pd.read_csv("top 100 streamed_songs.csv")

#Titulo
st.title("Mejores 100 canciones de spotify")
#descripcion
st.write("Explora los mejores temas")


# Mostrar los enlaces en formato interactivo usando st.markdown
st.subheader("Canciones y Enlaces a Spotify")
for i in range(len(df)):
    song = df['name'].iloc[i]
    link = df['spotify_url'].iloc[i]
    # Mostrar cada canción como un enlace clickeable
    st.markdown(f"[{song}]({link})")







# Mostrar una breve descripción de los datos
st.subheader("Descripción de los Datos")
st.write("Este conjunto de datos contiene información sobre las canciones más populares en Spotify. Algunas de las columnas incluyen:")
st.write(df.columns)









# Gráfico interactivo de las canciones más populares por artista
st.subheader("Canciones Más Populares por Artista")
artist_counts = df['artist'].value_counts().head(10)
st.bar_chart(artist_counts)

# Filtro de géneros
st.subheader("Filtrar por Género")
genre_filter = st.selectbox("Selecciona un género:", df['genre'].unique())
filtered_df = df[df['genre'] == genre_filter]
st.write(f"Mostrando canciones del género: {genre_filter}")
st.write(filtered_df)

# Gráfico de las canciones más populares por género
st.subheader(f"Top Canciones del Género {genre_filter}")
top_songs_by_genre = filtered_df['song'].value_counts().head(10)
st.bar_chart(top_songs_by_genre)

# Histograma de las "Streams" (número de reproducciones)
st.subheader("Distribución de Reproducciones (Streams)")
plt.figure(figsize=(10, 6))
plt.hist(df['streams'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribución de Reproducciones')
plt.xlabel('Reproducciones')
plt.ylabel('Frecuencia')
st.pyplot(plt)

# Opción para mostrar detalles de una canción seleccionada
st.subheader("Detalles de una Canción")
song_title = st.selectbox("Selecciona una canción:", df['song'].unique())
song_details = df[df['song'] == song_title].iloc[0]
st.write(f"**Título:** {song_details['song']}")
st.write(f"**Artista:** {song_details['artist']}")
st.write(f"**Género:** {song_details['genre']}")
st.write(f"**Reproducciones:** {song_details['streams']}")
st.write(f"**Fecha de lanzamiento:** {song_details['release_date']}")


