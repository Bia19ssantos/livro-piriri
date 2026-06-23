import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Piriri e o Livro Perdido", layout="wide")

st.markdown("<h1 style='text-align:center;'>Piriri e o Livro Perdido</h1>", unsafe_allow_html=True)

pages_dir = Path("pages")
pages = sorted(list(pages_dir.glob("*.png")) + list(pages_dir.glob("*.jpg")) + list(pages_dir.glob("*.jpeg")))

if not pages:
    st.error("Nenhuma imagem foi encontrada na pasta 'pages'. Verifique se as páginas do livro estão dentro dessa pasta.")
    st.stop()

if "page" not in st.session_state:
    st.session_state.page = 0

if st.session_state.page < 0:
    st.session_state.page = 0

if st.session_state.page >= len(pages):
    st.session_state.page = len(pages) - 1

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
    st.image(str(pages[st.session_state.page]), use_container_width=True)
    st.markdown(
        f"<p style='text-align:center;'>Página {st.session_state.page + 1} de {len(pages)}</p>",
        unsafe_allow_html=True
    )
