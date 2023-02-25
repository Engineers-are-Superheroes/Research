# make api call to https://goadmin.ifrc.org/api/v2/appeal_document/?appeal=3693
import requests
from PyPDF2 import PdfReader
import urllib.request
import re

TASKS = ['Shelter Bousing And Settlements\n']

id = 3691
url = "https://goadmin.ifrc.org/api/v2/appeal_document/?appeal={}".format(id)
response = requests.get(url)
response = response.json()
dref_url = response['results'][0]['document_url']
print(dref_url)

#urllib.request.urlretrieve(dref_url, "dref.pdf")

 
# creating a pdf reader object
reader = PdfReader('dref.pdf')

# getting a specific page from the pdf file
text = ''
for page in reader.pages:
    text += page.extract_text()

tasks = re.findall(r'(?:Needs \(Gaps\))((\n|.)*)(?:Operational Strat)', text)
print(tasks)

shelter = re.findall(r'(?:Shelter)((\n|.)*)(?:ealth)', str(tasks))
print(shelter)
#with open('dref.txt', 'w') as f:
#     f.write(text)
