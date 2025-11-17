# prompts.py — UPDATED to extract structural domains and regions
from dataclasses import dataclass


@dataclass
class PubmedQueryGeneration:
    # Locked sections (cannot be edited - critical for app functionality)
    _prompt_header: str = """Respond only in JSON. If you cannot construct a pubmed query, respond {}.
All fields are required; if unknown, use null.
"""

    _prompt_output_rules: str = """OUTPUT RULES (format-lock)
• Respond ONLY with a valid JSON that passes json.loads().
• No prose, no markdown, no trailing commas, no comments.
• One JSON object containing the pubmed query in "pubmed_query" parameter.
"""

    _prompt_schema: str = """SCHEMA
The output must follow exactly:
{
  "pubmed_query": "<Pubmed query string or null>"
}
"""

    _prompt_examples: str = """AN EXAMPLE (keep these)
  {
    "pubmed_query": "((Dengue[Title]) AND (protein)) AND ((active site[Text Word]) OR (mutation[Text Word]))",
  }
"""

    _prompt_footer: str = """**CRITICAL**: The generated query must follow the Pubmed query syntax.
"""

    # Editable sections (can be modified by users)
    # Part 1: SYSTEM/INSTRUCTION and DEFINITIONS (comes before OUTPUT RULES)
    _analyst_prompt_instruction: str = """SYSTEM / INSTRUCTION
You are a biomedical text-mining specialist. Write a query to search Pubmed for the given specification: '{_analyst_pubmed_query_instruction}'.
"""


    def generate_analyst_prompt(self, pubmed_query_instruction) -> str:
        """Assemble the full prompt from locked and editable sections."""
        # If there's an override (set directly), use it for backward compatibility

        # Otherwise, assemble from parts in the correct order:
        # Header → Editable Part1 (SYSTEM + DEFINITIONS) → OUTPUT RULES → SCHEMA → EXAMPLES → Editable Part2 (INSTRUCTIONS) → Footer
        return (
            self._prompt_header +
            "\n" +
            self._analyst_prompt_instruction.format(_analyst_pubmed_query_instruction=pubmed_query_instruction) +
            "\n" +
            self._prompt_output_rules +
            "\n" +
            self._prompt_schema +
            "\n" +
            self._prompt_examples +
            "\n" +
            self._prompt_footer
        )

    def pubmed_query(self, value:str):
        self._pubmed_query = value
        return self._pubmed_query

PUBMED_QUERY = PubmedQueryGeneration()

