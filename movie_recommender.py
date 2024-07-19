import streamlit as st
import  pickle

df = pickle.load(open("mov.pkl","rb"))
sim = pickle.load(open("simi.pkl","rb"))

st.sidebar.header(":rainbow[Movie Recommender System]",divider='grey')
# def poster(name):

def recommend(movie):
    m_index = df[df["Series_Title"] == movie].index[0]
    dist = sim[m_index]
    m_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:8]
    recommended_m = []
    for i in m_list:
        movie_id = i[0]
        recommended_m.append(df["Series_Title"][i[0]])
    return recommended_m
def poster(movie):
    m_index = df[df["Series_Title"] == movie].index[0]
    dist = sim[m_index]
    m_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:8]
    l1 = []
    for i in m_list:
        movie_id = i[0]
        l1.append(df["Poster_Link"][i[0]])
    return l1

sel = st.sidebar.selectbox("Select Movie",df["Series_Title"].unique())

if st.sidebar.button("Play Now"):
    st.subheader(":rainbow[More Like This: ]",divider="grey")

    rec= recommend(sel)
    pos = poster(sel)

    col1,col2,col3= st.columns(3)
    with col1:
        st.write(rec[0])
        st.image(pos[0])
    with col2:
        st.write(rec[1])
        st.image(pos[1])
    with col3:
        st.write(rec[2])
        st.image(pos[2])
    col4,col5,col6 = st.columns(3)
    with col4:
        st.write(rec[3])
        st.image(pos[3])
    with col5:
        st.write(rec[4])
        st.image(pos[4])
    with col6:
        st.write(rec[5])
        st.image(pos[5])


    st.sidebar.subheader(sel)
    j =df[df["Series_Title"] == sel]
    a = (j.iloc[0][2])
    st.sidebar.image(a)
