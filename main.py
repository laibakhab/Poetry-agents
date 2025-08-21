
from agents import Agent, Runner, trace
from connection import config                                              
import asyncio    
# from functions import analyze_dramatic_poem, analyze_lyric_poem, analyze_narrative_poem   

lyric_agent = Agent(                                                                                                 
    name="Lyric Analyst Agent",                        
    instructions="""                                                    
        You analyze lyric poetry focusing on emotions, feelings, and musicality.
        Provide insights about the poem's mood, use of rhythm, and personal voice.
        Your analysis should be in English.
    """,     
)                               
         
narrative_agent = Agent(
    name="NarrativeAgent",
    instructions="""                    
    You are a narrative structure analysis agent. Identify 
    any story structure, character development, or sequence 
    of events within the poetry. If no narrative elements are 
    found, state so and provide a brief reason.""",
)
dramatic_agent = Agent(
    name="DramaticAgent",
    instructions="""
    You are a dramatic poetry analysis agent. Detect
      emotional intensity, dramatic language, or psychological 
      conflict in the poetry and explain it. If no dramatic 
      elements are found, state so and provide a brief reason.""",

       handoffs=[lyric_agent, narrative_agent]
    
)

async def main():
    with trace("Class 06"):
        result = await Runner.run(
            dramatic_agent, 
            """
                On the Mountains of the Prairie,
On the great Red Pipe-stone Quarry,
Gitche Manito, the mighty,
He the Master of Life, descending,
On the red crags of the quarry
Stood erect, and called the nations,
Called the tribes of men together

            """, 
            run_config=config)
        print(result.final_output)
        print("Last Agent ==> ",result.last_agent.name)


if __name__ == "__main__":
    asyncio.run(main())

