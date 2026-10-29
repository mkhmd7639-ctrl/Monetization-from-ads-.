import streamlit as st
import hashlib
import re

st.set_page_config(page_title="تطبيق ميثاق الشامل", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    .main {background-color: #f4f4f4;}
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 45px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ أدوات ميثاق الرقمية المتكاملة")
st.write("مرحباً بك! هذا تطبيق متعدد الأدوات مبني بايثون ومصمم ليتحول إلى تطبيق جوال.")

menu = st.sidebar.selectbox("القائمة الرئيسية", ["اختر خدمة مطلوبة:", "فحص قوة كلمات المرور", "استخراج الروابط من النص", "حاسبة رقمية سريعة"])

if menu == "فحص قوة كلمات المرور":
    st.subheader("🔒 فحص أمان كلمة المرور")
    password = st.text_input("أدخل كلمة المرور لفحصها:", type="password")
    
    if password:
        score = 0
        feedback = []
        
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("❌ يجب أن تكون كلمة المرور من 8 أحرف على الأقل.")
            
        if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
            score += 1
        else:
            feedback.append("❌ يفضل استخدام حروف كبيرة وصغيرة.")
            
        if re.search(r"\d", password):
            score += 1
        else:
            feedback.append("❌ يفضل أن تحتوي على أرقام.")
            
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1
        else:
            feedback.append("❌ يفضل إضافة رموز خاصة مثل (!@#).")
            
        if score >= 4:
            st.success("🟢 كلمة المرور قوية وآمنة تماماً!")
        elif score >= 2:
            st.warning("🟡 كلمة المرور متوسطة، يمكنك تحسينها.")
        else:
            st.error("🔴 كلمة المرور ضعيفة جداً!")
            
        for f in feedback:
            st.write(f)

elif menu == "استخراج الروابط من النص":
    st.subheader("🔗 استخراج الروابط من النص")
    text_input = st.text_area("ألصق النص هنا لاستخراج الروابط الموجودة:")
    if text_input:
        urls = re.findall(r'(https?://[^\s]+)', text_input)
        if urls:
            st.success(f"تم العثور على {len(urls)} رابط:")
            for url in urls:
                st.write(url)
        else:
            st.info("لم يتم العثور على روابط في النص.")

elif menu == "حاسبة رقمية سريعة":
    st.subheader("🔢 حاسبة العمليات السريعة")
    n1 = st.number_input("الرقم الأول:", value=0.0)
    n2 = st.number_input("الرقم الثاني:", value=0.0)
    operation = st.selectbox("العملية الحسابية:", ["جمع (+)", "طرح (-)", "ضرب (×)", "قسمة (÷)"])
    
    if st.button("احسب النتيجة"):
        if operation == "جمع (+)":
            res = n1 + n2
        elif operation == "طرح (-)":
            res = n1 - n2
        elif operation == "ضرب (×)":
            res = n1 * n2
        elif operation == "قسمة (÷)":
            res = n1 / n2 if n2 != 0 else "لا يمكن القسمة على صفر!"
        st.success(f"النتيجة النهائية هي: {res}")
