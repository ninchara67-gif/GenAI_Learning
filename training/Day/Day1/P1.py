#variables
temperature=0.7
max_tokens=1024
is_streaming=False
content_type=None

#type Hints
model_name:str="gemini-2.0-flash"
temperature:float=0.7
max_tokens:int=1024
is_streaming:bool=False
content_type:str|None=None
print(type(model_name))

#string:immutable |string formatting
#old version
name="LLM"
score=97.3
print("Hello %s"%name)
print("Score %.1f"%score)

#f=strings (py 3.6+)
print(f"Hello {name}")
print(f"score: {score:.1f}")


#expressions inside f-strings
word_limit=200
print(f"{'over' if word_limit >150 else'under'}limit")
data={"Topic":"RAG"}
print(f"Topic:{data['Topic']}")

#format specifiers
pi=3.14159265
print(f"pi:{pi:.2f}")


#debugging
temp=0.7
print(f"{temp=}")


#multi line f-string formatting
user_input="what is langchain?"
context_text="langchain is a framework for building LLM apps"
system_prompt=f""""
you are a helpful AI tutor.
Context provided:{context_text}
student question:{user_input}
-Answer based only on the context above
-If the answer is not in the context, say "I dont't know"
-keep your answers under 3 sentences 
""".strip()
print(system_prompt)


# lists:ordered,mutable,heterogenous sequeces
# In Gen AI: chat history,chunks of retreived documents
#Token sequenes
chat_history:list[dict]=[
    {"role":"user","content":"what is an LLM"},
    {"role":"assistant","content":"A LLM is neutral n/w trained on vast amounts of text."},
]

#access
first_msg=chat_history[0]
print(first_msg)
print(chat_history[-1]["content"])

#modify
chat_history.append({"role":"user","content":"what is an RAG"})
print(chat_history)
chat_history.pop(0)
print(chat_history)

#iterate 
for msg in chat_history:
    print(f"{msg['role'].upper()}:{msg['content']}")


# list of document chunks
chunk:list[str]=[
    "RAG stand for Retreival augmnted Genration",
    "It combines a retreiver wiht a generation",
]

#filter chunks based on length
valid_chunks=[c for c in chunk if len(c.split())>=6]
print(valid_chunks)

