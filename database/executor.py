import pandas as pd
from sqlalchemy import text

from database.connector import get_engine


def query_to_df(sql_query: str) -> pd.DataFrame:
    """
    Executes a SELECT query and returns a Pandas DataFrame.
    """

    engine = get_engine()

    with engine.connect() as connection:
        df = pd.read_sql(
            text(sql_query),
            connection
        )

    return df