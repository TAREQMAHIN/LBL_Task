import openai

class NLPProcessingAgent:
    def __init__(self, api_key):
        openai.api_key = api_key

    def process_text(self, text):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an NLP processing assistant. Analyze the text and extract key insights."},
                {"role": "user", "content": text}
            ]
        )
        return response['choices'][0]['message']['content']

# Example usage:
# agent = NLPProcessingAgent("your_openai_api_key")
# processed_data = agent.process_text("Sample text to process")