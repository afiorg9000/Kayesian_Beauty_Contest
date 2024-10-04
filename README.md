# EAGxBerkeley 2024 Conference Feedback Analysis

## Key Takeaways and Insights

### Most Accurate Mental Model
- Participants with Entry IDs 3, 17, and 21 had the most accurate perception of other attendees.
- Their consensus rating (9/10) aligned well with the overall conference ratings (Median: 6, Mean: 6.3).

### Most Outlier Experience
- The participant with Entry ID 7 had the most outlier experience.
- Provided a consensus rating of 3/10, significantly lower than the overall ratings.

### Least Favorite Sessions
- Wild Animal Suffering and EA Fundraising were frequently mentioned as least favorite.
- These sessions should be reviewed and possibly revamped to better meet attendee expectations.

### Public Perception of the Missing Stair Problem
- Widely recognized by participants.
- Many expressed frustration over the lack of accountability and action in addressing this problem.
- Feedback points to a need for transparent measures and active efforts to tackle these internal issues.

## Key Patterns Worth Noting

1. Frustration with the 'Missing Stair' Issue
   - Majority of participants are aware of problematic individuals not held accountable.
   - Significant source of discontent requiring urgent attention.

2. Session Quality Concerns
   - Specific sessions, particularly Wild Animal Suffering and EA Fundraising, not meeting expectations.
   - Organizers should consider revising content or improving delivery.

## Actionable Recommendations

1. Improve Session Quality
   - Revamp content or presentation style of poorly-received sessions.
   - Gather more detailed feedback for specific areas of improvement.

2. Address the 'Missing Stair' Problem
   - Create clear policies for accountability and transparency.
   - Proactively communicate steps being taken to resolve these issues.

3. Enhance Community Accountability
   - Handle internal issues visibly to the community.
   - Foster a stronger, healthier community through transparency.

## Running the Python Code for Analysis

### Prerequisites
- Python Version: 3.x
- Virtual Environment (Optional):
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```

### Required Libraries
```bash
pip install pandas openai
```

### Running the Script
```python
import pandas as pd
from openai import OpenAI

# Load feedback data
df = pd.read_csv('EAG_Berkeley_2024_Feedback.csv')

# Convert CSV data to JSON
csv_data = df.to_json(orient='records')

# Initialize OpenAI client
client = OpenAI()

# Request GPT-4 model for analysis
completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an expert in human psychology and collective psychology..."},
        {
            "role": "user",
            "content": f"Jump right in... {csv_data}"
        }
    ]
)

# Output the response
print(completion.choices[0].message)
```

### Expected Output
The output will provide a concise and actionable analysis of the feedback, detailing:
- Participants with the most accurate mental models
- Those who experienced the most outlier perspectives
- Least favorite sessions
- Community's overall perception of the "Missing Stair" issue
- Key patterns and suggestions for future improvements