# 문제
# 도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다. 이때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.

# 국어 점수가 감소하는 순서로
# 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

# 입력
# 첫째 줄에 도현이네 반의 학생의 수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 한 줄에 하나씩 각 학생의 이름, 국어, 영어, 수학 점수가 공백으로 구분해 주어진다. 
# 점수는 1보다 크거나 같고, 100보다 작거나 같은 자연수이다. 이름은 알파벳 대소문자로 이루어진 문자열이고, 길이는 10자리를 넘지 않는다.

# 출력
# 문제에 나와있는 정렬 기준으로 정렬한 후 첫째 줄부터 N개의 줄에 걸쳐 각 학생의 이름을 출력한다.

n = int(input("반 학생 수 :"))

data =[]
for i in range(n):
    data.append(input("이름 국어 영어 수학 의 형식으로 입력하세요").split())
    #print(data[i][0])

for a in range(len(data)):
    for b in range(1,4):
        data[a][b] = int(data[a][b])

for i in range(n):
    kormax = data[i][1]
    kormaxidx = i

    for j in range(i+1,n):
        if data[j][1] > kormax:
            kormax = data[j][1]
            kormaxidx = j
                
    data[i], data[kormaxidx] = data[kormaxidx], data[i]    #sort로 다시 풀어보기


for i in range(n):
    for j in range(i+1,n):
        if data[i][1] == data[j][1]:
            if data[i][2] > data[j][2]:
                data[i], data[j] = data[j],data[i]
            elif data[i][2] == data[j][2]:
                if data[i][3] < data[j][3]:
                    data[i], data[j] = data[j],data[i]


for i in range(n):
    print(data[i][0])


#print(data)
