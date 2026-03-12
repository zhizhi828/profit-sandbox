import streamlit as st
import streamlit.components.v1 as components

# 设置页面配置（为了让沙盘全屏显示）
st.set_page_config(
    page_title="门店利润沙盘",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 读取 HTML 文件内容
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 在 Streamlit 中嵌入 HTML
# 注意：height 需要根据你的内容调整，1000 左右通常能覆盖大部分显示屏
components.html(html_content, height=1200, scrolling=True)

# 移除 Streamlit 默认的多余间距（可选，优化视觉）
st.markdown("""
    <style>
    .main .block-container {
        padding: 0;
        max-width: 100%;
    }
    iframe {
        width: 100%;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)