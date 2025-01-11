import gradio as gr
from agents.data_retrieval_agent import DataRetrievalAgent
from agents.nlp_processing_agent import NLPProcessingAgent
from agents.feature_comparison_agent import FeatureComparisonAgent
from agents.swot_analysis_agent import SWOTAnalysisAgent
from agents.reporting_agent import ReportingAgent
from data.data_ingestion import ingest_data
from data.data_normalization import normalize_data

# Replace with your actual OpenAI API key
API_KEY = "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"

def generate_competitor_analysis(query):
    # Step 1: Data Ingestion
    sources = ["Crunchbase", "LinkedIn", "Reddit"]
    raw_data = ingest_data(API_KEY, sources)

    # Step 2: Data Normalization
    normalized_data = normalize_data(raw_data)

    # Step 3: NLP Processing
    nlp_agent = NLPProcessingAgent(API_KEY)
    processed_data = nlp_agent.process_text(str(normalized_data))

    # Step 4: Feature Comparison
    feature_agent = FeatureComparisonAgent(API_KEY)
    feature_comparison = feature_agent.compare_features(normalized_data)

    # Step 5: SWOT Analysis
    swot_agent = SWOTAnalysisAgent(API_KEY)
    swot_analysis = swot_agent.generate_swot(processed_data)

    # Step 6: Reporting
    reporting_agent = ReportingAgent(API_KEY)
    report = reporting_agent.generate_report(swot_analysis, feature_comparison)

    return report

# Gradio Interface
def gradio_interface(query):
    report = generate_competitor_analysis(query)
    return report

# Create a Gradio app
iface = gr.Interface(
    fn=gradio_interface,
    inputs=gr.Textbox(lines=2, placeholder="Enter a startup website or product query..."),
    outputs=gr.Textbox(lines=20, label="Competitor Analysis Report"),
    title="Competitor Analysis Tool",
    description="Enter a startup website or product query to generate a comprehensive competitor analysis report."
)

# Launch the Gradio app
iface.launch()