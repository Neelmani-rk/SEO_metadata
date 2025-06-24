# import streamlit as st
# import pandas as pd
# import google.generativeai as genai

# # Configure Gemini API key
# genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# # Dataset with 36 rows
# COLLECTION_DATA = [
#     ["Engagement Rings", "engagement rings, engagement rings for women, diamond engagement rings, gold engagement rings, jewellery website", "https://www.blissdiamond.com/collections/engagement"],
#     ["Wedding Rings", "wedding rings, guys wedding rings, wedding bands for him, wedding rings for women, female wedding rings, gold wedding rings, unique wedding rings", "https://www.blissdiamond.com/collections/wedding-rings"],
#     ["Jewelry", "diamond rings, lab grown diamond, diamond earrings, diamond engagement rings, gold jewlary, diamond jewellery, jewellery website", "https://www.blissdiamond.com/collections/jewelry"],
#     ["Solitaire (Engagement Rings)", "solitaire diamond ring, solitaire ring, solitaire engagement ring, oval solitaire engagement ring, solitaire diamond, emerald cut solitaire ring", "https://www.blissdiamond.com/collections/engagement-rings-solitaire"],
#     ["Three Stone (Engagement Rings)", "three stone engagement ring, three stone wedding ring, three stone ring, three stone oval engagement ring, three stone diamond ring", "https://www.blissdiamond.com/collections/engagement-rings-three-stone"],
#     ["Bridal Sets (Engagement Rings)", "bridal set rings, womens bridal sets, engagement rings and bridal sets, moissanite bridal sets, moissanite bridal set rings", "https://www.blissdiamond.com/collections/engagement-rings-bridal-sets"],
#     ["Side Stones (Engagement Rings)", "oval engagement ring with side stones, side stone engagement rings", "https://www.blissdiamond.com/collections/engagement-rings-side-stones"],
#     ["Vintage (Engagement Rings)", "vintage engagement rings, vintage wedding rings, vintage style engagement rings, vintage diamond rings, vintage diamond engagement rings", "https://www.blissdiamond.com/collections/engagement-rings-vintage"],
#     ["Men's Rings (Wedding Rings)", "mens wedding bands, men marriage rings, bands for mens wedding, marriage bands for men, guys wedding rings", "https://www.blissdiamond.com/collections/wedding-anniversary-mens-rings"],
#     ["Women's Rings (Wedding Rings)", "engagement rings for women, female engagement rings, wedding bands for women, diamond rings for women, women marriage rings", "https://www.blissdiamond.com/collections/wedding-anniversary-womens-rings"],
#     ["Eternity Rings (Wedding Rings)", "eternity rings, eternity wedding rings, wedding rings online", "https://www.blissdiamond.com/collections/wedding-anniversary-eternity-rings"],
#     ["Diamond Rings (Wedding Rings)", "diamond rings, lab grown diamond rings, lab created diamond rings, diamond rings for women, lab diamond rings", "https://www.blissdiamond.com/collections/wedding-anniversary-diamond-rings"],
#     ["Gemstone (Wedding Rings)", "gemstone engagement rings, gemstone wedding rings, best gemstones for engagement rings, unique gemstone engagement rings, emerald gemstone engagement rings", "https://www.blissdiamond.com/collections/wedding-anniversary-rings-gemstone"],
#     ["Plain Bands (Wedding Rings)", "wedding band ring, mens wedding bands, masculine wedding bands, wedding bands for women, mens gold wedding bands, female wedding bands, ladies wedding bands", "https://www.blissdiamond.com/collections/wedding-anniversary-plain-bands"],
#     ["Pendants", "cross pendant necklace, diamond s necklace, pendants, gold cross necklace, pendant necklace", "https://www.blissdiamond.com/collections/pendants"],
#     ["Solitaire (Pendants)", "diamond solitaire necklace, solitaire diamond necklace 1 ct, diamond solitaire pendant, solitaire pendant diamond", "https://www.blissdiamond.com/collections/solitaire-pendants"],
#     ["Halo (Pendants)", "halo diamond necklace, diamond halo pendant, halo pendant", "https://www.blissdiamond.com/collections/halo-pendants"],
#     ["Three Stone (Pendants)", "three stone diamond necklace, 3 stone diamond necklace", "https://www.blissdiamond.com/collections/three-stone-pendants"],
#     ["Heart Shape (Pendants)", "heart diamond necklaces, diamond pendant heart, heart diamond pendent, necklace heart shape, heart cut diamond necklace", "https://www.blissdiamond.com/collections/heart-shape-pendants"],
#     ["Circle (Pendants)", "diamond circle necklace, necklace with diamond circle, necklace circle diamonds, circle necklace", "https://www.blissdiamond.com/collections/circle-pendants"],
#     ["Earrings", "diamond earrings, lab grown diamonds earrings, diamond earrings for men, diamond earrings for women, 1 carat diamond earrings, 2 carat diamond earrings", "https://www.blissdiamond.com/collections/earrings"],
#     ["Stud (Earrings)", "diamond stud earrings 2 carat, diamond stud earrings, diamond stud earrings for women, diamond stud earrings for men", "https://www.blissdiamond.com/collections/earrings-studs"],
#     ["Halo (Earrings)", "halo diamond earrings, halo diamond, halo earrings, halo stud earrings", "https://www.blissdiamond.com/collections/halo-earrings"],
#     ["Hoops (Earrings)", "diamond hoop earrings, diamond hoop earrings for women, gold diamond hoop earrings, gold and diamond hoop earrings, small diamond hoop earrings", "https://www.blissdiamond.com/collections/earrings-hoops"],
#     ["Gemstone (Earrings)", "gemstone shop online, gemstone earrings, best gemstone earrings", "https://www.blissdiamond.com/collections/gemstone-earrings"],
#     ["Lab Grown Diamonds", "lab grown diamond rings, lab grown diamond, lab grown diamond engagement rings, lab made diamond rings, lab grown diamonds earrings, best lab grown diamonds", "https://www.blissdiamond.com/collections/lab-grown-diamonds"],
#     ["Engagement Rings (Lab Grown)", "lab grown diamond engagement rings, lab created diamond engagement rings, lab diamond engagement rings, lab grown diamond rings", "https://www.blissdiamond.com/collections/lab-grown-engagement-rings"],
#     ["Wedding Rings (Lab Grown)", "lab grown diamond, wedding rings for women, best lab grown diamonds, 3 carat lab grown diamond ring, lab grown diamond rings for sale", "https://www.blissdiamond.com/collections/lab-grown-wedding-rings"],
#     ["Earrings (Lab Grown)", "lab grown diamond stud earrings, diamond earrings, lab grown diamonds earrings, lab created diamond earrings", "https://www.blissdiamond.com/collections/lab-grown-earrings"],
#     ["Bracelets (Lab Grown)", "lab grown diamond tennis bracelet", "https://www.blissdiamond.com/collections/lab-grown-bracelets"],
#     ["Fashion", "fashion jewelry, fashion jewelry shop, fashion jewelry store", "https://www.blissdiamond.com/collections/fashion"],
#     ["Bracelets (Fashion)", "tennis bracelets, gold bracelets, diamond tennis bracelet, gold bracelets for women, ladies gold bracelets, female gold bracelet, gold bangle bracelet", "https://www.blissdiamond.com/collections/fashion-bracelets"],
#     ["Blue Diamond (Fashion)", "blue diamond, blue diamond ring, diamond ring with blue diamond, diamond blue ring", "https://www.blissdiamond.com/collections/blue-diamond-fashion-jewelry"],
#     ["Black Diamond (Fashion)", "black diamond, black diamond ring, diamond ring with black diamonds, diamond black engagement rings", "https://www.blissdiamond.com/collections/black-diamond-fashion-jewelry"],
#     ["Rings (Fashion)", "rings, diamond rings, promise rings, a diamond ring, gold rings, mens rings, birthstone rings", "https://www.blissdiamond.com/collections/fashion-jewelry-rings"],
#     ["Necklaces (Fashion)", "gold necklaces, diamond necklaces, gold necklace women, men's necklace", "https://www.blissdiamond.com/collections/fashion-jewelry-necklaces"]
# ]

# # Dataset for main pages
# MAIN_PAGES_DATA = [
#     ["Home Page", "online jewelry store, best online jewelry store, best places to buy engagement rings online, gold jewellery online, diamonds", "https://www.blissdiamond.com/"],
#     ["About Us", "gold jewellery online, best online wedding rings, buy jewellery online, wedding rings online, diamonds", "https://www.blissdiamond.com/pages/about-us/"],
#     ["Contact Us", "engagement rings, diamonds, wedding rings, gold jewelry, Earrings, Bracelets", "https://www.blissdiamond.com/pages/contact-us"],
#     ["Custom Design", "custom engagement rings online, custom jewelry online, customised jewellery online", "https://www.blissdiamond.com/pages/custom-design"]
# ]

# # Convert datasets to DataFrames
# COLLECTION_DF = pd.DataFrame(COLLECTION_DATA, columns=["Page Name", "Main Keywords", "URL"])
# COLLECTION_DF.index += 1
# MAIN_PAGES_DF = pd.DataFrame(MAIN_PAGES_DATA, columns=["Page Name", "Main Keywords", "URL"])
# MAIN_PAGES_DF.index += 1


# def validate_meta_content(content):
#     """
#     Validate the generated meta content against requirements
#     Returns dict with 'valid' boolean and 'errors' list
#     """
#     errors = []
    
#     try:
#         # Extract meta title and description using regex
#         title_match = re.search(r'META TITLE:\s*(.+)', content, re.IGNORECASE)
#         desc_match = re.search(r'META DESCRIPTION:\s*(.+)', content, re.IGNORECASE)
        
#         if not title_match:
#             errors.append("Meta title not found in expected format")
#         else:
#             title = title_match.group(1).strip()
#             title_length = len(title)
            
#             if title_length < 30:
#                 errors.append(f"Meta title too short: {title_length} characters (minimum 30)")
#             elif title_length > 60:
#                 errors.append(f"Meta title too long: {title_length} characters (maximum 60)")
        
#         if not desc_match:
#             errors.append("Meta description not found in expected format")
#         else:
#             description = desc_match.group(1).strip()
#             desc_length = len(description)
            
#             if desc_length < 120:
#                 errors.append(f"Meta description too short: {desc_length} characters (minimum 120)")
#             elif desc_length > 160:
#                 errors.append(f"Meta description too long: {desc_length} characters (maximum 160)")
            
#             # Check if it ends with "Shop Now!"
#             if not description.endswith("Shop Now!"):
#                 errors.append("Meta description must end with 'Shop Now!'")
    
#     except Exception as e:
#         errors.append(f"Validation error: {str(e)}")
    
#     return {
#         "valid": len(errors) == 0,
#         "errors": errors
#     }


# def generate_meta_content(page_name, main_keywords, url):
#     try:
#         model = genai.GenerativeModel("gemini-2.5-flash")

#         prompt = f"""
#         You are an SEO expert. Based on the following information, generate a meta title and meta description for a webpage:

#         Page Name: {page_name}
#         Main Keywords: {main_keywords}
#         URL: {url}

#         Requirements:
#         1. Meta Title: Must be between 30-60 characters (make sure the title is more than 30 characters and less than 60 characters including space ,strictly enforce this limit )
#         2. Meta Description: Must be between 120-145 characters (strictly enforce this limit, DO NOT EXCEED 150 characters AND MORE THAN 125 characters )
#         3. ** prioritize the Description Must be of Maximum 138 characters **
#         4. Include relevant keywords naturally
#         5. Make it compelling and click-worthy
#         6. Ensure it's relevant to the page content
#         7. Make it crisp and very short Strictly and catchy.
#         8. Do not leave space when starting a new line , keep the sentence very short , at maximum use only 2 sentence.
#         9. End the description with "Shop Now!" .

#         Please provide the output in this exact format:
#         META TITLE: [your meta title here]
#         META DESCRIPTION: [your meta description here]
#         """
       


#         response = model.generate_content(prompt)
#         return response.text if hasattr(response, "text") else str(response)

#     except Exception as e:
#         return f"Error: {str(e)}"
    
# def parse_response(response_text):
#     lines = response_text.strip().split('\n')
#     meta_title = ""
#     meta_description = ""
#     for line in lines:
#         if line.startswith("META TITLE:"):
#             meta_title = line.replace("META TITLE:", "").strip()
#         elif line.startswith("META DESCRIPTION:"):
#             meta_description = line.replace("META DESCRIPTION:", "").strip()
#     return meta_title, meta_description

# def main():
#     st.set_page_config(
#         page_title="SEO Meta Generator",
#         page_icon="🔍",
#         layout="wide"
#     )

#     st.title("🔍 SEO Meta Title & Description Generator VERSION 1")
#     st.write("Generate optimized meta titles and descriptions using Gemini AI")

#     with st.sidebar:
#         st.header("Configuration")
#         if "GEMINI_API_KEY" in st.secrets:
#             st.success("✅ API Key loaded from secrets.toml")
#         else:
#             st.error("❌ Missing GEMINI_API_KEY in secrets")

#         data_type = st.radio("Select Data Type", ["Collections", "Main Pages"])

#         if data_type == "Collections":
#             selected_row = st.selectbox("Select Collection Row (1–36)", options=COLLECTION_DF.index, format_func=lambda x: f"Row {x} - {COLLECTION_DF.loc[x, 'Page Name']}")
#             selected_data = COLLECTION_DF.loc[selected_row]
#             default_page_name = selected_data["Page Name"]
#             default_keywords = selected_data["Main Keywords"]
#             default_url = selected_data["URL"]
#         else:
#             selected_row = st.selectbox("Select Main Page", options=MAIN_PAGES_DF.index, format_func=lambda x: f"{MAIN_PAGES_DF.loc[x, 'Page Name']}")
#             selected_data = MAIN_PAGES_DF.loc[selected_row]
#             default_page_name = selected_data["Page Name"]
#             default_keywords = selected_data["Main Keywords"]
#             default_url = selected_data["URL"]

#     st.header("Input Information")

#     col1, col2 = st.columns(2)
#     with col1:
#         page_name = st.text_input("Page Name *", value=default_page_name)
#         main_keywords = st.text_area("Main Keywords *", value=default_keywords, height=100)

#     with col2:
#         url = st.text_input("URL *", value=default_url)
#         st.write("")
#         st.write("")
#         generate_button = st.button("🚀 Generate Meta Tags", type="primary", use_container_width=True)

#     if generate_button:
#         if not all([page_name, main_keywords, url]):
#             st.error("❌ Please fill in all required fields")
#         else:
#             with st.spinner("🤖 Generating meta tags..."):
#                 response = generate_meta_content(page_name, main_keywords, url)

#                 if response.startswith("Error:"):
#                     st.error(f"❌ {response}")
#                 else:
#                     meta_title, meta_description = parse_response(response)
#                     st.header("Results")

#                     with st.expander("📋 Input Summary", expanded=True):
#                         col_i1, col_i2, col_i3 = st.columns(3)
#                         with col_i1:
#                             st.write("**Page Name:**")
#                             st.info(page_name)
#                         with col_i2:
#                             st.write("**Main Keywords:**")
#                             st.info(main_keywords)
#                         with col_i3:
#                             st.write("**URL:**")
#                             st.info(url)

#                     st.subheader("🎯 Generated Meta Tags")
#                     out1, out2 = st.columns(2)
#                     with out1:
#                         st.write("**Meta Title:**")
#                         if meta_title:
#                             count = len(meta_title)
#                             if 30 <= count <= 60:
#                                 st.success(f" {meta_title}")
#                                 st.caption(f"Character count: {count}/60 (Perfect!)")
#                             else:
#                                 st.warning(f"⚠️ {meta_title}")
#                                 st.caption(f"Character count: {count}/60 (Outside optimal range)")
#                         else:
#                             st.error("❌ Failed to generate meta title")

#                     with out2:
#                         st.write("**Meta Description:**")
#                         if meta_description:
#                             count = len(meta_description)
#                             if 120 <= count <= 160:
#                                 st.success(f" {meta_description}")
#                                 st.caption(f"Character count: {count}/160 (Perfect!)")
#                             else:
#                                 st.warning(f"⚠️ {meta_description}")
#                                 st.caption(f"Character count: {count}/160 (Outside optimal range)")
#                         else:
#                             st.error("❌ Failed to generate meta description")

#                     if meta_title and meta_description:
#                         st.subheader("📋 Copy Ready Format")
#                         st.code(f"""<title>{meta_title}</title>\n<meta name=\"description\" content=\"{meta_description}\">""", language="html")

#                         with st.expander("📝 Raw Text"):
#                             st.text(f"Meta Title: {meta_title}")
#                             st.text(f"Meta Description: {meta_description}")

#     with st.expander("📖 How to use this tool"):
#         st.write("""
#         1. **Add API Key**: Place your Gemini API key in `.streamlit/secrets.toml`
#         2. **Select Data Type**: Choose between 'Collections' or 'Main Pages'
#         3. **Select a row**: Auto-fill inputs from dropdown
#         4. **Review & edit**: Optionally modify Page Name, Keywords, or URL
#         5. **Click Generate**: Get SEO-optimized meta tags
#         6. **Copy Output**: Paste generated tags into your HTML head
#         """)



import streamlit as st
import pandas as pd
import time
import google.generativeai as genai
import concurrent.futures
import re
from io import StringIO

# Load API keys from secrets.toml
API_KEYS = [
    st.secrets["GEMINI_API_KEY_1"],
    st.secrets["GEMINI_API_KEY_2"],
    st.secrets["GEMINI_API_KEY_3"],
    st.secrets["GEMINI_API_KEY_4"]
]

# Prompt template
PROMPT_TEMPLATE = """
You are an expert SEO specialist.

Your task is to craft a compelling Meta Title and Meta Description for a webpage. These will appear on Google search results and are crucial to maximize Click-Through Rate (CTR) and improve visibility on Search Engine Results Pages (SERPs).

Please strictly follow these requirements:

1. Meta Title: 30–60 characters only
2. ** Meta Description: 120–140 characters only or 2 very brief sentences. Do not exceed 150 character limit. **
3. Integrate the primary keywords naturally
4. Ensure relevance to the page name and URL
5. Make it action-oriented and enticing to click
6. Do not include the links , keep the sentences very short and up to the point .

Write output in this exact format:
META TITLE: [your title here]
META DESCRIPTION: [your description here]

Input:
- Product Name: {product_name}
"""

def generate_with_model(api_key, product_name):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = PROMPT_TEMPLATE.format(product_name=product_name)
        response = model.generate_content(prompt)
        return parse_response(product_name, response.text)
    except Exception as e:
        return {"Product Name": product_name, "Meta Title": f"Error: {e}", "Meta Description": ""}

def parse_response(product_name, response_text):
    lines = response_text.strip().split('\n')
    meta_title = ""
    meta_description = ""
    for line in lines:
        if line.startswith("META TITLE:"):
            meta_title = line.replace("META TITLE:", "").strip()
        elif line.startswith("META DESCRIPTION:"):
            meta_description = line.replace("META DESCRIPTION:", "").strip()
    return {"Product Name": product_name, "Meta Title": meta_title, "Meta Description": meta_description}

def run_bulk_processing(product_names):
    results = []
    batch_size = 4
    total = len(product_names)
    status_placeholder = st.empty()

    with st.spinner("🚀 Bulk processing started..."):
        for i in range(0, total, batch_size):
            batch = product_names[i:i + batch_size]
            futures = []
            status_lines = []

            with concurrent.futures.ThreadPoolExecutor() as executor:
                for j, product in enumerate(batch):
                    key = API_KEYS[j % len(API_KEYS)]
                    futures.append(executor.submit(generate_with_model, key, product))

                for k, future in enumerate(futures):
                    result = future.result()
                    results.append(result)
                    row_index = i + k + 1
                    status_lines.append(f"✅ Row {row_index}: Processing done")

            status_placeholder.markdown("**Progress:**\n" + "\n".join(status_lines))
            time.sleep(1)

    return results

def main():
    st.set_page_config(page_title="Bulk Meta Generator", layout="wide")
    st.title("📦 Bulk SEO Meta Title & Description Generator")

    uploaded_file = st.file_uploader("Upload CSV file with 'Product Name' column", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        if "Product Name" not in df.columns:
            st.error("CSV must contain a 'Product Name' column")
            return

        st.success(f"✅ {len(df)} products loaded.")
        if st.button("🚀 Start Bulk Generation"):
            results = run_bulk_processing(df["Product Name"].tolist())
            result_df = pd.DataFrame(results)
            st.dataframe(result_df)

            csv = result_df.to_csv(index=False)
            st.download_button(
                label="📥 Download as CSV",
                data=csv,
                file_name="generated_meta_tags.csv",
                mime="text/csv"
            )

if __name__ == "__main__":
    main()


# if __name__ == "__main__":
#     main()
