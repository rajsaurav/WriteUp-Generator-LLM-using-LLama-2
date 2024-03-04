import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain_community.chat_models import ChatOpenAI



#Creating functions that get response from Llama-2 model

def getLLamaresponse(input_text,no_words,blog_style):

    #Calling LLAMA-2 model

    llm=CTransformers(model='Model2/llama-2-7b-chat.ggmlv3.q6_K.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})


    template="""
        Write a cover letter for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
            """

    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response


st.set_page_config(page_title="Professional Writeup Generator",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')




st.header("Professional WriteUp Generator 🤖")

input_text=st.text_input("Enter the writeup style")

col1,col2=st.columns([5,5])
with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Generate WriteUp for',
                            ('Data Analysts','Data Scientist','Data Engineers','ML Engineer','Product Managers','Project Managers','Technical Manager'),index=0)
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))

