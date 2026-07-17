import streamlit as st
import streamlit.components.v1 as components
from utils.utils import get_valores_servicos, ToggleNumberInput, apply_css, formata_moeda

st.set_page_config(
    page_title="Calculadora BPO | BRAC",
    page_icon="💼",
    layout="wide",
)

apply_css("assets/style.css")

valores_servicos = get_valores_servicos()

campos_dict = {
    "tesouraria": {
        "label": "Tesouraria",
        "items": {
            "gestao_conta": {
                "label": "Gestão de Conta Bancária",
                "default_toggle": False,
                "help_text": "Coloque a dica aqui",
                "min_value": 1,
                "max_value": 15,
                "step": 1,
                "default_value": 1,
            },

            "gestao_plataforma_recebimento": {
                "label": "Gestão de Plataformas de Recebimento",
                "default_toggle": False,
                "help_text": "Coloque a dica aqui",
                "min_value": 1,
                "max_value": 5,
                "step": 1,
                "default_value": 1,
            },

            "conciliacao_movimentacao": {
                "label": "Conciliação de Movimentação",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 15,
                "step": 1,
                "default_value": 1,
            }
        },
    },

    "faturamento": {
        "label": "Faturamento",
        "items": {
            "emissao_nf": {
                "label": "Emissão de Notas Fiscais (NF)",
                "default_toggle": False,
                "help_text": "",
                "min_value": 5,
                "max_value": 300,
                "step": 5,
                "default_value": 5,
            },
            "relatorio_mensal_faturamento": {
                "label": "Relatório Mensal",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
                "default_value": 1,
            },
        },
    },

    "contas_receber": {
        "label": "Contas à Receber",
        "items": {
            "emissao_boleto": {
                "label": "Emissão de Boleto",
                "default_toggle": False,
                "help_text": "",
                "min_value": 5,
                "max_value": 300,
                "step": 5,
                "default_value": 5,
            },
            "antecipacao_recebiveis": {
                "label": "Antecipação de Recebíveis",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 1,
                "step": 1,
                "default_value": 1,
            },
            "conciliacao_recebimentos": {
                "label": "Conciliação de Recebimentos",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 15,
                "step": 1,
                "default_value": 1,
            },
            "controle_recebimento_cartao": {
                "label": "Controle de Recebimento de Cartão",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 15,
                "step": 1,
                "default_value": 1,
            },
            "atendimento_suporte": {
                "label": "Atendimento e Suporte (Help Desk)",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 2,
                "step": 1,
                "default_value": 1,
            },
            "cobranca_ativa": {
                "label": "Cobrança ativa",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 15,
                "step": 1,
                "default_value": 1,
            },
            "relatorio_mensal_contas_receber": {
                "label": "Relatório Mensal",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
                "default_value": 1,
            },
        },
    },

    "contas_pagar": {
        "label": "Contas à Pagar",
        "items": {
            "agendamento_pagamentos": {
                "label": "Agendamento de Pagamentos",
                "default_toggle": False,
                "help_text": "",
                "min_value": 5,
                "max_value": 300,
                "step": 5,
                "default_value": 5,
            },
            "adiantamento_salarial": {
                "label": "Adiantamento Salarial",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 100,
                "step": 1,
                "default_value": 1,
            },
            "gestao_comprovantes": {
                "label": "Gestão de Comprovantes",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 15,
                "step": 1,
                "default_value": 1,
            },
            "conciliacao_fatura_cartao": {
                "label": "Conciliação de Fatura de Cartão",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 15,
                "step": 1,
                "default_value": 1,
            },
            "relatorio_mensal_contas_pagar": {
                "label": "Relatório Mensal",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
                "default_value": 1,
            },
        },
    },

    "gestao_estoque": {
        "label": "Gestão de Estoque",
        "items": {
            "lancamento_entradas": {
                "label": "Lançamento de Entradas",
                "default_toggle": False,
                "help_text": "",
                "min_value": 5,
                "max_value": 300,
                "step": 5,
                "default_value": 5,
            },
            "conferencia_sistema": {
                "label": "Conferência entre o informado pelo que está no sistema",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 5,
                "step": 1,
                "default_value": 1,
            },
            "analise_cmv": {
                "label": "Análise de CMV (Custo de Mercadoria Vendida)",
                "default_toggle": False,
                "help_text": "",
                "min_value": 5,
                "max_value": 500,
                "step": 5,
                "default_value": 5,
            },
            "relatorio_mensal_gestao_estoque": {
                "label": "Relatório Mensal",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
                "default_value": 1,
            },
        },
    },

    "gestao_contratos": {
        "label": "Gestão de contratos",
        "items": {
            "controle_contratos": {
                "label": "Controle dos contratos",
                "default_toggle": False,
                "help_text": "",
                "min_value": 5,
                "max_value": 300,
                "step": 1,
                "default_value": 5,
            },
            "controle_prazos": {
                "label": "Controle dos prazos de renovação e índices de reajuste",
                "default_toggle": False,
                "help_text": "",
                "min_value": 5,
                "max_value": 300,
                "step": 1,
                "default_value": 5,
            },
            "relatorio_mensal_gestao_contratos": {
                "label": "Relatório Mensal",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
                "default_value": 1,
            },
        },
    },

    "levantamento_resultados": {
        "label": "Levantamento de resultados e métricas",
        "items": {
            "fluxo_caixa": {
                "label": "Fluxo de Caixa",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 5,
                "step": 1,
                "default_value": 1,
            },
            "orcamento": {
                "label": "Orçamento",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 5,
                "step": 1,
                "default_value": 1,
            },
            "dre": {
                "label": "DRE",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 5,
                "step": 1,
                "default_value": 1,
            },
            "relatorio_mensal_levantamento_resultados": {
                "label": "Relatório Mensal",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
                "default_value": 1,
            },
        },
    },

    "contato_contabilidade": {
        "label": "Contato com a contabilidade",
        "items": {
            "entrega_extratos": {
                "label": "Entrega de extratos para o contador",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 15,
                "step": 1,
                "default_value": 1,
            },
            "entrega_fiscal": {
                "label": "Entrega da movimentação fiscal",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 15,
                "step": 1,
                "default_value": 1,
            },
            "entrega_financeira": {
                "label": "Entrega da movimentação financeira",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 15,
                "step": 1,
                "default_value": 1,
            },
            "demanda_contabilidade": {
                "label": "Demanda da contabilidade",
                "default_toggle": False,
                "help_text": "",
                "min_value": 5,
                "max_value": 20,
                "step": 5,
                "default_value": 5,
            },
        },
    },

    "tempo_supervisao": {
        "label": "Tempo de Supervisão",
        "items": {
            "supervisao": {
                "label": "Supervisão",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 1,
                "step": 1,
                "default_value": 1,
            },

            "diretoria": {
                "label": "Diretoria",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 1,
                "step": 1,
                "default_value": 1,
            },
        },
    },

    "sistemas_erp": {
        "label": "Sistemas ERP",
        "items": {
            "d4c": {
                "label": "D4C",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 5,
                "step": 1,
                "default_value": 1,
            },
            "pier": {
                "label": "PIER",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 5,
                "step": 1,
                "default_value": 1,
            },
            "conta_azul": {
                "label": "CONTA AZUL",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 5,
                "step": 1,
                "default_value": 1,
            },
            "omie": {
                "label": "OMIE",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 5,
                "step": 1,
                "default_value": 1,
            },
            "conciliadora": {
                "label": "CONCILIADORA",
                "default_toggle": False,
                "help_text": "",
                "min_value": 1,
                "max_value": 5,
                "step": 1,
                "default_value": 1,
            },
        },
    },
}

pages_list = list(campos_dict.keys())

if "pagina" not in st.session_state:
    st.session_state.pagina = pages_list[0]

current_page = pages_list.index(st.session_state.pagina)

st.markdown("""
<div class="app-header">
    <div class="app-header-brand">
        <span class="app-header-logo">BRAC<span class="app-header-logo-accent">BPO</span></span>
        <span class="app-header-tagline">Organização Financeira</span>
    </div>
    <div class="app-header-title">Calculadora de Proposta — BPO Financeiro</div>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<div class='sidebar-brand'>Serviços</div>", unsafe_allow_html=True)
    for page in pages_list:
        is_active = st.session_state.pagina == page
        if st.button(
            campos_dict[page]["label"],
            use_container_width=True,
            key=f"nav_{page}",
            type="primary" if is_active else "secondary",
        ):
            st.session_state.pagina = page
            st.rerun()
    st.markdown(
        """
        <div class="sidebar-footer">
            Desenvolvido por:
            <a href="mailto:vduarted1994@gmail.com" class="sidebar-footer-link">Victor Diniz</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

components.html(f"""
<script>
function scroll() {{
    const el = parent.document.getElementById("{st.session_state.pagina}");

    if (el) {{
        el.scrollIntoView({{
            behavior: "smooth",
            block: "start"
        }});
    }} else {{
        setTimeout(scroll, 100);
    }}
}}

scroll();
</script>
""", height=1)

valores = {}

for indice, page in enumerate(pages_list, start=1):
    st.markdown(f"<div id='{page}' class='section-anchor'></div>", unsafe_allow_html=True)  # Tag de marca pagina

    with st.container():
        # st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="section-header">
                <span class="section-index">{indice:02d}</span>
                <span class="section-title">{campos_dict[page]["label"]}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        subtotal_secao = 0.0

        for campo, valor in campos_dict[page]["items"].items():
            item = ToggleNumberInput(
                label=valor["label"],
                key_prefix=campo,
                default_toggle=valor["default_toggle"],
                help_text=valor["help_text"],
                min_value=valor["min_value"],
                max_value=valor["max_value"],
                step=valor["step"],
                default_value=valor.get("default_value"),
            )

            valor_calculado = item.render() * valores_servicos.get(valor["label"])
            valores[campo] = valor_calculado
            subtotal_secao += valor_calculado

        st.markdown(
            f"""
            <div class="subtotal-box">
                <span class="subtotal-label">Subtotal — {campos_dict[page]["label"]}</span>
                <span class="subtotal-value">{formata_moeda(subtotal_secao)}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        # st.markdown("</div>", unsafe_allow_html=True)  # fecha section-card

st.markdown(
    f"""
    <div class="total-geral-box">
        <span class="total-geral-label">Valor Total Estimado da Proposta</span>
        <span class="total-geral-value">{formata_moeda(sum(valores.values()))}</span>
    </div>
    """,
    unsafe_allow_html=True,
)

col_slider, col_comissao = st.columns([3, 1], vertical_alignment="bottom")

with col_slider:
    st.markdown(
        """
        <div class="margem-header">
            <div class="margem-icon">%</div>
            <div class="margem-text">
                <span class="margem-eyebrow">Personalize sua Proposta</span>
                <span class="margem-title">Sua Margem de Lucro</span>
                <span class="margem-subtitle">
                    Defina o percentual que será aplicado sobre o valor estimado acima
                    para chegar ao preço final a ser cobrado do seu cliente.
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    margem_lucro = st.slider(
        label="Margem de lucro (%)",
        min_value=0,
        max_value=30,
        value=st.session_state.get("margem_lucro", 20),
        step=1,
        key="margem_lucro",
        label_visibility="collapsed",
    )

valor_total_estimado = sum(valores.values())
valor_final_cliente = valor_total_estimado / (1 - (margem_lucro / 100))
valor_comissao = valor_final_cliente * (margem_lucro / 100)

with col_comissao:
    st.markdown(
        f"""
        <div class="comissao-box">
            <span class="comissao-label">Sua Comissão</span>
            <span class="comissao-value">{formata_moeda(valor_comissao)}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    f"""
    <div class="valor-final-box">
        <span class="valor-final-label">
            Preço Final para o seu Cliente
            <span class="valor-final-margem">(+{margem_lucro}% de margem)</span>
        </span>
        <span class="valor-final-value">{formata_moeda(valor_final_cliente)}</span>
    </div>
    """,
    unsafe_allow_html=True,
)