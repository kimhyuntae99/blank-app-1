import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🧪 카탈레이스(H₂O₂ 분해) 실험 활동지")
st.write("""
**실험 목표:**
카탈레이스(간·감자 추출액)를 이용해 H₂O₂(과산화수소) 분해 반응을 관찰하고, 실험 결과를 시각화하며 소감을 작성해봅시다.
""")

st.header("1. 실험 데이터 입력")
st.write("아래 표에 실험에서 측정한 값을 입력하세요.")

default_data = {
    "시료": ["간 추출액", "감자 추출액"],
    "H₂O₂ 농도(mM)": [10, 10],
    "반응 시간(초)": [60, 60],
    "기포량(ml)": [0.0, 0.0],
}

df = pd.DataFrame(default_data)
edited_df = st.data_editor(
    df,
    num_rows="dynamic",
    use_container_width=True,
    key="exp_data"
)

st.header("2. 결과 시각화")
if len(edited_df) > 0 and pd.to_numeric(edited_df["기포량(ml)"], errors="coerce").sum() > 0:
    # 데이터 타입 변환 및 색상 배열 동적 처리
    x = edited_df["시료"].astype(str)
    y = pd.to_numeric(edited_df["기포량(ml)"], errors="coerce").fillna(0)
    colors = ["#ffb347", "#b0e0e6", "#90ee90", "#f08080", "#b19cd9"]
    fig, ax = plt.subplots()
    ax.bar(x, y, color=colors[:len(x)])
    ax.set_ylabel("기포량 (ml)")
    ax.set_title("시료별 H₂O₂ 분해 생성 기포량")
    st.pyplot(fig)
else:
    st.info("실험값을 입력하면 결과가 시각화됩니다.")

st.header("3. 실험 소감 작성")
reflection = st.text_area(
    "실험을 하며 느낀 점, 궁금한 점, 알게 된 점을 자유롭게 작성하세요.",
    height=120,
    key="reflection"
)
if st.button("소감 제출"):
    st.success("소감이 저장되었습니다! 😊")
