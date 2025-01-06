
# from tkinter import *

# # German dictionary
# dictionary = {
#     "German":{
#     "hello": "Hallo",
#     "goodbye": "Auf Wiedersehen",
#     "thank you": "Danke",
#     "please": "Bitte",
#     "yes": "Ja",
#     "no": "Nein",
#     "good": "gut",
#     "bad": "schlecht",
#     "big": "groß",
#     "small": "klein",
#     "hot": "heiß",
#     "cold": "kalt",
#     "fast": "schnell",
#     "slow": "langsam",
#     "happy": "glücklich",
#     "sad": "traurig",
#     "hungry": "hungrig",
#     "thirsty": "durstig",
#     "beautiful": "schön",
#     "welcome": "Willkommen"
# }}

# # Create the main window
# window = Tk()
# window.title("German Dictionary")

# # Create a label for the English word
# english_word_label = Label(window, text="English Word:")
# english_word_label.pack()

# # Create an entry box for the English word
# english_word_entry = Entry(window, bg="white", fg="black")
# english_word_entry.pack()

# # Create a label for the German translation
# german_word_label = Label(window, text="German Translation:")
# german_word_label.pack(pady=(10,3))

# # Create a label to display the German translation
# german_word_display = Label(window, text="")
# german_word_display.pack()

# # Function to translate the English word
# def translate():
#     english_word = english_word_entry.get().lower
#     if english_word in dictionary :
#         german_word_display.config(text= dictionary[english_word])
#         english_word.config(text = f"Translation:{translate}")
#     else:
#         german_word_display.config(text="Word not found.")

# # Create a button to trigger the translation
# translate_button = Button(window, text="Translate", command=translate, bg="blue", fg="white")
# translate_button.pack(pady=10)
# translate_button.pack()

# # Run the main event loop
# window.mainloop()

from tkinter import *
import tkinter.messagebox as messagebox

# Dictionary of languages and their translations
languages = {
    "English": {
        "hello": "Hello",
        "goodbye": "Goodbye",
        "thank you": "Thank you",
        "please": "Please",
        "yes": "Yes",
        "no": "No"
    },
    "Spanish": {
        "hello": "Hola",
        "goodbye": "Adiós",
        "thank you": "Gracias",
        "please": "Por favor",
        "yes": "Sí",
        "no": "No"
    },
    "French": {
        "Yes": "Oui",
        "goodbye": "Au revoir",
        "Help":"Aide",
        "thank you": "Merci",
        "please": "S'il vous plaît",
        "yes": "Oui",
        "no": "Non",
        "Mother":"Mere",
        "Excuse me":"Excusez-moi",
        "No":"Non",
        "Menu":"Menu",
        "computer":"Ordinateur",
        "Trip":"Voyage",
        "Good luck":"Bonne nuit",
        "see you soon":"A bientot",
        "see you later":"A plus Tard",
        "Father":"Frere",
        "Sorry":"desole(e)",
        "how are you":"Comment ca va",
        "Your welcome":"De rien"

    },
    "German": {
        "hello": "Hallo",
        "goodbye": "Auf Wiedersehen",
        "thank you": "Danke",
        "please": "Bitte",
        "yes": "Ja",
        "no": "Nein"
    }
}

def translate():
    selected_language = language_var.get()
    word = word_entry.get()

    if selected_language in languages and word in languages[selected_language]:
        translation = languages[selected_language][word]
        messagebox.showinfo("Translation", f"{word} in {selected_language}: {translation}")
    else:
        messagebox.showerror("Error", "Word not found or language not supported.")

# Create the main window
window = Tk()
window.title("Colorful Language Translator")
window.geometry("400x300")  # Set window dimensions for spaciousness
window.configure(bg="#f0f0f0")  # Set background color

# Create a label for word input
word_label = Label(window, text="Enter Word:", bg="#f0f0f0", font=("Arial", 12))
word_label.pack(pady=10)

# Create an entry box for word input
word_entry = Entry(window, width=30, font=("Arial", 12))
word_entry.pack()

# Create a frame for language buttons
language_buttons_frame = Frame(window, bg="#f0f0f0")
language_buttons_frame.pack(pady=10)

# Create a StringVar to hold the selected language
language_var = StringVar(window) 

# Create language buttons
for language in languages.keys():
    def create_language_button(lang):
        def translate_to_lang():
            language_var.set(lang) 
            translate() 
        return translate_to_lang

    button = Button(language_buttons_frame, text=language, command=create_language_button(language),
                    width=15, height=2, bg="#4CAF50", fg="white", font=("Arial", 12))
    button.pack(side=LEFT, padx=10)

# Run the main event loop
window.mainloop()