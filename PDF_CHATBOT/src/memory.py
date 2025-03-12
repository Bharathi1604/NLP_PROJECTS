from typing import List,Dict
from typing import TypedDict,Union


class Conversation(TypedDict):
    User: str
    Assistant: str




class Memory():

    def __init__(self, user_name="User : ",ai_name = "Assistant : "):
        self.memory:List[Dict] = []
        self.user_name = user_name
        self.ai_name = ai_name

    def append_conversation(self,conversation:Conversation):
        self.memory.append(conversation)

    def clear_memory(self):
        self.memory = []

    def memory_as_string(self,num_conv:Union[int,None]=None):
        if num_conv == None or num_conv > len(self.memory) or num_conv <= 0:
            num_conv = len(self.memory)
        response_string = ''
        if len(self.memory) == 0:
            return response_string
        for conversation in self.memory[-num_conv:]:
            response_string = response_string +  "\n" + self.user_name + conversation["User"] + "\n"  + self.ai_name + conversation["Assistant"] 
        return response_string




class Memory_Buffer(Memory):

    def __init__(self, buffer_size:int,**kwargs):
        super().__init__(**kwargs)    def append_conversation(self, conversation: Conversation):

        self.buffer_size = buffer_size

    def append_conversation(self, conversation: Conversation):
        print(len(self.memory))
        if len(self.memory) == self.buffer_size:
            self.memory.pop(0)
        return super().append_conversation(conversation)
    



def get_memory(buffer_size:int=5):
    memory =  Memory_Buffer(buffer_size=buffer_size)
    return memory
    