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
       
           
                 