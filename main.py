import streamlit as st

main_page=st.Page("pages/Main_Page.py",title="Eventos planificados",icon='📅') 
second_page=st.Page("pages/Second_page.py",title="Eventos y recursos",icon='📝') 
third_page=st.Page("pages/Third_Page.py",title="Planificar eventos",icon='🕥')
fourth_page=st.Page("pages/Fourth_Page.py",title="Info",icon='🔎') 

pg=st.navigation([main_page,second_page,third_page,fourth_page])

pg.run()