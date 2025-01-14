import json
from agents.research_agent import research_industry_with_summary
from agents.use_case_agent import generate_use_cases
from agents.resource_asset_agent import resource_asset_agent
from agents.final_proposal_agent import final_proposal_agent

def main():
    print("Welcome to the Multi-Agent System for AI/GenAI Solutions!")
    
    # Step 1: Market Research (Research Agent)
    industry = input("Enter the company or industry name: ")

    print("\nConducting market research...")
    research_insights = research_industry_with_summary(industry)
    print("Market Research Insights:\n", research_insights)

    # # Step 2: Generate Use Cases (Use Case Agent)
    # print("\nGenerating relevant AI/GenAI use cases...")
    # use_cases = generate_use_cases(industry,research_insights)
    # print("Proposed Use Cases:")
    # for idx, use_case in enumerate(use_cases, 1):
    #     print(f"{idx}. {use_case}")

    # # Save proposed use cases to a JSON file
    # with open("proposed_use_cases.json", "w") as f:
    #     json.dump(use_cases, f, indent=4)
    # print("\nUse cases saved to 'proposed_use_cases.json'.")

    # # Step 3: Collect Resource Assets (Resource Asset Agent)
    # print("\nCollecting resource assets for proposed use cases...")
    # for use_case in use_cases:
    #     print(f"\nSearching resources for use case: {use_case}")
    #     resource_asset_agent(use_case)
    # print("\nResources saved to 'resources.md'.")

    # # Step 4: Generate Final Proposal (Final Proposal Agent)
    # print("\nGenerating final proposal...")
    # final_proposal_agent(research_insights, use_cases, "resources.md")
    # print("Final proposal saved to 'final_proposal.md'.")

if __name__ == "__main__":
    main()
