import json

from llm.pubmed_query_generation import PUBMED_QUERY
from llm import gemini, utils

def generate_pubmed_query(pubmed_query_instruction):
    print(f"Entered pubmed_query_instruction = {pubmed_query_instruction}")

    pubmed_query_generation_prompt = PUBMED_QUERY.generate_analyst_prompt(pubmed_query_instruction)

    print(f"constructed pubmed_query_generation_prompt: {pubmed_query_generation_prompt}")
    gemini_output = gemini._gemini_complete(pubmed_query_generation_prompt)
    print(f"Output from Gemini = {gemini_output}")
    return utils.safe_json_value(gemini_output)["pubmed_query"]