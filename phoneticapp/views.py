from django.shortcuts import render
from .phonet import TextConverter
from .models import Translation

def index(request):
    # Fetch the last 5 translations
    last_five_translations = Translation.objects.order_by('-id')[:5]

    # Pass the last 5 translations to the template
    context = {'last_five_translations': last_five_translations}

    if request.method == 'POST':
        input_text = request.POST.get('inputText', '')
        text_converter = TextConverter()
        nepali_translation = text_converter.translate_eng_to_nepali(input_text)
        hindi_translation = text_converter.translate_eng_to_hindi(input_text)
        urdu_translation = text_converter.translate_eng_to_urdu(input_text)
        telugu_translation = text_converter.translate_eng_to_telugu(input_text)
        original_ipa = text_converter.english_to_ipa(input_text)
        hindi_ipa = text_converter.hindi_to_ipa(hindi_translation)
        urdu_ipa = text_converter.urdu_to_ipa(urdu_translation)
        nepali_ipa = text_converter.nepali_to_ipa(nepali_translation)
        telugu_ipa = text_converter.telugu_to_ipa(telugu_translation)
        
        translation = Translation.objects.create(
            original_text=input_text,
            nepali_translation=nepali_translation,
            hindi_translation=hindi_translation,
            urdu_translation=urdu_translation,
            telugu_translation= telugu_translation,
            original_phonetic=original_ipa,
            hindi_phonetic=hindi_ipa,
            urdu_phonetic=urdu_ipa,
            nepali_phonetic = nepali_ipa,
            telugu_phonetic=telugu_ipa
        )
        translation.save()

        # Update the context with form data and translation results
        context.update({
            'original_text': input_text,
            'nepali_translation': nepali_translation,
            'hindi_translation': hindi_translation,
            'urdu_translation': urdu_translation,
            'telugu_translation':telugu_translation,
            'original_phonetic': original_ipa,
            'nepali_phonetic':nepali_ipa,
            'hindi_phonetic': hindi_ipa,
            'urdu_phonetic': urdu_ipa,
            'telugu_phonetic':telugu_ipa
        })

    # Render the template with the combined context
    return render(request, 'index.html', context)
