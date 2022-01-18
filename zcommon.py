import re
from typing import Text
from bs4 import BeautifulSoup

filename="tesla2019.html"
if filename.split('.')[-1] == 'html':
    with open(filename, encoding="utf-8") as fp:
        soup = BeautifulSoup(fp, "html.parser")
elif filename.split('.')[-1] == 'htm':
    with open(filename) as fp:
        soup = BeautifulSoup(fp, "html.parser")

all_text = soup.text
all_anchors = soup.find_all('a')
required_anchors = []

for anchor in all_anchors:
    try:
        if '#' not in anchor['href']:
            continue
        link = anchor['href'].split('#')[-1]

        if link not in required_anchors:
            required_anchors.append(link)
    except KeyError:
        continue

first_anchor, second_anchor = required_anchors[0], required_anchors[1]
length = len(required_anchors)
count = 1
section_texts = []

for index, anchor in enumerate(required_anchors):
    try:
        element = soup.find('a', id = anchor).parent.next_sibling        
        element2= soup.find('a', id = required_anchors[index + 1]).parent.next_sibling
        while element.next_sibling != soup.find('a', id = required_anchors[index + 1]).parent:
            section_texts.append(element.text)
            element = element.next_sibling
    except:
        continue

while count<(length-1):
    try:
        find_anchor_parent_1 = soup.find('a', {'name':first_anchor}).parent
        find_anchor_parent_2 = soup.find('a', {'name':second_anchor}).parent
        text_between = all_text[all_text.find(find_anchor_parent_1.text):all_text.find(find_anchor_parent_2.text)]
        section_texts.append({find_anchor_parent_1.text.replace('\n', '').replace('\xa0', ''): text_between.replace('\n', '').replace('\xa0', '')})
        first_anchor, second_anchor = required_anchors[count], required_anchors[count+1]
        count += 1
    
    except AttributeError:        
        find_anchor_parent_1 = soup.find('p',id = first_anchor)
        find_anchor_parent_2 = soup.find('p',id = second_anchor)
        text_between = all_text[all_text.find(find_anchor_parent_1.text):all_text.find(find_anchor_parent_2.text)]
        section_texts.append({find_anchor_parent_1.text.replace('\n', '').replace('\xa0', ''): text_between.replace('\n', '').replace('\xa0', '')})
        first_anchor, second_anchor = required_anchors[count], required_anchors[count+1]
        count += 1

    except IndexError:
        break

    except : 
        break      

for text in section_texts:
    asd= str(text)
    with open('ztesla10k.txt', 'a', encoding='utf-8') as f:
     f.write(asd + "\n" + "\n")