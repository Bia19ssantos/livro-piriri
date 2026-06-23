from pathlib import Path
from PIL import Image
import streamlit as st
import base64
from io import BytesIO

st.set_page_config(page_title="Piriri e o Livro Perdido", layout="wide")

PAGES_DIR = Path("pages")
image_files = sorted(PAGES_DIR.glob("*.png"))

if not image_files:
    st.error("Nenhuma imagem encontrada na pasta pages.")
    st.stop()


def image_to_base64(path):
    img = Image.open(path).convert("RGB")
    img.thumbnail((1300, 1300))

    buffer = BytesIO()
    img.save(buffer, format="JPEG", quality=85)
    return base64.b64encode(buffer.getvalue()).decode()


pages_base64 = []

for file in image_files:
    try:
        pages_base64.append(image_to_base64(file))
    except Exception:
        st.warning(f"Imagem ignorada porque está com erro: {file.name}")

if not pages_base64:
    st.error("Nenhuma imagem válida foi encontrada.")
    st.stop()

pages_js = str(pages_base64)

html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{
    margin: 0;
    background: #0e1117;
    font-family: Arial, sans-serif;
    color: white;
}}

.title {{
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #f3b35a;
    margin: 25px 0;
}}

.controls {{
    display: flex;
    justify-content: space-between;
    margin: 0 40px 20px 40px;
}}

button {{
    background: #161b22;
    color: white;
    border: 1px solid #444;
    border-radius: 8px;
    padding: 12px 20px;
    font-size: 16px;
    cursor: pointer;
}}

button:hover {{
    background: #2b313a;
}}

.book {{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 0;
    margin: auto;
    max-width: 1400px;
}}

.page {{
    width: 48%;
    background: #f5ead4;
    padding: 18px;
    box-shadow: 0 0 25px rgba(0,0,0,0.6);
    cursor: pointer;
}}

.left {{
    border-radius: 10px 0 0 10px;
    border-right: 2px solid #bda77a;
}}

.right {{
    border-radius: 0 10px 10px 0;
    border-left: 2px solid #bda77a;
}}

.page img {{
    width: 100%;
    height: auto;
    display: block;
}}

.counter {{
    text-align: center;
    margin-top: 20px;
    font-size: 18px;
    color: #ddd;
}}

.hint {{
    text-align: center;
    margin-top: 10px;
    color: #999;
    font-size: 14px;
}}
</style>
</head>

<body>

<div class="title">Piriri e o Livro Perdido</div>

<div class="controls">
    <button onclick="previousPage()">⬅️ Anterior</button>
    <button onclick="nextPage()">Próxima ➡️</button>
</div>

<div class="book">
    <div class="page left" onclick="previousPage()">
        <img id="leftPage">
    </div>

    <div class="page right" onclick="nextPage()">
        <img id="rightPage">
    </div>
</div>

<div class="counter" id="counter"></div>
<div class="hint">Use as setas do teclado ← → ou clique nas páginas para virar.</div>

<script>
let pages = {pages_js};
let currentPage = 0;

function showPages() {{
    document.getElementById("leftPage").src = "data:image/jpeg;base64," + pages[currentPage];

    if (currentPage + 1 < pages.length) {{
        document.getElementById("rightPage").src = "data:image/jpeg;base64," + pages[currentPage + 1];
        document.getElementById("rightPage").style.visibility = "visible";
    }} else {{
        document.getElementById("rightPage").style.visibility = "hidden";
    }}

    let lastPage = Math.min(currentPage + 2, pages.length);
    document.getElementById("counter").innerHTML =
        "Páginas " + (currentPage + 1) + " - " + lastPage + " de " + pages.length;
}}

function nextPage() {{
    if (currentPage + 2 < pages.length) {{
        currentPage += 2;
        showPages();
    }}
}}

function previousPage() {{
    if (currentPage - 2 >= 0) {{
        currentPage -= 2;
        showPages();
    }}
}}

document.addEventListener("keydown", function(event) {{
    if (event.key === "ArrowRight") {{
        nextPage();
    }}

    if (event.key === "ArrowLeft") {{
        previousPage();
    }}
}});

showPages();
</script>

</body>
</html>
"""

st.components.v1.html(html, height=950, scrolling=False)
