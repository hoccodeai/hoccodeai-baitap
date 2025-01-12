import utils


def exercise1():
    messages = [{"role":"system", "content": "You are a guru"},]
    while(True):
        question = utils.require_user_input("Please enter your question: ")

        if question == "e" or question == "q":
            break

        messages.append({"role": "user", "content": question})

        stream = utils.client.chat.completions.create(
            messages=messages,
            model="gemma2-9b-it",
            stream=True
        )
        print("LLM is thinking...", end="\n\n")

        for chunk in stream:
            print(chunk.choices[0].delta.content or "", end="")


exercise1()