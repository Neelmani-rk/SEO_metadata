import streamlit as st
import google.generativeai as genai

# Configure API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Generate meta content using advanced, task-focused SEO prompt
def generate_meta_content(page_name, main_keywords, url):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"""
You are an expert SEO specialist.

Your task is to craft a compelling Meta Title and Meta Description for a webpage. These will appear on Google search results and are crucial to maximize Click-Through Rate (CTR) and improve visibility on Search Engine Results Pages (SERPs).

Please strictly follow these requirements:

1. Meta Title: 30–60 characters only
2. Meta Description: 120–160 characters only
3. Integrate the primary keywords naturally
4. Ensure relevance to the page name and URL
5. Make it action-oriented and enticing to click

Write output in this exact format:
META TITLE: [your title here]
META DESCRIPTION: [your description here]

Inputs:
- Page Name: {page_name}
- Primary Keywords: {main_keywords}
- Page URL: {url}
        """

        response = model.generate_content(prompt)

        return response.text if hasattr(response, "text") else str(response)

    except Exception as e:
        return f"Error: {str(e)}"

# Parse response into meta title and description
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

# Streamlit interface
def main():
    st.set_page_config(
        page_title="2ndSEO Meta Generator ",
        page_icon="🔍",
        layout="wide"
    )

    st.title("🔍 SEO Meta Title & Description Generator")
    st.write("Craft CTR-boosting meta tags with Gemini AI")

    # Sidebar API key check
    with st.sidebar:
        st.header("Configuration")
        if "GEMINI_API_KEY" in st.secrets:
            st.success("✅ API Key loaded from secrets.toml")
        else:
            st.error("❌ Missing GEMINI_API_KEY in secrets")

    # Input fields
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
            placeholder="e.g., engagement rings, diamond rings, wedding jewelry",
            help="Enter comma-separated primary keywords",
            height=100
        )

    with col2:
        url = st.text_input(
            "URL *",
            placeholder="e.g., https://www.example.com/engagement-rings",
            help="Enter the live page URL"
        )

        st.write("")  # spacing
        st.write("")
        generate_button = st.button(
            "🚀 Generate Meta Tags",
            type="primary",
            use_container_width=True
        )

    # Generate output
    if generate_button:
        if not all([page_name, main_keywords, url]):
            st.error("❌ Please fill in all required fields")
        else:
            with st.spinner("🤖 Generating SEO content..."):
                response = generate_meta_content(page_name, main_keywords, url)

                if response.startswith("Error:"):
                    st.error(f"❌ {response}")
                else:
                    meta_title, meta_description = parse_response(response)

                    # Display output
                    st.header("Results")

                    with st.expander("📋 Input Summary", expanded=True):
                        col_i1, col_i2, col_i3 = st.columns(3)
                        col_i1.markdown(f"**Page Name:**\n{page_name}")
                        col_i2.markdown(f"**Main Keywords:**\n{main_keywords}")
                        col_i3.markdown(f"**URL:**\n{url}")

                    st.subheader("🎯 Generated Meta Tags")
                    out1, out2 = st.columns(2)

                    with out1:
                        st.markdown("**Meta Title:**")
                        if meta_title:
                            count = len(meta_title)
                            if 30 <= count <= 60:
                                st.success(f"{meta_title}")
                                st.caption(f" {count}/60 characters (Perfect!)")
                            else:
                                st.warning(f"{meta_title}")
                                st.caption(f"⚠️ {count}/60 characters (Outside range)")
                        else:
                            st.error("❌ No Meta Title generated")

                    with out2:
                        st.markdown("**Meta Description:**")
                        if meta_description:
                            count = len(meta_description)
                            if 120 <= count <= 160:
                                st.success(f"{meta_description}")
                                st.caption(f" {count}/160 characters (Perfect!)")
                            else:
                                st.warning(f"{meta_description}")
                                st.caption(f"⚠️ {count}/160 characters (Outside range)")
                        else:
                            st.error("❌ No Meta Description generated")

                    if meta_title and meta_description:
                        st.subheader("📋 Copyable HTML Tags")
                        st.code(
                            f"""<title>{meta_title}</title>
<meta name="description" content="{meta_description}">""",
                            language="html"
                        )

                        with st.expander("📝 Raw Text Copy"):
                            st.text(f"Meta Title: {meta_title}")
                            st.text(f"Meta Description: {meta_description}")

    with st.expander("📖 How to use this tool"):
        st.write("""
1. **API Key**: Add your Gemini API key in `.streamlit/secrets.toml`
2. **Input Fields**:
   - Page Name: What the page is about (e.g., product category)
   - Main Keywords: Keywords to be included for SEO (comma-separated)
   - URL: The actual page URL
3. **Generate**: Click the generate button
4. **Review**: Character limits and SEO impact hints will guide optimization
5. **Copy HTML Tags**: Easily integrate into your webpage head section
        """)

if __name__ == "__main__":
    main()
