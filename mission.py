import subprocess

def ask_ollama(question):
    # Ollama CLI 명령어 실행
    command = f'ollama chat llama --system "You are a helpful AI assistant." --prompt "{question}"'
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # 결과에서 출력만 추출
    output = result.stdout.strip()
    
    # 결과 반환
    return output

# 사용자로부터 질문을 입력받기
user_question = input("Ollama에게 물어볼 질문을 입력하세요: ")

# Ollama에 질문하고 답변 받기
ollama_answer = ask_ollama(user_question)

# 답변 출력
print("Ollama의 답변:", ollama_answer)

# 답변을 파일에 저장
with open("answers.txt", "a") as file:
    file.write(f"Q: {user_question}\nA: {ollama_answer}\n\n")

print("답변이 answers.txt 파일에 저장되었습니다.")