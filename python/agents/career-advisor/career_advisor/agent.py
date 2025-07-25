
"""Interview-preparer: Research the job posting, related findings, web knowledge access."""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.job_ad_websearch import job_ad_websearch_agent

MODEL = "gemini-2.5-pro"


job_posting_coordinator_agent = LlmAgent(
    name="job-posting-coordinator",
    model=MODEL,
    description=(
        "Analyze the job posting URL provided "
        "to extract key skills, experiences, and qualifications "
        "required. Use the tools to gather content and identify "
        "and categorize the requirements."
    ),
    instruction=prompt.JOB_POSTING_COORDINATOR_PROMPT,
    output_key="job-ad",
    tools=[
        AgentTool(agent=job_ad_research_agent),
    ],
)

root_agent = job_posting_coordinator_agent 