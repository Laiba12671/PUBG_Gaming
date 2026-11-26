
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("PUBG Gaming Dashboard")

df = pd.read_csv("PUBG.csv")

st.write("Dataset Preview")
st.dataframe(df.head())

st.subheader("Player Statistics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Players", len(df))
col2.metric("Average Kills", round(df["Kills"].mean(), 2))
col3.metric("Average Damage", round(df["Damage_Dealt"].mean(), 2))

st.subheader("PUBG Graphs")

questions = [
    ("Top 10 Players", "Kills"),
    ("Player Damage", "Damage_Dealt"),
    ("Survival Time", "Survival_Time_Minutes")
]

for title, column in questions:
    st.write(title)
    fig, ax = plt.subplots()
    sns.histplot(df[column], ax=ax)
    st.pyplot(fig)
    plt.close(fig)

st.subheader("Conclusion")
st.write("This project analyzes PUBG player performance using data and graphs.")
