import streamlit as st
from pathlib import Path

PASSWORD = "arabicgrade2025"
TEMPLATE_PATH = Path("templates/arabic_grade_protected_backup_ADVANCED_v8.html")

st.set_page_config(page_title="دفتر متابعة اللغة العربية", page_icon="📖", layout="wide")

# حماية بكلمة مرور
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    pw = st.text_input("أدخل كلمة المرور:", type="password")
    if pw == PASSWORD:
        st.session_state.authenticated = True
        st.experimental_rerun()
    elif pw:
        st.error("كلمة المرور غير صحيحة!")
    st.stop()

st.title("📖 دفتر متابعة اللغة العربية - الأستاذ إبراهيم أحمد متاش")

st.markdown(
    """
    <div style="direction:rtl; text-align:right; font-size:17px; color:#14563e;">
    مرحبًا بك في تطبيق دفتر المتابعة الإلكتروني!<br>
    يمكنك تحميل النموذج التفاعلي لاستخدامه محليًا أو مشاركة رابط التطبيق مع طلابك وزملائك.<br>
    <b>جميع الحقوق محفوظة للأستاذ إبراهيم أحمد متاش.</b>
    </div>
    """,
    unsafe_allow_html=True
)

# تحميل النموذج HTML
if TEMPLATE_PATH.exists():
    with open(TEMPLATE_PATH, "rb") as file:
        st.download_button(
            label="⬇️ تحميل نموذج الدفتر (HTML تفاعلي)",
            data=file,
            file_name="arabic_grade_protected_backup_ADVANCED_v8.html",
            mime="text/html"
        )
else:
    st.warning("ملف النموذج غير موجود! تأكد من رفعه في مجلد templates.")

st.divider()

# (اختياري) يمكنك إضافة أدوات تحليل أو رفع ملفات Excel/Backup هنا لاحقا
st.info("يمكنك لاحقًا إضافة أدوات لمعالجة البيانات أو رفع النسخ الاحتياطية من الدفتر هنا.")

st.markdown(
    """
    <hr>
    <div style="font-size:13px;color:#888;text-align:center;">
    جميع الحقوق محفوظة © للأستاذ إبراهيم أحمد متاش - لا يجوز إعادة النشر أو التعديل إلا بإذن خطي.
    </div>
    """,
    unsafe_allow_html=True
)