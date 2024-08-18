import streamlit as st
import pandas as pd
import numpy as np

# import CSV file :-
df = pd.read_csv('Namuna9_2024-25_Final.csv').set_index('मालमत्ता_क्रमांक')

# set page configuration:-
st.set_page_config(layout='wide', page_title='gpKamod')

# define columns
col,col0 = st.columns(2)
col1,col2, = st.columns(2)
col3,col4,col5,col6 ,col7= st.columns(5)
col8,col9= st.columns(2)
col10,col11,col12 =st.columns(3)
col13,col14, col15 =st.columns(3)

# create function for owner
def load_owner_details(owner):
# load details
    st.subheader('कर आकारणी व मागणी तपशील')
    Details = df[df['मालमत्ता_धारकाचे_नाव'].str.contains(owner)]
    st.dataframe(Details)
    with col:
        st.subheader(owner)
    with col1:
        st.subheader("")
        st.subheader('एकूण वसूली')
        total_recovery = df[df['मालमत्ता_धारकाचे_नाव'].str.contains(owner)][['एकूण_एकंदर_वसूली']].sum()
        st.metric('',total_recovery)
    with col2:
        st.subheader("")
        st.subheader('एकूण येणे बाकी')
        total_Dues = df[df['मालमत्ता_धारकाचे_नाव'].str.contains(owner)][['एकूण_येणे_बाकी ']].sum()
        st.metric('',total_Dues)
    with col3:
        st.subheader("")
        st.subheader('मागील कर मागणी')
        Detail2 = df[df['मालमत्ता_धारकाचे_नाव'].str.contains(owner)][['मागील_घरपट्टी_कर', 'मागील_दिवाबत्ती_कर', 'मागील_आरोग्य_कर', 'मागील_पाणीपट्टी_कर']].sum()
        st.dataframe(Detail2)
    with col4:
        st.subheader("")
        st.subheader('चालू कर मागणी')
        Detail1 = df[df['मालमत्ता_धारकाचे_नाव'].str.contains(owner)][['चालू_घरपट्टी_कर','चालू_दिवाबत्ती_कर','चालू_आरोग्य_कर', 'चालू_पाणीपट्टी_कर']].sum()
        st.dataframe(Detail1)
    with col5:
        st.subheader("")
        st.subheader('मागील कर वसुली')
        Detail3 = df[df['मालमत्ता_धारकाचे_नाव'].str.contains(owner)][['मागील_घरपट्टी_कर_वसूली', 'मागील_दिवाबत्ती_कर_वसूली', 'मागील_आरोग्य_कर_वसूली','मागील_पाणीपट्टी_कर_वसूली']].sum()
        st.dataframe(Detail3)
    with col6:
        st.subheader("")
        st.subheader('चालू कर वसुली')
        Detail3 = df[df['मालमत्ता_धारकाचे_नाव'].str.contains(owner)][['चालू_घरपट्टी_कर_वसूली','चालू_दिवाबत्ती_कर_वसूली','चालू_आरोग्य_कर_वसूली', 'चालू_पाणीपट्टी_कर_वसूली']].sum()
        st.dataframe(Detail3)
    with col7:
        st.subheader("")
        st.subheader('कर येणे बाकी')
        Detail3 = df[df['मालमत्ता_धारकाचे_नाव'].str.contains(owner)][['येणे_बाकी_घरपट्टी','येणे_बाकी_दिवाबत्ती','येणे_बाकी_आरोग्य', 'येणे_बाकी_पाणीपट्टी']].sum()
        st.dataframe(Detail3)

# All Report section :-
option = st.sidebar.selectbox('रिपोर्टचा प्रकार निवडा',['संपूर्ण_रिपोर्ट','मालमत्ता_धारकाचे_नावानुसार_रिपोर्ट','पाड्याच्या_नावानुसार_रिपोर्ट'])
if option == "संपूर्ण_रिपोर्ट":
    with col8:
        st.title('सन 2024-25 कर मागणी रिपोर्ट')
    with col10:
        st.subheader("")
        All_total = df['एकूण_एकंदर'].sum()
        st.metric('एकूण एकंदर कर मागणी', All_total)
    with col11:
        st.subheader("")
        Due_total = df['मागील_एकूण'].sum()
        st.metric('एकूण मागील कर मागणी', Due_total)
    with col12:
        st.subheader("")
        current_total = df['चालू_एकूण'].sum()
        st.metric('एकूण चालू कर मागणी',current_total)
# पाड्यानिहाय खातेदारांची संख्या
    with col13:
        st.title("")
        st.subheader('वस्ती/ पाड्यानिहाय \n खातेदारांची संख्या')
        new = df.groupby('पाड्याचे_नाव')['मालमत्ता_धारकाचे_नाव'].count()
        Area_count = pd.DataFrame(new).rename(columns={'मालमत्ता_धारकाचे_नाव': 'घरांची संख्या'})
        st.dataframe(Area_count)
# पाड्यानिहाय खातेदारांची एकूण कर मागणी
    with col14:
        st.title("")
        st.subheader('वस्ती/ पाड्यानिहाय \n एकूण कर मागणी ')
        new = df.groupby('पाड्याचे_नाव')['एकूण_एकंदर'].sum()
        Area_demand = pd.DataFrame(new)
        st.dataframe(Area_demand)
# पाड्यानिहाय खातेदारांची एकूण कर वसुली
    with col15:
        st.title("")
        st.subheader('वस्ती/ पाड्यानिहाय \n एकूण कर वसुली')
        new = df.groupby('पाड्याचे_नाव')['एकूण_एकंदर_वसूली'].sum()
        Area_recov = pd.DataFrame(new)
        st.dataframe(Area_recov)

    #st.dataframe(df)
elif option == 'मालमत्ता_धारकाचे_नावानुसार_रिपोर्ट':
    selected_owner = st.sidebar.selectbox('मालमत्ता_धारकाचे_नाव निवडा', df['मालमत्ता_धारकाचे_नाव'].tolist())
    btn1 =st.sidebar.button('नावानुसार तपशील पाहा')
    if btn1:
        load_owner_details(selected_owner)
elif option == "पाड्याच्या_नावानुसार_रिपोर्ट":
    area =st.sidebar.selectbox('पाड्याच_नाव निवडा', df['पाड्याचे_नाव'].unique().tolist())
    st.title("पाड्यानिहाय तपशील पाहा")

    if area == 'घिसलीपाडा':
        selected_Ghasalipada = df.groupby('पाड्याचे_नाव').get_group('घिसलीपाडा')[['मालमत्ता_धारकाचे_नाव', 'एकूण_एकंदर', 'एकूण_एकंदर_वसूली']]
        Ghisalipada = pd.DataFrame(selected_Ghasalipada)
        st.write(Ghisalipada)
    elif area == 'नवीदिल्ली':
        selected_navidilli = df.groupby('पाड्याचे_नाव').get_group('नवीदिल्ली')[['मालमत्ता_धारकाचे_नाव', 'एकूण_एकंदर', 'एकूण_एकंदर_वसूली']]
        navidilli = pd.DataFrame(selected_navidilli)
        st.write(navidilli)
    elif area == 'बेडफळी':
        selected_bedfali = df.groupby('पाड्याचे_नाव').get_group('बेडफळी')[['मालमत्ता_धारकाचे_नाव', 'एकूण_एकंदर', 'एकूण_एकंदर_वसूली']]
        bedfali = pd.DataFrame(selected_bedfali)
        st.write(bedfali)
    elif area == 'वडफळी':
        selected_vadfali = df.groupby('पाड्याचे_नाव').get_group('वडफळी')[['मालमत्ता_धारकाचे_नाव', 'एकूण_एकंदर', 'एकूण_एकंदर_वसूली']]
        vadfali = pd.DataFrame(selected_vadfali)
        st.write(vadfali)
    elif area == 'मोठीफळी':
        selected_mothifali = df.groupby('पाड्याचे_नाव').get_group('मोठीफळी')[['मालमत्ता_धारकाचे_नाव', 'एकूण_एकंदर', 'एकूण_एकंदर_वसूली']]
        mothifali = pd.DataFrame(selected_mothifali)
        st.write(mothifali)
    elif area == 'टाकलीफळी':
        selected_Taklifali = df.groupby('पाड्याचे_नाव').get_group('टाकलीफळी')[['मालमत्ता_धारकाचे_नाव', 'एकूण_एकंदर', 'एकूण_एकंदर_वसूली']]
        Taklifali = pd.DataFrame(selected_Taklifali)
        st.write(Taklifali)
    elif area == 'डोगालीफळी':
        selected_Dogalifali = df.groupby('पाड्याचे_नाव').get_group('डोगालीफळी')[['मालमत्ता_धारकाचे_नाव', 'एकूण_एकंदर', 'एकूण_एकंदर_वसूली']]
        Dogalifali = pd.DataFrame(selected_Dogalifali)
        st.write(Dogalifali)
    elif area == 'चिचलीपाडा':
        selected_chichalipada = df.groupby('पाड्याचे_नाव').get_group('चिचलीपाडा')[['मालमत्ता_धारकाचे_नाव', 'एकूण_एकंदर', 'एकूण_एकंदर_वसूली']]
        chichalipada = pd.DataFrame(selected_chichalipada)
        st.write(chichalipada)
    elif area == 'कामोद':
        selected_kamod = df.groupby('पाड्याचे_नाव').get_group('कामोद')[['मालमत्ता_धारकाचे_नाव', 'एकूण_एकंदर', 'एकूण_एकंदर_वसूली']]
        kamod = pd.DataFrame(selected_kamod)
        st.write(kamod)
    else:
        pass

else:
    pass
# function End -------------------------------------




