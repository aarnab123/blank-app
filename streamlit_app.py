import streamlit as st
about_page = st.Page(
    page="view/about_me.py",
    title="About me",
    icon= ,
    default=True,
)
Project1 = st.Page(
    page="view/visualizationss.py",
    title="Visualizations",
    icon= ,)
Project2 = st.Page(
    page="view/ml_projects.py,
    title="Machine Learning Tasks",
    icon= ,)

pg = st.nevigation(pages=['about_page','Project1','Project2'])
pg.run()
