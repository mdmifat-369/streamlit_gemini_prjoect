import streamlit as st
from api_calling import note_generator,audio_generator,Quiz_question_genaretor
from PIL import Image

# title work
st.title("Note Summary and Quiz Generator")
st.markdown("upload upto 3 images to generate Note summary and Quiz")
st.divider()

# sidebar work

with st.sidebar:

    # *******************Images portion*******************
    st.header("Controls")
    images=st.file_uploader(
        "Upload the photos of your note",
        ['jpg','png','jpeg'],
        accept_multiple_files=True
    )

    if images:
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            st.subheader("Your images: ")
            cols = st.columns(len(images)) 
            for i, img in enumerate(images):
                with cols[i]:
                    st.image(img)
    #*****************************************************

# difficulty

    oder=st.selectbox(
        "Chosse your difficulty",
         ["easy","medium","hard"],
         index=None
         )
    
    pressed=st.button("Click to Generate",type="primary")
# ****************************************************************
# now front section work

if pressed:
    if not images:
        st.error("You must upload a photo🙄")
    if not oder:
        st.error("you must select a difficulty😏")
    
    if images and oder:
        
        # note
         with st.container(border=True):
             st.subheader("Your note")
            
             with st.spinner("Please wait....."):
                  pil_images = [Image.open(img) for img in images]
                  text=note_generator(pil_images)
                  st.markdown(text)

        # Audio Transcipt
         with st.container(border=True):
             with st.spinner("Please wait....."):
               st.subheader("Your Audio clip")
               Audio=audio_generator(text)
               st.audio(Audio)
        
        # QUIZ
         with st.container(border=True):
               st.subheader("Your Quiz Question:")
               with st.spinner("Please wait....."):
                  Question=Quiz_question_genaretor(text)
                  st.markdown(Question)
