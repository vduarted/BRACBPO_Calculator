import streamlit as st
from utils.utils import get_valores_servicos, ToggleNumberInput, apply_css

st.set_page_config(layout="wide")

# apply_css("assets/style.css")

valores_servicos = get_valores_servicos()

campos_dict = {
    "tesouraria": {
        "label": "Tesouraria",
        "items": {
            "gestao_conta": {
                "label": "Gestão de Conta Bancária",
                "default_toggle": True,
                "help_text": "Coloque a dica aqui",
                "min_value": 1,
                "max_value": 5,
                "step": 1,
            },

            "gestao_plataforma_recebimento": {
                "label": "Gestão de Plataformas de Recebimento",
                "default_toggle": True,
                "help_text": "Coloque a dica aqui",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },

            "conciliacao_movimentacao": {
                "label": "Conciliação de Movimentação",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            }
        },
    },

    "faturamento": {
        "label": "Faturamento",
        "items": {
            "emissao_nf": {
                "label": "Emissão de Notas Fiscais (NF)",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "relatorio_mensal_faturamento": {
                "label": "Relatório Mensal",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
        },
    },

    "contas_receber": {
        "label": "Contas à Receber",
        "items": {
            "emissao_boleto": {
                "label": "Emissão de Boleto",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "antecipacao_recebiveis": {
                "label": "Antecipação de Recebíveis",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "conciliacao_recebimentos": {
                "label": "Conciliação de Recebimentos",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "controle_recebimento_cartao": {
                "label": "Controle de Recebimento de Cartão",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "atendimento_suporte": {
                "label": "Atendimento e Suporte (Help Desk)",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "cobranca_ativa": {
                "label": "Cobrança ativa",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "relatorio_mensal_contas_receber": {
                "label": "Relatório Mensal",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
        },
    },

    "contas_pagar": {
        "label": "Contas à Pagar",
        "items": {
            "agendamento_pagamentos": {
                "label": "Agendamento de Pagamentos",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "adiantamento_salarial": {
                "label": "Adiantamento Salarial",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "gestao_comprovantes": {
                "label": "Gestão de Comprovantes",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "conciliacao_fatura_cartao": {
                "label": "Conciliação de Fatura de Cartão:",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "relatorio_mensal_contas_pagar": {
                "label": "Relatório Mensal",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
        },
    },

    "gestao_estoque": {
        "label": "Gestão de Estoque",
        "items": {
            "lancamento_entradas": {
                "label": "Lançamento de Entradas",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "conferencia_sistema": {
                "label": "Conferência entre o informado pelo que está no sistema",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "analise_cmv": {
                "label": "Análise de CMV (Custo de Mercadoria Vendida)",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
        },
    },

    "gestao_contratos": {
        "label": "Gestão de contratos",
        "items": {
            "controle_saldos_contrato": {
                "label": "Controle dos saldos do contrato",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "controle_apuracao_receitas": {
                "label": "Controle da apuração de receitas",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "controle_prazos": {
                "label": "Controle dos prazos de renovação e índices de reajuste.",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "relatorio_mensal_gestao_contratos": {
                "label": "Relatório Mensal",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
        },
    },

    "levantamento_resultados": {
        "label": "Levantamento de resultados e métricas",
        "items": {
            "fluxo_caixa": {
                "label": "Fluxo de Caixa",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "orcamento": {
                "label": "Orçamento",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "dre": {
                "label": "DRE",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "relatorio_mensal_levantamento_resultados": {
                "label": "Relatório Mensal",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
        },
    },

    "contato_contabilidade": {
        "label": "Contato com a contabilidade",
        "items": {
            "entrega_extratos": {
                "label": "Entrega de extratos para o contador",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "entrega_fiscal": {
                "label": "Entrega da movimentação fiscal",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "entrega_financeira": {
                "label": "Entrega da movimentação finaceira",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "demanda_contabilidade": {
                "label": "Demanda da contabilidade",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
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
                "max_value": 3,
                "step": 1,
            },

            "diretoria": {
                "label": "Diretoria",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
        },
    },

    "sistemas_erp": {
        "label": "Sistemas ERP",
        "items": {
            "d4c": {
                "label": "D4C",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "pier": {
                "label": "PIER",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "conta_azul": {
                "label": "CONTA AZUL",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "omie": {
                "label": "OMIE",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
            "conciliadora": {
                "label": "CONCILIADORA",
                "default_toggle": True,
                "help_text": "",
                "min_value": 1,
                "max_value": 3,
                "step": 1,
            },
        },
    },
}

pages_list = list(campos_dict.keys())

if "pagina" not in st.session_state:
    st.session_state.pagina = pages_list[0]

current_page = pages_list.index(st.session_state.pagina)

with st.sidebar:
    st.write("""<div class='SideBarCustom'></div>""", unsafe_allow_html=True)
    for page in pages_list:
        if st.button(campos_dict[page]["label"], use_container_width=True):
            st.session_state.pagina = page

st.iframe(f"""
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

for page in pages_list:
    st.markdown(f"""<div id='{page}' style="position:relative; top:-30px;""></div>""", unsafe_allow_html=True) # Tag de marca pagina
    st.header(campos_dict[page]["label"])

    for campo, valor in campos_dict[page]["items"].items():
        item = ToggleNumberInput(
            label=valor["label"],
            key_prefix=campo,
            default_toggle=valor["default_toggle"],
            help_text=valor["help_text"],
            min_value=valor["min_value"],
            max_value=valor["max_value"],
            step=valor["step"],
        )

        valores[campo] = item.render() * valores_servicos.get(valor["label"])

st.warning(sum(valores.values()))