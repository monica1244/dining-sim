import re
import string
from collections import OrderedDict


frequency = {}
document_text = open('test.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{4,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     

frequency = OrderedDict(sorted(frequency.items(), key=lambda v: v[1], reverse=True))
frequency_list = frequency.keys()
for words in frequency_list:
    print(frequency[words])