import requests
from bs4 import BeautifulSoup

def get_paradigm(judge_first, judge_last):
    url = "https://www.tabroom.com/index/paradigm.mhtml"

    form_data = {
        'search_first': judge_first,
        'search_last': judge_last
    }

    response = requests.post(url, data=form_data)
    print(response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')
    unformatted_paradigm = soup.find("div", class_="paradigm ltborderbottom") # Paradigm
    if unformatted_paradigm is None:
        raise Exception("Womp womp judge not found. try again")

    paradigm = ""
    paragraphs = unformatted_paradigm.find_all('p') # Get paragraphs

    for i, paragraph in enumerate(paragraphs, 1):
        text_content = paragraph.get_text(strip=True) # No whitespace
        paradigm += text_content
        paradigm += '\n'
    
    return paradigm

print(get_paradigm("Bugs", "Bunny")) # Should raise exception