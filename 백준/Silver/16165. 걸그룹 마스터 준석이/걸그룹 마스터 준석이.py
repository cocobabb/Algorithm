import sys
input = sys.stdin.readline

n,m = map(int, input().split())

girls = dict()
for _ in range(n):
    team = input().rstrip()
    member_counts = int(input())
    # 입력 받은 이름을 key로 팀 이름은 value로  dict에 넣기
    for _ in range(member_counts):
        name = input().rstrip()
        girls[name] = team
sorted_group = set()
for _ in range(m):
        # 팀 이름 또는 멤버 이름
        q = input().rstrip()
        # 퀴즈 타입
        # 0: 해당 팀에 속한 멤버 이름 사전순 한줄 한명 출력
        # 1: 해당 멤버가 속한 팀 이름 출력
        q_type = input().rstrip()
        if q_type == '1':
            print(girls.get(q))
        else:
            for name, team in girls.items():
                if team == q:
                    sorted_group.add(name)
            print(*sorted(sorted_group), sep="\n")
            # 다음 값을 위해 초기화 처리
            sorted_group = set()     