import os
import openai
openai.api_key = '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'

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
