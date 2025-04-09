import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency
from moedas import get_moedas
from fake_useragente import UserAgent

table = get_moedas()
for index,pais in enumerate(table):
  print("#" + str(index+1) + " " + pais['pais'])
print("para sair, digite 'sair'")

def verific_number(imput):
  try:
    if imput == "sair" or imput == "exit": return "sair"
    num_select = int(imput)
  except:
    print("Opção Invalida")
    return False
  
  if num_select > len(table) or  num_select <= 0:
    print("Opção invalida, selecione um entre a lista acima")
    return False
  else:
    return num_select - 1

print("Bem vindo ao negociador de moedas")

while True:
  
  print("Escolha pelo numero o país de origem da moeda \n")
  select1 = input(">>> ")
  
  if verific_number(select1) == False : continue
  
  elif verific_number(select1) == 'sair' : break
    
  else:
    moeda1 = { 'cd_moeda':table[verific_number(select1)]['cd_moeda'],
              'pais': table[verific_number(select1)]['pais']
             }
    print("Quer Negociar com qual outro país ?")
    select2 = input(">>> ")
    
    if verific_number(select2) == False : continue
      
    elif verific_number(select2) == 'sair' : break
      
    else:
      moeda2 = { 'cd_moeda':table[verific_number(select2)]['cd_moeda'],
              'pais': table[verific_number(select2)]['pais']
             }
      
    print("Quantos " + moeda1["cd_moeda"] + " você quer converter para " + moeda2['cd_moeda'])
    value_select = input(">>> ")

    try : 
      format(float(value_select), ".2f")
    except:
      print(" O valor inserido é invalido")
      continue
    

    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}

    url = f"https://wise.com/gb/currency-converter/{moeda1['cd_moeda']}-to-{moeda2['cd_moeda']}-rate?amount={value_select}"

    #US$ 00.00 é igual a ETB 00.00
    convert = requests.get(url,headers=header)
    html = convert.text
    soup = BeautifulSoup(html,'html.parser')
    value = soup.find_all('div', class_='tw-money-input input-group input-group-lg')
    print(value)
    for valor in value:
      valor_convert = valor.find('input').get('value')
      print(valor_convert)
  
   
    
