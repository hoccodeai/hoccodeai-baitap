    try:
        while True:
            question = input("Question: ")
            messages.append({
                "role": "user",
                "content": question
            })
            if question.lower() == "bye":
                print("Goodbye. See you soon!")
                break
            else:
                answer = answer_question(messages)
                messages.append({
                    "role": "assistant",
                    "content": answer
                })
                print(f"Answer: {answer}")
    except Exception as e:      
        print(f"Error: {e}")