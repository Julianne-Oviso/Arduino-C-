# Challenge Number 2

def greet(lang):
  if lang == 'Swahili':
    return'Habari'
  elif lang == 'Ukrainian':
    return'Pryvit'
  else:
    return'Hello'

def main():
    print(greet('Swahili'),'Zuri')
    print(greet('Ukrainian'),'Olena')
    print(greet('en'),'Alex')
    
main() 
