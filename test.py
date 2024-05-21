from indic_transliteration import sanscript

def hindi_to_english_script(hindi_text):
    # Transliterate Hindi script to English script
    english_script = sanscript.transliterate(hindi_text, sanscript.DEVANAGARI, sanscript.ITRANS)
    return english_script

hindi_text = "आप कैसे हैं?"
english_script_hindi = hindi_to_english_script(hindi_text)
print("Hindi Transliteration:", english_script_hindi)