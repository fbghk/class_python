import requests
import json

def save_to_markdown(question, answer, filename='questions_answers.md'):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"**질문:** {question}\n\n")
        file.write(f"**답변:** {answer}\n\n")
        file.write("---\n\n")

while True:
    prompt = input("You: ")

    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama3.1",
        "messages": [
            {
                "role": "system",
                "content": "친구에게 말하듯이 사근사근하게 반말을 이용한 한국말로 설명해줘"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }

    json_data = json.dumps(data)

    response = requests.post(url, headers=headers, data=json_data)

    if response.status_code == 200:
        response_data = json.loads(response.content.decode())
        answer = response_data['message']['content']
        print(answer)
        save_to_markdown(prompt, answer)
    else:
        print(f"API 호출 실패: {response.status_code}")

