import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("¡Deja volar tu imaginación y dibuja!")
bg_color = '#000000'

with st.sidebar:
    stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
    drawing_mode = st.selectbox(
    "How would you like to be contacted?",
    ("freedraw", "line", "rect"),
    )
    stroke_color = st.color_picker("Pick A Color", "#00f900")
    
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=200,
    width=200,
    key="canvas",
)
