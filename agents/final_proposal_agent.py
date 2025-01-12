def generate_final_proposal(company_name, use_cases, datasets):
    proposal = f"Proposal for {company_name}\n\n"
    proposal += "Use Cases:\n" + "\n".join(use_cases) + "\n\n"
    proposal += "Datasets:\n" + "\n".join(datasets) + "\n"
    return proposal
