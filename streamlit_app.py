import streamlit as st
import streamlit.web.cli as stcli
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="TheStatsWay Ratings",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title('📊 Player Average Ratings 📊')
st.subheader('Check www.thestatsway.com for articles!', divider="grey")

df = pd.read_csv('24_25AvgRatingData.csv')

st.sidebar.header("🔍 @TheStatsWay", divider="grey")

#Competition Filter

CompFilter = st.selectbox(
    "How would you like to be contacted?",
    ("UEFA Champions League 2024/25", "UEFA Europa League 2024/25", "UEFA Conference League 2024/25",
    "Premier League 2024/25", "La Liga 2024/25", "Serie A 2024/25", "Bundesliga 2024/25",
    "Ligue 1 2024/25", "Liga Portugal 2024/25", "Eredivisie 2024/25"),
)

st.write("You selected:", CompFilter)

#CompFilter = st.sidebar.multiselect(
    #"Competition Filter:",
    #options=df["Competition"].unique(),
    #default="UEFA Champions League 2024/25"
#)

if CompFilter:
    df = df[df["Competition"].isin(CompFilter)]

#Team Filter

TeamFilter = st.sidebar.multiselect(
    "Team Filter:",
    options=df["Team"].unique(),
    default=df["Team"].unique()
)

if TeamFilter:
    df = df[df["Team"].isin(TeamFilter)]

#Age Filter

AgeFilter = st.sidebar.slider(
    "Age Filter:", 
    15, 
    42, 
    (15, 42)
) 

if AgeFilter:
    df = df[df["Age"].between(AgeFilter[0], AgeFilter[1])]

#Position Filter

PositionFilter = st.sidebar.multiselect(
    "Position Filter:",
    options=df["Position"].unique(),
    default=df["Position"].unique(),
)

if PositionFilter:
    df = df[df["Position"].isin(PositionFilter)]

#Minutes Filter

MinutesFilter = st.sidebar.slider(
    "Minutes Filter:", 
    0, 
    3420, 
    (0, 3420)
) 

if MinutesFilter:
    df = df[df["Minutes"].between(MinutesFilter[0], MinutesFilter[1])]

RatingsFilter = st.sidebar.slider(
    "Average Rating Filter:", 
    0, 
    10, 
    (0, 10)
) 

if RatingsFilter:
    df = df[df["Avg.Rating"].between(RatingsFilter[0], RatingsFilter[1])]

GoalsFilter = st.sidebar.slider(
    "Goals Filter:", 
    0, 
    40, 
    (0, 40)
) 

if GoalsFilter:
    df = df[df["Goals"].between(GoalsFilter[0], GoalsFilter[1])]

AssistsFilter = st.sidebar.slider(
    "Assists Filter:", 
    0, 
    40, 
    (0, 40)
) 

if AssistsFilter:
    df = df[df["Assists"].between(AssistsFilter[0], AssistsFilter[1])]

GAFilter = st.sidebar.slider(
    "G+A Filter:", 
    0, 
    80, 
    (0, 80)
) 

if GAFilter:
    df = df[df["Assists"].between(GAFilter[0], GAFilter[1])]

    
st.sidebar.divider()
st.sidebar.write('𝐯𝟏.𝟏.𝟎𝟏')
st.sidebar.write("Last Updated: Nov 01, 2025")
st.sidebar.write("Data from FBref")

#Data Frame display
st.dataframe(df, height = 1000)
