import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
prompt = "write python code say hello\n\n"
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response['choices'][0]['text'])