import streamlit as st
from groq import Groq
import time


# Le agregamos el nombre a la pestaña y un ícono. Esta configuración tiene que ser la primer linea de streamlit.
st.set_page_config(
    page_title="ChatBot Talento Tech",
    page_icon="8️⃣",
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


MODELOS = ['llama3-8b-8192', 'llama3-70b-8192'] # Se modifica en Clase 7
def configurar_pagina():
    st.title("Mi chat de IA")
    
    st.sidebar.title("Modelos disponibles")
    
    # Selector de modelo
    elegirModelo = st.sidebar.selectbox('Elegí un Modelo', options=MODELOS, index=0)
    
    # Separador visual
    st.sidebar.markdown("---")

    # 🧪 Laboratorio de Prompts con reflexiones
    st.sidebar.subheader("🧪 Laboratorio de Prompts - Prácticas por Categoría")

    with st.sidebar.expander("🧮 Data Analytics"):
        st.markdown("""
        💬 **Consigna:**  
        Representá la evolución de ventas mensuales con Matplotlib.  
        👉 Usá el chatbot para diseñar un prompt claro, específico y alineado con lo que necesitás lograr.  
        🤔 ¿Qué elementos del prompt creés que lo hacen más efectivo?
        """)

    with st.sidebar.expander("🌐 Desarrollo Full Stack"):
        st.markdown("""
        💬 **Consigna:**  
        Creá una API RESTful en Flask que reciba datos por POST.  
        👉 Usá el chatbot para diseñar un prompt claro, específico y alineado con lo que necesitás lograr.  
        🤔 ¿Cómo podrías ajustar tu prompt para obtener una respuesta más precisa?
        """)

    with st.sidebar.expander("🎨 UX/UI"):
        st.markdown("""
        💬 **Consigna:**  
        Justificá decisiones de diseño para una app orientada a adolescentes, con foco en accesibilidad.  
        👉 Usá el chatbot para diseñar un prompt claro, específico y alineado con lo que necesitás lograr.  
        🤔 ¿Cómo podés lograr que el chatbot entienda mejor el contexto de usuario?
        """)

    with st.sidebar.expander("🎮 Videojuegos"):
        st.markdown("""
        💬 **Consigna:**  
        Depurá un script de Unity que no permite saltar con la barra espaciadora.  
        👉 Usá el chatbot para diseñar un prompt claro, específico y alineado con lo que necesitás lograr.  
        🤔 ¿Incluiste suficiente contexto en el prompt para que la IA entienda tu problema?
        """)

    with st.sidebar.expander("🧪 Tester QA"):
        st.markdown("""
        💬 **Consigna:**  
        Generá casos de prueba funcionales para una app de login.  
        👉 Usá el chatbot para diseñar un prompt claro, específico y alineado con lo que necesitás lograr.  
        🤔 ¿Qué estructura tiene un buen prompt para pedir test cases?
        """)

    with st.sidebar.expander("💻 Front-End"):
        st.markdown("""
        💬 **Consigna:**  
        Validá el campo email de un formulario usando HTML + JavaScript.  
        👉 Usá el chatbot para diseñar un prompt claro, específico y alineado con lo que necesitás lograr.  
        🤔 ¿Cómo mejora el resultado al incluir código en el prompt?
        """)

    with st.sidebar.expander("🚀 Solidity"):
        st.markdown("""
        💬 **Consigna:**  
        Revisá un contrato inteligente en Solidity que no acepta pagos correctamente.  
        👉 Usá el chatbot para diseñar un prompt claro, específico y alineado con lo que necesitás lograr.  
        🤔 ¿Qué detalles técnicos conviene incluir para depurar con IA?
        """)

    with st.sidebar.expander("📈 Marketing Digital"):
        st.markdown("""
        💬 **Consigna:**  
        Mejorá la segmentación de un anuncio de productos ecológicos en redes sociales.  
        👉 Usá el chatbot para diseñar un prompt claro, específico y alineado con lo que necesitás lograr.  
        🤔 ¿Cómo incluir tu audiencia objetivo en el prompt mejora la respuesta?
        """)

    with st.sidebar.expander("🧠 Soft Skills"):
        st.markdown("""
        💬 **Consigna:**  
        Redactá un perfil profesional enfocado en Testing QA para colocar en tu CV o LinkedIn.  
        👉 Usá el chatbot para diseñar un prompt claro, específico y alineado con lo que necesitás lograr.  
        🤔 ¿Qué información personal deberías incluir para lograr una respuesta más auténtica?
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

        
