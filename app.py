import streamlit as st
import google.generativeai as genai
from google.generativeai import types


# Fetch API key from Streamlit secrets
DEFAULT_API_KEY = st.secrets["API_KEY"]


def generate_meta_content(page_name, main_keywords, url, api_key):
    """
    Generate meta title and description using Gemini API
    """
    try:
        client = genai.Client(api_key=api_key)
        model = "gemini-2.0-flash"

        prompt = f"""
        You are an SEO expert. Based on the following information, generate a meta title and meta description for a webpage:

        Page Name: {page_name}
        Main Keywords: {main_keywords}
        URL: {url}

        Requirements:
        1. Meta Title: Must be between 30-60 characters (strictly enforce this limit)
        2. Meta Description: Must be between 120-160 characters (strictly enforce this limit)
        3. Include relevant keywords naturally
        4. Make it compelling and click-worthy
        5. Ensure it's relevant to the page content

        Please provide the output in this exact format:
        META TITLE: [your meta title here]
        META DESCRIPTION: [your meta description here]
        """

        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=prompt),
                ],
            ),
        ]

        generate_content_config = types.GenerateContentConfig(
            response_mime_type="text/plain",
        )

        response_text = ""
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            response_text += chunk.text

        return response_text

    except Exception as e:
        return f"Error: {str(e)}"


def parse_response(response_text):
    """
    Parse the response to extract meta title and description
    """
    lines = response_text.strip().split('\n')
    meta_title = ""
    meta_description = ""

    for line in lines:
        if line.startswith("META TITLE:"):
            meta_title = line.replace("META TITLE:", "").strip()
        elif line.startswith("META DESCRIPTION:"):
            meta_description = line.replace("META DESCRIPTION:", "").strip()

    return meta_title, meta_description


def main():
    st.set_page_config(
        page_title="SEO Meta Generator",
        page_icon="🔍",
        layout="wide"
    )

    st.title("🔍 SEO Meta Title & Description Generator")
    st.write("Generate optimized meta titles and descriptions using Gemini AI")

    with st.sidebar:
        st.header("🔑 Gemini API Key")
        api_key = st.text_input(
            "Enter your Gemini API Key",
            value=DEFAULT_API_KEY,
            type="password",
            help="Pre-filled from Streamlit secrets"
        )
        if api_key:
            st.success("API Key is set and ready to use ✅")
        else:
            st.warning("Please enter your Gemini API key")


    # Main input form
    st.header("Input Information")

    col1, col2 = st.columns(2)

    with col1:
        page_name = st.text_input(
            "Page Name *",
            placeholder="e.g., Engagement Rings",
            help="Enter the name/title of the page"
        )

        main_keywords = st.text_area(
            "Main Keywords *",
            placeholder="e.g., engagement rings, diamond rings, gold engagement rings",
            help="Enter comma-separated keywords relevant to the page",
            height=100
        )

    with col2:
        url = st.text_input(
            "URL *",
            placeholder="e.g., https://www.example.com/page",
            help="Enter the URL of the page"
        )

        st.write("")  # spacing
        st.write("")  # spacing
        generate_button = st.button(
            "🚀 Generate Meta Tags",
            type="primary",
            use_container_width=True
        )

    # Validation and generation
    if generate_button:
        if not api_key:
            st.error("❌ Please provide your Gemini API key in the sidebar")
        elif not all([page_name, main_keywords, url]):
            st.error("❌ Please fill in all required fields")
        else:
            with st.spinner("🤖 Generating meta tags..."):
                response = generate_meta_content(page_name, main_keywords, url, api_key)

                if response.startswith("Error:"):
                    st.error(f"❌ {response}")
                else:
                    meta_title, meta_description = parse_response(response)

                    # Display results
                    st.header("Results")

                    with st.expander("📋 Input Summary", expanded=True):
                        input_col1, input_col2, input_col3 = st.columns(3)

                        with input_col1:
                            st.write("**Page Name:**")
                            st.info(page_name)

                        with input_col2:
                            st.write("**Main Keywords:**")
                            st.info(main_keywords)

                        with input_col3:
                            st.write("**URL:**")
                            st.info(url)

                    # Output
                    st.subheader("🎯 Generated Meta Tags")

                    output_col1, output_col2 = st.columns(2)

                    with output_col1:
                        st.write("**Meta Title:**")
                        if meta_title:
                            char_count_title = len(meta_title)
                            if 30 <= char_count_title <= 60:
                                st.success(f" {meta_title}")
                                st.caption(f"Character count: {char_count_title}/60 (Perfect!)")
                            else:
                                st.warning(f" {meta_title}")
                                st.caption(f"Character count: {char_count_title}/60 (Outside optimal range)")
                        else:
                            st.error("Failed to generate meta title")

                    with output_col2:
                        st.write("**Meta Description:**")
                        if meta_description:
                            char_count_desc = len(meta_description)
                            if 120 <= char_count_desc <= 160:
                                st.success(f" {meta_description}")
                                st.caption(f"Character count: {char_count_desc}/160 (Perfect!)")
                            else:
                                st.warning(f" {meta_description}")
                                st.caption(f"Character count: {char_count_desc}/160 (Outside optimal range)")
                        else:
                            st.error("Failed to generate meta description")

                    if meta_title and meta_description:
                        st.subheader("📋 Copy Ready Format")
                        copy_text = f"""<title>{meta_title}</title>
<meta name="description" content="{meta_description}">"""

                        st.code(copy_text, language="html")

                        with st.expander("📝 Raw Text (for easy copying)"):
                            st.text(f"Meta Title: {meta_title}")
                            st.text(f"Meta Description: {meta_description}")

    # How to use
    with st.expander("📖 How to use this tool"):
        st.write("""
        1. **Enter Gemini API Key** (or load from your environment variable `GEMINI_API_KEY`)
        2. **Fill Input Fields**:
           - **Page Name**: The title or name of your webpage
           - **Main Keywords**: Comma-separated list of relevant keywords
           - **URL**: The actual URL of the page
        3. **Generate**: Click the generate button to create optimized meta tags
        4. **Review & Copy**: Check character counts and copy the generated HTML code

        **Character Limits:**
        - Meta Title: 30-60 characters
        - Meta Description: 120-160 characters
        """)

if __name__ == "__main__":
    main()
