import requests
from bs4 import BeautifulSoup as bs

def intBudgetMaker(budgetStr):
    
    budgetStr = budgetStr.replace("$", "").replace(",", "").replace("(estimated)", "").strip()
    budgetInt = int(budgetStr)
    return budgetInt

    
URL = "https://www.imdb.com/list/ls056515174/?st_dt=&mode=simple&page=1&sort=user_rating,desc"

page = requests.get(URL)

content = bs(page.content, 'html.parser')

counter= 0

print("Name                                                Year     Rate     Budget          Link")
print()
for item in content.find_all('div', {'class': 'lister-item mode-simple'}):
    link = "https://www.imdb.com/"+item.find('div', class_='lister-item-image').find('a')['href']+"?ref_=ttls_li_tt"

    name = item.find('span', class_='lister-item-header').find('a').text.strip()
    year = int(item.find('span', class_='lister-item-year').text[1:5])
    rate = float(item.find('strong').text.strip())
    
    budgetPage = requests.get(link, headers=headers)
    budgetPageContent = bs(budgetPage.content, 'html.parser')
    try:
        budget = budgetPageContent.find(attrs={"data-testid": "title-boxoffice-cumulativeworldwidegross"}).find('span', class_='ipc-metadata-list-item__list-content-item').text
        counter +=1
        
        print(name, " "*(50-len(name)), year, " "*3, rate, " "*4, "$" , intBudgetMaker(budget)+1, " "*10, link)
    except:
        continue
     
print()
print(counter)
