import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="نتائج الشهادة الإعدادية", page_icon="🎓")

st.title("🎓 نظام استعلام نتائج الشهادة الإعدادية")
st.write("قم برفع ملف الإكسيل ثم ادخل رقم الجلوس للاستعلام")

# رفع ملف الإكسيل
uploaded_file = st.file_uploader("اختر ملف الإكسيل (Excel)", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        # قراءة البيانات
        df = pd.read_excel(uploaded_file)
        
        # التأكد من تنظيف البيانات (إزالة الفراغات من أسماء الأعمدة)
        df.columns = [str(col).strip() for col in df.columns]
        
        st.success("تم رفع الملف بنجاح!")
        
        # واجهة الاستعلام
        with st.container():
            seat_number = st.text_input("أدخل رقم الجلوس:")
            
            if seat_number:
                # البحث عن رقم الجلوس (تحويل العمود لنص للمطابقة الصحيحة)
                # افترضنا هنا أن اسم العمود هو "رقم الجلوس"
                column_name = "رقم الجلوس" 
                
                if column_name in df.columns:
                    # البحث عن النتيجة
                    result = df[df[column_name].astype(str) == seat_number.strip()]
                    
                    if not result.empty:
                        st.balloons()
                        
                        # عرض البيانات في جدول منسق
                        st.table(result.T)
                    else:
                        st.error("عذراً، رقم الجلوس غير موجود.")
                else:
                    st.warning(f"لم يتم العثور على عمود باسم '{column_name}' في الملف.")
                    st.info(f"الأعمدة المتاحة هي: {', '.join(df.columns)}")

    except Exception as e:
        st.error(f"حدث خطأ أثناء معالجة الملف: {e}")
