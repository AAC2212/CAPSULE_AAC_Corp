import streamlit as st

st.set_page_config(page_title="Info",layout="wide")

st.header("Información acerca del proyecto")

st.divider()

st.subheader("Acerca de la funcionalidad:")
st.write("El programa simula un planificador de eventos para un centro de investigación de medicamentos ficticio, el 'Centro de Investigación AAC', cualquier similitud con la realidad es completamente coincidencia. Mediante el programa el usuario podrá planificar los eventos para dicho centro de investigación y utilizar los recursos (el personal del centro) disponibles para la realización de los mismos. Para cualquier duda que pueda surgir durante el uso del programa, referirse al documento 'README.md' o consultar con el creador.")

st.divider()

st.subheader("Acerca del diseño:")
st.write("El programa se basa en las experiencias del creador al formar parte de este tipo de centros de invesstigación. Se tomaron como referencia allgunos eventos que suelen realizarse con frecuencia en la vida real y el creador pudo experimentar. Se han reducido y acomodado la duración de algunos eventos en comparación a sus contrapartes de la vida real; por ejemplo, el evento 'Creación de medicamentos' en el programa tiene una duración de 10 días, sin embargo en la vida real este proceso puede durar de entre 10 a 20 años.")


st.divider()

st.subheader("Creador:")
st.write("Andro Aguilera Cazanave")