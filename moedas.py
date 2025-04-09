import requests
from bs4 import BeautifulSoup

def get_moedas():
  url = "https://iban.com/currency-codes"
  request = requests.get(url)
  
  html = request.text
  soup = BeautifulSoup(html, "html.parser")
  tabela = soup.find_all('table', class_='table table-bordered downloads tablesorter')
  for row in tabela:
      a = row.find_all('tr')
      break
  
  table = []
  for cell in a:
      a = (cell.get_text().split("\n"))
      for l in a:
          if l == '':
              a.remove(l)
      if a[1].lower() == "no universal currency":
        continue
      
      lista = {
        'pais':a[0],
        'moeda':a[1],
        'cd_moeda':a[2],
        'number_moeda': a[3]
      }
      table.append(lista)
  table.pop(0)
  
  return table
  
