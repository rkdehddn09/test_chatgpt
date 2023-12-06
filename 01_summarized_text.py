import streamlit as st
import openai

#챗지피티에게 글 요약을 요청하는 함수
def askGPT(prompt, apiKey):
    client = openai.OpenAI(api_key=apiKey)
    response=client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'user', 'content':prompt}
        ]
    )
    #회신 메세지
    finalResponse = response.choices[0].message.content
    return finalResponse


#Main 함수
def main():
    #웹페이지 타이틀
    st.set_page_config(
        page_title='요약 프로그램'
    )

    #세션 상태 초기화 (추후 Streamlit을 사용할 때, Refresh가 되더라도 값이 남아있게하기 위해서 세션 사용)
    ## st.session_state 변수 내부에 "OPENAI_API"가 포함되어 있는지 확인
    ## st.session_state: Dictionary 형태
    if "OPENAI_API" not in st.session_state:
        st.session_state['OPENAI_API'] = ''

    
    with st.sidebar:
        open_apiKey=st.text_input(
            label='OPEN API 키',
            placeholder='Enter your api key'
        )

        if open_apiKey:
            st.session_state['OPENAI_API'] = open_apiKey

        st.markdown('---')

    st.header(':scroll:요약 프로그램:scroll:')
    st.markdown('---')

    text = st.text_area('요약 할 글을 입력하세요.')
    if st.button('요약'):
        prompt = f'''
        ***Instructions**
    - You are an expert assistant that summarizes text into **Korean language**
    - Your task is to Summarize the **text** sentences in ** Korean language**.
    - Yout summaries should include the following:
        - Omit duplicate content, but increase the summary weight of duplicate content.
        - Summarize by emphasizing concepts and arguments rather than case evidence.
        - Summarize in 3 lines.
        - Use the format of a bullet point.
    -text: {text}
    '''
        st.info(askGPT(prompt, st.session_state['OPENAI_API']))

## python c.py 실행 --> __name__는 '__main__'으로 지정 됨.
if __name__ == "__main__":
    main()