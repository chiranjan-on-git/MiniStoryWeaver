import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the API key
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file or environment variables.")
    genai.configure(api_key=api_key)
except ValueError as e:
    print(f"Error: {e}")
    print("Please ensure your GOOGLE_API_KEY is set in a .env file in the project root.")
    exit()

# --- Model Configuration ---
# For text-only input, use the gemini-pro model
# As of mid-2024, 'gemini-1.0-pro' is a good general-purpose free tier model.
# You can also try 'gemini-1.5-flash-latest' which is very fast and capable.
MODEL_NAME = "gemini-1.5-flash-latest" # or "gemini-1.5-flash-latest"
model = genai.GenerativeModel(MODEL_NAME)

# --- Generation Configuration (Optional, but good for controlling output) ---
generation_config = genai.types.GenerationConfig(
    temperature=0.8,  # Controls randomness: lower is more deterministic, higher is more creative
    top_p=0.9,        # Nucleus sampling: considers the smallest set of tokens whose cumulative probability exceeds top_p
    top_k=40,         # Top-k sampling: considers the top k most probable tokens
    max_output_tokens=200 # Limits the length of the generated story paragraph
)

# --- Safety Settings (Optional, good for responsible AI) ---
# You can adjust these to be more or less restrictive.
# BLOCK_NONE, BLOCK_ONLY_HIGH, BLOCK_MEDIUM_AND_ABOVE, BLOCK_LOW_AND_ABOVE
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

def generate_story_paragraph(prompt_text):
    """
    Generates a story paragraph based on the given prompt using the Gemini API.
    """
    try:
        full_prompt = f"Write a short, imaginative story paragraph (about 3-5 sentences) based on this idea: '{prompt_text}'"
        
        response = model.generate_content(
            full_prompt,
            generation_config=generation_config,
            safety_settings=safety_settings
        )

        # Check for safety blocks or empty response
        if not response.candidates:
            return "The model could not generate a response, possibly due to safety filters or other issues."
        
        # Accessing the text from the first candidate
        if response.candidates[0].content and response.candidates[0].content.parts:
            story_text = response.candidates[0].content.parts[0].text
            return story_text.strip()
        else:
            return "Received an empty or malformed response from the API."

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("--- Mini Story Weaver ---")
    print("Enter a starting sentence or a few keywords for your story.")
    
    user_input = input("Story idea: ")

    if user_input:
        print("\nWeaving your story...\n")
        story_paragraph = generate_story_paragraph(user_input)
        print("--- Your Story Paragraph ---")
        print(story_paragraph)
        print("--------------------------")
    else:
        print("No input provided. Exiting.")