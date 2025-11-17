from llm.pubmed_query import PUBMED_QUERY
from llm import gemini, utils

def generate_pubmed_query(pubmed_query_instruction):
    pubmed_query_generation_prompt = PUBMED_QUERY.generate_prompt_for_pubmed_query(pubmed_query_instruction)
    gemini_output = gemini._gemini_complete(pubmed_query_generation_prompt)
    return utils.safe_json_value(gemini_output)["pubmed_query"]