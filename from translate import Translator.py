from translate import Translator
#translator = Translator(to_lang="hi")
#translation = translator.translate("I love sushi.")
#print(translation)
while True:
    to = input("\nenter the language abbreviation : ")
    text = input("enter text : ")
    translation = Translator(from_lang="en",to_lang=to).translate(text)
    print("translated text: ",translation)