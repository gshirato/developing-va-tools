import marimo

__generated_with = "0.6.17"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __():
    import pandas as pd
    return pd,


@app.cell
def __():
    from kloppy import metrica
    return metrica,


@app.cell
def __(metrica):
    dataset = metrica.load_tracking_csv(
        home_data="../data/raw/Sample_Game_2_RawTrackingData_Home_Team.csv",
        away_data="../data/raw/Sample_Game_2_RawTrackingData_Away_Team.csv",
    )
    return dataset,


@app.cell
def __(dataset):
    dataset.to_df().head()
    return


@app.cell
def __(dataset):
    df = dataset.to_df()
    return df,


@app.cell
def __(df):
    first = df[df['period_id'] == 1]
    second = df[df['period_id'] == 2]
    return first, second


@app.cell
def __(first, second):
    first.to_csv('../data/processed/Sample_Game_2_RawTrackingData_1st.csv', index=False)
    second.to_csv('../data/processed/Sample_Game_2_RawTrackingData_2nd.csv', index=False)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
