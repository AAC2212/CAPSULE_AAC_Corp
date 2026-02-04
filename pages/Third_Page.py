import streamlit as st
import Funciones
from datetime import datetime,timedelta

able=Funciones.cargar_recursos()
dispo=Funciones.cargar_eventos()
planes=Funciones.planes()

lista_id=[]
for e in planes:
    lista_id.append(e["ID"])
proximo_id=max(lista_id)+1 if lista_id else 1

opciones_de_evento=[evento["Nombre"] for evento in dispo]

opciones_de_lugar=[]
for evento in dispo:
    if evento["Lugar"] in opciones_de_lugar or evento["Lugar"]=="":
        continue
    else:
        opciones_de_lugar.append(evento["Lugar"])


# Cree esta nueva para que desde esta se planifiquen los eventos, o sea los que se añaden al calendario.

st.header("Planificación de eventos")
st.divider()
st.subheader("¿Qué evento quieres planificar?")

evento_seleccionado=st.selectbox("",opciones_de_evento)
advertencia=False

col1,col2,col3=st.columns(3)
with col1:
    dia=st.date_input("Día de inicio:",min_value=datetime.now().date(),max_value=datetime.now().date()+timedelta(days=3650))
with col2:
    lugar=st.selectbox("Elija el lugar:",opciones_de_lugar)
    if not lugar:
        lugar=""
with col3:
    duracion=st.slider("Elija la duración:",min_value=1,max_value=30,step=1)

col4,col5,col6=st.columns(3)
with col4:
    DC=st.checkbox("¿Necesitas al director del centro?")
with col5:
    DA=st.checkbox("¿Necesitas al director adjunto?")
with col6:
    DN=st.checkbox("¿Necesitas al director de negocios?")


col7,col8,col9,col10,col11=st.columns(5)
with col7:
    IP=st.number_input("¿Cuántos investigadores princinpales?",min_value=0,step=1)
with col8:
    IA=st.number_input("¿Cuántos investigadores asistentes?",min_value=0,step=1)
with col9:
    EL=st.number_input("¿Cuántos encargados de limpieza?",min_value=0,step=1)
with col10:
    EA=st.number_input("¿Cuántos encargados de almacén?",min_value=0,step=1)
with col11:
    A=st.number_input("¿Cuántos asistentes vas a necesitar?",min_value=0,step=1)

st.divider()

st.subheader("Restricciones")
if evento_seleccionado=="Control de Calidad": 
    if lugar!="Laboratorio 1":
        st.warning("El control de calidad debe realizarse en el Laboratorio 1.")
        advertencia=True
    if duracion<2:
        st.warning("El control de calidad debe durar al menos 2 días.")
        advertencia=True
    if IP<3:
        st.warning("El control de calidad debe estar supervisado por no menos de 3 investigadores principales.")
        advertencia=True
    if IA<5:
        st.warning("Se necesitan como mínimo 5 investigadores asistentes para el control de calidad.")
        advertencia=True
    if A>5:
        st.warning("El máximo de asistentes que se pueden asignar a este evento es 5.")
        advertencia=True
    if IP==0 and IA!=0:
        st.warning("Los investigadores asistentes deben estar acompañados por al menos un investigador principal.")
        advertencia=True

if evento_seleccionado=="Creación de medicamentos":
    if lugar!="Laboratorio 2":
        st.warning("La creación de medicamentos debe realizarse en el Laboratorio 2.")
        advertencia=True
    if duracion<10:
        st.warning("La creación de medicamentos debe durar al menos 10 días.")
        advertencia=True
    if IP<5:
        st.warning("La creación de medicamentos debe estar supervisada por no menos de 5 investigadores principales.")
        advertencia=True
    if IA<10:
        st.warning("La creación de medicamentos requiere de al menos 10 investigadores asistentes.")
        advertencia=True
    if A>10:
        st.warning("El máximo de asistentes que se pueden asignar a este evento es 10.")
        advertencia=True
    if IP==0 and IA!=0:
        st.warning("Los investigadores asistentes deben estar acompañados por al menos un investigador principal.")
        advertencia=True

if evento_seleccionado=="Reunión de planes": 
    if lugar!="Salón de reuniones":
        st.warning("Las reuniones deben realizarse en el salón de reuniones.")
        advertencia=True
    if duracion<1:
        st.warning("Las reuniones deben durar al menos 1 día.")
        advertencia=True
    if DN==False:
        st.warning("El director de negocios debe formar parte de este evento.")
        advertencia=True
    if DC==False and DA==False:
        st.warning("Es necesario que esté presente el director del centro o el director adjunto.")
        advertencia=True
    if IP==0 and IA!=0:
        st.warning("Para que un investigador asistente participe en esta reunión debe estar acompañado por al menos un investigador principal.")
        advertencia=True
    if IA>3:
        st.warning("El máximo de investigadores asistentes que puede haber es 3.")
        advertencia=True
    if A>3:
        st.warning("El máximo de asistentes que se pueden asignar a este evento es 3.")
        advertencia=True

if evento_seleccionado=="Revisión de almacén":
    if lugar!="Almacén":
        st.warning("La revisión del almacén debe realizarse en el almacén.")
        advertencia=True
    if duracion<1:
        st.warning("Las revisiones del almacén deben durar al menos 1 día.")
        advertencia=True
    if IP!=0:
        st.warning("Los investigadores principales no pueden formar parte de este evento.")
        advertencia=True
    if IA!=0:
        st.warning("Los investigadores asistentes no pueden formar parte de este evento.")
        advertencia=True
    if EA<1:
        st.warning("Se necesitan al menos 3 encargados de almacén para hacer la revisión.")
        advertencia=True
    if EA>3:
        st.warning("El máximo de encargados que se pueden asignar para una sola revisión son 3.")
        advertencia=True
    if A>3:
        st.warning("El máximo de asistentes que se pueden asignar a este evento es 3.")
        advertencia=True    

if evento_seleccionado=="Limpieza":
    if duracion>1:
        st.warning("La limpieza no debe durar más de un día.")
        advertencia=True
    if IP!=0:
        st.warning("Los investigadores principales no pueden formar parte de este evento.")
        advertencia=True
    if IA!=0:
        st.warning("Los investigadores asistentes no pueden formar parte de este evento.")
        advertencia=True
    if EL<2:
        st.warning("Se necesitan al menos 2 encargados de limpieza para realizar este evento.")
        advertencia=True
    if A>15:
        st.warning("El máximo de asistentes que se pueden asignar a este evento es 15.")
        advertencia=True
    if EL>4:
        st.warning("El máximo de encargados que se pueden asignar para una sola limpieza es 4.")
        advertencia=True

if evento_seleccionado=="Escalado de productos": 
    if lugar!= "Laboratorio 2":
        st.warning("El escalado de productos debe realizarse en el Laboratorio 2.")
        advertencia=True
    if duracion<2:
        st.warning("El escalado de productos debe durar al menos 2 días.")
        advertencia=True
    if IP<3:
        st.warning("El escalado de productos debe estar supervisado por no menos de 3 investigadores principales.")
        advertencia=True
    if IA<8:
        st.warning("El escalado de productos requiere de al menos 8 investigadores asistentes.")
        advertencia=True
    if A>5:
        st.warning("El máximo de asistentes que se pueden asignar a este evento es 5.")
        advertencia=True

if EL!=0 and evento_seleccionado!="Limpieza":
    st.warning("El encargado de limpieza solo puede ser llamado para el evento 'Limpieza'.")
    advertencia=True

if EA!=0 and evento_seleccionado!="Revisión de almacén":
    st.warning("El encargado del almacén solo puede ser llamado para el evento 'Revisión del almacén'.")
    advertencia=True

if IP>6:
    st.warning("El máximo de investigadores principales que se pueden asignar a un solo evento es 6.")
    advertencia=True

if IA>15:
    st.warning("El máximo de investigadores asistentes que se pueden a un mismo evento es 15.")
    advertencia=True

if A>20:
    st.warning("El máximo de asistentes que se pueden asignar a un mismo evento es 20.")
    advertencia=True

for d in dispo:
    if evento_seleccionado==d["Nombre"]:
        if lugar!=d["Lugar"] and d["Lugar"]!="":
            st.warning("El lugar seleccionado no coincide con el necesario para llevar a cabo este evento.")
            advertencia=True
        if duracion<d["Duracion"]:
            st.warning("La duración seleccionada es menor que la duración míninma de este evento.")
            advertencia=True

if not advertencia:
    st.success("Se cumplen todas las restricciones, puede proceder a planificar el evento.")

if st.button("Planificar evento"):
    res_necesarios={"Investigador principal":IP,"Investigador asistente":IA,"Encargado de limpieza":EL,"Encargado de almacén":EA,"Asistentes":A}
    if res_necesarios["Investigador principal"]==0:
        res_necesarios.pop("Investigador principal")
    if res_necesarios["Investigador asistente"]==0:
        res_necesarios.pop("Investigador asistente")
    if res_necesarios["Encargado de limpieza"]==0:
        res_necesarios.pop("Encargado de limpieza")
    if res_necesarios["Encargado de almacén"]==0:
        res_necesarios.pop("Encargado de almacén")
    if res_necesarios["Asistentes"]==0:
        res_necesarios.pop("Asistentes")        
    if DC:
        res_necesarios["Director del centro"]=1
    if DA:
        res_necesarios["Director adjunto"]=1
    if DN:
        res_necesarios["Director de negocios"]=1
    # Chequeo que se cumplan todas las restricciones, si hay al menos una que no se cumpla, devuelvo el error 1.
    if not advertencia:
        try_event=Funciones.Eventos(proximo_id,evento_seleccionado,dia,duracion,lugar,res_necesarios)
        for e in planes:
            # Chequeo que no haya problemas con las fechas, si no los hay, directamente no los hay con nada más y se puede añadir el evento sin problemas.
            if try_event.choque_fecha(e):
                # Si hay problemas con la fecha chequeo que no haya problemas con el lugar, si los hay, devuelvo el error 2.
                if try_event.choque_lugar(e):
                    # error 2
                    st.error(f"No se pudo planificar el nuevo evento debido a que el lugar '{lugar}' estará ocupado por el evento '{e["Nombre"]}' desde el {e["Fecha de inicio"]} hasta el {e["Fecha de fin"]}.")
                    advertencia=True
                    break
                else:
                    # Si no hay problemas con el lugar chequeo los recursos, si hay problemas, devuelvo el error 3 o el 4 dependiendo de si se encontró o no un hueco disponible.
                    recursos_en_uso={}
                    for e in planes:
                        if try_event.inicio>datetime.strptime(e["Fecha de fin"],"%Y-%m-%d").date():
                            continue
                        else:
                            for ru in e["Recursos utilizados"].keys():
                                if ru in recursos_en_uso.keys():
                                    recursos_en_uso[ru] = recursos_en_uso[ru]+e["Recursos utilizados"][ru]
                                else:
                                    recursos_en_uso[ru]=e["Recursos utilizados"][ru]
                    clash,clash_res=try_event.choque_recurso(e,recursos_en_uso)
                    if clash:
                        overlimit=[]
                        for j in clash_res.keys():
                            if clash_res[j]>able[j]:
                                overlimit.append(j)
                        if overlimit:
                            intervalo=try_event.find_hole()
                            if intervalo["disponible"]:
                                # error 3
                                st.error(f"No se pudo planificar el nuevo evento debido a que el(los) siguiente(s) recurso(s): {[k for k in overlimit]} supera(n) el maximo de inventario, se aconseja bajar la cantidad o planificar este evento en el periodo {intervalo["mensaje"]}")
                            else:
                                # error 4
                                st.error(f"No se pudo planificar el nuevo evento debido a que el(los) siguiente(s) recurso(s): {[k for k in overlimit]} supera(n) el maximo de inventario, se aconseja bajar la cantidad.{intervalo['mensaje']}")
                            advertencia=True
                            break
            else:
                continue
    else:
        # error 1
        st.error("No se cumplen las restricciones")
    if not advertencia:
        final_event=Funciones.Eventos(len(planes)+1,evento_seleccionado,dia,duracion,lugar,res_necesarios)
        new_event=final_event.detalles()
        Funciones.añadir_plan(new_event)
        st.success("Se ha añadido el evento correctamente")
