from bs4 import BeautifulSoup
import requests

url_link="https://www.microsoft.com/en-us/?ql=2"
result= requests.get(url_link).text
#issuing html data
print(result)
#prettify allow us to print html content
#find()=finds the first matched element
#find_all()= find all the matched element
doc = BeautifulSoup(result, "html.parser")
print(doc.prettify())

#find elements by id
res = doc.find(id = "highlight-uid6a3b")
print(res)

#find element by class
highlight = doc.find(class_="highlight")
print(highlight)