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

col2, col3, col4, = st.columns([1.5,5,2])
with col2:
    st.markdown('#')
    st.page_link("pages/01_Start.py", label="### **Start**", )
    st.page_link("pages/02_Stand van zaken.py", label="### **Stand van zaken**")
    st.page_link("pages/03_Q&A.py", label="### **Q&A**")

with col3:
    st.title("Q&A")
    
    st.subheader("Q: Waarom is netbewust laden belangrijk voor Amsterdam? ")
    st.markdown("A: Het vermindert de druk op het elektriciteitsnet op piekmomenten. Hierdoor zijn minder uitbreidingen van het net nodig, wat tijd en geld bespaart. Ook helpt het bij het voorkomen van netcongestie. Zo kunnen er nieuwe huizen worden gebouwd, meer laadpalen worden geplaatst, en kunnen we doorgaan met de energietransitie. ", unsafe_allow_html=True)
    
    
    st.subheader("Q: Wat is er nodig om een laadpaal netbewust te maken en om overal netbewust te kunnen laden?")
    st.markdown("A: Er zijn afspraken nodig tussen de laadpaalaanbieders, netbeheerders en een gemeente over het uitwisselen van informatie. Technisch gezien zijn alle laadpalen van Equans in Amsterdam al geschikt voor netbewust laden. We blijven intern het proces aansturen en begeleiden om storingen te voorkomen. Concreet laat Liander steeds aan Equans weten hoeveel ruimte er is op het elektriciteitsnet om een auto op te laden, zodat Equans de palen kan aansturen. We zijn bezig om dit op steeds grotere schaal te kunnen doen.  ", unsafe_allow_html=True)
    
    st.subheader("Q: Waar zijn de laadpalen in Amsterdam waar netbewust wordt geladen? ")
    st.markdown("A: Op openbare laadpalen verspreid over de stad. We breiden dit uit en willen dit eind 2025 op alle Equans-palen toepassen", unsafe_allow_html=True)
    
    st.subheader("Q: Is Equans de enige laadpaalaanbieder in Amsterdam waar netbewust kan worden geladen? ")
    st.markdown("A: De gemeente en Liander zijn voornemens om netbewust laden op alle laadpalen toe te passen. Zo verdelen we de beperking in transportcapaciteit eerlijker over alle laadpalen. Equans is de belangrijkste laadpaalaanbieder in deze regio en daarom is met hen gestart. ", unsafe_allow_html=True)
    
    st.subheader("Q: Hoe verhoudt het project Flexpower zich tot netbewust laden?  ")
    st.markdown("A: Flexpower was een pilot om te testen hoe laden met minimale impact op het net en maximaal comfort voor de elektrische rijder kon worden toegepast. Netbewust laden is de vertaling van de pilot uitkomsten naar een landelijke aanpak.   ", unsafe_allow_html=True)
    
    st.subheader("Q: Wat merkt de elektrische rijder van netbewust laden? ")
    st.markdown("A: Afhankelijk van waar u laadt en wat de verwachte belasting is op dat stuk net kunt u meer of minder ervan merken. Wanneer er moet worden beperkt vanwege overbelasting, merkt u dit doordat de laadsessie dan vaker wordt onderbroken. Dit is gebaseerd op een slim roulatiesysteem. Dit kan zowel in de avondpiek als overdag gebeuren. In de nacht zal dit vrijwel niet voorkomen.", unsafe_allow_html=True)
    
    st.subheader("Q: (Hoe) Kan een elektrische rijder netbewust laden uitschakelen in Amsterdam? ")
    st.markdown("A: Ja dat kan. Er is voorlopig een mogelijkheid om uzelf voorrang te geven via de Charge Assist app. Daarmee geeft u prioriteit aan het laden van uw auto boven het laden van de andere auto’s die worden geladen in het gebied. En op basis van de beschikbare capaciteit kan de laadpaalaanbieder op basis van de beschikbare capaciteit extra vermogen geven aan uw laadsessie. Als u veel haast hebt tijdens een piekmoment dan kunt beter naar een snellader gaan. </br> In de Charge Assist app kunt u uw laadpas of andere betaalmethode registreren en vervolgens in de app prioriteit aanvragen voor uw laadsessie, waardoor u met de hoogst mogelijke laadsnelheid voorrang krijgt.", unsafe_allow_html=True)
    
    st.subheader("Q: Gaat Liander de laadpalen ook uitzetten net zoals Stedin? ")
    st.markdown("A: Nee, het uitgangspunt is dat u altijd kunt laden. Netbewust laden maakt dit mogelijk en daarom is het belangrijk dat dit de norm wordt. Alleen in zeer uitzonderlijk gevallen, bijvoorbeeld bij extreme kou in combinatie met zware belasting, is laden niet mogelijk. Dit is een absoluut noodscenario voor Liander. ", unsafe_allow_html=True)
    
    st.subheader("Q: Hoe verhoudt netbewust laden zich tot het laden op momenten dat het goedkoop is? Is prijs niet een betere stimulans? Of krijg ik korting, subsidies of incentives voor het gebruik van netbewust laden? ")
    st.markdown("A: Het is belangrijk dat we bewuster omgaan met het netwerk dat er al ligt. Om alle elektrische auto’s de ruimte te kunnen geven op het elektriciteitsnet, is de prijs als prikkel om op andere tijden te laden onvoldoende. Dat kan namelijk voor grote pieken zorgen in de belasting van het elektriciteitsnet. </br> Netbewust laden moet het uitgangspunt worden om belasting te verspreiden en hoge maatschappelijke kosten te voorkomen. </br> We gaan onderzoeken hoe en of we in de toekomst kortingen of incentives kunnen geven, zoals lagere energietarieven tijdens daluren.", unsafe_allow_html=True)
    
    st.subheader("Q: Is mijn elektrische auto compatibel voor netbewust laden?")
    st.markdown("A: De meeste moderne elektrische auto's zijn compatibel met netbewust laden, maar het is belangrijk om de specificaties van uw voertuig te controleren. Er zijn enkele modellen (circa 15 % van de elektrische auto’s) die langdurig pauzeren niet ondersteunen. Er wordt op dit moment onderzoek gedaan door ElaadNL naar welke modellen het betreft. De betreffende automerken zullen samen met ElaadNL hun best doen om het op deze auto’s ook te laten werken.", unsafe_allow_html=True)
    
    st.subheader("Q: Waar zijn de laadpalen in Amsterdam waar netbewust wordt geladen? Q: Waar zijn de laadpalen in Amsterdam waar netbewust wordt geladen? ")
    st.markdown("A: Op openbare laadpalen verspreid over de stad. We breiden dit uit en willen dit eind 2025 op alle Equans-palen toepassen", unsafe_allow_html=True)
    
    st.subheader("Q: Waar zijn de laadpalen in Amsterdam waar netbewust wordt geladen? Q: Waar zijn de laadpalen in Amsterdam waar netbewust wordt geladen? ")
    st.markdown("A: Op openbare laadpalen verspreid over de stad. We breiden dit uit en willen dit eind 2025 op alle Equans-palen toepassen", unsafe_allow_html=True)

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
<img src="https://www.theleansixsigmacompany.eu/wp-content/uploads/sites/30/equans-logo.png", height=100>
<img src="https://www.liander.nl/assets/logo.png", height=100>
<img src="https://upload.wikimedia.org/wikipedia/commons/4/4c/Logo_of_Gemeente_Amsterdam.svg", height=100>
<img src="https://zakelijkschrijven.nl/wp-content/uploads/2021/01/HvA-logo.png", height=100>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)        