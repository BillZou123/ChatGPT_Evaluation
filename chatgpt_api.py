import os
import openai
import requests
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_prompt(animal):
  return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
    animal.capitalize()
  )


response = openai.Completion.create(
  model="text-davinci-003",
  prompt=generate_prompt("Cat"),
  temperature=0.6
)

print(response)