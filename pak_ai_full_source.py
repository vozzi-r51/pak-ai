# Pak AI - Ultra Pro Version (Text to Image, Video, Voice)
# Main Streamlit App

import streamlit as st
from tools import text_to_image, text_to_video, text_to_voice, image_to_video, image_animation, voice_to_text, video_dubbing

# Page config
st.set_page_config(page_title="Pak AI - Creative AI Suite", layout="wide")

# Sidebar Navigation
st.sidebar.image("assets/logo.png", use_column_width=True)
page = st.sidebar.radio("Navigate", ["Home", "Text to Image", "Text to Video", "Voiceover", "Image to Video", "Animate Image", "Voice to Text", "Dubbing"])

st.markdown("""
    <style>
    .css-18e3th9 {padding: 2rem; background-color: #f7fff7;}
    .css-1d391kg {color: #116611; font-size: 1.4rem;}
    </style>
""", unsafe_allow_html=True)

# Home Page
if page == "Home":
    st.title("🇵🇰 Pak AI - Create Anything with AI")
    st.write("Welcome to Pak AI – A multilingual, ultra pro-level creative AI suite for image, video, and voice generation.")
    st.video("assets/demo.mp4")

# Text to Image
elif page == "Text to Image":
    st.header("🖼 Text to Image Generator")
    prompt = st.text_input("Describe your image")
    style = st.selectbox("Select Style", ["Realistic", "Fantasy", "Anime", "Sketch"])
    frame = st.selectbox("Aspect Ratio", ["16:9", "4:5", "9:16"])
    if st.button("Generate Image"):
        outputs = text_to_image(prompt, style, frame)
        for img in outputs:
            st.image(img)

# Text to Video
elif page == "Text to Video":
    st.header("🎥 Text to Video Generator")
    prompt = st.text_area("Enter your video script")
    mode = st.selectbox("Video Style", ["Slideshow", "Cinematic Flow"])
    length = st.select_slider("Video Length", ["10 sec", "30 sec", "1 min"])
    if st.button("Generate Video"):
        video = text_to_video(prompt, mode, length)
        st.video(video)

# Voiceover
elif page == "Voiceover":
    st.header("🎙 AI Voiceover Generator")
    text = st.text_area("Enter the text to convert to voice")
    lang = st.selectbox("Language", ["Urdu", "English", "Arabic", "Hindi", "French"])
    voice = st.selectbox("Voice Sample", ["Male 1", "Male 2", "Female 1", "Female 2", "Narrator", "Girl", "Old Man", "Deep Male", "Soft Female", "Robotic"])
    if st.button("Generate Voice"):
        audio = text_to_voice(text, lang, voice)
        st.audio(audio)

# Image to Video
elif page == "Image to Video":
    st.header("🖼➡️🎞 Image to Video Generator")
    uploaded = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded and st.button("Generate Video"):
        video = image_to_video(uploaded)
        st.video(video)

# Image Animation
elif page == "Animate Image":
    st.header("📸 Image Animation with Lip Sync")
    uploaded = st.file_uploader("Upload Face Image", type=["png", "jpg", "jpeg"])
    speech = st.text_input("Enter text for lip sync")
    if uploaded and speech and st.button("Animate"):
        animated = image_animation(uploaded, speech)
        st.video(animated)

# Voice to Text
elif page == "Voice to Text":
    st.header("🗣➡️📝 Voice to Text Transcription")
    audio = st.file_uploader("Upload audio file", type=["mp3", "wav"])
    if audio and st.button("Transcribe"):
        transcript = voice_to_text(audio)
        st.write(transcript)

# Dubbing
elif page == "Dubbing":
    st.header("🌍 AI Video Dubbing")
    video_file = st.file_uploader("Upload video to dub", type=["mp4", "mov"])
    target_lang = st.selectbox("Select target language", ["English", "Urdu", "French", "Spanish", "Hindi"])
    if video_file and st.button("Dub Video"):
        dubbed = video_dubbing(video_file, target_lang)
        st.video(dubbed)
