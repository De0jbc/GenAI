import os
from dotenv import load_dotenv
from crewai import Agent, Task, Process,Crew
from openai import OpenAI
from langchain_openai import ChatOpenAI

load_dotenv()  # Carga las variables desde el archivo .env

#llmAI = ChatOpenAI(
#    model = "ollama/llama3:8b",
#    base_url = "http://localhost:11434/v1",
#    api_key='sk-11111111111111'
#    )

# Create a researcher agent
researcher = Agent(
  role='Senior Researcher',
  goal='Discover groundbreaking technologies',
  verbose=True,
  #llm=llmAI,
  backstory='A curious mind fascinated by cutting-edge innovation and the potential to change the world, you know everything about tech.'
)
# Create a writer agent
writer = Agent(
  role='Writer',
  goal='Craft compelling stories about tech discoveries',
  verbose=True,
  #llm=llmAI,
  backstory='A creative soul who translates complex tech jargon into engaging narratives for the masses, you write using simple words in a friendly and inviting tone that does not sounds like AI.'
)

# Task for the researcher
research_task = Task(
  description='Identify the next big trend in AI',
  expected_output="A list of technologies",
  agent=researcher  # Assigning the task to the researcher
)

# Task for the writer
write_task = Task(
  description='Write an article on AI advancements leveraging the research made.',
  expected_output="A list of technologies",
  agent=writer  # Assigning the task to the writer
)

# Instantiate your crew
tech_crew = Crew(
  agents=[researcher, writer],
  tasks=[research_task, write_task],
  process=Process.sequential  # Tasks will be executed one after the other
)

result = tech_crew.kickoff()
print("---------------Here is the Result-----------------")
print(result)
