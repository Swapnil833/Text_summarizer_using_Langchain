import validators
import streamlit as st
from langchain_classic.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_classic.chains import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, WebBaseLoader


#Streamlit app
st.title("Langchain : Summarize text from YT or website")
st.subheader("Summarize URL")

#Get GROQ API KEY and URL from user
with st.sidebar:
    groq_api_key = st.text_input("Groq Api Key", value="", type="password")

generic_url = st.text_input("URL", label_visibility="collapsed")

llm = ChatGroq(api_key=groq_api_key, model="openai/gpt-oss-20b")


prompt_template="""
Provide a summary of the following content in 300 words:
Content:{text}

"""
prompt=PromptTemplate(template=prompt_template,input_variables=["text"])

if st.button("Summarize the Content from YT or Website"):
    ## Validate all the inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid Url. It can may be a YT video utl or website url")

    else:
        try:
            with st.spinner("Waiting..."):
                ## loading the website or yt video data
                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    loader=YoutubeLoader.from_youtube_url(generic_url,add_video_info=False)
                else:
                    loader = WebBaseLoader(generic_url)

                docs=loader.load()  

                ## Chain For Summarization
                chain=load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                result=chain.invoke(docs)

                st.success(result["output_text"])
        except Exception as e:
            st.exception(e)
                    