import speech_recognition as sr
from os import system as komut

buyukHarflertr='ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
kucukHarflertr='abcçdefgğhıijklmnoöprsştuüvyz'

def lower(text:str):
    newText=str()
    for i in text:
        if i in buyukHarflertr:
            index=buyukHarflertr.index(i)
            newText +=kucukHarflertr[index]      
                        
        else:              
            newText += i  
               
        return newText



r = sr.Recognizer()
with sr.Microphone() as source:
    komut('cls')
    print("Merhabalar efendim ben ulak sizi dinliyorum")
    audio = r.listen(source)

flag=False
    
try:
    text=r.recognize_google(audio, language='tr')
    print("Bunu mu söylemek istediniz efendim: " + text)
    flag=True
    text=lower(text)
    
except sr.UnknownValueError:
    print("Sizi Anlayamadım")
except sr.RequestError as e:
    print("Eşleşme Bulunamadı; {0}".format(e))
    
    
if flag:
    if text =='müzik aç':   
        komut("spotify çalıştır")   