# 소스코드내에 사용된 탭(Tab) 문자를 공백 4개(4 space)로 바꾸어 주는 프로그램을 작성하시오.

def tabtospace(text):
    result = text.replace("    "," ")
    return result

text = input("변환할 문자열은?")
print(tabtospace(text))
