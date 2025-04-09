import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from langchain_core.messages.ai import AIMessage

# Load environment variables
load_dotenv()

# Get API keys
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
TAVILY_API_KEY = os.environ.get('TAVILY_API_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# Check for API keys
if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key. Set OPENAI_API_KEY environment variable.")
if not GROQ_API_KEY:
    raise ValueError("Missing Groq API Key. Set GROQ_API_KEY environment variable.")
if not TAVILY_API_KEY:
    raise ValueError("Missing Tavily API Key. Set TAVILY_API_KEY environment variable.")

# Initialize LLM (you can switch between openai_llm or groq_llm)
openai_llm=ChatOpenAI(model="gpt-4o-mini" , api_key= OPENAI_API_KEY)
groq_llm = ChatGroq(model="llama3-70b-8192", api_key=GROQ_API_KEY)

# Search Tool
search_tool = TavilySearchResults(api_key=TAVILY_API_KEY, max_results=2)

# Create the ReAct agent executor (new method)
system_prompt= "ACt as an AI bot who is smart and friendly"

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="OpenAI":
        llm=ChatOpenAI(model=llm_id)
        
    tools=[TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model = groq_llm,
        tools=tools,
        state_modifier=system_prompt
)

# Query Execution

    state = {"messages": query}
    response = agent.invoke(state)
    messages=response.get('messages')
    ai_messages=[ message.content for message in messages if isinstance (message, AIMessage)]

    return ai_messages[-1]
