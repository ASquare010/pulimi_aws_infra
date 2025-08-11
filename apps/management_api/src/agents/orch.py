import json, base64
from src.utils import *
from typing import Literal, Annotated
from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict
from IPython.display import Image, display
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


class ChatOrchestratorState(TypedDict):
    messages: Annotated[list, add_messages]

class ChatOrchestrator():
    
    def __init__(self,metadata: str, insight: dict):

        tools = [self.text_to_sql_tool]
        self.llm = ChatOpenAI(model="gpt-4o").bind_tools(tools)
        self.tool_node = ToolNode(tools=tools)
        self.metadata = metadata
        self.insight = insight
        self.base64_image = ""
        self.compile()
    
    def make_system_prompt(self):
        return SystemMessage(
            sys_data["orchestrator"] +
            f"\n- Metadata = {self.metadata}" +
            f"\n- Insight = {self.insight}"
        )
    
    def text_to_sql_tool(self, query: str) -> list:
        """
        Converts natural language text to SQL queries.

        Parameters:
            query (str): The natural language description for the desired SQL query.

        Returns:
            list: A list of generated SQL query strings and their corresponding results.
        """
        txt2sql_agent = Text2SQL_Agent(query, sys_data["text_to_sql"]).invoke()
        return txt2sql_agent.get("result_data", [])
    
    def orchestrator_node(self, state: ChatOrchestratorState):
        sys_prompt = self.make_system_prompt()
        return {"messages": [self.llm.invoke([sys_prompt] + state["messages"])]}
    
    def compile(self):
        builder = StateGraph(ChatOrchestratorState)
        builder.add_node("orchestrator", self.orchestrator_node)
        builder.add_node("tools", self.tool_node)

        builder.add_edge(START, "orchestrator")
        builder.add_edge("tools", "orchestrator")
        builder.add_conditional_edges("orchestrator", tools_condition)
        
        # Compile the graph
        self.graph = builder.compile()
    
    def print_base64_image(self):
        try:
            png_data = base64.b64decode(self.base64_image)
            display(Image(data=png_data))
        except Exception as e:
            print("Failed to render base64 image:", e)

    def print_graph(self):
        try:
            png_data = self.graph.get_graph(xray=True).draw_mermaid_png()
            display(Image(png_data))
        except Exception as e:
            print("Failed to render graph image:", e)
            print(self.graph.get_graph(xray=True).draw_mermaid())

    def invoke(self, prompt:str):
        reply = self.graph.invoke({"messages": [HumanMessage(prompt)]})
        result = reply["messages"][-1].content if reply["messages"][-1].content is not None else ""
        img = self.base64_image
        self.base64_image = ""
        return result, img, reply