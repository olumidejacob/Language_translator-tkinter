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

    },

    "Spanish": {
  "yes":"si",
  "no":"non",
  "myu heart":"mi crayon",
  "bitch":"puta",
  "witch":"gringo",
  "elder":"senior",
  "tamales":"bread",
  "mi gustas":"my freind",
  "hello":"halo",
  "love":"amor",
  "head":"tete",
  "familia":"family",
  "casa":"house",
  "gato":"cat",
  "esculea":"school",
  "agua":"water",
  "felix":"happy",
  "comida":"food",
  "lento":"slow",
  "cielo":"sky",
},

  "arabic" : {
    "peace" : "salam",
    "love" : "hob",
    "book" : "kitab",
    "knowledge" : "ilm",
    "friend" : "sadeeq",
    "sun" : "shams",
    "moon" : "qamar",
    "homeland" : "watan",
    "hope" : "amal",
    "freedom" : "hurriya",
    "dream" : "hulum",
    "house" : "bayt",
    "road" : "tariq",
    "sea" : "bahr",
    "flower" : "wardah",
    "heat" : "qalb",
    "language" : "lugha",
    "world" : "aalam",
    "soul" : "rouh",
    "generousity" : "karam"
},
    
    "german_words" : {
"hello": "hallo",
"goodbye": "auf wiedersehen",
"thank_you": "danke",
"yes": "ja",
"no": "nein",
"water": "wasser",
"food": "essen",
"house": "haus",
"car": "auto",
"tree": "baum",
"dog": "hund",
"cat": "katze",
"sun": "sonne",
"moon": "mond",
"school": "schule",
"book": "buch",
"pen": "stift",
"paper": "papier"
},
    "Yoruba_dict" : {
"hello": "Bawo ni",
"goodbye": "O dabọ",
"thank you": "E se",
"yes": "Bẹẹni",
"no": "Rara",
"water": "Omi",
"food": "Ounje",
"house": "Ile",
"car": "Okọ",
"tree": "Igi",
"dog": "Aja",
"cat": "Ologbo",
"sun": "Oorun",
"moon": "Osupa",
"school": "Ile-ẹkọ",
"book": "Iwe",
"pen": "Biro",
"paper": "Kaga"
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
