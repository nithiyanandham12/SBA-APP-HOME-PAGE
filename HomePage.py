import streamlit as st


# Define the company logo and app details
company_logo = "sba.jpg"  # Replace with the path to your company logo
app_details = [
    {"logo": "_8fd6e0cf-fde4-4843-8edd-a64337932233.jpg", "name": "PDF URL ANALYZER", "link": "https://5gyk9cpo8hvmeekfgmrqyu.streamlit.app/"},
    {"logo": "_e316abec-51da-443f-bde9-ef340c79d369.jpg", "name": "Marketing Email Genrator", "link": "https://marketing-generation-sba.streamlit.app/"},
    {"logo": "_a691c73b-69b6-4778-92d8-e399f8333e6b.jpg", "name": "DOCUMENT RAG ASSISTANT", "link": "https://sbainfosolutions.streamlit.app/"},
    {"logo": "_ac2912c1-3aee-4072-be42-7461421dd569.jpg", "name": "SBA SEARCH ENGINE", "link": "https://sbasearch.streamlit.app/"},
    {"logo": "_071cd6cb-45c1-49d2-a3ba-a1551b11418e.jpg", "name": "Invoice Processing", "link": "https://kobel.onrender.com/"},
    {"logo": "_67719771-fafa-467e-b2f8-557b229d48fc.jpg", "name": "MEETING TRANSCRIPTION", "link": "https://meeting-transcription-cncvjdrgt3pd9b7adtucyw.streamlit.app/"},
    {"logo": "_55bc0b3f-2019-494c-9978-bbb0129a11d8.jpg", "name": "AUDIO ANALYZER", "link": "https://watsonx-ai-audio-analysis.onrender.com/"},
    {"logo": "_8590e2f5-3550-4dfd-be77-1606a13e4a34.jpg", "name": "SPEECH TO TEXT", "link": "https://663e0d1381ac3e069fe00384--gilded-dieffenbachia-1bccb4.netlify.app/"},
]

# Set the page layout
st.set_page_config(layout="wide")

# Inject custom CSS to change the background color
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: grey;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the title at the top
st.title("Home Screen")

# Sidebar with company logo and name
st.sidebar.image(company_logo, use_column_width=True)
st.sidebar.title("SBA INFO SOLUTIONS")

# Main area with app logos, names, and launch buttons
cols = st.columns(4)

for col, app in zip(cols * (len(app_details) // len(cols) + 1), app_details):
    with col:
        st.image(app["logo"], use_column_width=True)
        st.write(f"**{app['name']}**")
        if st.button("Launch", key=app['name']):
            js = f"window.open('{app['link']}')"
            st.components.v1.html(f"<script>{js}</script>", height=0, width=0)

# Run the Streamlit app
if __name__ == "__main__":
    pass  # The main block can be left empty or used for additional initializations
