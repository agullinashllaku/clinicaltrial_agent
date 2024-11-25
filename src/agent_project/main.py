#!/usr/bin/env python
import sys
import warnings

from agent_project.crew import AgentProject

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    inputs = {
        "profile": """Patient Medical Report Patient ID: 12345
Age: 55
Gender: Female
Location: Los Angeles, California, United States

The patient is a 55-year-old female living in Los Angeles, California. She has a medical history significant for hypertension, type 2 diabetes, and osteoarthritis. Currently, she is being managed on Metformin for her diabetes, Lisinopril to control her blood pressure, and Ibuprofen to alleviate the pain from osteoarthritis. She has no known history of heart disease or cancer.

In 2010, she underwent an appendectomy without any complications. The patient has also reported allergies to Penicillin and shellfish. Family history includes a father who had type 2 diabetes and a mother with hypertension.

The patient’s lifestyle includes moderate exercise, a low-sodium diet, and occasional alcohol consumption. She does not smoke."""
    }
    AgentProject().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "profile": """Patient Medical Report Patient ID: 12345
Age: 55
Gender: Female
Location: Los Angeles, California, United States

The patient is a 55-year-old female living in Los Angeles, California. She has a medical history significant for hypertension, type 2 diabetes, and osteoarthritis. Currently, she is being managed on Metformin for her diabetes, Lisinopril to control her blood pressure, and Ibuprofen to alleviate the pain from osteoarthritis. She has no known history of heart disease or cancer.

In 2010, she underwent an appendectomy without any complications. The patient has also reported allergies to Penicillin and shellfish. Family history includes a father who had type 2 diabetes and a mother with hypertension.

The patient’s lifestyle includes moderate exercise, a low-sodium diet, and occasional alcohol consumption. She does not smoke."""}
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
        "profile": """Patient Medical Report Patient ID: 12345
Age: 55
Gender: Female
Location: Los Angeles, California, United States

The patient is a 55-year-old female living in Los Angeles, California. She has a medical history significant for hypertension, type 2 diabetes, and osteoarthritis. Currently, she is being managed on Metformin for her diabetes, Lisinopril to control her blood pressure, and Ibuprofen to alleviate the pain from osteoarthritis. She has no known history of heart disease or cancer.

In 2010, she underwent an appendectomy without any complications. The patient has also reported allergies to Penicillin and shellfish. Family history includes a father who had type 2 diabetes and a mother with hypertension.

The patient’s lifestyle includes moderate exercise, a low-sodium diet, and occasional alcohol consumption. She does not smoke."""}
    try:
        AgentProject().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
