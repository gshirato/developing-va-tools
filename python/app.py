import pandas as pd
import streamlit as st
import plotly.express as px

st.title('Visual Analytics demo')

tab_data, tab_vis, tab_animation = st.tabs(['Data', 'Snapshot', 'Animation'])

df = pd.read_csv('../data/processed/tracking_1.csv')
df_short = df[(df['frame_id'] > 50) & (df['frame_id'] < 250)]

fig = px.scatter(df_short, x='x', y='y', color='team', animation_frame='frame_id', range_x=[0, 1], range_y=[0, 1])
with tab_data:
    st.write(df)




with tab_vis:
    frame = st.slider('Frame', 50, 2500, 400)
    snapshot = df[df['frame_id'] == frame]
    snap_fig = px.scatter(snapshot, x='x', y='y', color='team', range_x=[0, 1], range_y=[0, 1])
    st.plotly_chart(snap_fig)



with tab_animation:
    st.plotly_chart(fig)


st.header('More')

st.markdown("https://cheat-sheet.streamlit.app/")