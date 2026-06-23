from pathlib import Path
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Piriri e o Livro Perdido", layout="wide")

st.markdown("<h1 style='text-align:center;'>Piriri e o Livro Perdido</h1>", unsafe_allow_html=True)

pages = sorted(Path("pages").glob("*.png"))

if not pages:
    st.error("Nenhuma imagem encontrada na pasta pages.")
    st.stop()

if "page" not in st.session_state:
    st.session_state.page = 0

st.session_state.page = max(0, min(st.session_state.page, len(pages) - 1))

col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    if st.button("⬅️ Anterior", disabled=st.session_state.page == 0):
        st.session_state.page -= 1
        st.rerun()

with col3:
    if st.button("Próxima ➡️", disabled=st.session_state.page == len(pages) - 1):
        st.session_state.page += 1
        st.rerun()

with col2:
    img = Image.open(pages[st.session_state.page])
    img.thumbnail((1600, 1600))
    st.image(img, use_container_width=True)

st.markdown(
    f"<p style='text-align:center;'>Página {st.session_state.page + 1} de {len(pages)}</p>",
    unsafe_allow_html=True
)
