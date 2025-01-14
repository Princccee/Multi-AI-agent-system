import json

def final_proposal_agent(research_insights, use_cases, resources_file):
    with open("final_proposal.md", "w") as f:
        # Convert dict to JSON string or format it as needed
        research_insights_str = json.dumps(research_insights, indent=4)
        f.write(research_insights_str + "\n\n")
        f.write("Use Cases:\n")
        f.write("\n".join(use_cases) + "\n\n")
        f.write(f"Resources: See {resources_file}\n")
