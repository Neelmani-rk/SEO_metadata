import streamlit as st
import google.generativeai as genai

# Configure API key from secrets.toml
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Function to generate meta content
def generate_meta_content(page_name, main_keywords, url):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

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

        response = model.generate_content(prompt)

        return response.text if hasattr(response, "text") else str(response)

    except Exception as e:
        return f"Error: {str(e)}"

# Function to parse model output
def parse_response(response_text):
    lines = response_text.strip().split('\n')
    meta_title = ""
    meta_description = ""

    for line in lines:
        if line.startswith("META TITLE:"):
            meta_title = line.replace("META TITLE:", "").strip()
        elif line.startswith("META DESCRIPTION:"):
            meta_description = line.replace("META DESCRIPTION:", "").strip()

    return meta_title, meta_description

# Streamlit app layout
def main():
    st.set_page_config(
        page_title="SEO Meta Generator",
        page_icon="🔍",
        layout="wide"
    )

    st.title("🔍 SEO Meta Title & Description Generator")
    st.write("Generate optimized meta titles and descriptions using Gemini AI")

    # Sidebar (show key present status)
    with st.sidebar:
        st.header("Configuration")
        if "GEMINI_API_KEY" in st.secrets:
            st.success("✅ API Key loaded from secrets.toml")
        else:
            st.error("❌ Missing GEMINI_API_KEY in secrets")

    # Input form
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
            placeholder="e.g., engagement rings, engagement rings for women, diamond engagement rings, gold engagement rings, jewellery website",
            help="Enter comma-separated keywords relevant to the page",
            height=100
        )

    with col2:
        url = st.text_input(
            "URL *",
            placeholder="e.g., https://www.blissdiamond.com/collections/engagement",
            help="Enter the URL of the page"
        )

        st.write("")  # spacing
        st.write("")
        generate_button = st.button(
            "🚀 Generate Meta Tags",
            type="primary",
            use_container_width=True
        )

    # Generate and display
    if generate_button:
        if not all([page_name, main_keywords, url]):
            st.error("❌ Please fill in all required fields")
        else:
            with st.spinner("🤖 Generating meta tags..."):
                response = generate_meta_content(page_name, main_keywords, url)

                if response.startswith("Error:"):
                    st.error(f"❌ {response}")
                else:
                    meta_title, meta_description = parse_response(response)

                    # Display results
                    st.header("Results")

                    with st.expander("📋 Input Summary", expanded=True):
                        col_i1, col_i2, col_i3 = st.columns(3)
                        with col_i1:
                            st.write("**Page Name:**")
                            st.info(page_name)
                        with col_i2:
                            st.write("**Main Keywords:**")
                            st.info(main_keywords)
                        with col_i3:
                            st.write("**URL:**")
                            st.info(url)

                    st.subheader("🎯 Generated Meta Tags")
                    out1, out2 = st.columns(2)

                    with out1:
                        st.write("**Meta Title:**")
                        if meta_title:
                            count = len(meta_title)
                            if 30 <= count <= 60:
                                st.success(f"✅ {meta_title}")
                                st.caption(f"Character count: {count}/60 (Perfect!)")
                            else:
                                st.warning(f"⚠️ {meta_title}")
                                st.caption(f"Character count: {count}/60 (Outside optimal range)")
                        else:
                            st.error("❌ Failed to generate meta title")

                    with out2:
                        st.write("**Meta Description:**")
                        if meta_description:
                            count = len(meta_description)
                            if 120 <= count <= 160:
                                st.success(f"✅ {meta_description}")
                                st.caption(f"Character count: {count}/160 (Perfect!)")
                            else:
                                st.warning(f"⚠️ {meta_description}")
                                st.caption(f"Character count: {count}/160 (Outside optimal range)")
                        else:
                            st.error("❌ Failed to generate meta description")

                    # Copyable block
                    if meta_title and meta_description:
                        st.subheader("📋 Copy Ready Format")
                        st.code(f"""<title>{meta_title}</title>
<meta name="description" content="{meta_description}">""", language="html")

                        with st.expander("📝 Raw Text"):
                            st.text(f"Meta Title: {meta_title}")
                            st.text(f"Meta Description: {meta_description}")

    with st.expander("📖 How to use this tool"):
        st.write("""
        1. **Add API Key**: Place your Gemini API key in `.streamlit/secrets.toml`
        2. **Fill Fields**:
           - **Page Name**: Web page title
           - **Main Keywords**: Comma-separated SEO keywords
           - **URL**: The full web page link
        3. **Click Generate**: Wait for Gemini AI to generate results
        4. **Copy Output**: Paste tags into your HTML head
        """)

if __name__ == "__main__":
    main()
