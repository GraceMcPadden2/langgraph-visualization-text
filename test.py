from typing import Annotated, List, TypedDict
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
import os,sys

load_dotenv()
# ---------- 1. Graph state ---------------------------------------------------
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]

# ---------- 2. Tool ----------------------------------------------------------
@tool
def get_categories(data) -> dict:
    """takes in a data set, returns a dictionary describing data set
    Args:
        data (string): name of dataset

    Returns:
        dict: dictionary describing data set, contains pairs of
        a category (string) and a type (type)
    """
    #todo, implement function.

    #mock function
    dict = {"time of incident": int, "app": str, "severity": int}
    return dict

tools = [get_categories]

# ---------- 3. LLM bound to tools -------------------------------------------
llm = ChatOpenAI(model="gpt-4o").bind_tools(tools)
tool_node = ToolNode(tools)

# ---------- 4. Agent (reasoning) node ---------------------------------------
def agent_node(state: AgentState) -> AgentState:
    system_msg = SystemMessage(content="""
You are an expert data analyst who uses python to create visualizations
of incident reports using plotly.

- If a user asks for a specific data visualization, first call tool get_categories
to get information regarding the data set.
- after getting informatino regarding the data set, generate a python script that 
uses Plotly to visualize data according to the user query and data set information.
""")

    # prepend system instruction each turn
    
    response = llm.invoke([system_msg] + state["messages"])

    if response.content:
        print(f"\nAI: {response.content}\n")
    elif response.tool_calls:
        print(f"\nTool call: {response.tool_calls}\n")
    else:
        print("\n No content or tool call returned.\n")

    state["messages"].append(response)
    return state

# ---------- 5. Stop/continue logic ------------------------------------------
def should_continue(state: AgentState) -> str:
    last = state["messages"][-1]

    # If the AI queued a tool call, let the ToolNode run next
    if isinstance(last, AIMessage) and last.tool_calls:
        return "continue"

    # Otherwise we’re finished
    return "end"

# ---------- 6. Build graph ---------------------------------------------------
graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.add_node("tool", tool_node)

graph.set_entry_point("agent")
graph.add_conditional_edges("agent", should_continue,
                            {"continue": "tool", "end": END})
graph.add_edge("tool", "agent")

agent = graph.compile()

# ---------- 7. Chat loop -----------------------------------------------------
history: List[BaseMessage] = []

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    history.append(HumanMessage(content=user))
    result = agent.invoke({"messages": history})
    history = result["messages"]