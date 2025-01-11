from agents.data_retrieval_agent import DataRetrievalAgent

def ingest_data(api_key, sources):
    agent = DataRetrievalAgent(api_key)
    data = {}
    for source in sources:
        data[source] = agent.fetch_data(f"Fetch data from {source}")
    return data

# Example usage:
# sources = ["Crunchbase", "LinkedIn", "Reddit"]
# data = ingest_data("your_openai_api_key", sources)