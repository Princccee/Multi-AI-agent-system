import os
import requests
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from dotenv import load_dotenv
load_dotenv()


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


def summarize_with_gpt(text):
    # Initialize the OpenAI model
    chat_model = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")  # Use your model

    # Create the prompt template
    system_template = "You are an expert in market research. Summarize the following information clearly and concisely."
    human_template = "{text}"

    system_message = SystemMessagePromptTemplate.from_template(system_template)
    human_message = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])

    # Format the prompt with the input text
    formatted_prompt = chat_prompt.format_prompt(text=text)

    # Generate the response
    response = chat_model(formatted_prompt.to_messages())
    return response.content


def research_industry_with_summary(company_name):
    raw_data = research_industry(company_name)

    # Summarize company info
    summarized_company_info = summarize_with_gpt(raw_data["company_info"])
    
    # Summarize industry trends
    summarized_trends = summarize_with_gpt(" ".join(raw_data["industry_trends"]))

    return {
        "company_info": summarized_company_info,
        "industry_trends": summarized_trends
    }

if __name__ == "__main__":
    company_name = input("Enter the company name: ")
    results = research_industry_with_summary(company_name)
    
    print("\n--- Research Results ---")
    print(f"Company Info:\n{results['company_info']}")
    print(f"\nIndustry Trends:\n{results['industry_trends']}")
