import openai

class DataRetrievalAgent:
    def __init__(self, api_key):
        openai.api_key = api_key

    def fetch_data(self, query):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a data retrieval assistant. Fetch relevant data about competitors based on the user's query."},
                {"role": "user", "content": query}
            ]
        )
        return response['choices'][0]['message']['content']

# Example usage:
# agent = DataRetrievalAgent("your_openai_api_key")
# data = agent.fetch_data("Find competitors for a SaaS startup offering project management tools.")