'''
다 넣어보기?
안 들어가는 2개를 결정해야함
9개중 2개 선택하는 거 9C2
그 선택한 2개를 제외한 나머지 숫자들의 총합이 100이 되는가
'''
dwarfs = []
answerIndexs = []
for i in range(9):
    dwarfs.append(int(input()))
all = sum(dwarfs)

'''
# 인덱스 0~8중에서 0,1 0,2 .... 8,1 ... 8,8 -> 2개 조합
# 이중 for문
# 예외상황
:같은 인덱스를 두번 선택하는 경우 제외
:똑같은 조합이 순서만 바껴서 두번씩 들어감        
'''
for i in range(len(dwarfs)):
    for j in range(i+1, len(dwarfs)):
        remain = all-(dwarfs[i] + dwarfs[j])
        if remain == 100:
            answerIndexs.append([i, j])
indexs = answerIndexs[0]
dwarfs = [dwarfs[k] for k in range(9) if k not in indexs]
dwarfs.sort()
for d in dwarfs:
    print(d)