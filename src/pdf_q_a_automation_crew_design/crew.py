from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import PDFSearchTool

@CrewBase
class PdfQAAutomationCrewDesignCrew():
    """PdfQAAutomationCrewDesign crew"""

    @agent
    def pdf_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['pdf_extractor'],
            tools=[PDFSearchTool()],
        )

    @agent
    def question_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['question_generator'],
            
        )

    @agent
    def fact_checker(self) -> Agent:
        return Agent(
            config=self.agents_config['fact_checker']
        )

    @agent
    def manager(self) -> Agent:
        return Agent(
            config=self.agents_config['manager'],
            allow_delegation=True
        )


    @task
    def extract_key_facts_task(self) -> Task:
        return Task(
            config=self.tasks_config['extract_key_facts_task'],
            tools=[PDFSearchTool()],
        )

    @task
    def generate_questions_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_questions_task'],
            
        )

    @task
    def fact_check_questions_task(self) -> Task:
        return Task(
            config=self.tasks_config['fact_check_questions_task']
        )

    @task
    def manage_revision_task(self) -> Task:
        return Task(
            config=self.tasks_config['manage_revision_task'],
            output_file="qa_report.md"
            
        )


    @crew
    def crew(self) -> Crew:
        """Creates the PdfQAAutomationCrewDesign crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
