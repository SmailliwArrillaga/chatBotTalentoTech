import streamlit as st
from groq import Groq
from groq._exceptions import BadRequestError
import time

# ──────────────────────────────────────────────────────────────────────────────
# Configuración de página
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ChatBot Talento Tech",
    page_icon="🤖",
    layout="wide"
)

# 🎨 Estilos para el sidebar y el chat_input
st.markdown(
    """
    <style>
    /* Sidebar: títulos de expanders */
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

    /* Contenido de expanders */
    [data-testid="stSidebar"] .stMarkdown {
        color: #1c1c1c;
        font-size: 14px;
    }
    [data-testid="stSidebar"] details[open] {
        background-color: #f9f9f9;
        border-radius: 5px;
        padding: 5px;
        margin-bottom: 8px;
    }

    /* Fondo del sidebar */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
    }

    /* Input de chat */
    textarea[aria-label="Escribí tu mensaje:"] {
        background-color: #e0f7f4 !important;
        color: #153244 !important;
        border: 2px solid #34b3a0 !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }
    textarea[aria-label="Escribí tu mensaje:"]:focus {
        border: 2px solid #0077b6 !important;
        outline: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ──────────────────────────────────────────────────────────────────────────────
# Portada
# ──────────────────────────────────────────────────────────────────────────────
st.image("imagen1.png", width=400)
st.title("Bienvenidos al chatBot de Talento Tech")

col1, col2 = st.columns([1, 2])
with col1:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.image("imagen2.png", width=200)

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

# ──────────────────────────────────────────────────────────────────────────────
# Configuración y UI lateral
# ──────────────────────────────────────────────────────────────────────────────
MODELOS = ['llama3-8b-8192', 'llama3-70b-8192']

def configurar_pagina():
    st.sidebar.title("Modelos disponibles")

    # Cliente temporal para listar modelos (si se desea)
    try:
        claveSecreta = st.secrets["clave_api"]
        _cliente_tmp = Groq(api_key=claveSecreta)
        disponibles = [m.id for m in _cliente_tmp.models.list().data]
        with st.sidebar.expander("Modelos habilitados en tu cuenta", expanded=False):
            st.write(disponibles)
        # Si alguno de MODELOS no está habilitado, avisamos
        faltantes = [m for m in MODELOS if m not in disponibles]
        if faltantes:
            st.sidebar.warning(
                f"Estos modelos no figuran habilitados: {', '.join(faltantes)}. "
                "Si elegís uno no habilitado, la API puede devolver BadRequest."
            )
    except Exception as e:
        st.sidebar.info("No se pudieron listar modelos. Verificá tu clave o permisos.")

    elegirModelo = st.sidebar.selectbox('Elegí un Modelo', options=MODELOS, index=0)
    st.sidebar.markdown("---")
    st.sidebar.subheader("🧪 Laboratorio de Prompts - Prácticas por Categoría")

    with st.sidebar.expander("🧮 Data Analytics"):
        st.markdown("""
        **Consigna 1**: Evolución de ventas con Matplotlib.  
        **Consigna 2**: Porcentaje de asistencia (gráfico torta).  
        **Consigna 3**: Tabla dinámica desde Excel (guía paso a paso).
        """)

    with st.sidebar.expander("🌐 Desarrollo Full Stack"):
        st.markdown("""
        **Consigna 1**: API REST con Flask (POST).  
        **Consigna 2**: Registro/login en Django.  
        **Consigna 3**: Endpoint para editar perfil.
        """)

    with st.sidebar.expander("🎨 UX/UI"):
        st.markdown("""
        **Consigna 1**: Justificación de accesibilidad.  
        **Consigna 2**: Pantalla de login moderna.  
        **Consigna 3**: Evaluación de contraste.
        """)

    with st.sidebar.expander("🎮 Videojuegos"):
        st.markdown("""
        **Consigna 1**: Depurar salto con barra espaciadora (Unity).  
        **Consigna 2**: Sistema de puntuación.  
        **Consigna 3**: Menú de pausa profesional.
        """)

    with st.sidebar.expander("🧪 Tester QA"):
        st.markdown("""
        **Consigna 1**: Casos de prueba de login (inválidos/vacíos).  
        **Consigna 2**: Plan de pruebas para formulario de contacto.  
        **Consigna 3**: Caso de prueba para dropdown incompleto.
        """)

    with st.sidebar.expander("💻 Front-End"):
        st.markdown("""
        **Consigna 1**: Validación de email (HTML+JS).  
        **Consigna 2**: Landing responsive base.  
        **Consigna 3**: Modernizar formulario con CSS.
        """)

    with st.sidebar.expander("🛠️ Desarrollo Backend"):
        st.markdown("""
        **Consigna 1**: Modelo de usuarios y roles (PostgreSQL).  
        **Consigna 2**: Autenticación JWT.  
        **Consigna 3**: Optimización de consulta SQL lenta.
        """)

    with st.sidebar.expander("🧠 Soft Skills"):
        st.markdown("""
        **Consigna 1**: Perfil de LinkedIn (QA).  
        **Consigna 2**: Email profesional post-conflicto.  
        **Consigna 3**: Preparación para entrevista.
        """)

    return elegirModelo

# ──────────────────────────────────────────────────────────────────────────────
# Cliente Groq
# ──────────────────────────────────────────────────────────────────────────────
def crear_usuario_groq():
    claveSecreta = st.secrets["clave_api"]  # Debe ser gsk_...
    return Groq(api_key=claveSecreta)

# ──────────────────────────────────────────────────────────────────────────────
# Llamadas a Groq
# ──────────────────────────────────────────────────────────────────────────────
def configurar_modelo(cliente, modelo, mensajeDeEntrada):
    """Llamada en streaming con parámetros seguros y manejo de error."""
    try:
        return cliente.chat.completions.create(
            model=modelo,
            messages=[
                {"role": "system", "content": "Sos un asistente claro, conciso y pedagógico."},
                {"role": "user", "content": str(mensajeDeEntrada)}
            ],
            temperature=0.3,
            top_p=1,
            max_tokens=512,   # Importante: Groq suele requerirlo
            stream=True
        )
    except BadRequestError as e:
        st.error("La API devolvió un BadRequest. Revisá los detalles debajo y los logs de la app.")
        try:
            st.write("Status:", getattr(e, "status_code", "N/D"))
            st.write("Detalle:", getattr(e, "body", None) or getattr(e, "response", None) or str(e))
        except Exception:
            pass
        raise

def test_llamada_simple(cliente, modelo, texto):
    """Utilidad de diagnóstico SIN streaming; útil para aislar errores."""
    resp = cliente.chat.completions.create(
        model=modelo,
        messages=[
            {"role": "system", "content": "Sos un asistente claro, conciso y pedagógico."},
            {"role": "user", "content": str(texto)}
        ],
        temperature=0.3,
        max_tokens=128,
        top_p=1,
        stream=False
    )
    return resp.choices[0].message.content

# ──────────────────────────────────────────────────────────────────────────────
# Estado, historial y UI de chat
# ──────────────────────────────────────────────────────────────────────────────
def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

def actualizar_historial(rol, contenido, avatar):
    st.session_state.mensajes.append({"role": rol, "content": contenido, "avatar": avatar})

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
    contenedorDelChat = st.container(height=400, border=True)
    with contenedorDelChat:
        mostrar_historial()

def generar_respuesta(chat_completo):
    """Concatena fragmentos del stream de manera robusta."""
    respuesta_completa = ""
    for fragmento in chat_completo:
        try:
            delta = fragmento.choices[0].delta
            if delta and getattr(delta, "content", None):
                respuesta_completa += delta.content
        except Exception:
            # Si cambia el shape de la respuesta, evitamos romper el flujo
            pass
    return respuesta_completa

# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────
def main():
    modelo = configurar_pagina()
    clienteUsuario = crear_usuario_groq()
    inicializar_estado()
    area_chat()

    # Descomentar esta línea para hacer una prueba rápida SIN streaming:
    # st.sidebar.button("Test sin streaming", on_click=lambda: st.sidebar.write(
    #     test_llamada_simple(clienteUsuario, modelo, "Decime un haiku sobre Talento Tech.")
    # ))

    mensaje = st.chat_input("Escribí tu mensaje:")

    if mensaje:
        actualizar_historial("user", mensaje, "🧑‍💻")

        chat_completo = configurar_modelo(clienteUsuario, modelo, mensaje)

        if chat_completo:
            with st.chat_message("assistant", avatar="🤖"):
                respuesta_completa = generar_respuesta(chat_completo)
                st.markdown(respuesta_completa)
                actualizar_historial("assistant", respuesta_completa, "🤖")

            st.rerun()

if __name__ == "__main__":
    main()

        

