import os
import requests
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Forefront API Query Function
def query_forefront(prompt, model="forefront/Mistral-7B-claude-chat", max_tokens=500, temperature=0.7):
    """
    Queries the Forefront API with a specified prompt and returns the model's response.
    
    Args:
        prompt (str): The input prompt to send to the model.
        model (str): The model name to use (default: "forefront/Mistral-7B-claude-chat").
        max_tokens (int): The maximum number of tokens to generate (default: 500).
        temperature (float): Sampling temperature for randomness in responses (default: 0.7).
    
    Returns:
        str: The response text from the model, or None if an error occurs.
    """
    # Forefront API endpoint
    url = "https://api.forefront.ai/v1/chat/completions"

    # Set API key
    api_key = os.getenv("FOREFRONT_API_KEY")
    if not api_key:
        raise ValueError("FOREFRONT_API_KEY environment variable is not set.")

    # Request payload
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": max_tokens,
        "temperature": temperature,
    }

    # Request headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    try:
        # Make the POST request
        response = requests.post(url, json=payload, headers=headers)
        
        # Handle response
        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("message", {}).get("content", None)
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Use Case Generation Function
def generate_use_cases(company_name, research_results):
    """
    Generates AI/GenAI use cases based on insights from the Research Agent.
    
    Args:
        company_name (str): Name of the company/industry.
        research_results (dict): Insights from the Research Agent.

    Returns:
        list: A list of proposed use cases.
    """
    # Construct the prompt
    prompt = (
        f"Based on the following insights about {company_name}, suggest AI/GenAI use cases:\n\n"
        f"Company Info:\n{research_results['company_info']}\n\n"
        f"Industry Trends:\n{research_results['industry_trends']}\n\n"
        "1. Suggest AI/GenAI use cases for the company.\n"
        "2. List operations that can benefit from AI.\n"
        "3. Include potential datasets and implementation steps for each use case.\n\n"
        "Provide concise but detailed recommendations."
    )
    
    # Query the Forefront API
    response = query_forefront(prompt)
    
    if response:
        # Process response into a structured list
        use_case_list = [line.strip() for line in response.split("\n") if line.strip()]
        return use_case_list
    else:
        return ["No use cases could be generated."]


if __name__ == "__main__":
    # Example execution
    # Mocked research results for testing
    research_results = {
        "company_info": "Tesla specializes in advanced AI for autonomous vehicles and robotics.",
        "industry_trends": (
            "AI is being heavily integrated into vehicle automation, robotics, and manufacturing. "
            "AI-driven predictive maintenance and supply chain optimization are gaining traction."
        ),
    }

    # Specify company name
    company_name = "Tesla"
    
    # Generate use cases
    use_cases = generate_use_cases(company_name, research_results)
    
    # Print and save the results
    print("\n--- Proposed Use Cases ---")
    for i, use_case in enumerate(use_cases, 1):
        print(f"{i}. {use_case}")
    
    # Save as a JSON file
    with open("proposed_use_cases.json", "w") as f:
        json.dump(use_cases, f, indent=4)
