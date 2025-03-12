import streamlit as st
import random
import time
import asyncio
import uuid

st.title("Worktual CAI with Streaming")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Intialize user Id and bot Id
if "user_id" not in st.session_state or "bot_id" not in st.session_state:
    st.session_state.user_id = uuid.uuid4()
    st.session_state.bot_id = uuid.uuid4()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

async def get_response(request):
    message_placeholder = st.empty()
    full_response = ""
    # result = await process_input(request=request)
    async for result in process_input(request=request):
        # result = await chunk
        current_result = result.replace(full_response,"")
        #print(current_result)
        full_response += current_result + " "
        await asyncio.sleep(0.05)
        message_placeholder.markdown(current_result + "▌")
    #message_placeholder.markdown(full_response)
    #print(full_response)
    message_placeholder.markdown(current_result)
    return current_result

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    request = Request(user_id=st.session_state.user_id,user_query=prompt,bot_id=st.session_state.bot_id,is_close=0)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        start = time.time()
        full_response = asyncio.run(get_response(request))
        print(f"Total Time : {time.time() - start}")
        print(f"Full Response : {full_response}")
        
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    update_dialog_state_after_streaming(request=request,final_bot_response=full_response)