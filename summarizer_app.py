import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import os

# Set up OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

# Initialize the ChatOpenAI model
llm = ChatOpenAI(model_name='gpt-3.5-turbo')

# Streamlit UI
st.title("News Article Summarizer")

# Text area for user to enter the news article
news_article = st.text_area("Paste the news article here:", height=300)

if st.button("Summarize"):
    if news_article:
        # Constructing the message format for the LLM
        summary_message = [
            SystemMessage(content='Summarize the following news article:'),
            HumanMessage(content=news_article)
        ]

        # Generating the summary
        output = llm(summary_message).content

        # Display the summary
        st.write("Summary:")
        st.write(output)
    else:
        st.warning("Please paste a news article to summarize.")