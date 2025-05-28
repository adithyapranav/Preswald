from preswald import connect, get_df, text, table, plotly
import plotly.express as px
import pandas as pd

connect()
players_df = get_df("data/players.csv")
games_df = get_df("data/games.csv")

text("# AFL Insights Dashboard")
text("## Player Physical Profile")

fig_hw = px.scatter(
    players_df,
    x="Height",
    y="Weight",
    color="Position",
    hover_name="DisplayName",
    title="Player Height vs Weight by Position"
)
plotly(fig_hw)

text("## Player Origins Breakdown")

origin_counts = players_df["Origin"].value_counts().reset_index()
origin_counts.columns = ["Origin", "Count"]
fig_origin = px.bar(origin_counts, x="Origin", y="Count", title="Player Origin Counts")
plotly(fig_origin)

text("## Match Attendance Trends")

fig_attendance = px.line(
    games_df.sort_values("Date"),
    x="Date",
    y="Attendance",
    color="Venue",
    title="Match Attendance Over Time by Venue"
)
plotly(fig_attendance)

text("## Does Weather Affect Attendance?")

fig_temp_attend = px.scatter(
    games_df,
    x="MaxTemp",
    y="Attendance",
    color="Year",
    hover_name="HomeTeam",
    title="Max Temperature vs Attendance"
)
plotly(fig_temp_attend)

text("## Final Score Comparison: Home vs Away")

fig_score_comp = px.scatter(
    games_df,
    x="HomeTeamScore",
    y="AwayTeamScore",
    hover_data=["HomeTeam", "AwayTeam", "Date"],
    color="Venue",
    title="Home vs Away Team Final Scores"
)
plotly(fig_score_comp)