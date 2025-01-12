import os
import requests

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
    # api_key = os.getenv("FOREFRONT_API_KEY", "your_forefront_api_key")

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
            print(f"Error {response.status_code}: {response.text}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    prompt = "Tell me about Apple Inc."
    response = query_forefront(prompt)
    if response:
        print("Model Response:")
        print(response)
    else:
        print("No response received.")
