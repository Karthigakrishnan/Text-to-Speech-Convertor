import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Function to set properties (voice and rate)
def set_properties():
    voices = engine.getProperty('voices')
    
    # Set voice (you can change index to switch between male/female voices)
    voice_choice = input("Choose voice (1 for Male, 2 for Female): ")
    if voice_choice == '1':
        engine.setProperty('voice', voices[0].id)  # Male voice
    else:
        engine.setProperty('voice', voices[1].id)  # Female voice
    
    # Set rate (speed of speech)
    rate = input("Enter the speech rate (default is 200, higher is faster): ")
    engine.setProperty('rate', int(rate) if rate else 200)

# Function to convert text to speech
def text_to_speech():
    text = input("Enter text to convert to speech: ")
    engine.say(text)
    engine.runAndWait()

def main():
    print("Welcome to the Text-to-Speech Converter!")
    while True:
        set_properties()
        text_to_speech()
        
        # Ask if the user wants to repeat or exit
        repeat = input("Do you want to convert another text? (y/n): ").strip().lower()
        if repeat != 'y':
            print("Thanks for using the Text-to-Speech Converter!")
            break

if __name__ == "__main__":
    main()
