import streamlit as st
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards
import geopandas as gpd
import pandas as pd

import plotly.express as px

st.set_page_config(page_title='RECOMENDATION DASBOARD',
                   page_icon=":bar_chart:",
                   layout="wide")

dkt=gpd.read_file('kokas_tomoco.geojson')
dkw=gpd.read_file('kokas_mobilewalla.geojson')
dqw=gpd.read_file('qbig_mobilewalla.geojson')
dqt=gpd.read_file('qbig_tomoco.geojson')
com=pd.read_parquet("comparation.parquet")


def plot_px(df, lat,lon,title):
    

    fig1 = px.scatter_mapbox(df, lat=lat, lon=lon,
                    color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=15,
                    mapbox_style="carto-positron",
                            height=600,
                            width=650,
                           title=title)
    
    return fig1

def get_icon_table(value):
    if value == 0:
        return '❌'
    elif value == 1:
        return '✅'



plot_px(dkt, 'latitude','longitude','Casablanka Tamoco 01 Juni 2023')
plot_px(dkw, 'latitude','longitude','Casablanka Mobilewalla 01 Juni 2023')
plot_px(dqt, 'latitude','longitude','QBIG Tamoco 01 Juni 2023')
plot_px(dqw, 'latitude','longitude','QBIG Mobilewalla 01 Juni 2023')

com1=com[com['Category ']=='Attribute Field '].reset_index(drop=True)
com2=com[com['Category '].isin(['Pricing '])].reset_index(drop=True)



com1['Mobilewalla '] = com1['Mobilewalla '].apply(get_icon_table)

com1['Tamoco '] = com1['Tamoco '].apply(get_icon_table)
   
   
st.header('Comparation Attributes')
st.table(com1)

st.header('Comparation Price')
st.table(com2)

st.header('')

st.header('Comparation Total Device ID (Indonesia)')
st.write('01 Juni 2023')
col1,col2= st.columns((1,1))

with col1:
    col1.metric(label='Tamoco',value=29718)
    
with col2:
    col2.metric(label='Mobilewalla',value=3178113)
    

st.header('')
st.header('Comparation People in Building (Casablanka Mall)')
col1,col2= st.columns((1,1))

with col1:
    st.plotly_chart(plot_px(dkt, 'latitude','longitude','Casablanka Tamoco 01 Juni 2023'))
    col1.metric(label='Tamoco',value=len(dkt))
    

with col2:
    st.plotly_chart(plot_px(dkw, 'latitude','longitude','Casablanka Mobilewalla 01 Juni 2023'))
    col2.metric(label='Mobilewalla',value=len(dkw))
    
    
st.header('')

st.header('Comparation People in Building (QBIG Mall)')
col11,col22= st.columns((1,1))



with col11:
    st.plotly_chart(plot_px(dqt, 'latitude','longitude','QBIG Tamoco 01 Juni 2023'))
    col11.metric(label='Tamoco',value=len(dqt))
    
    
with col22:
    st.plotly_chart(plot_px(dqw, 'latitude','longitude','QBIG Mobilewalla 01 Juni 2023'))
    col22.metric(label='Mobilewalla',value=len(dqw))
    
    
    


    
    
style_metric_cards()



# col1, col2, col3 = st.columns(3tr )
# col33, u=st.columns((4,1))
# # col1.metric(label="Gain", value=5000, delta=1000)
# # col2.metric(label="Loss", value=5000, delta=-1000)
# # col3.metric(label="No Change", value=5000, delta=0)
# # style_metric_cards()

       

#     col1.metric(label="Gain", value=5000, delta=1000)
#     col2.metric(label="Loss", value=5000, delta=-1000)
#     col3.metric(label="No Change", value=5000, delta=0)
#     style_metric_cards()
    

