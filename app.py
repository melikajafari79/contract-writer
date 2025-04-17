import streamlit as st
import openai
import os

# کلید API از محیط امن خوانده می‌شود
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("📝 تولید قرارداد هوشمند (فارسی)")

st.markdown("لطفاً اطلاعات قرارداد را وارد کنید:")

# فرم گرفتن اطلاعات از کاربر
with st.form("contract_form"):
    طرف_اول = st.text_input("نام طرف اول")
    طرف_دوم = st.text_input("نام طرف دوم")
    موضوع = st.text_area("موضوع قرارداد")
    مدت = st.text_input("مدت قرارداد (مثلاً: یک سال)")
    مبلغ = st.text_input("مبلغ قرارداد (مثلاً: ۱۰ میلیون تومان)")
    شرایط_فسخ = st.text_area("شرایط فسخ قرارداد", value="در صورت تخلف هر یک از طرفین...")
    
    submitted = st.form_submit_button("تولید قرارداد")

if submitted:
    with st.spinner("در حال تولید قرارداد..."):
        prompt = f"""
        یک قرارداد رسمی و حقوقی به زبان فارسی بنویس. اطلاعات زیر را استفاده کن:
        طرف اول: {طرف_اول}
        طرف دوم: {طرف_دوم}
        موضوع قرارداد: {موضوع}
        مدت: {مدت}
        مبلغ: {مبلغ}
        شرایط فسخ: {شرایط_فسخ}
        
        متن قرارداد را به زبان رسمی و کامل بنویس.
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
        )
        contract_text = response["choices"][0]["message"]["content"]
        st.success("قرارداد با موفقیت تولید شد!")
        st.text_area("🧾 متن قرارداد:", contract_text, height=400)
