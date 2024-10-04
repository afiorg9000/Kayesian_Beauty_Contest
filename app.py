import pandas as pd
from openai import OpenAI

df = pd.read_csv('EAG_Berkeley_2024_Feedback.csv')

csv_data = df.to_json(orient='records')

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an expert in human psychology and collective psychology. Whose sense of what others thought was most accurate? (what was their user number) Create a surprising and insightful, concise and actionable analysis of the EAGxBerkeley 2024 conference feedback, attached here: {EAG_Berkeley_2024_Feedback.csv}."},
        {
            "role": "user",
            "content": f"Jump right in. No preamble.Create a concise and actionable post of the EAGxBerkeley 2024 conference feedback, attached here: {csv_data}. Which participants had the most accurate mental model of other attendees? Who had the most outlier experiences? Which session was ranked as the least favorite? What are the key patterns worth noting? What is the public perception of the missing stair problem? Answer all the above simply and actionably that would provide for good blog post seed content for the rationality community."
        }
    ]
)

print(completion.choices[0].message)