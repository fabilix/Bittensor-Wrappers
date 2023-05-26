#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from bittensorWrapper import bitAPAI

os.environ["BITAPAI_KEY"] = "<your bitAPAI key>"

#Example
llm = bitAPAI()
llm.system = "You are a Zoologist"

print(llm("Who wins the fight between lion and velociraptor?"))
