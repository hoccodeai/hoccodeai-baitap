import client
import os

def export_code_reg_in_chat(prompt):
    keywords = ["export", "code", "file"]
    if any(keyword in prompt for keyword in keywords):
        return True
    return False

def process_file_code(prompt):
    completion = client.generate_chat_response(prompt, isStream=False)
    if completion:
        export_file_code(completion)

def export_file_code(completion):
    # Extract content between ```python and the first ```
    start_marker = "```python"
    end_marker = "```"
    start_index = completion.find(start_marker)
    end_index = completion.find(end_marker, start_index + len(start_marker))
    if start_index != -1 and end_index != -1:
        completion = completion[start_index + len(start_marker):end_index].strip()
    # Define the path to the data folder
    data_folder_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    os.makedirs(data_folder_path, exist_ok=True)
    with open(os.path.join(data_folder_path, 'output_file.py'), 'w', encoding='utf-8') as file:
        file.write(completion)