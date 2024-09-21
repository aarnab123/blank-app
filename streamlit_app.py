import streamlit as st
about_page = st.Page(
    page="Views/about_me.py",
    title="About me",
    icon=None,
    default=True,
)
Project1 = st.Page(
    page="Views/visualizations.py",
    title="Visualizations",
    icon=None ,)
Project2 = st.Page(
    page="Views/ml_projects.py",
    title="Machine Learning Tasks",
    icon=None ,)

pg = st.navigation(pages=['about_page','Project1','Project2'])
pg.run()
