#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import http.client
import json
from typing import Any, List, Mapping, Optional
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM


class bitAPAI(LLM):
    
    bitAPAI_key: str = os.environ.get('BITAPAI_KEY')
    
    system: str = "Assistant"
    
    Content_Type: str = 'application/json'
        
    @property
    def _llm_type(self) -> str:
        return "bitAPAI"
    
    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
    ) -> str:
        
        """Call out to bitAPAI endpoint on bittensor network.
        Args:
            payload: The prompt to pass to the API. Consisting of "system" and "user".
            stop: Optional list of stop words to use when generating.
        Returns:
            The string generated by the model.
        Example:
            .. code-block:: python
                conn.request("POST", "/api/v1/prompt", payload, headers)
                res = conn.getresponse()
        """
        
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
            
        payload = json.dumps({
          "system": self.system,
          "user": prompt
        })
        headers = {
          'Content-Type': self.Content_Type,
          'X-API-KEY': self.bitAPAI_key
        }
        conn = http.client.HTTPSConnection("dashboard.bitapai.io")
        conn.request("POST", "/api/v1/prompt", payload, headers)
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")
    
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"system": self.system, "model": 'bittensor bitAPAI'}
    
  
