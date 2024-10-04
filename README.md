# EAGxBerkeley 2024 Conference Feedback Analysis

## Project Overview

This project is a proof of concept for analyzing collective reality through conference feedback using natural language processing and machine learning techniques. The current implementation focuses on the EAGxBerkeley 2024 conference, but the methodology can be extended to other events in the future.

### Key Goals
1. Analyze participant feedback to identify patterns and insights of the collective
2. Provide actionable recommendations for future conference improvements
3. Demonstrate the patterns that arise from the collective.

## Current Implementation

The current codebase consists of a Python script that:
1. Loads conference feedback data from a CSV file
2. Converts the data to JSON format
3. Utilizes OpenAI's GPT-4 model to analyze the feedback
4. Generates a summary report with key insights and recommendations

### Key Findings (Proof of Concept)

- Identified participants with the most accurate perception of the conference
- Highlighted outlier experiences
- Pinpointed least favorite sessions
- Analyzed community perception of the "Missing Stair" problem
- Provided actionable recommendations for future improvements

## Future Work

This proof of concept lays the groundwork for a more comprehensive feedback analysis tool. Future plans include:

1. Incorporating all feedback from EAGxBerkeley
2. Developing a better pipeline (Dont know what that looks like yet)
3. Creating something for visualizing feedback patterns
4. Implementing report to posting on platforms like LessWrong for future Conferences
5. Extending the methodology to analyze feedback from multiple conferences over time

The goal is to create a useful tool for conference communities to analyze collective patterns and continuously improve the collective experience.

## Running the Analysis

### Prerequisites
- Python 3.x
- Virtual Environment (recommended)

### Setup
1. Clone the repository
2. Create and activate a virtual environment (optional):
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
3. Install required libraries:
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
The script generates a comprehensive analysis of the feedback, including:
- Participants with the most accurate mental models
- Outlier experiences
- Least favorite sessions
- Community perception of key issues (e.g., the "Missing Stair" problem)
- Key patterns and trends
- Actionable recommendations for future improvements

## Contributing

We welcome contributions to improve this proof of concept and develop it into a fully-fledged feedback analysis tool.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
