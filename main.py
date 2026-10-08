import speech_recognition as sr

# Create a recognizer object
recognizer = sr.Recognizer()


# Use the microphone
with sr.Microphone() as source:
    print("Adjusting for background noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

    print("Listening...")
    audio = recognizer.listen(source)

# Convert speech to text
try:
    text = recognizer.recognize_google(audio, language="en-IN")

    print("You said:")
    print(text)

except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")

except sr.RequestError:
    print("Sorry, the speech recognition service is unavailable.")

""" languages={"Hindi":"hi-IN",
"Telugu":"te-IN",
"Tamil":"ta-IN",
"Kannada":"kn-IN",
"Malayalam":"ml-IN",
"Marathi":"mr-IN",
"Bengali":"bn-IN",
"Gujarati":"gu-IN",
"Punjabi":"pa-IN",
"Urdu":"ur-IN",
"Odia":"or-IN",
"Assamese":"as-IN",
"Nepali":"ne-NP",
"Sanskrit":"sa-IN",
"French":"fr-FR",
"French(Canada)":"fr-CA",
"German":"de-DE",
"Spanish":"es-ES",
"Spanish(LatinAmerica)":"es-419",
"Italian":"it-IT",
"Portuguese":"pt-PT",
"Portuguese(Brazil)":"pt-BR",
"Dutch":"nl-NL",
"Russian":"ru-RU",
"Ukrainian":"uk-UA",
"Polish":"pl-PL",
"Czech":"cs-CZ",
"Slovak":"sk-SK",
"Romanian":"ro-RO",
"Hungarian":"hu-HU",
"Greek":"el-GR",
"Bulgarian":"bg-BG",
"Croatian":"hr-HR",
"Serbian":"sr-RS",
"Slovenian":"sl-SI",
"Danish":"da-DK",
"Swedish":"sv-SE",
"Norwegian":"no-NO",
"Finnish":"fi-FI",
"Icelandic":"is-IS",
"Turkish":"tr-TR"} """