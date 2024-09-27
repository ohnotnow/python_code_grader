# Python Assignment Feedback Generator - Proof of Concept

This project is a proof-of-concept Python script designed to automatically generate feedback for student Python assignments. The script utilizes pylint to analyze code quality and OpenAI's GPT-4o-mini model to generate detailed feedback based on code performance, an assignment description, and custom feedback instructions.

## Features

- Analyzes Python files using pylint to assess code quality.
- Generates feedback based on the code, pylint results, and user-defined assignment description and feedback instructions.
- Automatically processes multiple .py files in a directory.
- Writes the generated feedback to a specified output directory.

## Installation

### Requirements

- Python 3.x
- openai, yaspin, pylint, and other dependencies listed in requirements.txt.

### Setup

Clone the repository:

```bash
git clone https://github.com/ohnotnow/python_code_grader
cd python_code_grader
```

Set up a virtual environment:

- On macOS/Ubuntu:

```bash
python3 -m venv venv
source venv/bin/activate
```

- On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Arguments

The script accepts the following arguments:

- `--code-dir`: (Required) The path to the directory containing Python files.
- `--output-dir`: The path to the directory where the feedback will be written. Defaults to `reports/`.
- `--assignment-description`: The path to a file containing the assignment description. Defaults to `assignment_description.txt`.
- `--feedback-instructions`: The path to a file containing feedback generation instructions. Defaults to `feedback_instructions.txt`.

### Running the Script

To run the feedback generator, use the following command:

```bash
python main.py --code-dir <path_to_code_dir> --output-dir <path_to_output_dir> --assignment-description <path_to_assignment_description> --feedback-instructions <path_to_feedback_instructions>
```

For example:

```bash
python main.py --code-dir ./student_code --output-dir ./feedback_reports --assignment-description ./assignment_description.txt --feedback-instructions ./feedback_instructions.txt
```

### Example Output

Overall, you've made a great start with your code! It's clear and well-structured, which is essential for readability and maintainability. Here are some points to consider for improvement:

1. **Line Length**: You have multiple instances where the lines exceed the recommended limit of 100 characters (e.g., lines 58, 69, 72, 98, and 99). It's best to keep lines shorter for better readability. Try to refactor any long lines by breaking them into multiple lines while ensuring the code's clarity remains intact.

2. **Docstrings**: It seems you're missing a module-level docstring at the beginning of your script (as indicated at line 1). Adding a docstring can provide a quick overview of what your module does. Each function's docstrings are well done, so maintain that consistency at the module level.

3. **Subprocess Check**: When using `subprocess.run`, it's generally a good practice to set `check=True` unless you have a specific reason not to. This will raise an exception if the command exits with a non-zero exit code, helping you catch errors early.

4. **File Encoding**: You have several instances of using the `open()` function without explicitly specifying the `encoding` parameter (lines 24, 69, 81, 84). It's good practice to define an appropriate encoding (like 'utf-8') to ensure your script correctly handles different character sets across various platforms.

5. **Code Duplication**: In your `main` function, you are appending `.py` files from `code_dir` in two separate loops. Consider combining these blocks into one to avoid redundancy.

6. **Error Handling**: While you are managing the case where the directories/files do not exist, consider further improving error handling. For instance, you might want to handle unexpected errors when running `pylint` or reading files, potentially logging them for easier debugging.

In conclusion, your structure is solid, and you've demonstrated a strong grasp of Python programming. With these improvements, your code will become even more robust and maintainable. Overall, I'd give your existing code an 8/10! Keep up the great work, and continue to refine your skills!

## License

This project is licensed under the MIT License. See the LICENSE file for details.
