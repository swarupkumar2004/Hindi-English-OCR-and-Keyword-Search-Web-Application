import streamlit as st
from PIL import Image
import ocr_processing as ocr
import search_function as search

st.title("Hindi-English OCR and Keyword Search")

# Step 1: Image upload
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Step 2: Extract text
    st.write("Extracting text from the image...")
    extracted_text = ocr.process_image(image)
    
    # Display extracted text
    st.subheader("Extracted Text")
    st.write(extracted_text)

    # Step 3: Keyword search
    search_query = st.text_input("Enter a keyword to search:")
    
    if search_query:
        st.subheader(f"Search Results for '{search_query}':")
        highlighted_text = search.highlight_text(extracted_text, search_query)
        st.markdown(highlighted_text, unsafe_allow_html=True)
