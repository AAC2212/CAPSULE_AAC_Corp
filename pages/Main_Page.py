import streamlit as st
import Funciones
import pandas as pd
from streamlit_calendar import calendar as cal
from datetime import datetime

st.set_page_config(page_title="Gestionador de eventos",layout="wide")

eventos=Funciones.calendario()

lista_id=[]
for e in eventos:
    lista_id.append(e["ID"])

calendar_options = {
    "headerToolbar": {
        "left": "prev,next",
        "center": "title",
        "right": "today",
    },
    "initialView": "dayGridMonth",
    "locale": "en",
    "height": "650px"
}


@st.dialog("🚨ADVERTENCIA🚨")
def eliminar_terminados(a_eliminar:list[int]):
    texto=""
    for i in a_eliminar:
        texto+=f" '{eventos[Funciones.b_s(eventos,0,len(eventos),i)]['title']}' que empezó el {eventos[Funciones.b_s(eventos,0,len(eventos),i)]['start']} y terminó el {eventos[Funciones.b_s(eventos,0,len(eventos),i)]['end']},\n"
    st.write(f"Esta acción eliminará los siguientes eventos:\n {texto}\n Está seguro de continuar?")
    col5,col6=st.columns(2)
    with col5:
        if st.button("Cancelar"):
            st.rerun()
    with col6:
        if st.button("Aceptar"):
            for i in a_eliminar:
                Funciones.delete_by_ID(i)
            st.rerun()


@st.dialog("🚨ADVERTENCIA🚨")
def eliminar(id:int):
    texto=""
    texto+=f"Esto eliminará el evento '{eventos[Funciones.b_s(eventos,0,len(eventos),id)]['title']}' que ocurre del {eventos[Funciones.b_s(eventos,0,len(eventos),id)]['start']} al {eventos[Funciones.b_s(eventos,0,len(eventos),id)]['end']}.\n"
    st.write(f"{texto}\n Está seguro de continuar?")
    col3,col4=st.columns(2,gap='large')
    with col3:
        if st.button("Cancelar"):
            st.rerun()
    with col4:        
        if st.button("Aceptar"):
            Funciones.delete_by_ID(id)
            st.rerun()

st.title("Centro de Investigación AAC")

st.header("Bienvenido al organizador")
st.divider()

st.subheader("Calendario de eventos:")
if not eventos:
    st.info("No se han añadido eventos, diríjase a 'Planificar eventos' para agregar uno nuevo.")
calendario=cal(events=eventos,options=calendar_options)

st.divider()
st.subheader("Eventos planificados:")
if not eventos:
    st.info("No se han planificado eventos, diríjase a 'Planificar eventos' para agregar uno nuevo.")
else:
    st.dataframe(pd.DataFrame(eventos),hide_index=True,column_config={'id':"ID",'title':"Nombre",'start':"Inicio",'end':"Fin",'lugar':"Lugar",'recursos':"Recursos utilizados"})

st.divider()
st.subheader("Eliminar eventos")
col1,col2=st.columns(2)
with col1:
    st.subheader("Eliminar por ID:")
    if not eventos:
        st.info("No se han planificado eventos, diríjase a 'Planificar eventos' para agregar uno nuevo.")
    else:
        id=st.number_input(label="Elija el ID del evento a eliminar:",min_value=1)
        if st.button("Eliminar"):
            if id not in lista_id:
                st.warning("El ID seleccionado no pertenece a ningún evento planificado")
            else:
                eliminar(id)
            
with col2:
    st.subheader("Eliminar eventos terminados:")
    if not eventos:
        st.info("No se han planificado eventos, diríjase a 'Planificar eventos' para agregar uno nuevo.")
    else:
        ids_a_eliminar=[]
        for e in eventos:
            if datetime.strptime(e['end'],"%Y-%m-%d").date()<=datetime.now().date():
                ids_a_eliminar.append(e['ID'])
        st.info("Esto eliminará todos los eventos que ya hayan terminado")
        if st.button("Eliminar terminados"):
            if ids_a_eliminar:
                eliminar_terminados(ids_a_eliminar)
            else:
                st.warning("Todavía no ha terminado ningún evento planificado.")