import streamlit as st
import pages.info as info

def render_links():
    """Render the contact / social links in the sidebar using data from pages.info."""
    try:
        st.sidebar.header("Links")
        st.sidebar.text("Connect with me on LinkedIn")

        linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width="75" height="75"></a>'
        st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)

        st.sidebar.text("Checkout my work")
        github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="Github" width="65" height="65"></a>'
        st.sidebar.markdown(github_link, unsafe_allow_html=True)

        st.sidebar.text("Or email me!")
        email_html = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt="Email" width="75" height="75"></a>'
        st.sidebar.markdown(email_html, unsafe_allow_html=True)
    except Exception as e:
        # Avoid breaking the page rendering if info is missing or has errors
        st.sidebar.error(f"Sidebar failed to render: {e}")
