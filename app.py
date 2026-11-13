import random
import streamlit as st
from number_utils import load_best, save_best

# 새 게임 준비 (session_state에 값 저장)
def new_game():
    st.session_state.answer = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.msg = '1~100 사이의 수를 맞혀 보세요!'
    st.session_state.done = False

if 'answer' not in st.session_state:
    new_game()

# 화면 그리기
st.title('★ 숫자 맞히기 게임')
best = load_best('best.txt')
if best == 0:
    st.write('아직 최고 기록이 없습니다.')
else:
    st.write(f'현재 최고 기록: {best}번')

guess = st.number_input('1~100 사이의 수', min_value=1, max_value=100, step=1)

# [확인] 버튼 판정 로직
if st.button('확인', disabled=st.session_state.done):
    st.session_state.tries += 1
    answer = st.session_state.answer
    if guess < answer:
        st.session_state.msg = f'{guess} → UP! 더 큰 수예요.'
    elif guess > answer:
        st.session_state.msg = f'{guess} → DOWN! 더 작은 수예요.'
    else:
        tries = st.session_state.tries
        st.session_state.msg = f'정답! {tries}번 만에 맞혔습니다.'
        st.session_state.done = True
        if best == 0 or tries < best:
            save_best('best.txt', tries)
            st.session_state.msg += ' 최고 기록 갱신!'
    st.rerun()

# 결과 표시
st.info(st.session_state.msg)
st.write(f'시도 횟수: {st.session_state.tries}번')

if st.session_state.done:
    st.balloons()
    if st.button('새 게임'):
        new_game()
        st.rerun()