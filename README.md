# Market Research & Use Case Generation Agent

## Project Overview
This project is a Multi-Agent architecture system designed to generate relevant AI and Generative AI (GenAI) use cases for a given company or industry. The system conducts market research, understands the industry and products, and provides resource assets for AI/ML solutions. It focuses on enhancing operations and customer experiences while delivering actionable insights.

The Multi-Agent system includes the following agents:
1. **Research Agent**: Conducts market research and gathers industry insights.
2. **Use Case Agent**: Proposes AI/GenAI use cases based on research findings.
3. **Resource Asset Agent**: Identifies and collects datasets relevant to the proposed use cases.
4. **Final Proposal Agent**: Compiles the generated use cases and resource links into a comprehensive report.

---

## Features
- **Industry Research**: Analyzes market trends and company focus areas.
- **AI Use Case Generation**: Proposes actionable AI/GenAI use cases tailored to the company's needs.
- **Resource Collection**: Identifies relevant datasets from platforms like Kaggle, HuggingFace, and GitHub.
- **Extensible Framework**: Allows easy adaptation to new industries or companies.

---

## Project Structure
```plaintext
Market_Research_UseCase_Agent/
├── README.md
├── agents
│   ├── __init__.py
│   ├── research_agent.py          # Conducts industry and company research
│   ├── use_case_agent.py          # Generates AI/GenAI use cases
│   ├── resource_asset_agent.py    # Collects datasets for use cases
│   ├── final_proposal_agent.py    # Compiles and formats the final report
│   ├── proposed_use_cases.json    # Stores the generated use cases
│   ├── main.py                    # Entry point for running all agents
├── demo.py                        # Demonstrates the system's functionality
├── kaggle.json                    # API key for accessing Kaggle datasets
├── requirements.txt               # Python dependencies
```

## Prerequisites

- **Python 3.8 or higher**
- **Forefront API key**: Sign up at [Forefront AI](https://www.forefront.ai)
- **Internet connection**: Required for making API calls


## Setup and Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Princccee/Multi-AI-agent-system.git
    cd Multi_agent_system
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv .venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up API key**:
    - Place your `kaggle.json` file in the root directory of the project.
    - Create a .env file and store these API keys.
    ```plaintext
    FOREFRONT_API_KEY=your_forefront_api_key
    SERPAPI_API_KEY=your_serpapi_api_key
    KAGGLE_API_KEY=your_kaggle_api_key
    HUGGINGFACE_API_KEY=your_huggingface_api_key
    GITHUB_API_KEY=your_github_api_key
    GOOGLE_API_KEY=your_google_api_key
    GOOGLE_CSE_ID=your_google_cse_id
    API_KEY=your_kaggle_api_key
    ```

5. **Run the demo**:
    ```sh
    cd agents
    python main.py  # Execute the main.py file to start the app
    ```

---

This setup will ensure that you have all the necessary dependencies and configurations to run the Multi-Agent system effectively.
