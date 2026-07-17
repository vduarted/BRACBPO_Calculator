import pandas as pd
from urllib.parse import quote
from unicodedata import normalize
from re import sub
import streamlit as st

##################
# Funcoes
##################

def limpa_texto(text : str):
    text = normalize('NFKD', text).encode('ASCII', 'ignore').decode('UTF-8').lower()

    text = sub(r'[^a-z0-9_ ]', '', text)
    text = text.strip()
    text = text.replace(' ', '_')

    return text

@st.cache_data(ttl=300)  # atualiza a cada 5 minutos
def google_sheets_ingestion(file_id:str, sheet_name:str):
    sheet_name = quote(sheet_name)
    url = f"https://docs.google.com/spreadsheets/d/{file_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    df = pd.read_csv(filepath_or_buffer=url, encoding='utf-8', decimal=",")
    df = df.astype(str)
        
    col_dict = {}

    for col in list(df.columns):
        col_dict[col] = limpa_texto(col)

    df = df.rename(columns=col_dict)

    return df

def get_valores_servicos():
    df = google_sheets_ingestion(file_id="1HTDwKqiQCXuNJRCwxJnr_mS2ao32NUi6HXDOAP2ImRc", sheet_name="Serviços")
    df["valor"] = df["valor"].astype(float)
    servicos_dict = df.set_index("tabela_dos_servicos")["valor"].to_dict()

    return servicos_dict

# @st.cache_data
def load_css_cached(file_path: str):
    with open(file_path, encoding="utf-8") as f:
        return f.read()

def apply_css(file_path: str):
    css = load_css_cached(file_path)
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def formata_moeda(valor: float) -> str:
    """Formata um número float no padrão monetário brasileiro (R$ 1.234,56)."""
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"

##################
# Classes
##################

class ToggleNumberInput:
    def __init__(self, label: str, key_prefix: str, default_toggle : bool = False, help_text: str = "", min_value: int = 1, max_value: int = 100, step: int = 1, default_value: int = None):
        self.label = label
        self.key_toggle = f"{key_prefix}_toggle"
        self.key_value = f"{key_prefix}_value"
        self.default_toggle = default_toggle
        self.help_text = help_text
        self.min_value = min_value
        self.max_value = max_value
        self.step = step
        self.default_value = default_value if default_value is not None else min_value

    def render(self):
        col1, col2 = st.columns([13,3])

        with col1:
            toggle_value = st.toggle(label=self.label, value=self.default_toggle, key=self.key_toggle, help=self.help_text)
    
        with col2:
            value = st.number_input(label=self.label, label_visibility="collapsed", min_value=self.min_value, max_value=self.max_value, step=self.step, value=self.default_value, key=self.key_value, disabled=not toggle_value)

        if toggle_value:
            return value
        else:
            return 0