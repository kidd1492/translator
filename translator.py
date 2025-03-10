import translators as ts
import sys
import pyttsx3



def main():
    """Main function to run the program."""
    print("Welcome to the Language Translator!")
    engine = configure_engine()  # Initialize the TTS engine
    language = select_language()
    process_translation(language, engine)
    again(language, engine)


def configure_engine():
    """Configure and return the TTS engine."""
    engine = pyttsx3.init()
    voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice', voice_id)
    engine.setProperty('rate', 180)
    return engine


def select_language():
    """Prompt the user to select a language by name and return the language code."""
    supported_languages = {
        "spanish": "es", "french": "fr", "german": "de",
        "arabic": "ar", "italian": "it", "japanese": "ja",
        "russian": "ru", "chinese": "zh", "korean": "ko"
    }

    while True:
        print("Supported Languages:")
        for lang in supported_languages:
            print(f"- {lang.capitalize()}")

        language_name = input("Enter the language to translate to: ").strip().lower()
        if language_name in supported_languages:
            return supported_languages[language_name]
        print("Invalid language. Please try again.")


def translate(text, language):
    """Translate the given text into the selected language."""
    if not text.strip():
        return "No text to translate."
    try:
        return ts.translate_text(query_text=text, from_language='en', to_language=language)
    except Exception as e:
        return f"Translation failed: {e}"


def process_translation(language, engine):
    """Handle translation and speech."""
    text = input("Enter text: ").strip()
    translated_text = translate(text, language)
    print(translated_text)
    speak(translated_text, engine)


def speak(text, engine):
    """Speak the given text using the TTS engine."""
    engine.say(text)
    engine.runAndWait()


def again(language, engine):
    """Prompt the user to translate another phrase or exit."""
    while True:
        answer = input("Would you like to translate another? (Y/N): ").strip().lower()
        if answer == "y":
            process_translation(language, engine)
        elif answer == "n":
            sys.exit()
        else:
            print("Invalid input. Please enter Y or N.")


if __name__ == "__main__":
    main()
