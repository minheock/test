import random 

rn = random.randint(1,5)

gn = int(input("랜덤 숫자를 추측해주세요: "))

while gn != rn:
    if rn == gn :
        print("정답입니다.")
        break
    else :
        print(f"틀렸습니다. 정답은 {rn} 입니다.")
