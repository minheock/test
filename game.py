import random 

rn = random.randint(1,5)
# gn = -1

while gn != rn:    
    gn = int(input("랜덤 숫자를 추측해주세요: "))

    if rn == gn :
        print('정답')
    else :
        print('땡')    