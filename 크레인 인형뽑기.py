def solution(board, moves):
    moved = []
    count = 0
    for x in moves:
        for i in range(len(board)): #board's row
            c = x-1    #choosed cul
            if board[i][c] != 0:
                got = board[i][c]
                board[i][c] = 0
                if len(moved) == 0:
                    moved.append(got)
                elif len(moved) >= 0 and got != moved[-1]:
                    moved.append(got)
                else:
                    count += 1
                    del moved[-1]
                break
    return count*2

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))