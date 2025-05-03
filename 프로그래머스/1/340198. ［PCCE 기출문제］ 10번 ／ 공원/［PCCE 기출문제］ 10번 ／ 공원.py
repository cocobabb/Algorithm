def solution(mats, park):
   # 매트 사이즈를 하나 가져온다
    # 해당 매트 사이즈 만큼 공원에 크기를 대본다
    # 공원에 크기를 대봤을 때 좌표값이 전부 -1인게 있으면 가능, 아님 불가능

    # 공원에 깔 수 있는 영역 확인 함수
    def can_put(sx, sy, ex, ey):
        for i in range(sx, ex):
            for j in range(sy,ey):
                if park[i][j] != "-1":
                    return False
        return True


    mats.sort(reverse=True)
    for mat_size in mats:
        for i in range(len(park)-mat_size+1):
            for j in range(len(park[0])-mat_size+1):
                ex = i + mat_size
                ey = j + mat_size
                if can_put(i, j, ex, ey):
                    return mat_size
    return -1