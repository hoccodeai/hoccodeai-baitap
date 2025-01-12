import utils
import sys

def exercise5():
    want = "Let resolve this problem, the response should be executable code only, without explanation and without markdown and without```python tag"   
    output_file = "./final.py"

    while True:
        problem = utils.require_user_input("\nPlease enter your coding question: ")
        if problem == "e" or problem == "q":
            break
    
        question = " ".join([want,":",problem])
        messages = [
            {"role":"system", "content": "You are a senior python developer"},
            {"role": "user", "content": question}
        ]

        stream = utils.client.chat.completions.create(
            messages=messages,
            model="gemma2-9b-it",
            stream=True
        )
        print("LLM is thinking...", end="\n\n")

        with open(output_file,"w") as outfile:
            for chunk in stream:
                sys.stdout.write(">")
                sys.stdout.flush()
                outfile.write(chunk.choices[0].delta.content or "")

            print("\n\n=>Let check '"+output_file+"' for the final code")

exercise5()