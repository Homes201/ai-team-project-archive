"""Streamlit view of the shared, inspectable BRT demo retrieval logic."""

import sys
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from Chatbot_Deployment_aws.llm.llm import answer_question


st.set_page_config(page_title="BRT 문서 Q&A 시연", page_icon="🚅")
st.title("BRT 문서 Q&A 시연")
st.caption("가상 문서 기반 시연입니다. 실제 회사 규정으로 사용하지 마세요.")
st.write("휴가·교육 신청을 질문해보세요. 답이 없는 질문은 보류합니다.")

question = st.text_input("질문", max_chars=500)
if st.button("답변 찾기"):
    if not question.strip():
        st.warning("질문을 입력해주세요.")
    else:
        try:
            st.write(answer_question(question.strip()))
        except Exception:
            st.error("답변을 생성하지 못했습니다. 연결과 설정을 확인해주세요.")
