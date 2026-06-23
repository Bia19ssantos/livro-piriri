import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Piriri e o Livro Perdido",
    layout="wide"
)

st.markdown("""
<style>
body {
    background-color: #f7efe2;
}
.book-title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #5b3a1e;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="book-title">Piriri e o Livro Perdido</div>', unsafe_allow_html=True)

pages = sorted(Path("pages").glob("*.png"))

if "page" not in st.session_state:
    st.session_state.page = 0

col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    if st.button("⬅️ Anterior") and st.session_state.page > 0:
        st.session_state.page -= 1

with col3:
    if st.button("Próxima ➡️") and st.session_state.page < len(pages) - 1:
        st.session_state.page += 1

with col2:
    st.image(str(pages[st.session_state.page]), use_container_width=True)
    st.markdown(
        f"<p style='text-align:center;'>Página {st.session_state.page + 1} de {len(pages)}</p>",
        unsafe_allow_html=True
    )