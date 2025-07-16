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
    st.image("imagen2.png", width=200)  # Asegurate de que este nombre coincida con tu imagen subida

with col2:
    st.markdown("""
    🧠 **Este chatbot fue creado para que practiques lo aprendido en el Módulo 2: Diseño de Prompts del curso de Inteligencia Artificial.**  
    Vas a poder resolver desafíos reales de tu área profesional mientras mejorás tu capacidad para dar instrucciones claras, específicas y funcionales a una IA.  
    A la izquierda tenés distintas categorías por perfil profesional (Desarrollo Web, Testing QA, Videojuegos, UX/UI, etc).  
    Cada una tiene una consigna práctica que podés abordar diseñando un buen prompt y reflexionando sobre cómo mejorar las respuestas que recibís.

    ---

    🤖 **También podés elegir entre dos modelos de IA distintos:**  
        1.llama3-8b-8192: más liviano, rápido y eficiente para tareas generales.  
        2.llama3-70b-8192: más potente y detallado, ideal para respuestas complejas.

    💡 *Tip:* probá usar el mismo prompt en ambos modelos y compará sus respuestas.  
    👉 ¿Cuál te resultó más útil? ¿Por qué?
    """)
    
MODELOS = ['llama3-8b-8192', 'llama3-70b-8192'] # Se modifica en Clase 7
def configurar_pagina():
    
    st.sidebar.title("Modelos disponibles")
    elegirModelo = st.sidebar.selectbox('Elegí un Modelo', options=MODELOS, index=0)
    st.sidebar.markdown("---")
    st.sidebar.subheader("🧪 Laboratorio de Prompts - Prácticas por Categoría")

    with st.sidebar.expander("🧮 Data Analytics / Excel"):
        st.markdown("""
        💬 **Consigna 1:**
        Representá la evolución de ventas mensuales con Matplotlib.
        
        💬 **Consigna 2:**
        Generá un gráfico de torta que muestre el porcentaje de asistencia de una clase usando Python y Pandas.
        
        💬 **Consigna 3:**
        Creá una tabla dinámica en Excel que te permita analizar las ventas por región.
        
        👉 Usá el chatbot para diseñar un prompt claro, específico y alineado con lo que necesitás lograr.  
        🤔 ¿Qué elementos del prompt creés que lo hacen más efectivo?
        """)

    with st.sidebar.expander("🌐 Desarrollo Full Stack"):
        st.markdown("""
        💬 **Consigna 1:**
        Creá una API RESTful en Flask que reciba datos por POST.
        
        💬 **Consigna 2:**
        Diseñá un backend en Django que permita registro y login de usuarios.
        
        💬 **Consigna 3:**
        Generá un endpoint para editar perfiles en una app web.
        
        👉 Usá el chatbot para diseñar un prompt claro, específico y alineado con lo que necesitás lograr.  
        🤔 ¿Qué elementos del prompt creés que lo hacen más efectivo?
        """)

    with st.sidebar.expander("🎨 UX/UI"):
        st.markdown("""
        💬 **Consigna 1:**
        Justificá decisiones de diseño para una app orientada a adolescentes, con foco en accesibilidad.
        
        💬 **Consigna 2:**
        Redactá un prompt para diseñar una pantalla de login atractiva y funcional.
        
        💬 **Consigna 3:**
        Evaluá una interfaz con problemas de contraste y accesibilidad visual.
        
        👉 Usá el chatbot para diseñar un prompt claro, específico y alineado con lo que necesitás lograr.  
        🤔 ¿Qué elementos del prompt creés que lo hacen más efectivo?
        """)

    with st.sidebar.expander("🎮 Videojuegos"):
        st.markdown("""
        💬 **Consigna 1:**
        Depurá un script de Unity que no permite saltar con la barra espaciadora.
        
        💬 **Consigna 2:**
        Generá un sistema de puntuación para un juego 2D.
        
        💬 **Consigna 3:**
        Diseñá un menú de pausa funcional y estilizado en Unity.
        
        👉 Usá el chatbot para diseñar un prompt claro, específico y alineado con lo que necesitás lograr.  
        🤔 ¿Qué elementos del prompt creés que lo hacen más efectivo?
        """)

    with st.sidebar.expander("🧪 Tester QA"):
        st.markdown("""
        💬 **Consigna 1:**
        Generá casos de prueba funcionales para una app de login.
        
        💬 **Consigna 2:**
        Diseñá un plan de pruebas para un formulario de contacto.
        
        💬 **Consigna 3:**
        Redactá un caso de prueba para validar un selector desplegable.
        
        👉 Usá el chatbot para diseñar un prompt claro, específico y alineado con lo que necesitás lograr.  
        🤔 ¿Qué elementos del prompt creés que lo hacen más efectivo?
        """)

    with st.sidebar.expander("💻 Front-End"):
        st.markdown("""
        💬 **Consigna 1:**
        Validá el campo email de un formulario usando HTML + JavaScript.
        
        💬 **Consigna 2:**
        Creá una landing page responsive para un producto ficticio.
        
        💬 **Consigna 3:**
        Estilizá un formulario de contacto con CSS moderno.
        
        👉 Usá el chatbot para diseñar un prompt claro, específico y alineado con lo que necesitás lograr.  
        🤔 ¿Qué elementos del prompt creés que lo hacen más efectivo?
        """)

    with st.sidebar.expander("🛠️ Desarrollo Backend"):
        st.markdown("""
        💬 **Consigna 1:**
        Creá una base de datos en PostgreSQL para almacenar usuarios y sus roles.
        
        💬 **Consigna 2:**
        Implementá autenticación JWT en una API desarrollada con Node.js.
        
        💬 **Consigna 3:**
        Optimizá una consulta SQL que tarda mucho tiempo en ejecutarse.
        
        👉 Usá el chatbot para diseñar un prompt claro, específico y alineado con lo que necesitás lograr.  
        🤔 ¿Qué elementos del prompt creés que lo hacen más efectivo?
         """)
        
    with st.sidebar.expander("🧠 Soft Skills"):
        st.markdown("""
        💬 **Consigna 1:**
        Redactá un perfil profesional enfocado en Testing QA para colocar en tu CV o LinkedIn.
        
        💬 **Consigna 2:**
        Pedí ayuda para mejorar tu comunicación por email ante un conflicto laboral.
        
        💬 **Consigna 3:**
        Solicitá recomendaciones para preparar una entrevista de trabajo en tecnología.
        
        👉 Usá el chatbot para diseñar un prompt claro, específico y alineado con lo que necesitás lograr.  
        🤔 ¿Qué elementos del prompt creés que lo hacen más efectivo?
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

        
