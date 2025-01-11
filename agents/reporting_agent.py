import openai

class ReportingAgent:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_report(self, swot_analysis, feature_comparison):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a reporting assistant. Generate a comprehensive competitor analysis report."},
                {"role": "user", "content": f"SWOT Analysis: {swot_analysis}\nFeature Comparison: {feature_comparison}"}
            ]
        )
        return response['choices'][0]['message']['content']

# Example usage:
# agent = ReportingAgent("your_openai_api_key")
# report = agent.generate_report("SWOT analysis data", "Feature comparison data")