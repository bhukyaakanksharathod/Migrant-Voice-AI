# 🎤 Migrant Voice AI

## 1. Project Title

**Migrant Voice AI**

Migrant Voice AI is a voice-based artificial intelligence assistant designed to help migrants communicate with an AI system using their voice.

---

## 2. Abstract

Migrant Voice AI is an AI-powered voice assistant that allows users to interact with a computer using natural speech. The system accepts voice input from the user, converts the speech into text, sends the text to an AI model, and generates a useful response.

The project uses Python, Streamlit, Ollama, speech recognition, and text-to-speech technologies. The main goal of the project is to provide a simple and user-friendly communication system for people who may have difficulty using traditional text-based applications.

---

## 3. Introduction

Migration to a new city or country can create communication and information-related challenges. People may need information about accommodation, employment, transportation, education, healthcare, and local services.

Migrant Voice AI provides a simple voice-based interface where users can ask questions naturally. The AI processes the user's question and provides a clear response.

---

## 4. Objectives

The main objectives of the project are:

* To create a voice-based AI assistant.
* To convert speech into text.
* To process user questions using an AI model.
* To provide simple and understandable responses.
* To convert AI responses into speech.
* To provide an easy-to-use web interface.
* To demonstrate the practical use of Generative AI.

---

## 5. Technologies Used

| Technology         | Purpose                   |
| ------------------ | ------------------------- |
| Python             | Main programming language |
| Visual Studio Code | Development environment   |
| Streamlit          | Web interface             |
| Ollama             | Local AI model            |
| Gemma 3:1B         | AI language model         |
| SpeechRecognition  | Speech-to-text            |
| PyAudio            | Microphone input          |
| pyttsx3            | Text-to-speech            |

---

## 6. System Architecture

The system works according to the following flow:

```text
User
  ↓
Microphone
  ↓
Speech Recognition
  ↓
Speech to Text
  ↓
AI Model - Ollama
  ↓
AI Generated Response
  ↓
Text to Speech
  ↓
Speaker
```

---

## 7. Project Structure

```text
Migrant-Voice-AI/
│
├── .venv/
│
├── app.py
├── ai_model.py
├── speech_to_text.py
├── text_to_speech.py
├── requirements.txt
└── README.md
```

### File Description

**app.py**

Contains the Streamlit user interface.

**ai_model.py**

Connects the application to Ollama and generates AI responses.

**speech_to_text.py**

Handles conversion of the user's voice into text.

**text_to_speech.py**

Converts the AI-generated text into spoken audio.

**requirements.txt**

Contains the Python packages required to run the project.

**README.md**

Contains project documentation and instructions.

---

## 8. Installation

### Step 1: Create the project folder

Create a folder named:

```text
Migrant-Voice-AI
```

Open the folder in Visual Studio Code.

### Step 2: Create a virtual environment

Open the VS Code terminal and run:

```bash
python -m venv .venv
```

### Step 3: Activate the virtual environment

For Windows PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install required packages

```bash
python -m pip install streamlit SpeechRecognition PyAudio pyttsx3 ollama
```

---

## 9. Install Ollama

Install Ollama on the computer.

Check the installation:

```bash
ollama --version
```

Download the Gemma model:

```bash
ollama pull gemma3:1b
```

Test the model:

```bash
ollama run gemma3:1b
```

---

## 10. Running the Project

Activate the virtual environment:

```bash
.\.venv\Scripts\Activate.ps1
```

Then run:

```bash
python -m streamlit run app.py
```

The Streamlit application will open in the web browser.

---

## 11. Example Interaction

### User

```text
How can I find accommodation in a new city?
```

### Migrant Voice AI

```text
You can search for accommodation through
local housing websites, community groups,
and trusted rental services. Always verify
the accommodation and rental agreement before
making any payment.
```

---

## 12. Features

* 🎤 Voice-based interaction
* 🤖 AI-powered responses
* 🗣️ Speech recognition
* 🔊 Text-to-speech
* 💬 Chat interface
* 🖥️ Streamlit web application
* 🔒 Local AI processing using Ollama
* ⚡ Simple and beginner-friendly design

---

## 13. Advantages

* Easy to use
* Voice-based interaction
* Reduces dependence on typing
* Provides quick AI responses
* Can run with a local AI model
* Useful for demonstrating Generative AI
* Can be extended to support multiple languages

---

## 14. Future Enhancements

Future versions can include:

* Multiple language support
* Translation between languages
* Location-based information
* Emergency information
* Job information
* Accommodation information
* Government service information
* Mobile application support
* Improved speech recognition
* More advanced AI models

---

## 15. Conclusion

Migrant Voice AI demonstrates how artificial intelligence and voice technologies can be combined to create a useful communication assistant. The system allows users to communicate through speech and receive AI-generated responses.

The project provides a foundation for developing more advanced multilingual and voice-based applications that can assist people in different environments.

---

## 16. References

1. Python Documentation
2. Streamlit Documentation
3. Ollama Documentation
4. SpeechRecognition Python Library
5. pyttsx3 Python Library
6. Gemma AI Model Documentation
