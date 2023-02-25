key = "864609bac8e94b03aaaa19ec6bdf05a7"
endpoint = "https://smart-strategy.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Authenticate the client using your key and endpoint 
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

# Example function for extracting information from healthcare-related text 
def health_example(client):
    documents = [
        'The storms have impacted the ability of affected populations to access basic goods and services. This is due in part to access issues, with thousands of affected families facing extremely restricted movement and isolation from markets due to accumulation of snow, ice, and floodwater. In addition, road closures have an adverse impact on the income of those engaged in informal or daily labor. Affected families have reported difficulty accessing basic food and water, with some residents of ITS in the Arsal district of Baalbek-Hermel resorting to melting snow for drinking water.'
        ]

    response = client.recognize_entities(documents, language="en")
    result = [doc for doc in response if not doc.is_error]

    events = []
    for doc in result:
        for entity in doc.entities:
            if entity.category == 'Event':
                events.append(entity.text)

            # print(f"Entity: {entity.text}")
            # print(f"...Category: {entity.category}")
            # print(f"...Confidence Score: {entity.confidence_score}")
            # print(f"...Offset: {entity.offset}")

    return events

events = health_example(client)
print(events)