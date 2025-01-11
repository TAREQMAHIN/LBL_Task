import openai

class FeatureComparisonAgent:
    def __init__(self, api_key):
        openai.api_key = api_key

    def compare_features(self, competitors):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a feature comparison assistant. Compare the features of the given competitors."},
                {"role": "user", "content": str(competitors)}
            ]
        )
        return response['choices'][0]['message']['content']

# Example usage:
# agent = FeatureComparisonAgent("your_openai_api_key")
# competitors = {"Competitor A": ["Feature 1", "Feature 2"], "Competitor B": ["Feature 1", "Feature 3"]}
# comparison = agent.compare_features(competitors)