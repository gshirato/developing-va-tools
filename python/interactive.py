import marimo

__generated_with = "0.6.17"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    return mo, pd


@app.cell
def __(pd):
    df = pd.read_csv('../data/processed/tracking_1.csv')
    return df,


@app.cell
def __(df):
    df
    return


@app.cell
def __(df):
    df_short = df[(df['frame_id'] > 50) & (df['frame_id'] < 250)]
    return df_short,


@app.cell
def __(mo):
    mo.md("## Animation")
    return


@app.cell
def __(df_short):
    import plotly.express as px

    fig = px.scatter(df_short, x='x', y='y', color='team', animation_frame='frame_id', range_x=[0, 1], range_y=[0, 1])
    fig
    return fig, px


@app.cell
def __(mo):
    mo.md('## Interactive')
    return


@app.cell
def __(mo):
    frame = mo.ui.slider(50, 2500)
    return frame,


@app.cell
def __(frame, mo):
    mo.md(
        f"""
        [frame]: {frame} ({frame.value})
        """
    )
    return


@app.cell
def __(px, snapshot):
    snap_fig = px.scatter(snapshot, x='x', y='y', color='team', range_x=[0, 1], range_y=[0, 1])
    snap_fig
    return snap_fig,


@app.cell
def __(df, frame):
    snapshot = df[df['frame_id'] == frame.value]
    return snapshot,


@app.cell
def __(mo):
    mo.md('## Preprocessing')
    return


@app.cell
def __(mo, snapshot):
    mo.ui.dataframe(snapshot)
    return


@app.cell
def __(mo, snapshot):
    mo.ui.data_explorer(snapshot)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
