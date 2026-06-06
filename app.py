import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("IPL_Matches_2008_2022.csv")

st.title("🏏 IPL Data Storytelling App")
st.header("Introduction")

st.write("""
The Indian Premier League (IPL) is one of the most popular cricket leagues in the world.

In this project, we analyze IPL matches from 2008 to 2022 to understand team performance, player achievements, and tournament growth.
""")
st.header("Dataset Overview")

st.dataframe(df.head())

st.write("Dataset Shape:")
st.write(df.shape)
st.header("Exploratory Data Analysis")
st.write("Missing Values")

st.write(df.isnull().sum())
st.write("Statistical Summary")

st.write(df.describe())
st.header("Story 1: Growth of IPL")
season_count = df['Season'].value_counts().sort_index()

fig1 = px.bar(
    x=season_count.index,
    y=season_count.values,
    title="Matches Played Per Season"
)

st.plotly_chart(fig1)
st.write("""
Insight:

The number of matches generally increased over the years, showing IPL's expansion and popularity.
""")
st.header("Story 2: Most Successful Teams")
wins = df['WinningTeam'].value_counts().head(10)

fig2 = px.bar(
    x=wins.index,
    y=wins.values,
    title="Top Winning Teams"
)

st.plotly_chart(fig2)
st.write("""
Insight:

A few teams consistently won more matches and became the most successful IPL franchises.
""")
st.header("Story 3: Popular IPL Venues")
venues = df['Venue'].value_counts().head(10)

fig3 = px.bar(
    x=venues.index,
    y=venues.values,
    title="Top Match Venues"
)

st.plotly_chart(fig3)
st.write("""
Insight:

Certain stadiums host a large number of IPL matches compared to others.
""")
st.header("Story 4: Star Performers")
players = df['Player_of_Match'].value_counts().head(10)

fig4 = px.bar(
    x=players.index,
    y=players.values,
    title="Top Player of the Match Winners"
)

st.plotly_chart(fig4)
st.write("""
Insight:

Some players consistently delivered match-winning performances.
""")
st.header("Key Findings")

st.write("""
1. IPL expanded significantly from 2008 to 2022.

2. A few teams dominated the league.

3. Some venues hosted more matches than others.

4. A small group of players earned most Player of the Match awards.

5. IPL continues to grow in popularity.
""")
st.header("Conclusion & Recommendations")

st.write("""
Conclusion:

IPL has become one of the world's most successful cricket leagues.

Recommendations:

• Teams should use data-driven strategies.

• Venue-specific planning can improve performance.

• Consistent player development is important for success.
""")