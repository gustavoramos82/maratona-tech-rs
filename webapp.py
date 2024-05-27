# Este será o código do webapp, na qual será feita o mvp

## Importando as bliniotecas

import streamlit as st
import pandas as pd
import plotly.express as px

## Importando o datasets

##Url das barragens

url = 'https://raw.githubusercontent.com/gustavoramos82/maratona-tech-rs/main/Datasets%20Utilizados/Datframe-padrao-ouro.csv'
barragem_rs = pd.read_csv(url,encoding='latin1')

url2 = 'https://raw.githubusercontent.com/gustavoramos82/maratona-tech-rs/main/Datasets%20Utilizados/Reser%20barra%20grande.csv'
reserva_defluencia = pd.read_csv(url2)
reserva_defluencia['data'] = pd.to_datetime(reserva_defluencia['data'],format='%Y-%m-%d')

url3 = 'https://raw.githubusercontent.com/gustavoramos82/maratona-tech-rs/main/Datasets%20Utilizados/Previs%C3%A3o%20Sarima%20defluencia.csv'
previsao = pd.read_csv(url3)

topicos = ['Sobre o projeto','Análise inicial','Análise por mapa','Previsão']

barra_lateral = st.sidebar.empty()
estado_sel = st.sidebar.selectbox('Selecione as opções para as base de dados ou para acessar os tópicos',
                                  topicos)


### Tópico sobre o projeto

if estado_sel == topicos[0]:
    st.header('Hidrus')      
    st.subheader('monitoramento completo para máxima eficiência')  
    
    st.image('https://github.com/gustavoramos82/maratona-tech-rs/assets/39843884/fc92b5cb-689e-4f65-9250-53682dc7fd87',
             width=400)

    st.markdown('Neste mvp faremos uma análise de barragens de hidrelétrica ter mais facilidade no acesso de insigths')
    st.markdown('e pessoas, organizações, empresas e governo a se apoiar em suas decisões') 
    
    st.markdown('Amostras das barragens que tem o Rio Grande do sul')
    
    mostra_barragem = fig = px.scatter_mapbox(barragem_rs,lat='NumCoordNEmpreendimento',lon='NumCoordEEmpreendimento',color='DscDanoPotencialGeral',
                     hover_name='NomUsina', hover_data=['NomEmpresa','DscTipo','DscTipoConstrucaoBarragem'],
                     color_discrete_sequence=px.colors.qualitative.G10,
                     title='Barragens hidrelétricas no Rio Grande do Sul')
    mostra_barragem.update_layout(mapbox_style="open-street-map")
    
    st.plotly_chart(mostra_barragem)

### Tópico por Análise de mapa

if estado_sel == topicos[1]:
    
    st.header('Análise dos dados')
    
    st.markdown('Aqui está alguns grádico que podemos nos guiar')
    st.markdown('Neste MVP vamos da enfase a fazer em torno do dano em potencial que cada um apresenta')
    
    dano = px.histogram(barragem_rs,x='DscDanoPotencialGeral',title='Dano potencial das barragens',
                        labels={'count':'Quantidade','DscDanoPotencialGeral':'Nível do dano'})
    
    st.plotly_chart(dano)
    
    dano_sub_bacia = px.histogram(barragem_rs,y='DscSubBacia',color='DscDanoPotencialGeral',
                                  labels={'DscSubBacia':'Sub bacia','DscDanoPotencialGeral':'Dano potencial',
                                          'count':'Quantidade'},
                                  title="Dano de acordo com a sub bacia",barmode = 'group')
    
    st.plotly_chart(dano_sub_bacia)
    
    tipo_geracao = px.histogram(barragem_rs,x='SigTipoGeracao',color='DscDanoPotencialGeral',
                                  labels={'SigTipoGeracao':'Tipo de geração','DscDanoPotencialGeral':'Dano potencial',
                                          'count':'Quantidade'},
                                  title="Dano de acordo com a Tipo de geração da hidrelétrica",
                                  barmode = 'group')
    
    st.plotly_chart(tipo_geracao)
    
    tipo_contrucao = px.histogram(barragem_rs,y='DscTipoConstrucaoBarragem',color='DscDanoPotencialGeral',
                                  labels={'DscTipoConstrucaoBarragem':'Tipo','DscDanoPotencialGeral':'Dano potencial',
                                          'count':'Quantidade'},
                                  title="Dano de acordo com a Tipo de construção da hidreléterica",
                                  barmode = 'group')
    st.plotly_chart(tipo_contrucao)

    scat_gera_po = px.scatter(barragem_rs,x='MdaPotenciaOutorgadaKw',y='MdaGarantiaFisicaKw',color='DscDanoPotencialGeral',
          labels={'MdaPotenciaOutorgadaKw':'Potência total','MdaGarantiaFisicaKw':'Garantia Física',
                  'DscDanoPotencialGeral':'Potencial de dano'},
           title='Garantia física pela potência total outorgada de acordo com o dano')
    st.plotly_chart(scat_gera_po)
    
    comprimento = px.scatter(barragem_rs,x='MdaComprimento',y='MdaAlturaMacicoFundacao',color='DscDanoPotencialGeral',
          labels={'MdaComprimento':'Comprimento do barramento','MdaAlturaMacicoFundacao':'Altura do maciço (fundação)',
                  'DscDanoPotencialGeral':'Potencial de dano'},
           title='Comprimento do barramento pela Altura do maciço a partir da fundação',
           barmode = 'group')
    
    st.plotly_chart(comprimento)
    

##  Análise de mapas

if estado_sel == topicos[2]:
    
    mapa_dano = px.scatter_mapbox(barragem_rs,lat='NumCoordNEmpreendimento',lon='NumCoordEEmpreendimento',color='DscDanoPotencialGeral',
                     hover_name='NomUsina', hover_data=['NomEmpresa','DscTipo','DscTipoConstrucaoBarragem'],
                     color_discrete_sequence=px.colors.qualitative.G10,
                     title='Mapa das barragens de acordo com o dano')
    mapa_dano.update_layout(mapbox_style="open-street-map")
    
    st.plotly_chart(mapa_dano)
    
    mapa_dano_com = px.scatter_geo(barragem_rs,lat='NumCoordNEmpreendimento',lon='NumCoordEEmpreendimento',size='MdaAlturaMacicoFundacao',
                                   color='DscDanoPotencialGeral',hover_name='NomUsina', hover_data=['NomEmpresa','DscTipo','DscTipoConstrucaoBarragem'],
                                   color_discrete_sequence=px.colors.qualitative.G10,
                                   title='Comprimento do barramento em relação ao dano associado')
    mapa_dano_com.update_layout(mapbox_style="open-street-map")
    
    st.plotly_chart(mapa_dano_com)
    
    mapa_dano_po = px.scatter_geo(barragem_rs,lat='NumCoordNEmpreendimento',lon='NumCoordEEmpreendimento',size='MdaPotenciaOutorgadaKw',
                                   color='DscDanoPotencialGeral',hover_name='NomUsina', hover_data=['NomEmpresa','DscTipo','DscTipoConstrucaoBarragem'],
                                   color_discrete_sequence=px.colors.qualitative.G10,
                                   title='Potencial de geração em relação ao dano associado')
    mapa_dano_po.update_layout(mapbox_style="open-street-map")
    
    st.plotly_chart(mapa_dano_po)
    
##  Previsão

if estado_sel == topicos[3]:
        
        st.header('Previsão de defluencia')
        
        st.markdown('Agora é uma amostra de como seria as previsões, neste caso pegamos de uma varavel')
        st.markdown('cujo objetivo é prver uma possivel inundação de reservatorio e pode mexer nas estrutra das barragens')
        st.markdown('O escolhido foi o Barra Grande do Rio Grande do Sul e foi utiizado o modelo Sarima para previsão')
        
        defluencia_rio = px.line(reserva_defluencia,x='data',y='defluencia',labels={'data':'Data','defluencia':'Defluencia'},
                                 title='Defluencia do reservatorio Barra Grande')
        st.plotly_chart(defluencia_rio)
        
        st.markdown('A partir disso geramos um previsão de 30 dias')
        
        prev = px.line(previsao,x=previsao.index,y='predicted_mean',labels={'index':'Dia','predicted_mean':'Defluencia prevista'},
                                 title='Previsão da defluencia do reservatorio Barra Grande')
        st.plotly_chart(prev)