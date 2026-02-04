import streamlit as st
import Funciones

st.set_page_config(page_title="Eventos y recursos",layout="wide")


eventos=Funciones.cargar_eventos()
recursos=Funciones.cargar_recursos()

# Pa trabajar con los eventos
st.header("Eventos")
st.divider()
#Pa enseñar los eventos que se pueden planificar.
st.subheader("Disponibles:")
for evento in eventos:
    with st.expander(f"{evento["Nombre"]}"):
        st.write(f"Duración mínima:  {evento["Duracion"]} día/s")
        st.write(f"Lugar:  {evento["Lugar"]}")


#Crear un boton para agregar un evento al json.
st.subheader("Añadir evento:")
col1,col2,col3=st.columns(3)
with col1:
    nombre=st.text_input("Nombre del nuevo evento:")
with col2:
    duracion=st.number_input("Cuánto durará el nuevo evento(en días):",min_value=1,max_value=30,step=1)
with col3:
    lugar=st.text_input("Lugar del nuevo evento:")   
if st.button("Añadir evento"):
    if nombre:
        if not lugar:
            lugar=""
        Funciones.añadir_evento(nombre,duracion,lugar)
        st.rerun()
    else:
        st.error("Por favor, introduzca el nombre del nuevo evento que desea añadir.")

st.divider()


# Pa trabajar con los recursos.
st.header("Recursos")
st.divider()

# Pa enseñar los recursos que hay.
st.subheader("Disponibles:")
for i in recursos.keys():
    with st.expander(f"{i}"):
        st.write(f"Cantidad: {recursos[f"{i}"]}")

# Boton para agregar recursos al json.
st.subheader("Aumentar recurso:")
lsit_res=list(recursos.keys())
col1,col2=st.columns(2)
with col1:
    nombre=st.selectbox("Elija el recurso que desea aumentar:",lsit_res)
with col2:
    cantidad=st.number_input("Cantidad que quiere añadir al recurso:",min_value=0,max_value=100,step=1)
if st.button("Aumentar recurso"):
    if cantidad!=0:
        if nombre=="Director de negocios" or nombre=="Director adjunto" or nombre=="Director del centro":
            st.warning("Solo puede haber un director.")
        else:
            Funciones.aumentar_recurso(nombre,cantidad)
            st.rerun()
    else:
        st.error("Por favor, introduzca la cantidad en que desea aumentar el recurso.")