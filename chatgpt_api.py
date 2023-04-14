import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def promt_template(problem_content, header):
    prompt = f"Using Java language, provide only code do not include any explanation for the following prompt: {problem_content}, begin your answer with {header} and do not change it keep the structure. Don't change the basic structure of the header. Avoid runtime error and compile error"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response["choices"][0]["message"]["content"]

