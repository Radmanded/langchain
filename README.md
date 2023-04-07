# Realtime Search Agent

The Realtime Search Agent is a Python script that uses the LangChain library to perform a search based on user input. The script prompts the user to enter a search query, which is then passed to the LangChain agent for processing. The agent uses the SerpAPIWrapper tool to perform the search and returns the results to the user.

## Getting Started

```bash
# Clone the repository from GitHub:
git clone https://github.com/username/realtime-search-agent.git

# Navigate to the project directory:
cd realtime-search-agent

# Create a new Python virtual environment:
python3 -m venv venv

# Activate the virtual environment:
source venv/bin/activate

# Upgrade pip to the latest version:
pip install --upgrade pip

# Install the project dependencies:
pip install -r requirements.txt

# Set up the API keys for SerpAPIWrapper and OpenAI by creating a `.env` file in the project directory:
echo "SERPAPI_API_KEY=your_serpapi_api_key_here" > .env
echo "OPENAI_API_KEY=your_openai_api_key_here" >> .env

# Run the `realtime_search.py` script:
python3 realtime_search.py
```

Replace username in the git clone command with your actual GitHub username, and replace your_serpapi_api_key_here and your_openai_api_key_here in the .env file with your actual API keys.

Make sure to never commit your .env file to your Git repository by adding it to your .gitignore file.

License

The Realtime Search Agent is released under the MIT License. See the LICENSE file for more information.


