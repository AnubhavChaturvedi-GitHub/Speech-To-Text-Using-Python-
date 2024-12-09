import speech_recognition as sr # pip install speech recognition

def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 350
    recognizer.dynamic_energy_adjustment_damping = 0.3  # Adjusts to less/more active environments
    recognizer.dynamic_energy_ratio = 0.9
    recognizer.pause_threshold = 0.5
    recognizer.operation_timeout = None
    recognizer.non_speaking_duration = 0.5

    with sr.Microphone() as source:
        print("\033[92mListening...\033[0m", flush=True)  # Green text for style
        try:
            audio_data = recognizer.listen(source)
            print("\033[93mProcessing your input...\033[0m", flush=True)  # Yellow text for feedback

            # Recognize speech
            text = recognizer.recognize_google(audio_data, language="en-IN")
            print(f"\033[94mYou said:\033[0m {text}")  # Blue text for recognized speech
            return text

        except sr.UnknownValueError:
            print("\033[91mSorry, I couldn't understand that.\033[0m")  # Red text for errors
        except sr.RequestError as e:
            print(f"\033[91mError: Could not request results. {e}\033[0m")

