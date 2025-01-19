import streamlit as st

def generate_prompt(details):
    prompt = (
        f"Create a realistic image with the following details: \n"
        f"- Main subject: {details['main_subject']} \n"
        f"- Environment: {details['environment']} \n"
        f"- Background: {details['background']} \n"
        f"- People or animals: {details['people']} \n"
        f"- Activity: {details['activity']} \n"
        f"- Mood: {details['mood']} \n"
        f"- Color palette: {details['color_palette']} \n"
        f"- Lighting: {details['lighting']} \n"
        f"- Perspective: {details['perspective']} \n"
        f"- Additional details: {details['additional_details']}"
    )
    return prompt

def main():
    st.title("AI Image Prompt Generator")
    st.write("Fill out the form below to create a detailed prompt for an AI-generated image.")

    # Input fields for user details
    details = {
        'main_subject': st.text_input("Main subject of the image (e.g., a car, a person):"),
        'environment': st.text_input("Environment (e.g., indoors, outdoors, city, forest):"),
        'background': st.text_input("Background details (e.g., buildings, trees):"),
        'people': st.text_input("Describe people or animals, if any (e.g., age, gender, appearance):"),
        'activity': st.text_input("What are they doing (e.g., running, reading):"),
        'mood': st.text_input("Mood or atmosphere (e.g., relaxed, energetic):"),
        'color_palette': st.text_input("Color palette (e.g., warm, cool, pastel):"),
        'lighting': st.text_input("Lighting (e.g., natural, dim, spotlight):"),
        'perspective': st.text_input("Perspective or angle (e.g., bird's eye view, eye level):"),
        'additional_details': st.text_area("Additional details or specific requests:")
    }

    if st.button("Generate Prompt"):
        # Validate that all fields are filled
        if any(not value.strip() for value in details.values()):
            st.warning("All fields must be filled to generate a detailed prompt.")
        else:
            prompt = generate_prompt(details)
            st.success("Prompt successfully generated!")
            st.code(prompt, language='markdown')

if __name__ == "__main__":
    main()
