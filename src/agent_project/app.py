import streamlit as st
from agent_project.crew import AgentProject

# Initialize the AgentProject crew
agent_project = AgentProject()

# Streamlit app layout
st.title("Clinical Trials Data Generator")
st.write("Enter the patient profile below to generate clinical trials data as a CSV file.")

# User input for the patient profile
profile_input = st.text_area(
    "Patient Profile",
    placeholder="Enter the patient profile here, e.g., 'The patient is a 50-year-old female with persistent neck pain...'",
)

# Button to execute tasks and generate the CSV
if st.button("Generate Clinical Trials CSV"):
    if not profile_input.strip():
        st.error("Please enter a patient profile before proceeding.")
    else:
        try:
            # Prepare inputs
            inputs = {"profile": profile_input}

            # Kickoff the process
            st.write("Running tasks...")
            crew_instance = agent_project.crew()
            crew_instance.kickoff(inputs=inputs)

            # Once tasks complete, display download button
            csv_file_path = "clinicaltrials.csv"
            with open(csv_file_path, "rb") as file:
                st.download_button(
                    label="Download Clinical Trials CSV",
                    data=file,
                    file_name="clinicaltrials.csv",
                    mime="text/csv",
                )
            st.success("CSV file generated successfully. Click the button to download.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
