# Fibonacci 순열"""인자로 0 또는 양의 정수인 x 가 주어질 때,Fibonacci 순열의 해당 값을 구하여 반환하는 함수 solution() 을 완성하세요.Fibonacci 순열은 아래와 같이 정의됩니다.F0 = 0F1 = 1Fn = Fn - 1 + Fn - 2, n >= 2"""# 1) Recurisive versiondef solution(x):    if x == 0:        return x    elif x == 1:        return x    else:        return solution(x - 1) + solution(x - 2)if __name__ == "__main__":    x = 5    print(solution(x))# 2) Iterative version# def Iterative(a):#     # if a < 2:#     #     return a#     ##     # for _ in range(a):#     s = 0#     while s <= a:#         s += 1### if __name__ == "__main__":#     a = 6#     print(Iterative(a))