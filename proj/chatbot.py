import openai
openai.api_key = "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"
model_engine = "text-davinci-002"

def chatbot(prompt):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message

while True:
    prompt = input("you: ")
    response = chatbot(prompt)
    print("chatbot: " + response)