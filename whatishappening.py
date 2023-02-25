import openai
import os

openai.api_key = "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"

#from Matyi's Azure text analyzer
disaster = "earthquake" 

#ugly solution part 1
prompt1 = "happens. The following problem needs a solution:"

#From Matyi's pdf scaper
problem = "Because the earthquake demolished community shelters and structures, there is an urgent need to offer appropriate sheltering assistance to people staying in tents provided by PRCS. PRCS-S is sheltering 4,000 affected people and plans to set-up additional facilities (tents) to house up to 8,000 people."

#ugly solution part 2 
prompt2 = "Suggest volunteering activities from the above problems in the form: \n Name of the activity, this is not a sentence just a name\n Description of the activity in a maximum of 3 sentences also put a '*' after the descritpion."

#The full prompt: 
prompt = disaster + prompt1 + problem + prompt2

response = openai.Completion.create(
  model="text-davinci-003",
  prompt= prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response["choices"][0]["text"])


tasks = "IdentiHed\nShelter gousinB And Settlements\nBecause the earthquake demolished community shelters and structures, there is an urgent need to oﬀer \nappropriate sheltering assistance to people staying in tents provided by PRCS.\nPRCS-S is sheltering 4,000 aﬀected people and plans to set-up\xa0additional facilities (tents) to house up to 8,000 \npeople.\ngealth\nPRCS-S aims to mobilize emergency medical teams to provide emergency First Aid, PSP , and basic health support \nto 2,500 people. Based on future assessments, PRCS-S may need to scale-up\xa0its health support as needed.\nLivelihoods And basic Needs\nThe earthquake occurred during a particularly harsh winter, with some areas of the country experiencing sub-zero \ntemperatures, at a time when people are facing severe power, fuel, and water shortages.\nThose impacted have lost their fundamental means of subsistence and hence require food and household items \n(HHIs) as well as shelter support.\nAccording to the PRCS-S rapid assessment, the earthquake aﬀected 4,000 people in the Aleppo camps of Al \nNayrab and Handarat, as well as the Latika camp of Al Raml. Those aﬀected have lost their houses and belongings \nand are currently residing in large-scale\xa0tents set up by PRCS.\nThrough this DREF, PRCS-S will provide basic relief items including blankets, warm clothing, mattresses to a total \nof 8,000 people in the target refugees camps."

response2 = openai.Completion.create(
  model="text-davinci-003",
  prompt= "From the following text seperate the headings and the descriptions that follow the title. Correct the typos as well. The text is: {}".format(tasks),
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

response2 = response2["choices"][0]["text"]

response2 = response2.split("Heading:")
for a in range(len(response2)): 
    response2[a] = response2[a].split("Description:")

print(response2)

