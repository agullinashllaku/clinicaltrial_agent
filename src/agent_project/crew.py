from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

# Uncomment the following line to use an example of a custom tool
# from agent_project.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them

load_dotenv()
OPENAI_KEY=os.environ.get("OPENAI_API_KEY")
SERPER_KEY=os.environ.get("SERPER_KEY")

search_tool= SerperDevTool(api_key=SERPER_KEY)




@CrewBase
class AgentProject():
	"""AgentProject crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def medical_keyword_extractor(self) -> Agent:
		return Agent(
			config=self.agents_config['medical_keyword_extractor'],
			verbose=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True
		)
  
	@agent
	def api_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['api_agent'],
			verbose=True
		)
	@task
	def extract_keywords_task(self) -> Task:
		return Task(
			config=self.tasks_config['extract_keywords_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
		)
	
	@task
	def api_task(self) -> Task:
		return Task(
			config=self.tasks_config['api_task'],
			output_file='report.json'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the AgentProject crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
