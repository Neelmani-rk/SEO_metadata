import streamlit as st
import pandas as pd
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Dataset with 36 rows
DATA = [
    ["Engagement Rings", "engagement rings, engagement rings for women, diamond engagement rings, gold engagement rings, jewellery website", "https://www.blissdiamond.com/collections/engagement"],
    ["Wedding Rings", "wedding rings, guys wedding rings, wedding bands for him, wedding rings for women, female wedding rings, gold wedding rings, unique wedding rings", "https://www.blissdiamond.com/collections/wedding-rings"],
    ["Jewelry", "diamond rings, lab grown diamond, diamond earrings, diamond engagement rings, gold jewlary, diamond jewellery, jewellery website", "https://www.blissdiamond.com/collections/jewelry"],
    # Add remaining rows up to 36 as needed...
    ["Necklaces (Fashion)", "gold necklaces, diamond necklaces, gold necklace women, men's necklace", "https://www.blissdiamond.com/collections/fashion-jewelry-necklaces"]
]

# Convert dataset to DataFrame
DF = pd.DataFrame(DATA, columns=["Page Name", "Main Keywords", "URL"])
DF.index += 1

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

def main():
    st.set_page_config(
        page_title="SEO Meta Generator",
        page_icon="🔍",
        layout="wide"
    )

    st.title("🔍 SEO Meta Title & Description Generator VERSION 1")
    st.write("Generate optimized meta titles and descriptions using Gemini AI")

    with st.sidebar:
        st.header("Configuration")
        if "GEMINI_API_KEY" in st.secrets:
            st.success("✅ API Key loaded from secrets.toml")
        else:
            st.error("❌ Missing GEMINI_API_KEY in secrets")

        selected_row = st.selectbox("Select Data Row (1–36)", options=DF.index, format_func=lambda x: f"Row {x}")
        selected_data = DF.loc[selected_row]
        default_page_name = selected_data["Page Name"]
        default_keywords = selected_data["Main Keywords"]
        default_url = selected_data["URL"]

    st.header("Input Information")

    col1, col2 = st.columns(2)
    with col1:
        page_name = st.text_input("Page Name *", value=default_page_name)
        main_keywords = st.text_area("Main Keywords *", value=default_keywords, height=100)

    with col2:
        url = st.text_input("URL *", value=default_url)
        st.write("")
        st.write("")
        generate_button = st.button("🚀 Generate Meta Tags", type="primary", use_container_width=True)

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
                                st.success(f" {meta_title}")
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
                                st.success(f" {meta_description}")
                                st.caption(f"Character count: {count}/160 (Perfect!)")
                            else:
                                st.warning(f"⚠️ {meta_description}")
                                st.caption(f"Character count: {count}/160 (Outside optimal range)")
                        else:
                            st.error("❌ Failed to generate meta description")

                    if meta_title and meta_description:
                        st.subheader("📋 Copy Ready Format")
                        st.code(f"""<title>{meta_title}</title>\n<meta name=\"description\" content=\"{meta_description}\">""", language="html")

                        with st.expander("📝 Raw Text"):
                            st.text(f"Meta Title: {meta_title}")
                            st.text(f"Meta Description: {meta_description}")

    with st.expander("📖 How to use this tool"):
        st.write("""
        1. **Add API Key**: Place your Gemini API key in `.streamlit/secrets.toml`
        2. **Select a row**: Auto-fill inputs from dropdown (Row 1–36)
        3. **Review & edit**: Optionally modify Page Name, Keywords, or URL
        4. **Click Generate**: Get SEO-optimized meta tags
        5. **Copy Output**: Paste generated tags into your HTML head
        """)

if __name__ == "__main__":
    main()
