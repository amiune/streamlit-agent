# streamlit-agent
LangChain agent with streamlit UI

Save your OpenAI token in the OPENAI_API_KEY 
environment variable to load it automatically

Run with the following command:
streamlit run minimal_agent.py --server.port 8501

Or using docker with the following commands:
docker build -t streamlitagent .      
docker run -p 8501:8501 streamlitagent

To run the local Ollama model use the following command:
streamlit run local_llm.py --server.port 8501