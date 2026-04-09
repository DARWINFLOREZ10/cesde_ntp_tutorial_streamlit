import random
import streamlit as st

st.set_page_config(page_title="Ejercicios", page_icon="🧩")

st.markdown("# 09 - Ejercicios de Streamlit")
st.sidebar.header("Ejercicios")

st.write("Resuelve y prueba cada ejercicio interactuando con los widgets.")

st.divider()

st.header("Ejercicio 1: Saludo Simple")
nombre = st.text_input("Escribe tu nombre")
if nombre.strip():
    st.success(f"¡Hola, {nombre.strip()}!")

st.divider()

st.header("Ejercicio 2: Calculadora de Producto")
numero_1 = st.number_input("Número 1", value=0.0)
numero_2 = st.number_input("Número 2", value=0.0)
resultado_producto = numero_1 * numero_2
st.write(f"Resultado: {resultado_producto}")
if numero_1 > 100 or numero_2 > 100:
    st.warning("Números grandes")

st.divider()

st.header("Ejercicio 3: Convertidor de Temperatura")
direccion = st.radio(
    "Elige la conversión",
    ["Celsius a Fahrenheit", "Fahrenheit a Celsius"],
)
temperatura = st.number_input("Ingresa la temperatura", value=0.0, key="temp_convertidor")

if direccion == "Celsius a Fahrenheit":
    conversion = (temperatura * 9 / 5) + 32
    st.write(f"Resultado: {conversion:.2f} °F")
else:
    conversion = (temperatura - 32) * 5 / 9
    st.write(f"Resultado: {conversion:.2f} °C")

st.divider()

st.header("Ejercicio 4: Galería de Mascotas")
tab_gatos, tab_perros, tab_aves = st.tabs(["Gatos", "Perros", "Aves"])

with tab_gatos:
    st.image("https://placekitten.com/700/350", caption="Gato")
    if st.button("Me gusta", key="like_gato"):
        st.toast("Te gusta esta mascota")

with tab_perros:
    st.image(
        "https://images.dog.ceo/breeds/retriever-golden/n02099601_3004.jpg",
        caption="Perro",
    )
    if st.button("Me gusta", key="like_perro"):
        st.toast("Te gusta esta mascota")

with tab_aves:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/5/5f/Alcedo_atthis_-England_-male-8.jpg",
        caption="Ave",
    )
    if st.button("Me gusta", key="like_ave"):
        st.toast("Te gusta esta mascota")

st.divider()

st.header("Ejercicio 5: Caja de Comentarios")
with st.form("form_comentarios"):
    asunto = st.text_input("Asunto")
    mensaje = st.text_area("Mensaje")
    enviar = st.form_submit_button("Enviar")

if enviar:
    if mensaje.strip():
        st.json({"asunto": asunto, "mensaje": mensaje})
    else:
        st.warning("El mensaje no puede estar vacío")

st.divider()

st.header("Ejercicio 6: Login Simulado")
if "logueado" not in st.session_state:
    st.session_state.logueado = False

if st.session_state.logueado:
    st.success("Ya estás logueado")
    if st.button("Cerrar Sesión"):
        st.session_state.logueado = False
        st.rerun()
else:
    usuario = st.text_input("Usuario", key="login_usuario")
    contrasena = st.text_input("Contraseña", type="password", key="login_password")

    if st.button("Ingresar"):
        if usuario == "admin" and contrasena == "1234":
            st.session_state.logueado = True
            st.success("Ingreso exitoso")
            st.rerun()
        else:
            st.error("Credenciales incorrectas")

st.divider()

st.header("Ejercicio 7: Lista de Compras")
if "lista_compras" not in st.session_state:
    st.session_state.lista_compras = []

producto = st.text_input("Producto", key="producto_lista")
col_agregar, col_limpiar = st.columns(2)

with col_agregar:
    if st.button("Agregar") and producto.strip():
        st.session_state.lista_compras.append(producto.strip())

with col_limpiar:
    if st.button("Limpiar Lista"):
        st.session_state.lista_compras = []

st.write("Productos agregados:")
if st.session_state.lista_compras:
    st.write(st.session_state.lista_compras)
else:
    st.info("La lista está vacía")

st.divider()

st.header("Ejercicio 8: Gráfico Interactivo")
n = st.slider("Selecciona N", min_value=10, max_value=100, value=20)
datos_interactivos = [random.randint(0, 100) for _ in range(n)]
st.line_chart(datos_interactivos)

st.button("Regenerar")
