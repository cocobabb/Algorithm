def solution(n):
    # 하, 우, 좌상
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    x, y = -1, 0  # 초기 위치
    i = 0  # 방향
    mark = 1  # 마킹할 초기 숫자
    
    board = [[0] * n for _ in range(n)]  # 삼각 달팽이 보드 초기화
    
    # n개부터 1개까지 연속으로 작성
    for counts in range(n, 0, -1):
        for _ in range(counts):
            # 일단 이동 후
            x += dx[i]
            y += dy[i]
            
            board[x][y] = mark  # 마킹
            mark += 1  # 마킹 숫자 증가
        
        i = (i + 1) % 3  # 방향 이동 (델타값의 인덱스가 길이를 초과할 수 있어서 나머지 연산 사용)
    
    # 결과 담기
    result = []
    
    for line in board:
        for number in line:
            if number > 0:
                result.append(number)
    
    
    return result