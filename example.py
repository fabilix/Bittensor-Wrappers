#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 10:05:03 2023

@author: fabilix
"""

import os
from bittensorWrapper import bitAPAI

os.environ["BITAPAI_KEY"] = "your bitAPAI key"

#Example
llm = bitAPAI()
llm.system = "Assistant"

print(llm("Who would win between a fight of the lion and a boa snake?"))