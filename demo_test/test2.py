def solution(a, b):    answer = a + b    # for a in range(a):    for i in range(b):        print('*' * a)        # for b in range(b):        #     print('*' * a)        #     print('*' * b)    return answerif __name__ == "__main__":    a, b = map(int, input().strip().split())    print(solution(a, b))