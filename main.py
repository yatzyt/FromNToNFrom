from tkinter import *
from tkinter.ttk import Combobox
from googletrans import Translator

LANGS = {'Automatic': 'auto', 'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar',
         'Armenian': 'hy', 'Azerbaijani': 'az', 'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn',
         'Bosnian': 'bs', 'Bulgarian': 'bg', 'Catalan': 'ca', 'Cebuano': 'ceb', 'Chichewa': 'ny',
         'Chinese Simplified': 'zh-cn', 'Chinese Traditional': 'zh-tw', 'Corsican': 'co', 'Croatian': 'hr', 'Czech': 'cs',
         'Danish': 'da', 'Dutch': 'nl', 'English': 'en', 'Esperanto': 'eo', 'Estonian': 'et',
         'Filipino': 'fl', 'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy', 'Galician': 'gl',
         'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Gujarati': 'gu', 'Haitian Creole': 'ht',
         'Hausa': 'ha', 'Hawaiian': 'haw', 'Hebrew': 'iw', 'Hindi': 'hi', 'Hmong': 'hmn',
         'Hungarian': 'hu', 'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga',
         'Italian': 'it', 'Japanese': 'ja', 'Javanese': 'jw', 'Kannada': 'kn', 'Kazakh': 'kk',
         'Khmer': 'km', 'Korean': 'ko', 'Kurdish (Kurmanji)': 'ku', 'Kyrgyz': 'ky', 'Lao': 'lo',
         'Latin': 'la', 'Latvian': 'lv', 'Lithuanian': 'lt', 'Luxembourgish': 'lb', 'Macedonian': 'mk',
         'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml', 'Maltese': 'mt', 'Maori': 'mi',
         'Marathi': 'mr', 'Mongolian': 'mn', 'Myanmar (Burmese)': 'my', 'Nepali': 'ne', 'Norwegian': 'no',
         'Pashto': 'ps', 'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa',
         'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm', 'Scots Gaelic': 'gd', 'Serbian': 'sr',
         'Sesotho': 'st', 'Shona': 'sn', 'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk',
         'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw',
         'Swedish': 'sv', 'Tajik': 'tg', 'Tamil': 'ta', 'Telugu': 'te', 'Thai': 'th',
         'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uzbek': 'uz', 'Vietnamese': 'vi',
         'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'}

# Auto Translate Flag
auto = False

# The language to translate from
from_lang = "en"

# The language to translate to
to_lang = "zh-cn"

if __name__ == "__main__":
    r = Tk()

    # Creating auto translate option
    check_auto_var = IntVar()

    # updates autoflag
    def update_auto():
        global auto
        auto = check_auto_var.get()
        print(auto)

    check_auto_button = Checkbutton(r, text="Auto", variable=check_auto_var, height=5, width=20, command=update_auto)

    # Creating translate from language setting
    from_lang_var = StringVar()
    from_label_var = StringVar()
    from_label = Label(r, textvariable=from_label_var)

    # Sets the from_lang variable to a new value
    def from_tracer(n, m, x):
        global from_lang
        from_lang = LANGS[from_lang_var.get()]
        print("From: {}".format(from_lang))

    from_lang_var.set("English")
    from_lang_var.trace('w', from_tracer)

    from_lang_combo = Combobox(r, state="readonly", width=20, textvariable=from_lang_var)
    from_lang_combo['values'] = list(LANGS.keys())

    # Creating translate to language setting
    to_lang_var = StringVar()
    to_label_var = StringVar()
    to_label = Label(r, textvariable=to_label_var)

    # Sets the to_lang variable to a new value
    def to_tracer(n, m, x):
        global to_lang
        to_lang = LANGS[to_lang_var.get()]
        print("To: {}".format(to_lang))

    to_lang_var.set("Chinese Simplified")
    to_lang_var.trace('w', to_tracer)

    to_lang_combo = Combobox(r, state="readonly", width=20, textvariable=to_lang_var)
    to_lang_combo['values'] = list(LANGS.keys())

    button = Button(r)

    from_label_var.set("From:")
    to_label_var.set("To:")

    # Pack the widgets
    check_auto_button.pack()
    from_label.pack()
    from_lang_combo.pack()
    to_label.pack()
    to_lang_combo.pack()
    button.pack()

    r.mainloop()
