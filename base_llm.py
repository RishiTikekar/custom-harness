import os
import sys
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
base_url=os.environ["BASE_URL"],
api_key=os.environ["API_KET"]
)


user_input=input("Enter your message  : ")

SYSTEM_PROMPT=""" 
You are agent to apply for jobs. You job is to apply for developer jobs on job portals.
"""

response=client.chat.completions.create(
    model="stealth/space-bunny-alpha",
    messages=[
        {
            "role":"system","content":SYSTEM_PROMPT,
            
        },{
            "role":"user","content": user_input
        }
    ]
)

output= response.choices[0].message.content

completion_details=response.usage.completion_tokens_details
prompt_details=response.usage.prompt_tokens_details

usage = {
    "prompt_tokens":response.usage.prompt_tokens,
    "completion_tokens":response.usage.completion_tokens,
    "reasoning_tokens":getattr(completion_details,"reasoning_tokens",None),
    "cached_token":getattr(prompt_details,"cached_token",None),
}

print("\nAgent: ", output, "\n")
print(usage)