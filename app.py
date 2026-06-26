import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings("ignore")
import json
from database.connector import get_engine
from database.executor import query_to_df
from database.connector import get_engine
from llm.sql_generator import llm_response 
from database.executor import query_to_df
from database.schema import get_schema
from plots.charts import plot_charts


st.title("AI Data Visualizer")

question = st.text_input(
    "Ask a question",
    placeholder="Show revenue by movie categories"
)



if st.button("Generate"):
    response = llm_response(question)
    query = response['sql']

    df = query_to_df(query)

    st.subheader("Generated SQL")
    st.code(query, language="sql")

    st.subheader("Results")
    st.dataframe(df)

    chart_type = response["chart_type"]

    if chart_type == 'table':
        st.dataframe(df)

    else:
        fig = plot_charts(chart_type,df,response['x_axis'],response['y_axis'],response['title'])
        st.plotly_chart(fig,use_container_width=True)
