# 문자열 다루기 기본def solution(s):    if len(s) == 4 or len(s) == 6:        try:            int(s)        except ValueError:            return False        else:            return True    else:        return Falseif __name__ == "__main__":    s = '1234a'    print(solution(s))