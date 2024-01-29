import langid
def detect_language(text):
    lang, _ = langid.classify(text)
    return lang