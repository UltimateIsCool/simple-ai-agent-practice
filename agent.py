import requests
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("api_key") # gets the value from env
model_id = os.getenv("model_id") #gets the value from env
URL = "https://openrouter.ai/api/v1/chat/completions"
headers={
    "Authorization": f"Bearer {api_key}", #dont need the <> its just an example
    "Content-Type": "application/json",
  }
messages = []
new_message = {
    "role": "user", #what role are we ex assistant, which il learn later or are you the user there are a lot of roles i think
    "content": "how many r's in the word strawberry" #what your asking
}
messages.append(new_message)
data = {
    "model": model_id,
    "messages": messages,
    "reasoning": {"enabled": True} #true means it gives the user the reasoning behind its actions, false means it gives u the answer straight up no explantion for how it got it.
  }
response = requests.post(url = URL,headers=headers,json=data) #sends a post request to that url with our headers and json as our data we see what the model wants through the website its simple really
print(response)
response = response.json() #turns the reponse it gets from ai into json, there are a lot of stuff so its hard to see content, you wanna go through and see what in the [] array you need to get the content/reponse. do print(response) to see the whole json data and figure it out
agent_response = response["choices"][0]["message"]#choices of 0 in message is just the answer it gives in our case if you look through the json. agent reponse variable is so we can store it and make sure he doesnt forget later so we have the message
messages.append(agent_response) #so it stores the ais messages so he doesnt forget the conversation
new_message2 = {
  "role":"user",
  "content":"what did i ask you in the last prompt"
}
messages.append(new_message2)

# print(response["choices"][0]["message"]["reasoning"])
print("****************************")
print(response["choices"][0]["message"]["content"])

response = requests.post(url = URL,headers=headers,json=data) # we running it again and since new_message2 is the new message and we are running with messages it will ask the questions again and it will remember previous conversations and in this case it recalls it and will remember context and be able to say what the previous message was
response = response.json()
print(response["choices"][0]["message"]["content"])
#type cls to clear console