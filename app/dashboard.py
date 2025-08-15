import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet

# --- Configuração da página ---
st.set_page_config(page_title='Monitor de Sustentabilidade Urbana', layout='wide')
st.title('🌱 Monitor de Sustentabilidade Urbana')
st.markdown("Painel interativo de indicadores urbanos: poluição, trânsito e áreas verdes.")

# --- Carregar dados ---
@st.cache_data
def load_data():
    return pd.read_csv('data/dados.csv')

data = load_data()

# --- Verificações iniciais ---
if data.empty:
    st.error("Dados não encontrados ou CSV vazio!")
    st.stop()

# --- Conversão de datas ---
data['dia'] = pd.to_datetime(data['dia'], errors='coerce')
data = data.dropna(subset=['dia'])

# --- Filtros ---
st.sidebar.header('Filtros')
indicador = st.sidebar.selectbox(
    'Escolha o indicador para análise:',
    ['poluicao', 'transito', 'areas_verdes']
)

# Intervalo de datas
min_data = data['dia'].min()
max_data = data['dia'].max()
intervalo = st.sidebar.date_input('Período', [min_data, max_data], min_value=min_data, max_value=max_data)

if len(intervalo) == 2:
    data = data[(data['dia'] >= pd.to_datetime(intervalo[0])) & 
                (data['dia'] <= pd.to_datetime(intervalo[1]))]

if data.empty:
    st.warning("Nenhum dado encontrado no período selecionado.")
    st.stop()

# --- Gráfico principal ---
st.subheader(f'📈 {indicador.capitalize()} ao longo do tempo')

cores = {
    'poluicao': 'red',
    'transito': 'orange',
    'areas_verdes': 'green'
}

fig = px.line(
    data,
    x='dia',
    y=indicador,
    title=f'{indicador.capitalize()} ao longo do tempo',
    markers=True,
    color_discrete_sequence=[cores[indicador]],
    labels={indicador: f'{indicador.capitalize()}', 'dia':'Data'}
)
fig.update_layout(title_x=0.5, template='plotly_white')
st.plotly_chart(fig, use_container_width=True)

# --- Métricas principais ---
col1, col2, col3 = st.columns(3)
col1.metric('📈 Valor Máximo', f'{data[indicador].max():,.0f}')
col2.metric('📉 Valor Mínimo', f'{data[indicador].min():,.0f}')
col3.metric('📊 Média', f'{data[indicador].mean():.2f}')

# --- Comparação de indicadores ---
st.subheader('📊 Comparação entre indicadores')
comparar = st.multiselect(
    'Selecione indicadores para comparação:', 
    ['poluicao', 'transito', 'areas_verdes'], 
    default=['poluicao', 'transito']
)
if comparar:
    cores_comp = [cores[i] for i in comparar]
    fig_comp = px.line(
        data, 
        x='dia', 
        y=comparar, 
        markers=True,
        color_discrete_sequence=cores_comp,
        labels={'value':'Valor','variable':'Indicador','dia':'Data'},
        title='Comparação de indicadores'
    )
    fig_comp.update_layout(title_x=0.5, template='plotly_white')
    st.plotly_chart(fig_comp, use_container_width=True)

# --- Matriz de correlação ---
st.subheader('🔍 Matriz de Correlação')
correlacao = data[['poluicao','transito','areas_verdes']].corr()
fig_corr = px.imshow(
    correlacao, 
    text_auto=True, 
    color_continuous_scale='RdBu_r',
    title='Correlação entre indicadores'
)
fig_corr.update_layout(title_x=0.5, template='plotly_white')
st.plotly_chart(fig_corr, use_container_width=True)

# --- Previsão com Prophet ---
st.subheader('📈 Previsão Avançada (Prophet)')
dias_prever = st.slider('Quantos dias deseja prever?', 7, 60, 14)

df_prophet = data[['dia', indicador]].rename(columns={'dia':'ds', indicador:'y'})
modelo = Prophet(daily_seasonality=True)
modelo.fit(df_prophet)

futuro = modelo.make_future_dataframe(periods=dias_prever)
previsao = modelo.predict(futuro)

# Gráfico da previsão estilizado
fig_forecast = px.line(
    previsao, 
    x='ds', 
    y='yhat', 
    title=f'Previsão para {indicador}', 
    labels={'yhat':'Previsão','ds':'Data'},
    color_discrete_sequence=[cores[indicador]]
)
fig_forecast.add_scatter(
    x=df_prophet['ds'], 
    y=df_prophet['y'], 
    mode='markers', 
    name='Valores reais',
    marker=dict(color='black', size=6)
)
fig_forecast.update_layout(title_x=0.5, template='plotly_white')
st.plotly_chart(fig_forecast, use_container_width=True)

# Tabela de previsões
st.subheader('📅 Valores previstos')
st.dataframe(previsao[['ds','yhat','yhat_lower','yhat_upper']])

# --- Tabela de dados final ---
st.subheader('📄 Dados utilizados')
st.dataframe(data)
