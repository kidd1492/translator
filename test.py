import pyttsx3

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine = pyttsx3.init()
engine.setProperty('voice', voice_id)
engine.say("Hello, I can speak offline!")
engine.runAndWait()


help(pyttsx3.engine)