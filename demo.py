
import openai

# Set up your API key
openai.api_key = "your-api-key-here"

# Call the GPT model (e.g., GPT-3.5 or GPT-4)
response = openai.Completion.create(
            engine="text-davinci-003",  # Can also use gpt-3.5-turbo, gpt-4, etc.
                prompt="Write a short story about a robot learning emotions.",
                    max_tokens=100,  # Limits the number of tokens in the response
                        temperature=0.7  # Controls randomness (0.0 = deterministic, 1.0 = creative)
                        )

# Print the response
print(response.choices[0].text.strip())


