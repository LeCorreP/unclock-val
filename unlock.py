import streamlit as st

# Title and description
st.title("Les machines de l'anniversaire de Valentine")
st.write(
    "Attention, ne mettez pas d'espace ou de retour à la ligne à la fin de votre réponse"
)
st.write(
    "Entrez le numéro de la carte de la machine"
)

# Box pour entrer le numéro de la carte 
card_num = st.text_area(
    "Ecrivez ici le numéro de la carte):",
    value=None,
    height=70,
)
    
if card_num == "47":
    # Donner la date de naissance de G
    anniv = st.text_area(
        "Ecrivez ici la date de naissance (jj/mm/aaaa)):",
        value=None,
        height=70,
    )
    if st.button("Valider"):
        if anniv == "18/09/2001" :
            st.write("C'est bon, prenez la carte 31") 
        else : 
            st.write("FAUX") 

if card_num == "44":
    # Antoine
    mot = st.text_area(
        "Ecrivez ici le nom de l'invité.e:",
        value=None,
        height=70,
    )
    if st.button("Valider"):
        mot = mot.upper() 
        if mot == "ANTOINE" :
            st.write("C'est bon, prenez la carte 26") 
        else : 
            st.write("FAUX") 

if card_num == "19":
    # Clara
    mdp = st.text_area(
        "Ecrivez ici le mot de passe:",
        value=None,
        height=70,
    )
    if st.button("Valider"):
        if mdp == "lovinrosko" :
            st.write("C'est bon, prenez la carte 21") 
        else : 
            st.write("FAUX") 

if card_num == "32":
    # Morse
    morse = st.text_area(
        "Ecrivez ici le code:",
        value=None,
        height=70,
    )
    if st.button("Valider"):
        if morse == "6837" :
            st.write("C'est bon, prenez la carte 46") 
        else : 
            st.write("FAUX") 

if card_num == "23":
    # Elisa
    mot = st.text_area(
        "Ecrivez ici le nom de l'invité.e:",
        value=None,
        height=70,
    )
    if st.button("Valider"):
        mot = mot.upper() 
        if mot == "ELISA" :
            st.write("C'est bon, prenez la carte 26") 
        else : 
            st.write("FAUX") 

if card_num == "32":
    # Puzzle
    mot = st.text_area(
        "Ecrivez ici le nom de l'invité.e:",
        value=None,
        height=70,
    )
    if st.button("Valider"):
        mot = mot.upper() 
        if mot == "ANTOINE" :
            st.write("C'est bon, prenez la carte 26") 
        else : 
            st.write("FAUX") 

if card_num == "5":
    # Eliane
    mot = st.text_area(
        "Ecrivez ici le mot trouvé:",
        value=None,
        height=70,
    )
    if st.button("Valider"):
        mot = mot.upper() 
        if mot == "GALEROC" :
            st.write("C'est bon, prenez la carte 35") 
        else : 
            st.write("FAUX") 