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
