from agents.research_agent import research_industry
from agents.use_case_agent import generate_use_cases
from agents.resource_asset_agent import fetch_datasets
from agents.final_proposal_agent import generate_final_proposal

def main():
    company_name = input("Enter the company name: ")

    # Step 1: Research the company and industry
    insights = research_industry(company_name)

    # Step 2: Generate use cases
    use_cases = generate_use_cases(insights['company_info'], insights['industry_trends'])

    # Step 3: Fetch relevant datasets
    datasets = fetch_datasets(use_cases)

    # Step 4: Create the final proposal
    proposal = generate_final_proposal(company_name, use_cases, datasets)
    print(proposal)

    # Save proposal to file
    with open("proposal.txt", "w") as f:
        f.write(proposal)

if __name__ == "__main__":
    main()
