#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 10:05:03 2023

@author: fabilix
"""

import os
from bittensorWrapper import bitAPAI

os.environ["BITAPAI_KEY"] = "38207ab3-f8fe-494d-bf4d-9b09aa104eb0"

#LLM initialization
llm = bitAPAI()
llm.system = "You are an assistant"


"""READ ME

Go trough example 1-3 by commenting/uncommenting print(llm(prompt))
The non-conform behaviour will most likely show up in example 3)
"""


# Example 1
# Simple example, start of the chat with a basic prompt
# As there is no assistant prompt, instructions during the conversation are integrated in the prompt
prompt = """
The AI is talkative and provides lots of specific details from its context.
If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation with human:


Question:
Human: Hello, how are you?
Assistant:   
"""
# Uncomment for an answer, comment for example 2
print(llm(prompt))


# Example 2
# Now the chat history is integrated in the prompt, this is a standard format as used with other llm's like davincci-text-03
prompt = """
The AI is talkative and provides lots of specific details from its context.
If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation with human:
Human: Hello, how are you?
Assistant: I am doing well today! How about you?

Question:
Human: What is the strongest animal on the planet?
Assistant:   
"""
# Uncomment for an answer, comment for example 3
#print(llm(prompt))

 
# Example 3
# Chat history is added to the prompt.
prompt = """
The AI is talkative and provides lots of specific details from its context.
If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation with human:
Human: Hello, how are you?
Assistant: I am doing well today! How about you?
What is the strongest animal on the planet?
Assistant: The strongest animal on Earth is the elephant. 
It can weigh up to 12 tons and has been known to lift objects as heavy as 500 pounds. 
Elephants have incredibly strong muscles and bones that allow them to move large amounts of weight. 
They also have thick skin and tusks which make them formidable opponents in battle.

Question:
Human: Very interesting, and which one is the most dangerous?
Assistant:   
"""
# Uncomment for an answer
#print(llm(prompt))














