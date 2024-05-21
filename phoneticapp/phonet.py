from text2ipa import get_IPA
import eng_to_ipa
from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator
from googletrans import Translator
from indic_transliteration import sanscript

class TextConverter:
    def __init__(self):
        self.translator = Translator()

    urdu_to_english_mapping = {
        'آ': 'aa', 'ا': 'a', 'ب': 'b', 'پ': 'p', 'ت': 't', 'ٹ': 'ṭ',
        'ث': 'th', 'ج': 'j', 'چ': 'ch', 'ح': 'h', 'خ': 'kh', 'د': 'd',
        'ڈ': 'ḍ', 'ذ': 'z', 'ر': 'r', 'ڑ': 'ṛ', 'ز': 'z', 'ژ': 'zh',
        'س': 's', 'ش': 'sh', 'ص': 'ṣ', 'ض': 'ḍ', 'ط': 'ṭ', 'ظ': 'ẓ',
        'ع': 'a', 'غ': 'gh', 'ف': 'f', 'ق': 'q', 'ک': 'k', 'گ': 'g',
        'ل': 'l', 'م': 'm', 'ن': 'n', 'و': 'o', 'ہ': 'h', 'ھ': 'h',
        'ء': '', 'ئ': '', 'ی': 'y', 'ے': 'e', ' ':' '
    }

    telugu_to_english_mapping = {
    'అ': 'a', 'ఆ': 'aa', 'ఇ': 'i', 'ఈ': 'ii', 'ఉ': 'u', 'ఊ': 'uu',
    'ఋ': 'r', 'ౠ': 'rr', 'ఌ': 'l', 'ౡ': 'll', 'ఎ': 'e', 'ఏ': 'ee',
    'ఐ': 'ai', 'ఒ': 'o', 'ఓ': 'oo', 'ఔ': 'au', 'అం': 'am', 'అః': 'ah',
    'క': 'ka', 'ఖ': 'kha', 'గ': 'ga', 'ఘ': 'gha', 'ఙ': 'ṅa', 'చ': 'cha',
    'ఛ': 'chha', 'జ': 'ja', 'ఝ': 'jha', 'ఞ': 'ña', 'ట': 'ṭa', 'ఠ': 'ṭha',
    'డ': 'ḍa', 'ఢ': 'ḍha', 'ణ': 'ṇa', 'త': 'ta', 'థ': 'tha', 'ద': 'da',
    'ధ': 'dha', 'న': 'na', 'ప': 'pa', 'ఫ': 'pha', 'బ': 'ba', 'భ': 'bha',
    'మ': 'ma', 'య': 'ya', 'ర': 'ra', 'ల': 'la', 'వ': 'va', 'శ': 'śa',
    'ష': 'ṣa', 'స': 'sa', 'హ': 'ha', 'ళ': 'ḷa', 'క్ష': 'kṣa', 'ౘ': 't͟ha',
    'ౙ': 'd͟ha', 'ౚ': 'na', '౛': 'za', '౜': 'ra', 'ౝ': 'ṛa', '౞': 'fa',
    'ౠ': 'ṝa', 'ౡ': 'ḹa', 'ౢ': 'll', 'ౣ': 'lll', '౦': '0', '౧': '1',
    '౨': '2', '౩': '3', '౪': '4', '౫': '5', '౬': '6', '౭': '7', '౮': '8',
    '౯': '9', ' ':' '
    }


    def urdu_to_english_script(self, urdu_text):
        # Transliterate Urdu script to English script using custom mapping
        english_script = ''.join(self.urdu_to_english_mapping[char] if char in self.urdu_to_english_mapping else '' for char in urdu_text)
        return english_script.strip()

    def hindi_to_english_script(self,hindi_text):
        # Transliterate Hindi script to English script
        english_script = sanscript.transliterate(hindi_text, sanscript.DEVANAGARI, sanscript.ITRANS)
        return english_script

    def translate_eng_to_hindi(self, text):
        translation = self.translator.translate(text, dest="hi")
        return translation.text

    def translate_eng_to_nepali(self, text):
        translation = self.translator.translate(text, dest="ne")
        return translation.text

    def translate_eng_to_urdu(self, text):
        translation = self.translator.translate(text, dest="ur")
        return translation.text
    
    def telugu_to_english_script(self, telugu_text):
        # Transliterate Urdu script to English script using custom mapping
        english_script = ''.join(self.telugu_to_english_mapping[char] if char in self.telugu_to_english_mapping else '' for char in telugu_text)
        return english_script.strip()

    

    def translate_eng_to_telugu(self, text):
        translation = self.translator.translate(text, dest="te")
        return translation.text

    def english_to_ipa(self, text):
        ipa = eng_to_ipa.convert(text)
        return ipa

    def hindi_to_ipa(self, hindi_text):
        text = self.hindi_to_english_script(hindi_text)
        ipa = self.english_to_ipa(text)
        ipa = ipa.replace('*','')
        return ipa
    
    def nepali_to_ipa(self,nepali_text):
        text = self.hindi_to_english_script(nepali_text)
        ipa = self.english_to_ipa(text)
        ipa = ipa.replace('*','')
        return ipa

    def urdu_to_ipa(self, urdu_text):
        english_script = self.urdu_to_english_script(urdu_text)
        print(english_script)
        ipa = self.english_to_ipa(english_script)
        ipa = ipa.replace('*','')
        return ipa

    def telugu_to_ipa(self, telugu_text):
        english_script = self.telugu_to_english_script(telugu_text)
        print(english_script)
        ipa = self.english_to_ipa(english_script)
        ipa = ipa.replace('*','')
        return ipa