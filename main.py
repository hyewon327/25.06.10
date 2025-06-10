import streamlit as st
st.title("나의 첫 app")
st. write("hello")
name=st.text_input("이름입력") 
if name:
  if name=="이혜원"
  st.success("반갑습니다. 이혜원님!")
else:
  st.warning("누구세요?")
