import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def promt_template(problem_content, header):
    prompt = f"Using python, provide only code for the following prompt: {problem_content}, begin your answer with {header}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # model="GPT-3-DaVinci-003",
        messages=[
            {"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response["choices"][0]["message"]["content"]

