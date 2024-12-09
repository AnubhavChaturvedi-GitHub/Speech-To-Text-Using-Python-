# Speech Recognition Listener

This Python script provides a speech recognition interface using the `speech_recognition` library. The program captures audio from the microphone, processes it, and converts it to text using Google's Speech Recognition API.

---

### Features
- **Dynamic Energy Threshold**: Enables better adaptation to quieter or noisier environments.
- **Adjustable Settings**: Configurable parameters for energy threshold, pause duration, and more.
- **Error Handling**: Handles unrecognized speech and API errors gracefully.
- **Feedback in Terminal**: Styled console output to indicate the program's state (listening, processing, errors, etc.).

---

### Requirements
- Python 3.6 or higher
- `speech_recognition` library  
  Install it using:  
  ```bash
  pip install SpeechRecognition
  ```

---

### How to Use
1. Clone the repository or copy the script to your local machine.
2. Run the script in your terminal:
   ```bash
   python script_name.py
   ```
3. Speak into the microphone when prompted. The script will process your input and display the recognized text.

---

### Code Overview
```python
import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    # Configurations for better audio detection
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 350
    recognizer.dynamic_energy_adjustment_damping = 0.3
    recognizer.dynamic_energy_ratio = 0.9
    recognizer.pause_threshold = 0.5
    recognizer.operation_timeout = None
    recognizer.non_speaking_duration = 0.5

    # Audio capture and processing
    with sr.Microphone() as source:
        print("\033[92mListening...\033[0m", flush=True)  # Green text
        try:
            audio_data = recognizer.listen(source)
            print("\033[93mProcessing your input...\033[0m", flush=True)  # Yellow text

            # Speech recognition using Google API
            text = recognizer.recognize_google(audio_data, language="en-IN")
            print(f"\033[94mYou said:\033[0m {text}")  # Blue text
            return text

        except sr.UnknownValueError:
            print("\033[91mSorry, I couldn't understand that.\033[0m")  # Red text
        except sr.RequestError as e:
            print(f"\033[91mError: Could not request results. {e}\033[0m")
```

---

### Advanced Enhancements
To make the script more powerful, consider:
- **Multi-language Support**: Add options for recognizing different languages.
- **Custom API Keys**: Use private API keys for higher request quotas.
- **GUI Integration**: Build a user-friendly graphical interface using frameworks like `Tkinter` or `PyQt`.
- **Error Logging**: Log errors to a file for debugging.

---

### Contributing
Pull requests are welcome! For major changes, please open an issue to discuss the improvements.

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add YourFeature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Submit a pull request.

---

### Author
- **Name**: Anubhav Chaturvedi  
- **GitHub**: [AnubhavChaturvedi-GitHyb](https://github.com/AnubhavChaturvedi-GitHub)  
- **YouTube Channel**: [NethyTech](https://www.youtube.com/channel/@nethytech)

---

