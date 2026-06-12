import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task







@CrewBase
class GithubProfileHrOptimizerCrew:
    """GithubProfileHrOptimizer crew"""

    
    @agent
    def github_profile_analyzer(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["github_profile_analyzer"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-2.5-flash",
                api_key=os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
            ),
        )
        
    
    @agent
    def hr_focused_improvement_strategist(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["hr_focused_improvement_strategist"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-2.5-flash",
                api_key=os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
            ),
        )
        
    

    
    @task
    def analyze_github_profile(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_github_profile"],
            markdown=False,
            
            
        )
    
    @task
    def generate_improvement_recommendations(self) -> Task:
        return Task(
            config=self.tasks_config["generate_improvement_recommendations"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the GithubProfileHrOptimizer crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=LLM(
                model="gemini/gemini-2.5-flash",
                api_key=os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
            )
        )