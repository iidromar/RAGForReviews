
import streamlit as st
from main import get_response

st.set_page_config(
    page_title="Restaurant Review Assistant",
    page_icon="",
    layout="centered" 
)

st.title("Restaurant Review Assistant ")
st.markdown(
    "Ask a question about a restaurant, and I'll find the answer from its reviews for you! This demo uses RAG to ground the LLM's answers in real world feedback."
)
st.markdown("---")


with st.form(key='question_form'):
    question = st.text_input(
        "Ask your question:",
        placeholder="e.g., 'Is the outdoor seating comfortable in summer?'"
    )
    submit_button = st.form_submit_button(label='Get Answer')


if submit_button and question:
    with st.spinner("Finding answers in the reviews..."):
        answer, reviews = get_response(question)

        st.markdown("---")
        st.subheader("Answer")
        st.info(answer) 

        st.subheader("Source Reviews Used")
        
        if reviews:
            for i, doc in enumerate(reviews):
                with st.expander(f"Review #{i+1} - Rating: {doc.metadata.get('rating', 'N/A')}"):
                    st.text(f"Date: {doc.metadata.get('date', 'N/A')}")
                    st.markdown(f"> {doc.page_content}")
        else:
            st.warning("No relevant reviews were found to generate the answer.")
