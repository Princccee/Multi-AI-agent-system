import os
import requests
from dotenv import load_dotenv
load_dotenv()

# Helper Function: Search Kaggle for datasets
def search_kaggle_datasets(query):
    """
    Search Kaggle for datasets related to the query.
    """
    kaggle_api_token = os.getenv("KAGGLE_API_KEY")
    if not kaggle_api_token:
        raise ValueError("KAGGLE_API_KEY environment variable is not set.")
    
    url = f"https://www.kaggle.com/api/v1/datasets/list"
    headers = {
        "Authorization": f"Bearer {kaggle_api_token}",
        "Content-Type": "application/json",
    }
    params = {"search": query}
    
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        datasets = response.json()
        return [
            {"title": d["title"], "url": f"https://kaggle.com/{d['ref']}"} for d in datasets
        ]
    else:
        return []

# Helper Function: Search HuggingFace for datasets and models
def search_huggingface(query, search_type="dataset"):
    """
    Search HuggingFace for datasets or models.
    """
    url = f"https://huggingface.co/api/{search_type}s"
    params = {"search": query}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        items = response.json()
        return [
            {"name": item["id"], "url": f"https://huggingface.co/{item['id']}"} for item in items
        ]
    else:
        return []

# Helper Function: Search research papers using arXiv API
def search_arxiv_papers(query):
    """
    Search arXiv for research papers.
    """
    url = "http://export.arxiv.org/api/query"
    params = {"search_query": query, "start": 0, "max_results": 5}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        import xml.etree.ElementTree as ET

        root = ET.fromstring(response.content)
        papers = []
        for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
            title = entry.find("{http://www.w3.org/2005/Atom}title").text
            link = entry.find("{http://www.w3.org/2005/Atom}id").text
            papers.append({"title": title.strip(), "url": link.strip()})
        return papers
    else:
        return []

# Resource Asset Agent
def resource_asset_agent(use_case):
    """
    Search for datasets, models, and research resources for a specific use case.
    """
    print(f"Searching resources for use case: {use_case}")

    # Search for Kaggle datasets
    kaggle_results = search_kaggle_datasets(use_case)
    print("\nKaggle Datasets:")
    for dataset in kaggle_results:
        print(f"- {dataset['title']}: {dataset['url']}")

    # Search for HuggingFace datasets and models
    huggingface_datasets = search_huggingface(use_case, search_type="dataset")
    huggingface_models = search_huggingface(use_case, search_type="model")
    print("\nHuggingFace Datasets:")
    for dataset in huggingface_datasets:
        print(f"- {dataset['name']}: {dataset['url']}")
    print("\nHuggingFace Models:")
    for model in huggingface_models:
        print(f"- {model['name']}: {model['url']}")

    # Search for research papers
    arxiv_papers = search_arxiv_papers(use_case)
    print("\nResearch Papers:")
    for paper in arxiv_papers:
        print(f"- {paper['title']}: {paper['url']}")

if __name__ == "__main__":
    use_case = input("Enter the use case or topic: ")
    resource_asset_agent(use_case)
