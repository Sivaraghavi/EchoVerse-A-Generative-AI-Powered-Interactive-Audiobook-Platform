from transformers import pipeline
generator = pipeline('text-generation', model='gpt2')
print("GPT-2 loaded successfully!")