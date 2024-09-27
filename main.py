import os
import sys
import argparse
from subprocess import run
from openai import OpenAI
from yaspin import yaspin

def run_pylint(code_file_path: str) -> str:
    """
    Run pylint on the code file and return the results.
    """
    pylint_results = run(['pylint', code_file_path], capture_output=True, text=True)
    return pylint_results

def generate_feedback(
        lint_results: str,
        code_file_path: str,
        assignment_description: str,
        feedback_instructions: str
    ) -> str:
    """
    Generate feedback on the code file.
    """
    with open(code_file_path, "r", encoding="utf-8") as file:
        code = file.read()
    system_prompt = f"## Instructions\n{feedback_instructions}"
    user_prompt = f"""
    ## Assignment description
    {assignment_description}

    ## Students code
    {code}

    ## Pylint Results
    {lint_results}

    Please provide feedback on the students code.
    """
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return str(response.choices[0].message.content)

def get_feedback(
        code_file_path: str,
        assignment_description: str,
        feedback_instructions: str
    ) -> str:
    """
    Get feedback on the code file.
    """
    lint_results = run_pylint(code_file_path)
    feedback = generate_feedback(lint_results, code_file_path, assignment_description, feedback_instructions)
    return feedback

def write_feedback(
        feedback: str,
        code_file_path: str,
        output_dir: str
    ) -> None:
    """
    Write the feedback to the output directory.
    """
    with open(os.path.join(output_dir, f"{os.path.basename(code_file_path)}_feedback.txt"), "w", encoding="utf-8") as file:
        file.write(feedback)

def main(code_dir: str, output_dir: str, assignment_description: str, feedback_instructions: str) -> None:
    """
    Main function to get feedback on the code files.
    """
    with open(assignment_description, "r", encoding="utf-8") as file:
        assignment_description = file.read()

    with open(feedback_instructions, "r", encoding="utf-8") as file:
        feedback_instructions = file.read()

    code_files = []
    for file in os.listdir(code_dir):
        if file.endswith(".py"):
            code_files.append(os.path.join(code_dir, file))

    for code_file in code_files:
        with yaspin(text=f"Processing file {code_file}..."):
            feedback = get_feedback(code_file, assignment_description, feedback_instructions)
            write_feedback(feedback, code_file, output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Give students feedback on the python assignments.")
    parser.add_argument("--code-dir", type=str, help="The path to the directory containing the python files.")
    parser.add_argument(
        "--output-dir",
        type=str,
        default="reports",
        help="The path to the directory to write the feedback to."
    )
    parser.add_argument(
        "--assignment-description",
        type=str,
        default="assignment_description.txt",
        help="The path to the file containing the assignment description."
    )
    parser.add_argument(
        "--feedback-instructions",
        type=str,
        default="feedback_instructions.txt",
        help="The path to the file containing the feedback instructions."
    )

    args = parser.parse_args()

    if not args.code_dir:
        print("Error: --code-dir is required.")
        sys.exit(1)

    if not os.path.exists(args.code_dir):
        print(f"Error: --code-dir '{args.code_dir}' does not exist.")
        sys.exit(1)

    if not os.path.exists(args.assignment_description):
        print(f"Error: --assignment-description '{args.assignment_description}' does not exist.")
        sys.exit(1)

    if not os.path.exists(args.feedback_instructions):
        print(f"Error: --feedback-instructions '{args.feedback_instructions}' does not exist.")
        sys.exit(1)

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    main(args.code_dir, args.output_dir, args.assignment_description, args.feedback_instructions)
