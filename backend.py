import openai
import os
import requests
from PyPDF2 import PdfReader
import urllib.request
import re





def backend(id,d_type):

    # USE ID TO DOWNLOAD PDF AND EXTRACT txt

    openai.api_key = "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"

    url = "https://goadmin.ifrc.org/api/v2/appeal_document/?appeal={}".format(id)
    response = requests.get(url)
    response = response.json()
    dref_url = response['results'][0]['document_url']
    print(dref_url)

    urllib.request.urlretrieve(dref_url, "dref.pdf")


    # creating a pdf reader object
    reader = PdfReader('dref.pdf')

    # getting a specific page from the pdf file
    text = ''
    for page in reader.pages:
        text += page.extract_text()

    tasks = re.findall(r'(?:Needs \(Gaps\))((\n|.)*)(?:Operational Strat)', text)[0][0]

    #os.remove('dref.pdf')
    #os.remove('dref.txt')


    prompt = d_type + "happens. The following problem needs a solution: " + tasks + "Suggest volunteering activities from the above problems in the form: \n Name of the activity, this is not a sentence just a name\n Description of the activity in a maximum of 3 sentences."

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    jobs = response["choices"][0]["text"]

    jobs = jobs.split("\n")
    
    for a in range(len(jobs)):
        jobs[a] = jobs[a][2:]
        jobs[a] = jobs[a].split(":")

    jobs = jobs[2:]

    return jobs


if __name__ == "__main__":


    

    id = 3691
    d_type = "Earthquake"

    print(backend(id,d_type))