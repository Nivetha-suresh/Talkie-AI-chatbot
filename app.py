from flask import Flask, request, jsonify, render_template
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get API key securely from environment variable
API_KEY = os.getenv("API_KEY")

# Safety check (recommended)
if not API_KEY:
    raise ValueError("API_KEY not found. Please set it in the .env file.")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    return jsonify({"reply": response.text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


# NOTE:
# to run the app,
#--->1. Activate the virtual environment: "<env_variable>\Scripts\activate"
#--->2. run the command: "cd "C:\Users\User\Desktop\chat""
#--->3. Run the command: "python app.py"
# if it throws any knid of error reinstall the required libraries
#--->4. Open your web browser and go to "http://

#--->5. deactivate the virtual environment: "deactivate"

