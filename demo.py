#Trying the combination of text and loops
greeting = 'Hello'
name = ['Rishabh','Akshay','Ashok']
#method 1
for text in name:
    message = f'{greeting}, {text} Welcome!'
    print(message)
#method 2
for text in name:
    message = '{}, {} Welcome!'.format(greeting, text)
    print(message)