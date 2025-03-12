import requests

class LLM:
    
    def __init__(self,url = 'http://127.0.0.1:8000/generate'):
        self.url = url
        self.sampling_params = {
            "n" : 1,
            "presence_penalty" : 0.8,
            "frequency_penalty" : 1.1,
            "temperature" : 0.001,
            "top_p" : 0.95,
            "top_k" : -1,
            "use_beam_search" : False,
            "length_penalty" : 1.0,
            "early_stopping" : False,
            "stop" : ['User:', 'Assistant:', '[/SYS]','USER:'],
            "ignore_eos" : False,
            "max_tokens" : 512,
            "logprobs" : None,
            "prompt_logprobs" : None,
            "skip_special_tokens" : True,
            "stream" : False
        }

    def run(self,prompt) -> str:
        try:
            self.sampling_params.update({'prompt': prompt})
            response = requests.post(url = self.url,json=self.sampling_params)
            return response.json()['text'][0].replace(prompt,"")
        except Exception as e:
            raise e