import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import requests
from streamlit_lottie import st_lottie


def lot(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


animation = lot("https://assets5.lottiefiles.com/packages/lf20_ssaHB0.json")
animation2 = lot("https://assets2.lottiefiles.com/packages/lf20_l2l6hr2l.json")
page_title = 'Travelling Blog'
page_icon = ':camera:'
layout = 'centered'
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title+" "+page_icon)

selected = option_menu(
    menu_title="Main menu",
    options=["Home", "Gallery", "Contact"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",

)

if selected == "Home":
    img = Image.open("manali.png")
    st.image(img)
    st.write("Manali, amidst the hilly slopes, is a paradise for mountain lovers with spell-binding views, charming streams, the fairy-tale-like fog surrounding little hidden cottages, and a lingering scent of pines and freshness. Oh, and you can ride a yak or ride your bike up the famous Rohtang pass to Leh, the valley of the gods.")
    img = Image.open("manali2.png")
    st.image(img)
    st.write("Manali suits the needs of every kind of travel mindset. A family looking for some bonding time, a couple for some peace and quiet, solo travelers for some solitude or a group of friends seeking an adventure.Before we explore the itinerary, Let us get to know some basics about surroundings.")
    st.subheader("Weather in Manali")
    st.write("Average annual temperature: 4 °C - 26 °C\n")
    st.write("Summer temperature: 10 °C - 26 °C")
    st.write("Winter temperature: 15 °C  - 12 °C")
    st.subheader("What to Pack")
    st.write("During Summer & Spring months — Summer Clothes + Essentials & for evenings light jacket or windcheaters")
    st.write("During winters —- heavy woolens, warmers")
    st.write("Plus trekking boots, sunscreen, a poncho, comfortable walking shoes & camera to freeze the memories.")
    st.write("There are a whole lot of things to do in and around Manali. Here’s your ULTIMATE Manali travel guide to the hippie town in Himachal. ")
    img = Image.open("manali3.png")
    st.image(img)
    st.subheader("Day 1 & 2: Kullu Valley")
    img = Image.open("manali4.png")
    st.image(img)
    st.write("Rightly hailed as the Valley of Gods, Kullu’s divine beauty has been beckoning travelers from all over the world. Adventurists have been traversing its forbidden slopes and romantics have been idealizing its tranquil landscape. For almost all reasons or no reason at all, Kullu has never evaded any true snow-lovers’ map.")
    st.markdown("**Amazing Things to Do in Kullu-Manali – Kullu Valley**")
    st.write("Here’s a list of some of the most sought after things to do in Kullu-Manali")
    st.markdown("**1. Visit the Hot Springs at Manikaran**")
    st.write("Just 1.5 hours away from Kullu, the fabled hot springs of Manikaran are a sight for sore eyes. Any experience of Kullu-Manali tourism is incomplete without a visit.")
    st.markdown("**2. Spot Some Fauna at the Great Himalayan National Park**")
    st.write("With 31 species of animals and 181 species of birds existing in undisturbed Himalayan habitat, the wildlife lover in you won’t be disappointed. Of all the attractions in the valley, this is among the more offbeat things to do in Kullu Manali.")
    st.markdown("**3. Trek to Kheerganga**")
    st.write("Situated in the Parvati Valley, this is easily one of the most picturesque treks amidst the great mountains. The 11 km – the walk is rough but the view more than makes up for it.")
    st.markdown("**4. Explore History at Naggar Castle**")
    st.write("The former capital of Kullu, Naggar is brimming with heritage in the form of temples, a castle, and an art gallery dedicated to a Russian artist who made Naggar his home.")
    st.subheader("Day 3: Solang Valley")
    st.write("Solang, close to both Kullu and Manali, is a stop no true blood adrenaline-seeker can afford to miss this. You could either spend a night in Solang or use Kullu/ Manali as a base, to explore the energy and the snow-clad beauty of this valley. Whether you enjoy adventure or not, the terrains of Solang will inspire you to go out and face your fears. ")
    img = Image.open("manali5.png")
    st.image(img)
    st.markdown("**Amazing Things to Do in Kullu Manali: Solang Valley**")
    st.markdown("**1. Go Paragliding**")
    st.write("Watch the landscaped beauty of the valley and enjoy the thrill of sailing in the air. A short fly will cost you ₹600 per person and a high fly will cost you between ₹1500 to ₹3000 per person. Go all out, we would say!")
    st.markdown("**2. Try Rock Climbing and Rappelling**")
    st.write("Climb the untamed mountains of Solang and get a taste of raw adventure.₹700 per person.")
    st.markdown("**3. Go skiing**")
    st.write(" Embark on the ultimate Himalayan adventure down the slopes of Solang. A must-try of all the things to do in Kullu Manali. ₹300 per person.")
    st.subheader("Day 4 & 5: Manali")
    st.write("Manali is easily India’s summer vacation capital. From backpackers to enthusiastic tourists, Manali entertains all kinds of travelers. It’s often used as a base by adventurers to trek the nearby valleys and mountains as well as indulge in some adventure sports. On the other hand, Manali is an equally delighting place for the quiet traveler as well, with its green valleys and the ever-magnificent Beas River. ")
    img = Image.open("manali7.png")
    st.image(img)
    st.markdown("**Amazing Things to do in Manali**")
    st.markdown("**1. Drive Through the Rohtang Pass**")
    st.write("Passing through wonderful views of the surrounding mountains, the drive will be the one you won’t forget. The pass is mostly closed in winter between October and May. Permits are required.  ")
    st.markdown("**2. Go White-water Rafting in the Beas River**")
    st.write(" Feel the chilling glacial water hit against your skin as you wade your way through the scenic route of the river.")
    st.markdown("**3. Spend some time at the Monasteries**")
    st.write(" Peek into the culture and also enjoy a day of serenity after the mad adventure. Popular monasteries are Gadhan Thekchoking Gompa, Himalayan Nyingamapa Gompa, and Manali Gompa. One of Kullu Manali Tourism’s most spiritually uplifting delights.")
    st.markdown("4. Visit the Hadimba Temple")
    st.write("The popular 15th-century temple is known for its architecture as well as the beautiful cedar forest that surrounds it. ")
    st.subheader("Best Rated places to Eat in Manali")
    st.markdown("**1. Johnson Bar and Restaurant**")
    st.write("One of the most happening hangouts in Manali with a delicious menu and a well-stocked bar. ")
    st.markdown("**2. Drifters’ Cafe**")
    st.write(" A multi-cuisine treat with a great ambiance and some local flavor.")
    st.markdown("**3. Rasta Cafe**")
    st.write("A humble, street-side joint that serves an assortment of dishes to the weary traveler.")
    st.subheader("Best places to stay in Manali")
    st.markdown("**1.For luxury**")
    st.write("The Anantmaya Resort, Shivadya Resort & Spa, La Ri Sa Resort")
    st.markdown("**2.For mid-range**")
    st.write(" The Orchard Greens, Amneu Beas Valley, Mountain Green Villa")
    st.markdown("**3.For budget accommodations**")
    st.write("Bhoomi Holiday Homes, Nihal Cottage, Hotel Mountain Inn")
    st.markdown("**4.Best hotels**")
    st.write("The Tranquil Inn, Urvashi’s Retreat, De Phoenix Eye")
    st.markdown("**5.Best homestays**")
    st.write("Sunface Homestay, The Dog on the Hill, Jukaso Mrikula Cottage")
elif selected == "Gallery":
    st.title("Gallery")
    st_lottie(animation, height=400)
    st.subheader("MANALI")
    col1, col2, col3 = st.columns(3)
    with col1:
        img = Image.open("m1.png")
        st.image(img)
    with col2:
        img = Image.open("m2.png")
        st.image(img)
    with col3:
        img = Image.open("m4.png")
        st.image(img)

    st.subheader("KULLU")
    col1, col2, col3 = st.columns(3)
    with col1:
        img = Image.open("k1.png")
        st.image(img)
    with col2:
        img = Image.open("k2.png")
        st.image(img)
    with col3:
        img = Image.open("k3.png")
        st.image(img)

    st.subheader("ADVENTURE")
    col1, col2, col3 = st.columns(3)
    with col1:
        img = Image.open("a1.png")
        st.image(img)
    with col2:
        img = Image.open("a2.png")
        st.image(img)
    with col3:
        img = Image.open("a3.png")
        st.image(img)


    # tab1, tab2, tab3, tab4, tab5 = st.tabs(["tab1", "tab2", "tab3", "tab4", "tab5"])
    # #with tab1:
    # img = Image.open("manali8.png")
    # st.image(img)
    # #with tab2:
    # img = Image.open("manali9.png")
    # st.image(img)
    # #with tab3:
    # img = Image.open("manali10.png")
    # st.image(img)
    # #with tab4:
    # img = Image.open("manali11.png")
    # st.image(img)
    # #with tab5:
    # img = Image.open("manali12.png")
    # st.image(img)
elif selected == "Contact":
    col1, col2 = st.columns(2)
    with col1:
        with st.form("form"):
            st.subheader("Join With Us By Signing Up")
            st.write("Fill The Form")
            Name = st.text_input("Name")
            Email = st.text_input("Email")
            Password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("submit")
            if submitted:
                st.write("Name", Name)
                st.write("Email", Email)
                st.write("Password", Password)
    with col2:
        st_lottie(animation2, height=400)



