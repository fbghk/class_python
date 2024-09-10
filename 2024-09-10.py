# test = input("입력란 :")
# test_type = type(test)
# print(test_type)
# def print_type(test_type):
#     print(f" {test_type} 입니다.")
    # print(type({test}))
    # print("입니다.")

# print_type(test_type)


# print(type(3))


# def print_type(value):
#     try:
#         # 입력값을 정수로 변환 시도
#         value = int(value)
#         print("입력값은 정수입니다.")
#     except ValueError:
#         try:
#             # 입력값을 실수로 변환 시도
#             value = float(value)
#             print("입력값은 실수입니다.")
#         except ValueError:
#             print("입력값은 문자열입니다.")

# # 사용자 입력받기
# test = input("입력란: ")

# # 입력값의 타입 출력
# print_type(test)

import ast

def print_type(value):
    try:
        # 입력값을 파이썬 객체로 변환
        value = ast.literal_eval(value)
        print(f"입력값은 {type(value)}입니다.")
    except (ValueError, SyntaxError):
        # 변환할 수 없으면 문자열로 판단
        print("입력값은 문자열입니다.")

# 사용자 입력받기
test = input("입력란: ")

# 입력값의 타입 출력
print_type(test)