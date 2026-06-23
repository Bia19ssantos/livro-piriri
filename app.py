from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Piriri e o Livro Perdido",
    layout="wide"
)

st.title("Piriri e o Livro Perdido")

pages_dir = Path("pages")

pages = sorted(pages_dir.glob("*.png"))

if len(pages) == 0:
    st.error("Nenhuma página encontrada na pasta pages.")
    st.stop()

if "page" not in st.session_state:
    st.session_state.page = 0

col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    if st.button("⬅️ Anterior"):
        st.session_state.page = max(0, st.session_state.page - 1)

with col3:
    if st.button("Próxima ➡️"):
        st.session_state.page = min(
            len(pages) - 1,
            st.session_state.page + 1
        )

with col2:
    st.image(
        str(pages[st.session_state.page]),
        use_container_width=True
    )

st.markdown(
    f"Página {st.session_state.page + 1} de {len(pages)}"
)
