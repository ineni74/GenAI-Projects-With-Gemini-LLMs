from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import write_task, research_task


crew= Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process= Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Start the Task execution process with enhanced feedback
results= crew.kickoff(inputs={'topic':'AI VS ML VS DL VS Data Sceince'})
print(results)