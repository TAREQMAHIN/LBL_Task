import openai

class SWOTAnalysisAgent:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_swot(self, data):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a SWOT analysis assistant. Generate a SWOT analysis based on the provided data."},
                {"role": "user", "content": data}
            ]
        )
        return response['choices'][0]['message']['content']

# Example usage:
# agent = SWOTAnalysisAgent("your_openai_api_key")
# swot = agent.generate_swot("Data about a competitor")