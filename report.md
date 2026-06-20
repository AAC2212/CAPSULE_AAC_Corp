# CAPSULE AAC Corp.

## DESCRIPICÓN:
**CAPSULE AAC Corp.** es una aplicación web desarrollada en Python que simula un planificador de eventos para un centro de investigación de medicamentos. Se podrán planificar eventos como Controles de caliad o creaciones de medicamentos teniendo en cuenta que cada evento que se quiera planificar cumpla con las restricciones establecidas (exclusión o dependecia entre recursos), que no entre en conflicto con los eventos ya planificados.
La aplicación modela el Centro de Investigación AAC, en el cual se llevarían a cabo todos los eventos que se planifican usando los recursos disponibles(el personal del centro).La duración de cada evento estará dada en días y el período de planificación será de 10 años. ***El Centro de Investigación AAC es un lugar completamente imaginario, cualquier semejanza o parecido con la realidad es pura coincidencia.***

## USO:
Ejecutar la aplicación desde la terminal:
        streamlit run main.py
Abrir su navegador en la direciión http://localhost:8501 o la URL señalada.

## ESTRUCTURA:
- Funciones.py -> Lógica backend del programa para verificar validez de eventos, guardar tipos de evento, recursos y eventos planificados.
- main.py -> Página principal/home de la aplicación. En ella se define la navegación entre el resto de páginas.
- DataBase.json -> Archivo para persistencia de datos.
- Main_Page.py -> Primera página de la aplicación. (Descripción en 'Presentación'>'EVENTOS PLANIFICADOS')
- Second_Page.py -> Segunda página de la aplicación. (Descripción en 'Presentación'>'EVENTOS Y RECURSOS')
- Third_Page.py -> Tercera página de la aplicación. (Descripicón en 'Presentación'>'PLANIFICAR EVENTOS')
- Fourth_Page.py -> Cuarta página de la aplicación. (Descripición en 'Presentación'>'INFO')
- report.md -> Archivo de informe del proyecto.

## PRESENTACIÓN:

### EVENTOS PLANIFICADOS:
Primera página de la aplicación, en ella se presenta al usuario dos medios para visualizar los eventos planificados: un calendario, el cual muestra el rango de duración de cada evento y una tabla, la cual muestra información más detallada de cada evento(su ID, sus fechas de inicio y fin, el lugar en que ocurren y los recursos que utilizan). El usuario también podrá eliminar eventos ya planificados de dos formas diferentes: eligiendo el ID del elemento que eliminar o eliminar todo evento finalizado siguiendo una comparación entre su fecha de finalización y la fecha actual.

### EVENTOS Y RECURSOS:
Segunda página de la aplicación, desde esta el usuario podrá revisar los tipos de evento disponibles, ya sean los preestablecidos o los añadidos por él, así como la duración mínima que debe tener y el lugar en el que deben ser realizados (en caso de que no se introduzca o no se muestre información en el apartado 'Lugar' de algún evento se interpretará como que se puede realizar sin restricciones de lugar).
De igual forma, el usuario podrá revisar los recursos totales (total de trabajadores del centro) de los que se dispone.

### PLANIFICAR EVENTOS:
Tercera y más importante página de la aplicación, en esta es donde el usuario planifica cualquier evento deseado seleccionando el tipo de evento, su fecha de inicio, su duración, el lugar, y los recursos que necesite. Al seleccionar todo se mostrarán o no advertencias en dependencia del cumplimiento de las restricciones, si se intenta proseguir ignorando las restricciones el programa no planificará el evento. Por otro lado, si se respetan las restricciones el programa calculará automáticamente la fecha de finalización según la duración y comprobará si se puede planificar el evento en el intervalo seleccionado, en caso positivo se añadirá y en caso contrario se le sugerirá el próximo intervalo disponible en un rango de 30 días hacia delante desde la fecha de inicio seleccionada por el usuario.

### INFO:
Cuarta página de la aplicación, muestra un breve resumen del funcionamiento y características del programa. 


## USO DE LA APLICACIÓN:

### PARA CREAR NUEVOS TIPOS DE EVENTO:
1. Ir a la página 'Eventos y recursos'.
2. Introducir el nombre del tipo de evento (ej: Visita de colaboradores rusos).
3. Seleccionar la duración (en días) mínima que deberá tener el nuevo tipo de evento (ej: 1 día). ***La duración mínima que podrá tener cualquier tipo de evento es de 1 día y la máxima que puede tener es de 30 días.***
4. Introducir el lugar donde debe llevarse a cabo el nuevo tipo de evento.
5. Presionar el botón de aceptar. El usuario verá como se añade el nuevo evento aparecer en la lista de tipos de eventos disponibles.

### PARA PLANIFICAR LOS EVENTOS:
1. Ir a la página 'Planificar eventos'.
2. Seleccionar el evento que se desea planificar.
3. Seleccionar la fecha y duración del lugar.
4. Seleccionar el lugar donde se llevará a cabo el evento.
5. Seleccionar los recursos que se utilizarán.
6. Se mostrarán al usuario advertencias (texto con fondo amarillo) en caso de que se incumpla alguna restricción.
7. Si se cumplen las restricciones, presionar el botón 'Planificar evento' hará que el programa analice los datos seleccionados y comprobarlos con los eventos ya planificados, si no hay problemas, se añadirá el nuevo evento.

## RESTRICCIONES Y DEPENDENCIAS DE RECURSOS:
Estas serán comprobadas de manera automática por el programa antes de permitir la planificación del evento.
Restricciones: Los encargados de limpieza y encaragados de almacén solo pueden ser utilizados para los eventos 'Limpieza' y 'Revisión de almacén' respectivamente.
Dependencias: Para cualquier evento al que se le quiera asignar investigadores asistentes se le deberá asignar también al menos un investigador principal "para que los vigile".
Estos son solo algunos ejemplos de las restricciones implementadas.

# REQUISITOS PARA EL USO:
- Python: version 3.12 o superiores.
- streamlit: version 1.29.0 o superiores.
- pandas: version 1.0.0 o superiores.
- streamlit_calendar: version 0.2.0 o superiores.

# CREADOR:
  **ANDRO AGUILERA CAZANAVE**

# CONOCIMIENTOS ADQUIRIDOS:
Gracias al desarrollo de este programa, logré un mejor entendimiento del trabajo en python, el uso de las funciones, de las clases y a usar streamlit.