import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding = "utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
#print(root.tag)
#print(root.text)
#print(root.attrib)

description_list = root.findall("channel/item/description")
#print(description_list)

word_list = []

for descript in description_list:
  news2 = descript.text.lower()
  #print(news2)
  n_list = news2.split(" ")
  #print(n_list)
  for w in n_list:
    if len(w) >= 6:
      word_list.append(w)
      #print(word_list)

from collections import Counter
long_words = Counter(word_list).most_common(10)
for k in long_words:
  print(k)       

    
