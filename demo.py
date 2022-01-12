print("hello")
print("test")
print(3+4)

greeting = 'Hello'
name = ['Rishabh','Akshay','Ashok']

for text in name:
    message = f'{greeting}, {text} Welcome!'
    print(message)

for text in name:
    message = '{}, {} Welcome!'.format(greeting, text)
    print(message)