import streamlit as st
from work import *
import json
import os
def main():
    st.set_page_config(page_title="Resume Parser",layout='centered',page_icon='📃')
    st.title("📃 AI Resume Parser",)
    uploaded_file = st.file_uploader("Upload your Resume",type=['docx','pdf','txt'])

    if uploaded_file:
        with st.spinner('Loading Resume....'):
            docs = load_resume(uploaded_file)
            if not docs:
                st.error("Unsupported file found")
        st.subheader('Extracted Text (preview)')
        text_preview = "\n\n".join([d.page_content for d in docs])
        st.text_area("Preview",value=text_preview,height=200)

    if st.button("Ask LLM"):
        with st.spinner("Generating the answer.."):
            formated_prompt = prompt.format(text = text_preview)
            response = llm.invoke(formated_prompt)
        st.subheader("Parsed Json Output")
        # st.write(response)
        try:
            # parsed_json = json.loads(response)
            st.json(response.content)
            
            base_filename = os.path.splitext(uploaded_file.name)[0]
            download_filename = f"{base_filename}_parsed.json"
            st.download_button(
                    label="📥 Download JSON",
                    data=response.content, # The data to be downloaded
                    file_name=download_filename, # The name of the file
                    mime="application/json" # The MIME type of the file
                )
        except json.JSONDecodeError:
                st.error("The AI did not return a valid JSON. Displaying raw output:")
                st.text(response)


if __name__ == "__main__":
    main()
