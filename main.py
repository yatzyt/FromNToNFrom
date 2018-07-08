from tkinter import IntVar, StringVar, W
from tkinter.ttk import *
from ttkthemes import themed_tk as tk
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

# The language to translate from
from_lang = "en"

# The language to translate to
to_lang = "zh-cn"

# Id for tk's after
after_id = ""

if __name__ == "__main__":
    r = tk.ThemedTk()
    r.get_themes()
    r.set_theme("arc")
    Style().configure('.', font='Helvetica')

    # Initialize clipboard upon starting
    curr_clip = r.clipboard_get()

    r.title("FromNToNFrom")

    auto = 0

    def translate_auto(in_text):
        global translate_text, from_lang, to_lang, r, curr_clip, double_trans_flag
        translator = Translator()
        text_to_trans = in_text
        translated = translator.translate(text_to_trans, dest=to_lang, src=from_lang).text
        print("Translate 1: {}".format(translated))
        r.clipboard_clear()
        r.clipboard_append(translated)
        curr_clip = translated

        if double_trans_flag.get():
            translated = translator.translate(translated, src=to_lang, dest=from_lang).text
            print("Translate 2: {}".format(translated))
            r.clipboard_clear()
            r.clipboard_append(translated)
            curr_clip = translated

        return translated

    # Checks if clipboard was updated
    # Returns true if updated, false if not
    def check_clipboard():
        global curr_clip, r
        temp = r.clipboard_get()
        if temp != curr_clip:
            translated = translate_auto(temp)
            curr_clip = translated
            return True
        else:
            return False

    # Listens for intervals
    def run_listener(window, interval):
        global after_id
        check_clipboard()
        after_id = window.after(interval, run_listener, window, interval)

    # Creating auto translate option
    check_auto_var = IntVar()

    button_text = StringVar()
    button = Button(r, textvariable=button_text)

    # updates autoflag
    def update_auto():
        global auto, r
        auto = check_auto_var.get()
        if auto:
            button.config(state=DISABLED)
            run_listener(r, 500)
        else:
            button.config(state=NORMAL)
            r.after_cancel(after_id)

    check_auto_button = Checkbutton(r, text="Auto", variable=check_auto_var, command=update_auto)

    # Creating translate from language setting
    from_lang_var = StringVar()
    from_label_var = StringVar()
    from_label = Label(r, textvariable=from_label_var)

    # Sets the from_lang variable to a new value
    def from_tracer(n, m, x):
        global from_lang
        from_lang = LANGS[from_lang_var.get()]

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

    to_lang_var.set("Chinese Simplified")
    to_lang_var.trace('w', to_tracer)

    to_lang_combo = Combobox(r, state="readonly", width=20, textvariable=to_lang_var)
    to_lang_combo['values'] = list(LANGS.keys())

    button_text.set("Translate")

    from_label_var.set("From:")
    to_label_var.set("To:")

    double_trans_flag = IntVar()
    double_trans_flag.set(1)
    double_trans_check = Checkbutton(r, text="Translate from then back", variable=double_trans_flag)

    translate_text = StringVar()
    translate_textbox = Entry(r, width=46, textvariable=translate_text)

    def translate():
        global translate_text, from_lang, to_lang, r, curr_clip, double_trans_flag
        translator = Translator()
        text_to_trans = translate_text.get()
        translated = translator.translate(text_to_trans, dest=to_lang, src=from_lang).text
        r.clipboard_clear()
        r.clipboard_append(translated)
        curr_clip = translated

        if double_trans_flag.get():
            translated = translator.translate(translated, src=to_lang, dest=from_lang).text
            r.clipboard_clear()
            r.clipboard_append(translated)
            curr_clip = translated

        return translated

    button.config(command=translate)

    # Pack the widgets in grids
    from_label.grid()
    to_label.grid(row=0, column=1)
    from_lang_combo.grid(row=1)
    to_lang_combo.grid(row=1, column=1)
    check_auto_button.grid(row=1, column=2, sticky=W)
    translate_textbox.grid(row=2, columnspan=2)
    button.grid(row=2, column=2)
    double_trans_check.grid(row=0, column=2, sticky=W)

    r.mainloop()
