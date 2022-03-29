#i love you in different languages


import pyttsx3

data=open('iloveyou.txt',encoding='utf-8').readlines()
print(data) 
for  item in data:
    pyttsx3.speak(item)
