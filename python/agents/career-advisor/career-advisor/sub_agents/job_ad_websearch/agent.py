from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-pro"


job_ad_websearch_agent = Agent(
    name="job_ad_websearch",
    model=MODEL,
    instruction=prompt.JOB_AD_WEBSEARCH_PROMPT,
    tools=[google_search],
    output_key="job_ad_info",
)


