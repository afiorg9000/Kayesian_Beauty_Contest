import pandas as pd
from openai import OpenAI

df = pd.read_csv('EAG_Berkeley_2024_Feedback.csv')

csv_data = df.to_json(orient='records')

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are the hivemind of Esther Perel. You are an expert in human psychology and collective psychology. You are tasked with creating a concise and actionable analysis of the EAGxBerkeley 2024 conference feedback, attached here: {EAG_Berkeley_2024_Feedback.csv}."},
        {
            "role": "user",
            "content": f"Create a concise and actionable analysis of the EAGxBerkeley 2024 conference feedback, attached here: {csv_data}. Which participants had the most accurate mental model of other attendees? Who had the most outlier experiences? What are the key patterns worth noting? Answer all the above simply and actionably that would provide for good blog post content for the rationality community."
        }
    ]
)

print(completion.choices[0].message)