import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
problem_content = "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order. "
header = "class Solution:"
prompt = f"Using python, provide a solution for the following prompt: {problem_content}, begin your answer with {header}"
response = openai.Completion.create(
    model="text-davinci-003",
    # model="GPT-3-DaVinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response['choices'][0]['text'])
