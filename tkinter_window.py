from tkinter import *
import tkinter.messagebox as messagebox

# Dictionary of languages and their translations
languages = {
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
        "Father":"Fere",
        "Sorry":"desole(e)",
        "how are you":"Comment ca va",
        "Your welcome":"De rien"

    }, "Spanish": {
  "si":"yes",
  "non":"no",
  "mi corazon":"my heart",
  "puta":"bitch",
  "gringo":"witch",
  "senior":"elder",
  "tamales":"bread",
  "mi gustas":"my freind",
  "hola":"hello",
  "amor":"love",
  "tete":"head",
  "familia":"family",
  "casa":"house",
  "gato":"cat",
  "esculea":"school",
  "agua":"water",
  "felix":"happy",
  "comida":"food",
  "lento":"slow",
  "cielo":"sky",
} }


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
