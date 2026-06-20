# CAPSULE AAC Corp.

## DESCRIPICÓN:
**CAPSULE AAC Corp.** es una aplicación web desarrollada en Python que simula un planificador de eventos para un centro de investigación de medicamentos. Se podrán planificar eventos como controles de calidad o creaciones de medicamentos teniendo en cuenta que cada evento que se quiera planificar cumpla con las restricciones establecidas (exclusión o dependecia entre recursos), que no entre en conflicto con los eventos ya planificados.
La aplicación modela el Centro de Investigación AAC, en el cual se llevarían a cabo todos los eventos que se planifican usando los recursos disponibles (el personal del centro). La duración de cada evento estará dada en días y el período de planificación será de 10 años. ***El Centro de Investigación AAC es un lugar completamente imaginario, cualquier semejanza o parecido con la realidad es pura coincidencia.***

## ANTES DE USAR:
Asegúrese de leer todas las instrucciones de uso mencionadas más adelante en este documento para evitar posibles confusiones a la hora de utilizarlo.

## USO:
Ejecutar la aplicación desde la terminal de Visual Studio Code:
        streamlit run main.py
Abrir su navegador en la direciión http://localhost:8501 o la URL señalada.

## ESTRUCTURA:
- Funciones.py -> Lógica backend del programa para verificar validez de eventos, guardar tipos de evento, recursos y eventos planificados.
- main.py -> Página principal/home de la aplicación. En ella se define la navegación entre el resto de páginas que conforman la aplicación.
- DataBase.json -> Archivo para persistencia de datos.
- Main_Page.py -> Primera página de la aplicación. (Descripción en 'Presentación'>'EVENTOS PLANIFICADOS')
- Second_Page.py -> Segunda página de la aplicación. (Descripción en 'Presentación'>'EVENTOS Y RECURSOS')
- Third_Page.py -> Tercera página de la aplicación. (Descripción en 'Presentación'>'PLANIFICAR EVENTOS')
- Fourth_Page.py -> Cuarta página de la aplicación. (Descripción en 'Presentación'>'INFO')
- report.md -> Archivo de informe del proyecto.

## PRESENTACIÓN:

### EVENTOS PLANIFICADOS:
Primera página de la aplicación, en ella se presentan al usuario dos medios para visualizar los eventos planificados: un calendario, el cual muestra el rango de duración de cada evento y una tabla, la cual muestra información más detallada de cada evento (su ID, sus fechas de inicio y fin, el lugar en que ocurren y los recursos que utilizan). El usuario también podrá eliminar eventos ya planificados de dos formas diferentes: eligiendo el ID del elemento que eliminar o eliminar todo evento finalizado siguiendo una comparación entre su fecha de finalización y la fecha actual.

### EVENTOS Y RECURSOS:
Segunda página de la aplicación, desde esta el usuario podrá revisar los tipos de evento disponibles, ya sean los preestablecidos o los añadidos por él, así como la duración mínima que debe tener y el lugar en el que deben ser realizados (en caso de que no se introduzca o no se muestre información en el apartado 'Lugar' de algún evento se interpretará como que se puede realizar sin restricciones de lugar).
De igual forma, el usuario podrá revisar los recursos totales (total de trabajadores del centro) de los que se dispone.

### PLANIFICAR EVENTOS:
Tercera y más importante página de la aplicación, en esta es donde el usuario planifica cualquier evento deseado seleccionando el tipo de evento, su fecha de inicio, su duración, el lugar, y los recursos que necesite. Al seleccionar todo, se mostrarán o no advertencias (texto con fondo amarillo) en dependencia del cumplimiento de las restricciones, si se intenta proseguir ignorando las restricciones el programa no planificará el evento y saltará una advertencia (texto con fondo rojo). Por otro lado, si se respetan las restricciones el programa calculará automáticamente la fecha de finalización según la duración y comprobará si se puede planificar el evento en el intervalo seleccionado, en caso positivo se añadirá y se avisará al usuario mediante un mensaje de confirmación (texto con fondo verde) y en caso contrario se le sugerirá el próximo intervalo disponible en un rango de 30 días hacia delante desde la fecha de inicio seleccionada por el usuario.

### INFO:
Cuarta página de la aplicación, muestra un breve resumen del funcionamiento y características del programa. 


## USO DE LA APLICACIÓN:

### PARA CREAR NUEVOS TIPOS DE EVENTO:
1. Ir a la página 'Eventos y recursos'.
2. Introducir el nombre del tipo de evento (ejemplo: Visita de colaboradores rusos).
3. Seleccionar la duración (en días) mínima que deberá tener el nuevo tipo de evento (ejemplo: 1 día). ***La duración mínima que podrá tener cualquier tipo de evento es de 1 día y la máxima que puede tener es de 30 días.***
4. Introducir el lugar donde debe llevarse a cabo el nuevo tipo de evento.
5. Presionar el botón de aceptar. El usuario verá como al añadir el nuevo evento, este aparece en la lista de tipos de eventos disponibles.

### PARA PLANIFICAR LOS EVENTOS:
1. Ir a la página 'Planificar eventos'.
2. Seleccionar el evento que se desea planificar (ejemplo: Reunión de planes).
3. Seleccionar la fecha y duración del evento (ejemplo: 27/11/2026, 1 día).
4. Seleccionar el lugar donde se llevará a cabo el evento (ejemplo: Salón de reuniones).
5. Seleccionar los recursos que se utilizarán (ejemplo: Director del centro, Director de negocios,...).
6. Se mostrarán al usuario advertencias (texto con fondo amarillo) en caso de que se incumpla alguna restricción.
7. Si se cumplen las restricciones, presionar el botón 'Planificar evento' hará que el programa analice los datos seleccionados y comprobarlos con los eventos ya planificados, si no hay problemas, se añadirá el nuevo evento y se mostrará al usuario un mensaje de aviso (texto con fondo verde).
8. Si se intenta proceder a la creación de un evento sin rectificar las advertencias señaladas, se mostrará un mensaje de error al usuario (texto con fondo rojo).

## RESTRICCIONES Y DEPENDENCIAS DE RECURSOS:
Estas serán comprobadas de manera automática por el programa antes de permitir la planificación del evento.
- Restricciones:
1. Los encargados de limpieza y encargados de almacén solo pueden ser utilizados para los eventos 'Limpieza' y 'Revisión de almacén' respectivamente.
2. Sólo se pueden asignar un máximo de 20 asistentes por evento.
- Dependencias:
1. Para cualquier evento al que se le quiera asignar investigadores asistentes se le deberá asignar también al menos un investigador principal "para que los vigile".
2. Para realizar un evento de 'Limpieza' se necesitan al menos 2 encargados de limpieza.
*Estos son solo algunos ejemplos de las distintas restricciones implementadas en el programa.*

## REQUISITOS PARA EL USO:
- Python: version 3.12 o superiores.
- streamlit: version 1.29.0 o superiores.
- pandas: version 1.0.0 o superiores.
- streamlit_calendar: version 0.2.0 o superiores.

## PROBLEMAS DURANTE EL DESARROLLO DE LA APLICACIÓN:
Al principio no sabía bien por dónde empezar a trabajar ya que no conocía mucho acerca del tema, sin embargo, pregunté a conocidos míos para que me explicaran más o menos como se hacía lo básico.
El primer problema fue que no sabía como hacer la interfaz del proyecto, consulté con el profesor de programación y me aconsejó usar Streamlit y así lo hice, fue de gran ayuda por la gran comodidad que ofrece.
El segundo problema fue el uso de las bases de datos, al preguntar cómo se usaban los archivos tipo **.json** logré entender todas las características del mismo.
El tercer problema fue el cómo mostrar al usuario un calendario con los eventos planificados, después de buscar y preguntar por maneras de dibujar el calendario en streamlit, descubrí el streamlit_calendar (gracias al profesor Leyva) y pude programar el programa para que mostrara el calendario.
Ya dentro del código, durante principios del proceso de desarrollo, no tenía claro una diferencia muy importante en mi proyecto, siendo esta la diferencia entre 'tipos de eventos' y 'eventos planificados'. Al principio pensé que significaban lo mismo, pero gracias a la guía de los profesores me quedó bien claro que no era así. De esta manera se me presentó un nuevo problema: ¿cómo dejar clara esta diferencia? al pensar un poco recordé las clases de Programación Orientada a Objetos y las clases en Python, por lo que decidí crear una clase Eventos a la cual iban a pertenecer todos los eventos planificados por el usuario.  
Otro de los problemas que tuve fue que después de que se planificara el evento, este no aparecía en el calendario de eventos, esto lo logré solucionar creando en la base de datos un nuevo diccionario en el que se guardaran los eventos planificados, de ahí sacar los datos de los eventos y luego enseñarlos en el calendario; después de implementarlo de esta manera logré que aparecieran sin ningún problema.
Ya al final, cuando solo quedaban los últimos detalles, cuando se me ocurrió la idea de permitir eliminar eventos planificados, me di cuenta de que necesitaría una manera de identificarlos; ahí se me ocurrió ponerles un ID a cada uno, sin embargo, como no sabía muy bien como funcionaban los IDs, hubo problemas a la hora de asignarle un nuevo ID a un nuevo evento planificado, o sea, si ya existían eventos con IDs 1, 2, 3, 4 y eliminaba los eventos 2 y 3, al agregar un nuevo evento pensé que se le debía asignar el ID 2, pero no era así, después de investigar, aprendí que un ID no se debí repetir sin importar que se haya eliminado el evento que lo tenía previamente así que simplemente le asigné a cada nuevo evento el ID siguiente al ID más alto ya existente.

## DECISIONES DE DISEÑO:
A la hora de diseñar el proyecto, me puse a pensar en cosas que ya conociera para usarlas de inspiración, por ejemplo, la razón por la que el programa está basado en un centro de investigación es por la cercana relación que tengo con ellos debido a mis familiares y las dificultades que hay para coordinar debidamente algunos eventos en el mismo.
Ya al empezar a diseñar la interfaz del programa decidí mostrar los eventos de dos maneras diferentes: la primera, con un calendario interactivo que se actualiza cada vez que hay un nuevo evento y muestra de manera gráfica la duración del mismo, y la segunda, una tabla en la que se muestra una versión más detallada de la información de cada evento; de esta forma el usuario puede elegir una de las dos para verificar los eventos (la primera por si se quiere revisar el tiempo que ocupa cada evento y la segunda para más comodidad si solo se quieren revisar todos los eventos planificados).
Elegí darle más libertad al usuario permitiéndole añadir nuevos tipos de eventos que planificar para que estos no se vieran reducidos solamente a los ya creados por mí, así como también permitir al usuario eliminar eventos ya previamente planificados mediante el uso del ID correspondiente a dicho evento, para ello implementé una función que recibía el ID y mediante una búsqueda binaria, intentaba encontrar el evento y luego pedía una confirmación para eliminarlo.
Intenté que el programa fuera lo más cómodo e intuitivo posible a la hora de usarlo y dejar bien claro las cosas que se pueden hacer y cuales no para poder evitar cualquier posible complicación durante el empleo del mismo.

## CONOCIMIENTOS ADQUIRIDOS DURANTE EL DESARROLLO DEL PROYECTO:
Antes de realizar el proyecto, mis conocimientos sobre programación eran solamente lo que me habían enseñado a lo largo de la carrera, sin embargo, el tener que desarrollar el proyecto desde cero me obligó a buscar información sobre temas que no conocía o no había entendido del todo. Por ejemplo, gracias a canales de Youtube, preguntas a conocidos y familiares que supieran acerca del tema y preguntando a la IA sobre el funcionamiento de algunas cosas cuando no tenía a quien más preguntarle, logré un entendimiento más claro sobre el uso de las funciones y las clases en Python, así como el uso de bibliotecas como Streamlit y Pandas. Aprendí también como usar las bases de datos tipo Json. También aprendí (por las malas) a comentar el código y más específicamente que hace cada línea del mismo para no confundirme yo mismo con qué hacía cada línea de código. Aprendí, además, a usar la biblioteca datetime, la cual al principio me dio problemas para entender, pero luego de un rato comprendí cómo funcionaba. Pero lo más importante, aprendí que todavía me falta mucho por aprender acerca de programación y debo seguir estudiando para ampliar mis conocimientos.

## AGREDECIMIENTOS:
- Profesor Miguel Leyva
- Leonardo Albert López
- Orlando Valdés Montejo

# CREADOR:
  **ANDRO AGUILERA CAZANAVE**