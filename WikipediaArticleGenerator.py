from bs4 import BeautifulSoup
import requests
import webbrowser 

while True:
  url = requests.get('https://en.wikipedia.org/wiki/Special:Random')
  content = BeautifulSoup(url.content, 'html.parser')
  title = content.find(class_ = 'firstHeading').text

  print('{} \nPress "Y" to view this article or "N" to find a new one'.format(title))
  answer = input('').upper()

  if answer == 'Y':
    url = "https://en.wikipedia.org/wiki/%s" % title
    webbrowser.open(url)
    break
  elif answer == "N":
    print("Does this interest you?:")
    continue
  else:
    print("Wrong choice!")
    continue