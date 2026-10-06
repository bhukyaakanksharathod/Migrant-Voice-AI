import streamlit as st
import ollama
import speech_recognition as sr
from streamlit_mic_recorder import mic_recorder

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Migrant Voice AI",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎙️ Migrant Voice AI")
st.write("Speak your question and get an AI-powered response.")

# -----------------------------
# Ollama Settings
# -----------------------------
MODEL = "gemma3:1b"

SYSTEM_PROMPT = """
You are Migrant Voice AI, a helpful assistant for migrant workers.

Understand the user's question and answer in simple English.
Give clear, short and useful information.
If the user asks about government services, jobs, transport,
education, accommodation, or basic daily needs, explain clearly.
Avoid complicated words.
"""

# -----------------------------
# Speech Recognition Function
# -----------------------------
def speech_to_text(audio_bytes):
    recognizer = sr.Recognizer()

    try:
        # Convert recorded WAV bytes into AudioData
        with open("temp_audio.wav", "wb") as f:
            f.write(audio_bytes)

        with sr.AudioFile("temp_audio.wav") as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)

        return text

    except sr.UnknownValueError:
        return None

    except sr.RequestError as e:
        st.error(f"Speech recognition service error: {e}")
        return None

    except Exception as e:
        st.error(f"Audio processing error: {e}")
        return None


# -----------------------------
# Ollama AI Function
# -----------------------------
def get_ai_response(user_text):
    try:
        # IMPORTANT:
        # First create the response variable
        response = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_text
                }
            ]
        )

        # Then extract the answer
        answer = response["message"]["content"]

        return answer

    except Exception as e:
        return f"Ollama error: {e}"


# -----------------------------
# Voice Recorder
# -----------------------------
st.subheader("🎤 Speak Here")

audio = mic_recorder(
    start_prompt="🎤 Start Recording",
    stop_prompt="⏹️ Stop Recording",
    just_once=True,
    use_container_width=True,
    format="wav"
)

# -----------------------------
# Process Voice
# -----------------------------
if audio:

    st.success("✅ Voice recorded successfully!")

    # Play recorded audio
    st.audio(audio["bytes"], format="audio/wav")

    # Convert voice to text
    with st.spinner("🔄 Converting your voice to text..."):

        user_text = speech_to_text(audio["bytes"])

    if user_text:

        st.subheader("📝 Your Question")

        st.write(user_text)

        # Get AI answer
        with st.spinner("🤖 AI is thinking..."):

            answer = get_ai_response(user_text)

        st.subheader("🤖 Migrant Voice AI")

        st.write(answer)

    else:

        st.warning(
            "⚠️ Sorry, I could not understand your voice. "
            "Please record again and speak clearly."
        )


# -----------------------------
# Text Input Option
# -----------------------------
st.divider()

st.subheader("⌨️ Or Type Your Question")

typed_text = st.text_input(
    "Enter your question:"
)

if st.button("Ask AI"):

    if typed_text.strip():

        with st.spinner("🤖 AI is thinking..."):

            answer = get_ai_response(typed_text)

        st.subheader("🤖 Migrant Voice AI")

        st.write(answer)

    else:

        st.warning("Please enter a question.")