
# 🌱 Monitor de Sustentabilidade Urbana

Painel interativo que monitora indicadores urbanos como **poluição**, **trânsito** e **áreas verdes**, com análise histórica e previsão futura usando **Python**, **Streamlit**, **Plotly** e **Prophet**.

---

## 🔹 Funcionalidades

- Visualização temporal de indicadores urbanos.
- Filtros por período de datas.
- Comparação entre diferentes indicadores.
- Matriz de correlação entre os indicadores.
- Previsão futura de indicadores com Prophet.
- Métricas principais: máximo, mínimo e média.
- Tabela de dados utilizada e tabela de previsão.

---

## 💻 Tecnologias Utilizadas

- Python 3.10+
- Streamlit — criação do dashboard interativo
- Plotly — gráficos interativos
- Prophet — previsão de séries temporais
- Pandas — manipulação de dados

---

## 📂 Estrutura do Projeto
````
monitor-sustentabilidade-urbana/
│
├── app/
│   └── dashboard.py        # Código principal do dashboard
│
├── data/
│   └── dados_exemplo.csv   # Exemplo de dados (não sensíveis)
│
├── requirements.txt        # Dependências do projeto
├── .gitignore
└── README.md
````
---

## 🚀 Como Rodar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/ZaraTakion/monitor-sustentabilidade-urbana.git
cd monitor-sustentabilidade-urbana
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o dashboard:

```bash
streamlit run app/dashboard.py
```

5. Abra o link exibido no terminal (geralmente http://localhost:8501) para interagir com o painel.

---

## 📊 Visualizações do Dashboard

- Gráfico temporal do indicador selecionado  
- Comparação de indicadores  
- Matriz de correlação  
- Previsão futura de indicadores  

*(Adicione prints ou GIFs do dashboard aqui para deixar mais visual e atrativo)*

---

## ⚡ Dicas de Portfólio

- Mostre os gráficos interativos em ação com GIFs.
- Destaque o uso do Prophet para previsão — é um diferencial.
- Explique a utilidade prática do dashboard: análise de sustentabilidade urbana.

---

## 📌 Licença

MIT License
