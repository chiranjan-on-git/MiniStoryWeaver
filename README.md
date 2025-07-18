# Mini Story Weaver

Mini Story Weaver is a simple command-line application that leverages the Google Gemini API to generate short, imaginative story paragraphs based on user-provided prompts.

## Features

- **AI-Powered Story Generation:** Utilizes the Google Gemini model (`gemini-1.5-flash-latest` by default) to create creative story snippets.
- **Interactive Prompt:** Users can input a story idea or keywords directly in the terminal.
- **Configurable Generation:** Easily adjust parameters like `temperature`, `top_p`, `top_k`, and `max_output_tokens` to control the style and length of the generated story.
- **Safety Settings:** Includes default safety configurations to filter potentially harmful content.
- **Model Listing Utility:** A separate script (`list_my_models.py`) helps users discover available Gemini models compatible with text generation.

## Technologies Used

- **Python:** The core programming language.
- **Google Generative AI SDK:** Python library for interacting with Google's Gemini API.
- **python-dotenv:** For securely loading API keys from a `.env` file.

## Project Structure

```
MiniStoryWeaver/
├── .env                # Environment variables (e.g., GOOGLE_API_KEY)
├── .gitignore          # Specifies files/directories to ignore in Git
├── list_my_models.py   # Utility script to list available Gemini models
├── requirements.txt    # Python dependencies
├── story_weaver.py     # Main application script for generating stories
└── venv/               # Python virtual environment (ignored by Git)
```

## Setup and Installation

Follow these steps to get Mini Story Weaver up and running on your local machine.

### 1. Prerequisites

- **Python 3.8+**: Ensure Python is installed on your system.
- **Google Gemini API Key**: Obtain an API key from Google AI Studio. You can get one by visiting [Google AI Studio](https://aistudio.google.com/app/apikey) and creating a new API key.

### 2. Project Setup

1. **Navigate to the project directory**

```bash
cd MINI_STORY_WEAVER
```

2. **Create a Python virtual environment**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

- On **Windows**:

```bash
.\venv\Scripts\activate
```

- On **macOS/Linux**:

```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Configure your Google API Key**

Create a file named `.env` in the root of your project and add your API key:

```dotenv
GOOGLE_API_KEY="your_google_api_key_here"
```

> **Note:** Replace `your_google_api_key_here` with your actual API key. Keep this file private and do not commit it to GitHub.

## How to Run

### 1. (Optional) List Available Models

```bash
python list_my_models.py
```

This will print a list of Gemini models that support `generateContent`.

### 2. Generate a Story Paragraph

```bash
python story_weaver.py
```

You'll be prompted to enter a story idea or keywords.

#### Example Output

```
--- Mini Story Weaver ---
Enter a starting sentence or a few keywords for your story.
Story idea: A lone astronaut discovers a garden on Mars.

Weaving your story...

--- Your Story Paragraph ---
Crimson dust swirled around Commander Aris Thorne's boots as he surveyed the barren Martian landscape, a stark canvas of rust and rock. Yet, defying all logic, a vibrant patch of green shimmered in the distance, a small, impossible oasis beneath the alien sky. As he drew closer, the sweet scent of unknown blossoms filled his helmet, and he knelt, awestruck, before a tiny garden teeming with life, each delicate petal a testament to an unimaginable resilience.
--------------------------
```

## Configuration

Edit `story_weaver.py` to tweak the generation behavior:

- `MODEL_NAME`: Gemini model to use (e.g., `gemini-1.5-flash-latest`, `gemini-1.0-pro`)
- `generation_config`:
  - `temperature`: Controls randomness (0.2 = focused, 1.0 = creative)
  - `top_p`: Nucleus sampling
  - `top_k`: Top-k filtering
  - `max_output_tokens`: Controls length

- `safety_settings`: Adjust thresholds as needed (be mindful of responsible AI use).

## Error Handling

- **Missing API Key:** Script exits with an error if `.env` is missing or malformed.
- **Safety Blocks:** Google may block certain content; a warning will be shown.
- **API Errors:** Network/API issues are logged to the terminal.

## Acknowledgements

- **Google Generative AI:** For the powerful Gemini models and SDK.

---
