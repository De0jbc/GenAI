from crewai import Agent
from langchain_community.llms import OpenAI
from langchain_core.tools import BaseTool
from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from langchain.tools import StructuredTool
from typing import List
from langchain.tools import tool

#tools = [
#    SearchTools.search_internet,  # Ya es un StructuredTool
#    BrowserTools.scrape_and_summarize_website  # Asegúrate que este también lo sea
#]



tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ]

class TripAgents():
  
  def city_selection_agent(self):
    return Agent(
        role='City Selection Expert',
        goal='Select the best itinerari from selected cities based on weather, season, and prices',
        backstory=
        'An expert in analyzing travel data to pick ideal destinations',
        #tools=tools,
        verbose=True)

  def local_expert(self):
    return Agent(
        role='Local Expert at this city',
        goal='Provide the BEST insights about the selected cities',
        backstory="""A knowledgeable local guide with extensive information
        about the cities, it's attractions and customs""",
        #tools=tools,
        verbose=True)

  def travel_concierge(self):
    return Agent(
        role='Amazing Travel Concierge',
        goal="""Create the most amazing travel itineraries with budget and 
        packing suggestions for the cities""",
        backstory="""Specialist in travel planning and logistics with 
        decades of experience""",
        #tools=tools,
        verbose=True)