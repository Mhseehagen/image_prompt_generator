import streamlit as st

def generate_prompt(details):
    prompt = (
        f"Lav et realistisk billede med følgende detaljer: \n"
        f"- Hovedmotiv: {details['main_subject']} \n"
        f"- Miljø: {details['environment']} \n"
        f"- Baggrund: {details['background']} \n"
        f"- Personer eller dyr: {details['people']} \n"
        f"- Aktivitet: {details['activity']} \n"
        f"- Stemning: {details['mood']} \n"
        f"- Farvepalette: {details['color_palette']} \n"
        f"- Belysning: {details['lighting']} \n"
        f"- Perspektiv: {details['perspective']} \n"
        f"- Yderligere detaljer: {details['additional_details']}"
    )
    return prompt

def main():
    st.title("AI Billedbeskrivelsesgenerator")
    st.write("Udfyld formularen nedenfor for at skabe en detaljeret beskrivelse til et AI-genereret billede.")

    # Inputfelter til brugerens detaljer
    details = {
        'main_subject': st.text_input("Hovedmotiv i billedet (f.eks. en bil, en person):"),
        'environment': st.text_input("Miljø (f.eks. indendørs, udendørs, by, skov):"),
        'background': st.text_input("Baggrundsdetaljer (f.eks. bygninger, træer):"),
        'people': st.text_input("Beskriv personer eller dyr, hvis nogen (f.eks. alder, køn, udseende):"),
        'activity': st.text_input("Hvad laver de (f.eks. løber, læser):"),
        'mood': st.text_input("Stemning eller atmosfære (f.eks. afslappet, energisk):"),
        'color_palette': st.text_input("Farvepalette (f.eks. varm, kølig, pastel):"),
        'lighting': st.text_input("Belysning (f.eks. naturlig, dæmpet, spotlight):"),
        'perspective': st.text_input("Perspektiv eller vinkel (f.eks. fugleperspektiv, øjenhøjde):"),
        'additional_details': st.text_area("Yderligere detaljer eller specifikke ønsker (valgfrit):")
    }

    if st.button("Generer Beskrivelse"):
        # Valider at påkrævede felter er udfyldt
        required_fields = ['main_subject', 'environment', 'background', 'people', 'activity', 'mood', 'color_palette', 'lighting', 'perspective']
        if any(not details[field].strip() for field in required_fields):
            st.warning("Alle påkrævede felter skal udfyldes for at generere en detaljeret beskrivelse.")
        else:
            prompt = generate_prompt(details)
            st.success("Beskrivelse genereret med succes!")
            st.code(prompt, language='markdown')

if __name__ == "__main__":
    main()
