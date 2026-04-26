import streamlit as st
import urllib.parse
import json

st.set_page_config(page_title="Quick-Comm Compare", page_icon="🛒")

st.title("🛒 Quick Commerce Price Compare")
st.write("Enter a product to generate search links for all platforms.")

# User Input
product_name = st.text_input("What are you looking for?", placeholder="e.g. Paneer, Milk, Coffee")

if product_name:
    query = urllib.parse.quote(product_name)
    
    # Store URLs
    urls = {
        "Blinkit": f"https://blinkit.com/s/?q={query}",
        "BigBasket": f"https://www.bigbasket.com/ps/?q={query}",
        "Amazon Now": f"https://www.amazon.in/tez/browse/search?qcbrand=qqfsWw9RkO&searchKeyword={query}",
        "Flipkart Minutes": f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=HYPERLOCAL&as-show=on&as=off&pageUID",
        "Swiggy Instamart": f"https://www.swiggy.com/instamart/search?custom_back=true&query={query}",
        "JioMart": f"https://www.jiomart.com/search/{query}",
        #"Zepto": f"https://www.zeptonow.com/search?q={query}", 
        #"DMart": f"https://www.dmart.in/search?q={query}",
        #"Myntra Now": f"https://www.myntra.com/search?q={query}"
    }

    st.subheader(f"Results for '{product_name.title()}'")
    
    # Add "Open All" browser button that triggers a direct click event
    all_urls = list(urls.values())
    urls_json = json.dumps(all_urls)
    button_html = f"""
    <div style="padding: 0 0 10px 0;">
        <button style="width:100%;padding:12px;font-size:16px;border:none;border-radius:8px;background-color:#4CAF50;color:white;cursor:pointer;" onclick='const urls={urls_json}; urls.forEach((url, index) => setTimeout(() => window.open(url, "_blank"), index * 200));'>
            🔗 Open All Links
        </button>
    </div>
    """
    st.components.v1.html(button_html, height=90)
    st.success("✅ Click the button above to open all links in new tabs. If nothing opens, allow pop-ups for this site.")
    
    st.markdown("---")
    
    # Create columns for a clean UI
    cols = st.columns(2)
    for i, (platform, url) in enumerate(urls.items()):
        with cols[i % 2]:
            st.link_button(f"Search on {platform}", url, use_container_width=True)

    st.info("💡 Tip: Click 'Open All Links' above to open all platforms at once!")