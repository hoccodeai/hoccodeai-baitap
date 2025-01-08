import datetime
import os
from os.path import dirname, join

from dotenv import load_dotenv
from openai import OpenAI

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path, verbose=True)

client = OpenAI(
    base_url=os.environ.get("URL"),
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def solve_problem(problem: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gemma2-9b-it",
            n=1,
            max_tokens=500,
            temperature=0.3,
            messages=[
                {
                    "role": "system",
                    "content": """
You are a professional Python programmer.
Your task is to write Python code that solves the problems presented in the input.
Adhere strictly to the following output format, including the triple quotes, comments, and function structure.
Ensure your code is efficient, well-commented, and handles edge cases appropriately.  Prioritize clarity and readability in your solutions.

The input will consist of a problem description.
This description might include examples, constraints, and specific requirements for the solution.
Carefully analyze the input to understand the problem thoroughly before writing any code.
Your code should be robust enough to handle various inputs related to the described problem, not just the specific examples provided.
Consider edge cases and potential errors, and implement appropriate error handling mechanisms.

Your Python code should be written within the main() function.
If the problem requires external libraries, import them at the beginning, within the designated section.
Use comments effectively to explain your logic, especially for complex parts of the code.
Strive for clear and concise code that is easy to understand and maintain.
Avoid unnecessary complexity and prioritize efficiency.

Here are some additional points to consider when writing your code:
- Clarity: Use meaningful variable names and follow Python's PEP 8 style guide for readability.
- Efficiency: Optimize your code for performance, especially if the problem involves large datasets or complex computations.
- Error Handling: Implement appropriate error handling to gracefully manage unexpected inputs or situations. Use try-except blocks where necessary.
- Testability: Write code that is easy to test and debug. Consider including simple test cases within comments to demonstrate the functionality of your code.
- Modularity: If the problem can be broken down into smaller sub-problems, consider creating separate functions for each sub-problem to improve code organization and reusability.
- Comments: Explain the purpose of your code, the logic behind your approach, and any assumptions you've made. Clear comments are crucial for understanding and maintaining your code.
- Input Validation: Validate the input to ensure it meets the specified requirements and constraints. Handle invalid input gracefully.

Python code format as follows:
import [Import necessary libraries if used to solve the problem]

def main():
    # [Comment code to explain the logic]
    [Python code that addresses the problem]

if __name__ == "__main__":
    main()

                    """,
                },
                {"role": "user", "content": problem},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"要約中にエラーが発生しました: {str(e)}")
        return None


def main():
    print("問題を入力してください。終了するにはCtrl+Cを押してください。")
    try:
        while True:
            question_input = input("Question: ")
            if not question_input.strip():
                continue

            answer = solve_problem(question_input)
            if answer:
                current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"./final_{current_time}.py"
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(f"{answer}\n\n")
                print(f"解答が正常に書き込まれました: {filename}")
            else:
                print("解答が見つかりませんでした。")

    except KeyboardInterrupt:
        print("\nプログラムを終了します。お疲れ様でした!")


if __name__ == "__main__":
    main()
