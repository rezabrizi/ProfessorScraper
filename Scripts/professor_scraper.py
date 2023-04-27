 
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen



def get_page(url):
    req = Request(url)
    html_page = urlopen(req)
    return (BeautifulSoup(html_page, "lxml"))
    

def get_prof_urls():
    page_content = get_page("https://cs.utdallas.edu/people/faculty/")
    with open ('Scripts/text.txt', 'w') as file:  
        file.write(str(page_content))  
    prof_urls = []
    with open ('Scripts/text.txt', 'r') as file: 
        lines = file.readlines()
        counter = 0
        for i in range(len(lines)):
            if 'Professor' in lines[i]:
                temp = (lines[i-1].split('='))
                if len(temp) == 2 or len(temp) == 4: temp = temp[1]
                if len(temp) == 3 or len(temp) == 5: temp =temp[2]
                counter+=1 
                prof_urls.append(temp.split('"')[1])
    return prof_urls




def search_stanford_prof(url):
    page_content = get_page(url)
    if 'stanford' in str(page_content) or 'Stanford' in str(page_content):
        return url 
    


prof_urls = get_prof_urls()
for url in prof_urls:
    res = search_stanford_prof(url)
    if (res): print(res)