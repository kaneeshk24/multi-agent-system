from textwrap import dedent
from crewai import Task

class MeetingPrepTasks():
    def research_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description=dedent(f"""\
            Conducting comprehensive research on Each of the individuals
            and companies  involved in the upcoming meeting. Gather information
            
            Participants: {meeting_participants}
            Meeting Context : {meeting_context}"""),
            expected_output=dedent(f"""\
                                   a dedicatedreport summarizing key findings about each participation and company.""")
        )