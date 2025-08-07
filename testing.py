from googletrans import Translator

translator = Translator()
result = translator.translate("Hello", src="en", dest="hi")
print(result.text)  # Output: नमस्ते
