import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("streamlit ")
st.write("dataframe")

Image.open("IMG_1559.JPG")

'Start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Itertation{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Completed'

left_column ,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('文字表示')

expander = st.expander('といあわせ')
expander.write('問い合わせ内容')


condition = st.slider('今の真直度は？',0,100,50)
st.write('進捗度:',condition)
option = st.text_input('あなたの趣味は？')
'あなたの趣味は',option,'です'

option = st.selectbox(
    '好きな数字を選択してください',
    list(range(1,11)),
)
'好きな数字は、',option, 'です'
# if st.checkbox("Show image"):
#     img = Image.open("IMG_1559.JPG")
#     st.image(img, caption = 'mizuki',use_column_width=True)
