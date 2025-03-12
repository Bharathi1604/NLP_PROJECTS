from src.llm import LLM
from src.memory import Memory_Buffer
from src.vector_db import get_documents


llm = LLM()


''' MEMORY MANAGEMENT '''

class UserMemory:
    memory_dict = {}


def get_or_create_memory(session_id):

    if session_id not in UserMemory.memory_dict:
        UserMemory.memory_dict[session_id] = Memory_Buffer(buffer_size=5)
        return UserMemory.memory_dict[session_id]
    else:
        return UserMemory.memory_dict[session_id]


def update_history(session_id,user_input,bot_response):
    user_memory = get_or_create_memory(session_id)
    return user_memory.append_conversation({"User": user_input,"Assistant": bot_response})


def get_history(session_id,num_conv=3):
    user_memory = get_or_create_memory(session_id)
    return user_memory.memory_as_string(num_conv = num_conv)

''' MEMORY MANAGEMENT '''



def get_prompt(query,context,history):

    prompt = f"""### System:
    You are an helpful assistant answer the user query based on the given context.

    ### Context:
    {context}

    ### Current Conversation:
    {history}

    User: {query}
    Assistant: """

    return prompt



def get_response(query,session_id):
    context = get_documents(query=query,session_id=session_id)
    history = get_history(session_id)
    prompt = get_prompt(query,context,history)
    response = llm.run(prompt).strip().strip("\n")
    return response



