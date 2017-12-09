def input():
    return int(raw_input())

def dice2(n):
    answer = []
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == n:
                answer.append([i, j])
    if len(answer) % 2 == 0:
        range_answer = len(answer) // 2
    else:
        range_answer = len(answer) // 2 + 1
    for i in range(range_answer):
        for j in range(2):
            #print ', '.join(answer[i])
            print answer[i][j],
        print ''


def main():
    n = input()
    dice2(n)


main()
