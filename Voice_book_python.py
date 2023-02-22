import pyttsx3
book = open (r"book.text")
book_text=book.readline()
engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()