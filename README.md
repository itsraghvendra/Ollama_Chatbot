# Assignment 24: Ollama Chatbot (Task 1)

Simple local chatbot using Ollama + LangChain, tracked with LangSmith.

## Step 1: Install and run Ollama
1. Download and install Ollama from https://ollama.com/download
2. Check it works. Open a terminal and run:
   ```
   ollama --version
   ```
   (Ollama runs in the background after install. If not, run `ollama serve`.)

## Step 2: Pull a model
```
ollama pull llama3
```
(You can use `mistral` instead. Then change the model name in `app.py`.)

Test it quickly:
```
ollama run gemma 3:1b
```
Type `/bye` to exit.

## Step 3: Set up Python
```
python -m venv venv
venv\Scripts\activate        (Windows)
source venv/bin/activate     (Mac/Linux)

pip install -r requirements.txt
```

## Step 4: Set up LangSmith
1. Sign up (free) at https://smith.langchain.com
2. Go to Settings -> API Keys -> Create API Key and copy it.
3. Rename `.env.example` to `.env` and paste your key:
   ```
   LANGSMITH_API_KEY=your_key_here
   ```

## Step 5: Run the code

```
streamlit run app.py

```

## Step 6: Take the screenshot for Drive
1. Open https://smith.langchain.com
2. Go to Tracing -> Projects -> `ollama-chatbot-assignment24`
3. Click the latest run (OllamaLLM) so the input, output, latency and
   tokens are visible.
4. Take a screenshot and upload it to your Drive.

