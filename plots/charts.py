
import plotly.express as px
import plotly.graph_objects as go

def plot_charts(chart_type,df,x_axis,y_axis, title):
 

    if chart_type == "bar":
        fig = px.bar(
            df,
            x=x_axis,
            y=y_axis,
            title=title
        )
        # st.plotly_chart(fig, use_container_width=True)
      

    elif chart_type == "line":
        fig = px.line(
            df,
            x=x_axis,
            y=y_axis,
            title=title
        )
        # st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "pie":
        fig = px.pie(
            df,
            names=x_axis,
            values=y_axis,
            title=title
        )
        # st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "scatter":
        fig = px.scatter(
            df,
            x=x_axis,
            y=y_axis,
            title=title
        )
        # st.plotly_chart(fig, use_container_width=True)

    
    return fig