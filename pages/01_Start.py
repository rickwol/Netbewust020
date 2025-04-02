import streamlit as st

st.set_page_config(page_title=None, page_icon=None, initial_sidebar_state="auto", menu_items=None, layout="wide")

st.markdown("""
            <style>
            [data-testid="stSidebar"] {
                display: none
            }

            [data-testid="collapsedControl"] {
                display: none
            }
            </style>
            """, unsafe_allow_html=True)


st.markdown("""
    <style>
        [data-testid="column"]:nth-child(1){
            background-color: #a2cce9;
            font-size: 20px;
        }
    </style>
    """, unsafe_allow_html=True
)



#st.sidebar.header("Netbewust020")
col2, col3, col4, = st.columns([1.5,5,2])
with col2:
    st.markdown('#')
    st.page_link("pages/01_Start.py", label="### **Start**", )
    st.page_link("pages/02_Stand van zaken.py", label="### **Stand van zaken**")
    st.page_link("pages/03_Q&A.py", label="### **Q&A**")
   

with col3: 
    st.title("Netbewust020")

    st.subheader("Waarom Netbewust laden?")
    st.markdown("Het aantal elektrische auto’s in ons land groeit hard. Dat zorgt voor minder CO2-uitstoot, maar ook voor extra belasting van ons stroomnet. Elektrische auto’s gebruiken flink wat stroom om op te laden. Dat kan lastig zijn als het net al druk is. U kunt het vergelijken met filevorming op de snelweg. Daarom is het goed om het elektriciteitsnet uit te breiden en slimmer met ons stroomgebruik om te gaan. </br> In de winter gebruiken we vaak tegelijk elektriciteit voor koken, verwarmen en het opladen van elektrische auto's. Terwijl koken en verwarmen lastig op een ander moment kunnen, biedt het opladen van auto's veel kansen om slimmer met stroom om te gaan. </br> Netbeheerder Liander, laadpaalaanbieder Equans en de gemeente Amsterdam, met steun van de Hogeschool van Amsterdam, werken samen aan het uitbreiden van netbewust laden op openbare laadpalen in de stad. Zo kunnen we in de toekomst meer laadpalen, huishoudens en warmtepompen aansluiten.", unsafe_allow_html=True)
    
    
    st.subheader("Wat is netbewust laden?")
    
    st.markdown("Bij netbewust laden kijkt Liander, om te voorkomen dat het elektriciteitsnet wordt overbelast, naar de verwachte belasting en beschikbare ruimte op het transformatorhuisje en geeft aan de hand daarvan door aan de laadpaalaanbieder of en op welk moment er iets minder hard kan worden geladen. </br> In bepaalde gebieden krijgen laadpalen soms minder stroom op bepaalde momenten. De beschikbare elektriciteit wordt eerlijk verdeeld over de laadpalen. Hoe lang een auto al aan het laden is, bepaalt hoeveel hij krijgt. Soms kan het gebeuren dat een auto even geen elektriciteit krijgt. </br> Dit gebeurt alleen als het echt nodig is, en over het hele jaar zijn dat maar een paar uur. Het zal vooral in de winter zijn, aan het eind van de middag en het begin van de avond.", unsafe_allow_html=True)
    
    
    st.subheader("Hoe doen we dat in Amsterdam?")
    
    st.markdown("U merkt  hier niks van als uw auto de hele nacht aan de laadpaal staat. De auto is   ’s ochtends volledig opgeladen. Als de auto maar kort kan laden, kan het zijn dat hij iets langzamer oplaadt dan verwacht. Soms kan de app van de auto melden dat de sessie is onderbroken, maar dat is geen reden voor paniek. Dit betekent dat een andere auto, zoals die van een huisarts, even voorrang krijgt. Uw laadsessie gaat weer op volle kracht snelheid verder als er weer voldoende capaciteit beschikbaar is. Momenteel laden we netbewust bij 500 laadpalen. We breiden uit naar meer locaties waar flexibel laden nodig is voor het elektriciteitsnet. </br> U kunt via de Charge Assist app prioriteit aanvragen. Registreer uw laadpas of betaalmethode in de app en vraag prioriteit aan voor uw laadsessie, zodat u met de hoogste snelheid kunt laden.", unsafe_allow_html=True)

with col4:
    st.markdown('#')
    
####Design footer        
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<img src="https://www.theleansixsigmacompany.eu/wp-content/uploads/sites/30/equans-logo.png", height=80>
<img src="https://www.liander.nl/assets/logo.png", height=80>
<img src="https://upload.wikimedia.org/wikipedia/commons/4/4c/Logo_of_Gemeente_Amsterdam.svg", height=80>
<img src="https://zakelijkschrijven.nl/wp-content/uploads/2021/01/HvA-logo.png", height=80>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)        