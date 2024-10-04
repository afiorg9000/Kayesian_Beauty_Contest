# EAGxBerkeley 2024 Conference Feedback Analysis

## Project Overview

This project is a poc for interpreting collective reality through conference feedback using openai's API. The current implementation focuses on the EAGxBerkeley 2024 conference, but the methodology can be extended to other conferences in the future.

### Key Goals
- Analyze participant feedback to identify patterns and insights of the collective 
- Provide actionable recommendations for future conference improvements

## Current Implementation

The current codebase consists of a Python script that:
1. Loads conference feedback data from a CSV file
2. Converts the data to JSON format
3. Utilizes OpenAI's GPT-4o model to analyze the feedback
4. Generates a summary report with key insights and recommendations

   ```bash
   completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an expert in human psychology and collective psychology..."},
        {
            "role": "user",
            "content": f"Jump right in. No preamble.Create a concise and actionable post of the EAGxBerkeley 2024 conference feedback, attached here: {csv_data}. Which participants had the most accurate mental model of other attendees? Who had the most outlier experiences? Which session was ranked as the least favorite? What are the key patterns worth noting? What is the public perception of the missing stair problem? Answer all the above simply and actionably that would provide for good blog post seed content for the rationality community."
        }
    ]
   )   
   ```

### Key Findings

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

The goal is to create a useful collective awareness tool for conference communities to interpret patterns behind objective feedback.

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
4. Run the model:
   ```bash
   python3 app.py
   ```
### Expected Output
The script generates a comprehensive analysis of the feedback, including:
- Participants with the most accurate mental models
- Outlier experiences
- Least favorite sessions
- Community perception of key issues (e.g., the "Missing Stair" problem)
- Key patterns and trends within the collective
- Actionable recommendations for future improvements
