import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
print('Document opened without error.')