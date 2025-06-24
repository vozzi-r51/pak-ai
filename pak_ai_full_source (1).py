# tools.py – AI Logic for Pak AI

import os
from PIL import Image
from gtts import gTTS
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip
import uuid
import tempfile

# Dummy text-to-image generator (replace with real model later)
def text_to_image(prompt, style, frame):
    img = Image.new("RGB", (512, 512), color=(173, 216, 230))
    temp_path = os.path.join(tempfile.gettempdir(), f"img_{uuid.uuid4().hex}.png")
    img.save(temp_path)
    return [temp_path] * 2  # Return 2 images max

# Text-to-Video (Slideshow + Cinematic style)
def text_to_video(prompt, mode, length):
    clips = []
    for i in range(3):
        img = Image.new("RGB", (1280, 720), color=(100 + i*50, 180, 200))
        img_path = os.path.join(tempfile.gettempdir(), f"slide_{i}_{uuid.uuid4().hex}.png")
        img.save(img_path)
        clip = ImageClip(img_path).set_duration(3)
        clips.append(clip)
    final = concatenate_videoclips(clips, method="compose")
    video_path = os.path.join(tempfile.gettempdir(), f"video_{uuid.uuid4().hex}.mp4")
    final.write_videofile(video_path, fps=24)
    return video_path

# Voiceover generator using gTTS
def text_to_voice(text, lang, voice):
    lang_map = {"Urdu": "ur", "English": "en", "French": "fr", "Hindi": "hi", "Arabic": "ar"}
    tts = gTTS(text=text, lang=lang_map.get(lang, "en"))
    audio_path = os.path.join(tempfile.gettempdir(), f"voice_{uuid.uuid4().hex}.mp3")
    tts.save(audio_path)
    return audio_path

# Convert static image to basic video clip
def image_to_video(uploaded):
    image = Image.open(uploaded)
    path = os.path.join(tempfile.gettempdir(), f"imgvid_{uuid.uuid4().hex}.png")
    image.save(path)
    clip = ImageClip(path).set_duration(5)
    out = os.path.join(tempfile.gettempdir(), f"img_video_{uuid.uuid4().hex}.mp4")
    clip.write_videofile(out, fps=24)
    return out

# Fake image animation (placeholder)
def image_animation(uploaded, text):
    return image_to_video(uploaded)

# Dummy transcription
def voice_to_text(audio):
    return "(Transcribed text will appear here – demo only)"

# Dummy dubbing
def video_dubbing(video_file, target_lang):
    return video_file  # Simply return the same for now (mock)
