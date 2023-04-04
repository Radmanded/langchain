from langchain.agents import Tool, AgentExecutor, BaseSingleActionAgent
from langchain import SerpAPIWrapper

search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events",
        return_direct=True
    )
]

from typing import List, Tuple, Any, Union
from langchain.schema import AgentAction, AgentFinish

class RealtimeSearchAgent(BaseSingleActionAgent):
    """Agent that performs a search based on user input."""

    @property
    def input_keys(self):
        return []

    def plan(
        self, intermediate_steps: List[Tuple[AgentAction, str]], **kwargs: Any
    ) -> Union[AgentAction, AgentFinish]:
        """Given input, decide what to do.

        Args:
            intermediate_steps: Steps the LLM has taken to date,
                along with observations
            **kwargs: User inputs.

        Returns:
            Action specifying what tool to use.
        """
        query = input(kwargs.get("prompt", "Enter a search query: "))
        return AgentAction(tool="Search", tool_input=query, log="")

    async def aplan(
        self, intermediate_steps: List[Tuple[AgentAction, str]], **kwargs: Any
    ) -> Union[AgentAction, AgentFinish]:
        """Given input, decide what to do.

        Args:
            intermediate_steps: Steps the LLM has taken to date,
                along with observations
            **kwargs: User inputs.

        Returns:
            Action specifying what tool to use.
        """
        query = input(kwargs.get("prompt", "Enter a search query: "))
        return AgentAction(tool="Search", tool_input=query, log="")


agent = RealtimeSearchAgent()

agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)

agent_executor.run({}) # Pass an empty dictionary of inputs to the agent

