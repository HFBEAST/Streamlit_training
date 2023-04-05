import time
from PIL import Image
import pandas as pd
import streamlit as st
import numpy as np

left_column, colum, right_column = st.columns(3)
button = left_column.button('asdfasdf')
if button :
    right_column.write('223333')
    colum.write('58888')

expander = st.expander('ーーーーーーー')
expander.write('11111')
expander.write('1122222')


st.title('Stramlit Sample')

st.write('DataFrame')

df = pd.DataFrame({
        '12323': [1,3,4],
        '2433t': [2,8,4]
    })
# size 設定できない
#st.write(df, width=100, height=500)
# size 設定でき
st.dataframe(df, width=500, height=100)
# 最大値の色付け
st.dataframe(df.style.highlight_max(axis=0))
# 最小値の色付け
#st.dataframe(df.style.highlight_min(axis=0))
# 編集できないフレーム
#st.table(df.style.highlight_min(axis=0))

' !!!!!!!!! '
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'interation {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

# マジックコマンド
"""
# 章
## 節
### 項

```python
    st.title('Stramlit Sample')
```
"""

# チャート Chart
assd = pd.DataFrame(
    np.random.rand(5,2),
    columns=['a','b']
)
st.line_chart(assd)
#st.area_chart(assd)
#st.bar_chart(assd)

# 地图实时反应
yyy = pd.DataFrame(
    np.random.rand(100,2),
    columns=['lat','lon']
)
st.map(yyy)

# 照片的写入

if st.checkbox('show image 2333'):
    img = Image.open('2052882.jpg')
    st.image(img, caption='23333', use_column_width=True)

option = st.selectbox(
    '233333333',
    list(range(1, 11))
)

'sdfgsdfgsdfg', option, 'asdgfasdf'

text = st.text_input(
    '233333333',
    list(range(1, 11))
)
'23333333333333', text, 'asdg'

point1 = st.slider('sdfgerg',2,54,34)
point2 = st.sidebar.slider('sdfgerg',2,899,233)
point1,point2