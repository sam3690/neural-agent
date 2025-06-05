from typing import Annotated
from typing_extensions import TypedDict

from langchain.chat_models import ChatAnthropic
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

from dotenv import load_dotenv
load_dotenv()

class State(TypedDict):
    messages: Annotated[list, add_messages]


llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")  

graph_builder = StateGraph(State)

def chatbot(state: State) -> State:
    response = llm.invoke(state["messages"])
    return {"messages": state["messages"] + [response]}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)  


graph = graph_builder.compile()

input_state = {"messages": [{"role": "user", "content": "Hello, who are you?"}]}
final_state = graph.invoke(input_state)

print(final_state["messages"][-1]["content"])
