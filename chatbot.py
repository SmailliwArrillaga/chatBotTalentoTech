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

    🤖 **Modelos de IA disponibles:**  
    **1. Llama 3.1 8B Instant** (rápido/eficiente).  
    **2. Llama 3.3 70B Versatile** (más detallado para respuestas complejas).

    💡 *Tip:* probá usar el mismo prompt en ambos modelos y compará sus respuestas.  
    👉 ¿Cuál te resultó más útil? ¿Por qué?
    """)

# ──────────────────────────────────────────────────────────────────────────────
# Mapas de modelos (alias UI → ID real) y compatibilidad con IDs viejos
# ──────────────────────────────────────────────────────────────────────────────
OPCIONES_UI = {
    "⚡ Rápido (Llama 3.1 8B Instant)": "llama-3.1-8b-instant",
    "🧠 Detallado (Llama 3.3 70B Versatile)": "llama-3.3-70b-versatile",
    # Extras opcionales (si están habilitados en tu cuenta):
    "🧪 Reasoning (DeepSeek R1 Distill 70B)": "deepseek-r1-distill-llama-70b",
    "🌿 Gemma 2 9B (IT)": "gemma2-9b-it",
}

ALIAS_ANTIGUOS = {
    "llama3-8b-8192": "llama-3.1-8b-instant",
    "llama3-70b-8192": "llama-3.3-70b-versatile",
}

def normalizar_modelo(mid: str) -> str:
    return ALIAS_ANTIGUOS.get(mid, mid)

# ──────────────────────────────────────────────────────────────────────────────
# Flags de debug (para no mostrar la lista a estudiantes)
# ──────────────────────────────────────────────────────────────────────────────
def _is_debug_models() -> bool:
    """Activa modo debug si:
       - en Secrets: debug_models="1", o
       - en la URL agregás ?debug_models=1
    """
    try:
        if st.secrets.get("debug_models", "0") == "1":
            return True
    except Exception:
        pass
    try:
        params = st.query_params  # Streamlit >= 1.30
    except Exception:
        params = st.experimental_get_query_params()
    return params.get("debug_models", ["0"])[0] == "1"

# ──────────────────────────────────────────────────────────────────────────────
# Cliente Groq
# ──────────────────────────────────────────────────────────────────────────────
def crear_usuario_groq():
    claveSecreta = st.secrets["clave_api"]  # Debe ser gsk_...
    return Groq(api_key=claveSecreta)

# ──────────────────────────────────────────────────────────────────────────────
# Configuración y UI lateral (filtra por modelos habilitados; no muestra lista)
# ──────────────────────────────────────────────────────────────────────────────
def configurar_pagina(cliente_para_listar: Groq) -> str:
    st.sidebar.title("Modelos disponibles")

    # 1) Listar modelos habilitados en la cuenta/organización (sin mostrarlos)
    disponibles = set()
    try:
        disponibles = {m.id for m in cliente_para_listar.models.list().data}
    except Exception:
        st.sidebar.info("No se pudieron listar modelos. Verificá tu clave o permisos.")

    # 2) Filtrar opciones por lo que realmente existe en tu cuenta (si pudimos listar)
    opciones_validas = {label: mid for label, mid in OPCIONES_UI.items() if (not disponibles) or (mid in disponibles)}
    if not opciones_validas:
        st.sidebar.error("No hay modelos compatibles habilitados en tu cuenta.")
        st.stop()

    # 3) Selector limpio para estudiantes (sin warnings)
    etiqueta = st.sidebar.selectbox("Elegí un Modelo", options=list(opciones_validas.keys()), index=0)
    modelo_elegido = opciones_validas[etiqueta]
    st.sidebar.caption(f"Modelo seleccionado: `{modelo_elegido}`")

    # 4) SOLO en modo debug mostramos la lista cruda (para vos)
    if _is_debug_models() and disponibles:
        with st.sidebar.expander("DEBUG: Modelos habilitados", expanded=False):
            st.code("\n".join(sorted(disponibles)), language="text")

    # Sección de actividades (igual que antes)
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

    return modelo_elegido

# ──────────────────────────────────────────────────────────────────────────────
# Llamadas a Groq
# ──────────────────────────────────────────────────────────────────────────────
def configurar_modelo(cliente: Groq, modelo: str, mensajeDeEntrada: str):
    """Llamada en streaming con parámetros seguros y manejo de error."""
    try:
        return cliente.chat.completions.create(
            model=normalizar_modelo(modelo),
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

def test_llamada_simple(cliente: Groq, modelo: str, texto: str):
    """Utilidad de diagnóstico SIN streaming; útil para aislar errores."""
    resp = cliente.chat.completions.create(
        model=normalizar_modelo(modelo),
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
    clienteUsuario = crear_usuario_groq()                  # Crear cliente primero
    modelo = configurar_pagina(clienteUsuario)             # Selector sin mostrar lista (salvo debug)
    inicializar_estado()
    area_chat()

    # Botón de prueba SIN streaming (opcional)
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




