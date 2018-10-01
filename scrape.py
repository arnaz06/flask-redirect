from bs4 import BeautifulSoup
import requests

def scrape():
  base_url="http://go-jek.com"
  r_link= requests.get(base_url)
  soup= BeautifulSoup(r_link.text,"html.parser")
  find_link= soup.find_all('a',text=True)
  target_link=str(find_link[7])
  final = target_link.split('/')
  return final[1]



if __name__ == "__main__":
  print (scrape())

