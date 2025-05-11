def solution(board):
    # danger_zone(8방향)
    # 좌, 우, 상, 하, 좌하, 좌상, 우하, 우상
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]  
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    n = len(board)

    # 지뢰 위치 담기
    ping = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                ping.append([i,j])

    # 위험 지역 표시하기기
    for x, y in ping:
        # 반복 도는 것은 최대 위험 지역 갯수인 8로 잡아서 모든 경우의 수 잡기
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # danger_zone 1로 표시
            # x와 y가 겹치는 범위 부분 때문에 n번째는 범위에 포함x
            if 0 <= nx <n and 0 <= ny < n:
                board[nx][ny] = 1

    # 안전지대 갯수 세기
    safe_zone = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] ==  0:
                safe_zone += 1
    
    return safe_zone
