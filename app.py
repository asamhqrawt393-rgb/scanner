import streamlit as st
import requests

st.title("🛡️ درع الفحص الأمني")
url = st.text_input("ضع رابط الموقع هنا:")

if st.button("افحص الآن"):
    if url:
        try:
            if not url.startswith('http'): url = 'https://' + url
            r = requests.get(url, timeout=5)
            st.success(f"✅ الموقع يعمل! الكود: {r.status_code}")
        except:
            st.error("❌ تعذر الوصول للموقع.")
