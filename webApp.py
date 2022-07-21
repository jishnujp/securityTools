from pwdleak import searchPublicPasswords as search
import streamlit as st


st.title('Check Password Leaks')
st.write("""
This app cross checks your password with the already leaked and publically available passwords set,
 without compormising yours, using k anonimity model. 

""")
st.write("### Why is it important?")
st.write("""
We have a tendency to reuse passwords or use common and easy to remember passwords. So it is a good idea to verify that our password is not already exposed during any data breach. If we are using already exposed passwords, then you are facing a huge risk of compromising your account to a simple dictionary attack.We have a tendency to reuse passwords or use common and easy to remember passwords. So it is a good
idea to verify that our password is not already exposed during any data breach. If we are using already exposed 
passwords, then you are facing a huge risk of compormsing your account to a simple dictinary attack.
""")
st.write("#### Enter your password here to check")
p= st.text_input(" Password: ")
count = search(p)
if count == 0 and p!='':
    st.write("**Result:** Your Password is safe.")
elif count >0:
    st.write(f"**Result:** DONT use this password, it has been leaked {count} times.")

st.markdown("""
<style>
.footer {
    font-size:10px;
}
</style>
""", unsafe_allow_html=True)
st.markdown('''
<p class="footer"> 
<em>Thanks to Troy Hunt and his hardwork for maintaining the database of leaked passwords and his api which supports k anonimity model.
This project is powered by haveibeenpwned.com API</em>
</p>

''', unsafe_allow_html=True)
