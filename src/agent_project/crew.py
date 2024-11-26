from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import requests
import os

# Uncomment the following line to use an example of a custom tool
# from agent_project.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them

load_dotenv()
OPENAI_KEY=os.environ.get("OPENAI_API_KEY")
SERPER_KEY=os.environ.get("SERPER_KEY")

search_tool= SerperDevTool(api_key=SERPER_KEY)


def api_request(query):
    print(query)
    # Read the entire content of the report.txt file
    # with open("agent_project\\report.txt", "r") as r:
    #     query = r.read().strip()  # Read the entire file as a string

    try:

        response = requests.get(query)

        # Handle the response, assuming it's in CSV format
        if response.status_code == 200:
            print("API Request Successful!")
            with open("clinicaltrials.csv", "wb") as f:
                f.write(response.content)  # Save the CSV response to a file
            print("CSV saved as 'output.csv'.")
        else:
            print(f"API Request Failed! Status Code: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"An error occurred during the API request: {e}")

# Call the function to test it

        
    


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
			output_file='report.txt',
			callback= api_request
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
