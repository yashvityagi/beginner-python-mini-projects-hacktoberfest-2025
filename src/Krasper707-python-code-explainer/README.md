# Python Code Explainer using GenAI

This is a beginner-friendly Python mini-project that uses Google's Gemini Pro API to explain Python code snippets in simple terms. It's a great tool for anyone learning to code!

## Features

- Interactive command-line interface.
- Explains complex code in easy-to-understand language.
- Powered by the Google Gemini Pro model.

## Setup and Installation

To run this project, you'll need to set up a few things first.

**1. Install Dependencies:**

You only need one Python library. Open your terminal and run:

```bash
pip install  google-generativeai
```

**2. Get Your Google API Key:**

This project uses the Google Gemini API, which requires a free API key.

- Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
- Click **"Create API key"** and copy your key.

**3. Set the Environment Variable:**

To keep your API key secure, you must set it as an environment variable named `GOOGLE_API_KEY`. This is a crucial step.

- **On Windows (Command Prompt):**
  ```bash
  set GOOGLE_API_KEY="YOUR_API_KEY_HERE"
  ```
- **On Windows (PowerShell):**
  ```bash
  $env:GOOGLE_API_KEY="YOUR_API_KEY_HERE"
  ```
- **On macOS / Linux:**
  ```bash
  export GOOGLE_API_KEY="YOUR_API_KEY_HERE"
  ```
  _(Replace `YOUR_API_KEY_HERE` with the key you copied. Note: this environment variable only lasts for the current terminal session. You'll need to set it again if you open a new terminal.)_

## ▶️ How to Run

Once you've completed the setup, you can run the application:

1.  Navigate to this project directory in your terminal.
2.  Run the main script:
    ```bash
    python main.py
    ```
3.  Follow the on-screen prompts to paste your code snippet and get an explanation!
