# main.py for the "Python Code Explainer" project
# Author: Krasper707
# Date: October 4, 2025

#Imporing necessary libraries.
import google.generativeai as genai

try:
    # Configure the generative AI model with the API key
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
except KeyError:
    print("-"*50)
    print("ERROR: GOOGLE_API_KEY environment variable not set.")
    print("Please set the environment variable and run the script again.")
    print("-"*50)
    exit()

#Creating an instance of model
model = genai.GenerativeModel('gemini-2.5-flash-lite')

# Main logic

def explain_code(code_snippet):
    """
    Uses the Gemini API to generate an explanation for a given code snippet.
    """
    # This is our "prompt".
    #It lets us tell the AI exactly what we want it to do.
    # A good prompt is key to getting good results. (Art of prompt engineeering)
    prompt = f"""
    You are an expert Python tutor for beginners.
    Explain the following Python code snippet in a simple, clear, and friendly way.
    Break down what each part does. Assume the person asking is new to programming.

    Code Snippet:
    ```python
    {code_snippet}
    ```

    Explanation:
    """
    
    try:
        # Generate content using the model
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    """
    Main function to run the interactive code explainer application.
    """
    print("-"*50)
    print("🥸Welcome to the Python Code Explainer!🥸")
    print("-"*50)
    print("Paste your Python code snippet below and press Enter.")
    print("Type 'exit' or 'quit' to end the program.")
    print("=" * 50)

    while True:
        # Get user input
        user_input = []
        print("\nEnter your code snippet (press Enter on an empty line to submit):")
        
        while True:
            line = input()
            if line == "":
                break
            user_input.append(line)
        
        code_to_explain = "\n".join(user_input)

        if not code_to_explain:
            print("No code entered. Please try again.")
            continue

        if code_to_explain.lower() in ['exit', 'quit']:
            print("\nThank you for using the Python Code Explainer. Happy coding!")
            break

        print("\n🤖 Generating explanation, please wait...")
        
        # Get the explanation from the AI
        explanation = explain_code(code_to_explain)
        
        print("-" * 50)
        print("Here's the explanation:")
        print(explanation)
        print("-" * 50)

if __name__ == "__main__":
    main()