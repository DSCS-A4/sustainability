import pandas as pd


def combine_dfs(df1: pd.DataFrame, df2: pd.DataFrame, key: str, sort_by: str) -> pd.DataFrame:
    # Accepts as input 2 dataframes to be merged
    # We need to specify which column they have in common and which column to use for the sort
    result = pd.merge(df1, df2, on=key, how='inner')
    return result.sort_values(by=sort_by, ascending=False)
