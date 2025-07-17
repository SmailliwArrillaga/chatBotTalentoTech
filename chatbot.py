import streamlit as st
from groq import Groq
import time


# Le agregamos el nombre a la pestaña y un ícono. Esta configuración tiene que ser la primer linea de streamlit.
st.set_page_config(
    page_title="ChatBot Talento Tech",
    page_icon="🤖",
    layout="wide"  # ← ¡CAMBIA esto a wide!
)

# 🎨 Estilos para los expanders del sidebar
st.markdown(
    """
    <style>
    /* Color del texto de los expanders */
    [data-testid="stSidebar"] details summary {
        color: #153244;  /* Color del texto */
        font-weight: bold;
        font-size: 16px;
    }

    /* Al pasar el mouse */
    [data-testid="stSidebar"] details summary:hover {
        color: #34b3a0;  /* Color al hacer hover */
    }

    /* Cambiar el fondo del panel abierto */
    [data-testid="stSidebar"] details[open] > summary {
        background-color: #f0f0f0;
        border-radius: 5px;
        padding: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #ffffff; /* Cambiá este color a gusto */
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
) 

st.markdown(
    """
    <style>
    /* Estilo de los títulos de los expanders */
    [data-testid="stSidebar"] details summary {
        color: #153244;
        font-weight: bold;
        font-size: 16px;
    }

    [data-testid="stSidebar"] details summary:hover {
        color: #34b3a0;
    }

    [data-testid="stSidebar"] details[open] > summary {
        background-color: #f0f0f0;
        border-radius: 5px;
        padding: 5px;
    }

    /* Estilo del contenido interno de los expanders */
    [data-testid="stSidebar"] .stMarkdown {
        color: #1c1c1c;  /* Cambia el color del texto adentro */
        font-size: 14px;
    }

    /* Fondo opcional del contenido abierto */
    [data-testid="stSidebar"] details[open] {
        background-color: #f9f9f9;  /* Fondo clarito para separar visualmente */
        border-radius: 5px;
        padding: 5px;
        margin-bottom: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# 👉 Personalización visual del input del chat
st.markdown(
    """
    <style>
    /* Ajusta el input del chat_input */
    textarea[aria-label="Escribí tu mensaje:"] {
        background-color: #e0f7f4 !important;
        color: #153244 !important;
        border: 2px solid #34b3a0 !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }

    /* Opcional: cambia el borde cuando está enfocado */
    textarea[aria-label="Escribí tu mensaje:"]:focus {
        border: 2px solid #0077b6 !important;
        outline: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("imagen1.png", width=400)
st.title("Bienvenidos al chatBot de Talento Tech")

col1, col2 = st.columns([1, 2])  # 1 parte imagen, 2 partes texto

with col1:
    st.markdown("<br><br><br>", unsafe_allow_html=True)  # empuja la imagen hacia el centro
    st.image("imagen2.png", width=200)  # Asegurate de que este nombre coincida con tu imagen subida

with col2:
    st.markdown("""
    🧠 **Este chatbot fue creado para que practiques lo aprendido en el Módulo 2: Diseño de Prompts del curso de Inteligencia Artificial.**  
    Vas a poder resolver desafíos reales de tu área profesional mientras mejorás tu capacidad para dar instrucciones claras, específicas y funcionales a una IA.  
    A la izquierda tenés distintas categorías por perfil profesional (Desarrollo Web, Testing QA, Videojuegos, UX/UI, etc).  
    Cada una tiene una consigna práctica que podés abordar diseñando un buen prompt y reflexionando sobre cómo mejorar las respuestas que recibís.

    ---

    🤖 **También podés elegir entre dos modelos de IA distintos:**  
        **1. llama3-8b-8192**: más liviano, rápido y eficiente para tareas generales.  
        **2. llama3-70b-8192**: más potente y detallado, ideal para respuestas complejas.

    💡 *Tip:* probá usar el mismo prompt en ambos modelos y compará sus respuestas.  
    👉 ¿Cuál te resultó más útil? ¿Por qué?
    """)
    
MODELOS = ['llama3-8b-8192', 'llama3-70b-8192'] # Se modifica en Clase 7
def configurar_pagina():

    st.sidebar.title("Modelos disponibles")
    elegirModelo = st.sidebar.selectbox('Elegí un Modelo', options=MODELOS, index=0)
    st.sidebar.markdown("---")
    st.sidebar.subheader("🧪 Laboratorio de Prompts - Prácticas por Categoría")

    with st.sidebar.expander("🧮 Data Analytics"):
        st.markdown("""
        💬 **Consigna 1**
        📊 Estás preparando una presentación mensual para tu equipo y necesitás mostrar la evolución de las ventas de forma clara y visual.
        Te invito a usar el chatbot para generar el código en Matplotlib que te permita visualizar correctamente la información.  
        🤔 ¿Qué prompt usarías para lograrlo?

        💬 **Consigna 2**
        📈 Tenés los registros de asistencia de tu clase y querés mostrar qué porcentaje asistió en cada fecha.
        Te invito a usar el chatbot para crear un gráfico de torta con Pandas y Matplotlib.  
        🤔 ¿Qué datos necesitás incluir en el prompt para que la IA te ayude correctamente?

         💬 **Consigna 3**
        📋 Te compartieron una base de Excel con ventas por región y necesitás una tabla dinámica que te resuma esta información.
        Te invito a usar el chatbot para obtener una guía paso a paso sobre cómo armar esa tabla dinámica.  
        🤔 ¿Qué información debe contener tu prompt?
        """)

    with st.sidebar.expander("🌐 Desarrollo Full Stack"):
        st.markdown("""
        💬 **Consigna 1**
        🧾 Estás trabajando en una app de carga de datos y necesitás crear una API para que los usuarios envíen información.
        Te invito a usar el chatbot para generar una API RESTful con Flask que reciba datos por POST.  
        🤔 ¿Qué información del problema debés incluir en tu prompt?

        💬 **Consigna 2**
        🔐 Tenés que implementar una función de registro y login en un backend para que los usuarios accedan a su perfil.
        Te invito a usar el chatbot para estructurar un sistema de autenticación en Django.  
        🤔 ¿Cómo describirías tu necesidad de manera precisa en el prompt?

        💬 **Consigna 3**
        🧑‍💻 Estás desarrollando una plataforma donde los usuarios puedan editar su perfil de manera segura.
        Te invito a usar el chatbot para definir un endpoint funcional para esta tarea.  
        🤔 ¿Qué información necesitás compartirle a la IA para que lo diseñe correctamente?
        """)

    with st.sidebar.expander("🎨 UX/UI"):
        st.markdown("""
        💬 **Consigna 1**
        👩‍🎨 Estás diseñando una app para adolescentes con foco en inclusión y necesitás justificar decisiones clave de accesibilidad.
        Te invito a usar el chatbot para redactar tu justificación.  
        🤔 ¿Qué aspectos debés destacar en tu prompt para obtener una respuesta útil?

        💬 **Consigna 2**
        🔐 Te encargaron diseñar la pantalla de login para una app moderna y querés que sea visualmente atractiva y fácil de usar.
        Te invito a usar el chatbot para obtener sugerencias de diseño y estructura.  
        🤔 ¿Qué características querés que tenga la pantalla para poder incluirlas en tu prompt?
        
        💬 **Consigna 3**
        🧑‍🦯 Un colega detectó que algunos usuarios no distinguen bien los textos en tu diseño. Necesitás evaluar contraste y accesibilidad visual.
        Te invito a usar el chatbot para hacer esa evaluación.  
        🤔 ¿Qué tipo de interfaz o contexto tenés que describir para obtener buenos resultados?
        """)

    with st.sidebar.expander("🎮 Videojuegos"):
        st.markdown("""
        💬 **Consigna 1**
        🕹️ Estás desarrollando un juego en Unity pero el personaje no responde al presionar la barra espaciadora para saltar.
        Te invito a usar el chatbot para depurar el script.  
        🤔 ¿Qué parte del código o comportamiento necesitás explicarle al modelo para ayudarte mejor?

        💬 **Consigna 2**
        🧠 Querés implementar un sistema de puntuación que motive al jugador a avanzar en tu juego 2D.
        Te invito a usar el chatbot para desarrollar esa lógica.  
        🤔 ¿Qué condiciones o eventos clave debés describir en el prompt?

        💬 **Consigna 3**
        🎮 Necesitás un menú de pausa que no corte la experiencia del jugador y se vea profesional.
        Te invito a usar el chatbot para generar una interfaz funcional y estilizada.  
        🤔 ¿Qué aspectos visuales o técnicos deberías detallar?
        """)

    with st.sidebar.expander("🧪 Tester QA"):
        st.markdown("""
        💬 **Consigna 1**
        🔐 Te pasaron una app de login que tenés que testear. Querés validar qué pasa con credenciales inválidas y vacías.
        Te invito a usar el chatbot para generar casos de prueba funcionales.  
        🤔 ¿Cómo redactarías el prompt para que incluya distintos escenarios?

        💬 **Consigna 2**
        📨 Un nuevo formulario de contacto fue agregado a la web y necesitás asegurarte de que todo funcione correctamente.
        Te invito a usar el chatbot para diseñar un plan de pruebas adecuado.  
        🤔 ¿Qué partes del formulario necesitás mencionar en el prompt?

        💬 **Consigna 3**
        🔽 Estás verificando un selector desplegable que no muestra todas las opciones. Necesitás redactar un caso de prueba.
        Te invito a usar el chatbot para formular ese caso.  
        🤔 ¿Qué comportamientos deberías describir para que la IA entienda el problema?
        """)

    with st.sidebar.expander("💻 Front-End"):
        st.markdown("""
        💬 **Consigna 1**
        📧 Necesitás validar el campo de email en un formulario para evitar errores al enviar datos.
        Te invito a usar el chatbot para generar una solución con HTML y JavaScript.  
        🤔 ¿Qué condiciones o errores querés evitar?

        💬 **Consigna 2**
        🌐 Estás creando una landing page para promocionar un producto nuevo y necesitás que se vea bien en todos los dispositivos.
        Te invito a usar el chatbot para estructurar el código base.  
        🤔 ¿Qué detalles deberías incluir sobre el producto o la estética esperada?

        💬 **Consigna 3**
        🎨 Tenés un formulario de contacto muy básico y querés modernizar su apariencia con CSS.
        Te invito a usar el chatbot para estilizarlo.  
        🤔 ¿Qué tipo de estilo o efecto te gustaría lograr?
        """)

    with st.sidebar.expander("🛠️ Desarrollo Backend"):
        st.markdown("""
        💬 **Consigna 1**
        🧾 Estás construyendo un sistema interno que requiere guardar usuarios y roles. Necesitás estructurar la base de datos.
        Te invito a usar el chatbot para generar la base en PostgreSQL.  
        🤔 ¿Qué campos o relaciones querés que tenga?
        
        💬 **Consigna 2**
        🔑 Tenés que proteger tu API y te pidieron implementar autenticación basada en tokens JWT.
        Te invito a usar el chatbot para guiarte en la integración de JWT.  
        🤔 ¿Qué parte del flujo de autenticación necesitás implementar?

        💬 **Consigna 3**
        🐢 Tenés una consulta SQL que tarda demasiado y afecta el rendimiento general del sistema.
        Te invito a usar el chatbot para optimizarla.  
        🤔 ¿Qué datos deberías compartir en el prompt para que la IA analice correctamente?
        """)

    with st.sidebar.expander("🧠 Soft Skills"):
        st.markdown("""
        💬 **Consigna 1**
        👩‍💼 Estás actualizando tu perfil profesional en LinkedIn y querés que destaque tus habilidades en Testing QA.
        Te invito a usar el chatbot para redactar una versión clara y atractiva.  
        🤔 ¿Qué logros o conocimientos querés resaltar?

        💬 **Consigna 2**
        📧 Tuviste una discusión con un compañero por la distribución de tareas y necesitás enviarle un email profesional que no escale el conflicto.
        Te invito a usar el chatbot para generar un borrador empático y efectivo.  
        🤔 ¿Qué elementos deberías incluir en tu prompt para lograrlo?

        💬 **Consigna 3**
        🧑‍💼 Te convocaron a una entrevista de trabajo en tecnología y querés prepararte mejor para responder preguntas difíciles.
        Te invito a usar el chatbot para que te ayude a prepararte.  
        🤔 ¿Qué tipo de preguntas te gustaría practicar y qué contexto podrías dar?
        """)

    return elegirModelo






# Ciente
def crear_usuario_groq():
    claveSecreta = st.secrets["clave_api"]
    return Groq(api_key=claveSecreta)



def configurar_modelo(cliente, modelo, mensajeDeEntrada):
    return cliente.chat.completions.create(
        model=modelo,
        messages=[{"role": "user", "content": mensajeDeEntrada}],
        stream=True
    )

def inicializar_estado():
    '''
    st.session_state: Es un diccionario especial de Streamlit que permite almacenar datos persistentes entre interacciones de usuario en la aplicación.
    "mensajes" not in st.session_state: Comprueba si "mensajes" no es una clave existente en st.session_state.
    Esto es útil para mantener un estado persistente de los mensajes en la aplicación,
    permitiendo que los datos se almacenen y recuperen entre diferentes interacciones del usuario con la aplicación
    Este mecanismo es fundamental para aplicaciones interactivas donde el estado del usuario (como los mensajes en un chat) debe mantenerse a lo largo
    del uso de la aplicación.
    '''
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []
       






def actualizar_historial(rol, contenido, avatar):
    st.session_state.mensajes.append({"role": rol, "content": contenido, "avatar":avatar})
    
def mostrar_historial():
    for mensaje in st.session_state.mensajes:
        with st.chat_message(mensaje["role"], avatar=mensaje["avatar"]):
            fondo = "#e0f7f4" if mensaje["role"] == "user" else "#153244"
            texto = "#1c1c1c" if mensaje["role"] == "user" else "#ffffff"

            st.markdown(
                f"""
                <div style='
                    background-color:{fondo};
                    color:{texto};
                    padding: 12px 16px;
                    border-radius: 12px;
                    margin-bottom: 8px;
                    box-shadow: 1px 1px 6px rgba(0,0,0,0.1);
                '>
                    {mensaje["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )


def area_chat():
    contenedorDelChat = st.container(height=400,border=True)
    # Abrimos el contenedor del chat y mostramos el historial.
    with contenedorDelChat:
        mostrar_historial()
    



def generar_respuesta(chat_completo):
    respuesta_completa = ""
    for fragmento in chat_completo:
        if fragmento.choices[0].delta.content:
            respuesta_completa += fragmento.choices[0].delta.content
    return respuesta_completa


def main():
    modelo = configurar_pagina()
    clienteUsuario = crear_usuario_groq()
    inicializar_estado()
    area_chat()  # Muestra el historial del chat
    mensaje = st.chat_input("Escribí tu mensaje:")

    if mensaje:
        actualizar_historial("user", mensaje, "🧑‍💻")      

        chat_completo = configurar_modelo(clienteUsuario, modelo, mensaje)

        if chat_completo:
            with st.chat_message("assistant"):
                respuesta_completa = generar_respuesta(chat_completo)
                st.markdown(respuesta_completa)
                actualizar_historial("assistant", respuesta_completa, "🤖")

            st.rerun()



if __name__ == "__main__":
    main()

        
