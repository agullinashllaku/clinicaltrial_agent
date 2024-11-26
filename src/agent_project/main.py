#!/usr/bin/env python
import sys
import warnings

from agent_project.crew import AgentProject

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
print("HELLOOOOOOOOOOOOOOOO")


def run():
    """
    Run the crew.
    """
    inputs = {
        "profile": """The patient is a 50-year-old female who presents with a complaint of persistent neck pain. The pain has been ongoing for several weeks and is localized to the neck area. She reports stiffness and discomfort, especially after long periods of sitting or during movement. There are no additional symptoms such as numbness or weakness in the limbs. The patient does not have a history of significant injuries to the neck but has a sedentary lifestyle that may contribute to her symptoms."""
    }
    AgentProject().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "profile": """The patient is a 50-year-old female who presents with a complaint of persistent neck pain. The pain has been ongoing for several weeks and is localized to the neck area. She reports stiffness and discomfort, especially after long periods of sitting or during movement. There are no additional symptoms such as numbness or weakness in the limbs. The patient does not have a history of significant injuries to the neck but has a sedentary lifestyle that may contribute to her symptoms."""}
    try:
        AgentProject().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AgentProject().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "profile": """The patient is a 50-year-old female who presents with a complaint of persistent neck pain. The pain has been ongoing for several weeks and is localized to the neck area. She reports stiffness and discomfort, especially after long periods of sitting or during movement. There are no additional symptoms such as numbness or weakness in the limbs. The patient does not have a history of significant injuries to the neck but has a sedentary lifestyle that may contribute to her symptoms."""}
    try:
        AgentProject().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
