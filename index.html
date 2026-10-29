import streamlit as st
import re
import hashlib
import random

st.set_page_config(page_title="أداة المدافع الذكية", page_icon="⚡", layout="centered")

# تصميم الواجهة بالألوان والجماليات
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ أداة المدافع الرقمية المتكاملة")
st.write("مرحباً بك! هذا تطبيق متعدد المهام مبني بلغة بايثون ومصمم ليتحول إلى تطبيق جوال.")

# القائمة الجانبية لاختيار الأداة
option = st.sidebar.selectbox(
    "اختر الخدمة المطلوبة:",
    ("فحص قوة كلمة المرور", "استخراج الروابط من النص", "مولد النصوص والتشفير", "حاسبة رقمية سريعة")
)

st.markdown("---")

# 1. أداة فحص قوة كلمة المرور
if option == "فحص قوة كلمة المرور":
    st.subheader("🔒 فحص أمان كلمة المرور")
    password = st.text_input("أدخل كلمة المرور لفحصها:", type="password")
    
    if password:
        score = 0
        feedback = []
        
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("❌ يجب أن تكون كلمة المرور من 8 أحرف على الأقل.")
            
        if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            score += 1
        else:
            feedback.append("❌ يفضل استخدام حروف كبيرة وصغيرة.")
            
        if re.search(r"\d", password):
            score += 1
        else:
            feedback.append("❌ يفضل احتواءها على أرقام.")
            
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1
        else:
            feedback.append("❌ يفضل إضافة رموز خاصة مثل (!@#).")
            
        if score == 4:
            st.success("🟢 كلمة المرور قوية جداً وآمنة!")
        elif score >= 2:
            st.warning("🟡 كلمة المرور متوسطة، يمكنك تحسينها.")
        else:
            st.error("🔴 كلمة المرور ضعيفة جداً!")
            
        for f in feedback:
            st.write(f)

# 2. أداة استخراج الروابط
elif option == "استخراج الروابط من النص":
    st.subheader("🌐 مستخرج الروابط الذكي")
    text_input = st.text_area("ألصق أي نص طويل يحتوي على روابط هنا:")
    
    if st.button("استخراج الروابط"):
        urls = re.findall(r'https?://[^\s]+', text_input)
        if urls:
            st.success(f"تم العثور على {len(urls)} رابط:")
            for i, u in enumerate(urls, 1):
                st.markdown(f"{i}. [{u}]({u})")
        else:
            st.info("لا توجد روابط في هذا النص.")

# 3. مولد التشفير (MD5 / SHA256)
elif option == "مولد النصوص والتشفير":
    st.subheader("🔐 تشفير النصوص (Hash Generator)")
    plain_text = st.text_input("أدخل النص المراد تشفيره:")
    
    if plain_text:
        md5_hash = hashlib.md5(plain_text.encode()).hexdigest()
        sha_hash = hashlib.sha256(plain_text.encode()).hexdigest()
        
        st.write("**تشفير MD5:**")
        st.code(md5_hash)
        st.write("**تشفير SHA-256:**")
        st.code(sha_hash)

# 4. حاسبة ذكية بسيطة
elif option == "حاسبة رقمية سريعة":
    st.subheader("🔢 الحاسبة السريعة")
    col1, col2 = st.columns(2)
    with col1:
        n1 = st.number_input("الرقم الأول", value=0.0)
    with col2:
        n2 = st.number_input("الرقم الثاني", مستخدم القيمة=0.0) if 'مستخدم القيمة' in globals() else st.number_input("الرقم الثاني", value=0.0)
        
    operation = st.selectbox("العملية الحسابية:", ("جمع (+)", "طرح (-)", "ضرب (×)", "قسمة (÷)"))
    
    if st.button("احسب النتيجة"):
        if operation == "جمع (+)":
            res = n1 + n2
        elif operation == "طرح (-)":
            res = n1 - n2
        elif operation == "ضرب (×)":
            res = n1 * n2
        else:
            res = n1 / n2 if n2 != 0 else "خطأ: لا يمكن القسمة على صفر!"
        st.success(f"النتيجة: {res}")

st.markdown("---")
st.caption("تم تطوير هذه الأداة عبر بايثون لتكون جاهزة للتحويل إلى تطبيق جوال.")
