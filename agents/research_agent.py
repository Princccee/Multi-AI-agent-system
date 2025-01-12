import os
import requests
from dotenv import load_dotenv
load_dotenv()

# Define the query_forefront function
def query_forefront(prompt, model="forefront/Mistral-7B-claude-chat", max_tokens=300, temperature=0.5):
    """
    Queries the Forefront API with a specified prompt and returns the model's response.
    
    Args:
        prompt (str): The input prompt to send to the model.
        model (str): The model name to use (default: "forefront/Mistral-7B-claude-chat").
        max_tokens (int): The maximum number of tokens to generate (default: 128).
        temperature (float): Sampling temperature for randomness in responses (default: 0.5).
    
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

def research_industry(company_name):
    # Build search query
    search_query = f"{company_name} industry overview and AI trends"
    print(f"Researching: {search_query}")
    
    # Perform a web search using SerpAPI
    serpapi_api_key = os.getenv("SERPAPI_API_KEY")
    if not serpapi_api_key:
        raise ValueError("SERPAPI_API_KEY environment variable is not set.")

    serpapi_url = "https://serpapi.com/search"
    params = {
        "q": search_query,
        "api_key": serpapi_api_key,
        "engine": "google",
    }

    response = requests.get(serpapi_url, params=params)
    if response.status_code != 200:
        raise Exception(f"SerpAPI request failed: {response.text}")

    search_results = response.json().get("organic_results", [])
    if not search_results:
        return {"company_info": "No data found", "industry_trends": "No trends found"}

    # Parse and structure the results
    company_info = search_results[0].get("snippet", "No company info available")
    industry_trends = [result.get("snippet", "No snippet") for result in search_results[:3]]

    # Return results
    return {
        "company_info": company_info,
        "industry_trends": industry_trends
    }


def summarize_with_forefront(text):
    """
    Summarize text using Forefront API.
    """
    prompt = f"You are an expert in market research. Summarize the following information clearly and concisely:\n\n{text}"
    response = query_forefront(prompt, max_tokens=500)
    return response if response else "No summary available."


def research_industry_with_summary(company_name):
    # Retrieve raw industry data
    raw_data = research_industry(company_name)

    # Combine all retrieved industry trends for a more complete summary
    combined_trends = " ".join(raw_data["industry_trends"])

    # Summarize with error handling
    summarized_company_info = summarize_with_forefront(raw_data["company_info"] or "No company info available")
    summarized_trends = summarize_with_forefront(combined_trends or "No industry trends available")

    # Ensure summaries are not truncated
    if len(summarized_company_info) < 50:
        summarized_company_info += " (Info may be limited; please verify sources.)"
    if len(summarized_trends) < 50:
        summarized_trends += " (Trends may be incomplete; please verify sources.)"

    return {
        "company_info": summarized_company_info.strip(),
        "industry_trends": summarized_trends.strip()
    }

if __name__ == "__main__":
    company_name = input("Enter the company name: ")
    results = research_industry_with_summary(company_name)
    
    print("\n--- Research Results ---")
    print(f"Company Info:\n{results['company_info']}")
    print(f"\nIndustry Trends:\n{results['industry_trends']}")
