### 자료구조 공부
기본 문법 <br>
문자열 (str) "Hi" <br>
리스트 (list) [1,2,3,4] <br>
사전 (dict) {'a':1,'b':2} <br>
순서쌍 (tuple), 집합 (set), ... <br>

### 알고리즘
해결하고자 하는 문제에 따라 최적의 해법은 다르므로<br> 
여러가지 선택에 따라 자료구조를 이해해야함

=== 연습 ===<br>
* 배열(list)원소의 합 - solution.py<br>
* 선형 배열(Linear Array)<br>
```text
데이터가 선의 모습으로 줄지어 늘어져 있다고 해서 선형 배열이라고 한다.
배열 - 원소들을 순서대로 늘어놓은 것
        2 , 7 , -2 , 5 , 10
index   0   1    2   3   4
0부터 시작한다.
python에서는 배열 대신 list로 쓰인다.
.append()를 이용해 마지막부분에 덧붙일 수 있다.(삽입)
.pop()은 반대로 끝에서 하나의 원소를 꺼낸다.(삭제)

순식간에 (빠르게) 할 수 있는 일 
-> 리스트의 길이와 무관(상수 시간) -> O(1) _빅오 표기법이라 함.

중간에 원소를 삽입하는 방법
li = [20, 30, 55, 70]
li.insert(2, 46)
30뒷자리에 46을 넣을 수 있게 된다.

원소 삭제 방법
del(li[2]) -> li[2]인 30을 삭제 하고 index를 하나씩 앞당긴다.
* del() -> 특정 인덱스에서 항목을 제거
계산 복잡성 -> O(n-1)
* pop() -> 특정 인덱스에 있는 항목을 삭제 해 돌려준다.
계산 복잡성 -> O(n-1)
* remove() -> 특정 색인이 아닌 처음으로 일치하는 값을 remove 제거함.
계산 복잡성 -> O(n)

※ del인덱스를 기준으로 pop()으로 인해 요소를 제거하고,
반환값이 필요할 경우 인덱스를 사용하여 제거하고,
값이 remove() 기준으로 요소를 삭제할 때 사용함.

* 참고
리스트의 길이가 길면 오래 걸리는 일
-> 리스트의 길이에 비례(선형시간)

```
  - 리스트에 새로운 요소 삽입 - Linear Array_1.py
  - 리스트에서 원소 찾아내기  - Linear Array_2.py

* sort_정렬 / search_탐색
  - sort 말 그대로 정렬 차례대로 배열하여 정렬 시켜준다.(오름차순)
  1. sorted()
     * 내장 함수
     * 정렬된 새로운 리스트를 얻어낸다.
  2. sort()
     * 리스트의 메서드(method)
     * 해당 리스트를 정렬함 
  - 내림차순으로 정렬 하고 싶을땐 reverse = True 를 써주면 된다.
  
  - 문자열을 정렬 하고 싶을때는 알파벳순서를 따라 정렬이된다.
  - 문자열 길이 순서로 정렬하려면? -> 정렬에 이용하는 키(key)를 지정할 수 있다.
  
  * Lambda식에 대해
    * 익명함수 : 메모리를 아끼고 가독성을 향상 시킨다.
    * 익명함수이기 때문에 한번 쓰이고 다음줄로 넘어가면 힙 메모리 영역에서 증발
*****
#### 이진탐색
```text
# 탐색 알고리즘 1 - 선형탐색(Linear Search)
- 순차적으로 하나하나 비교해나가며 원하는 리스트를 찾는것
리스트의 길이를 비례하는 시간 요소 -> O(n)
* 최악의 경우 : 모든 원소를 다 비교해 보아야함

# 탐색 알고리즘 2 - 이진탐색(Binary Search)
- 탐색 하려는 리스트가 이미 정렬되어 있는 경우에만 적용 가능
- 크기 순으로 정렬되어 있다는 성질을 이용함

- 한 번 비교가 일어날 때마다 리스트 반씩 줄임 (divide & conquer) -> O(log n)

```
이진탐색 - Binary_Search.py
*****
#### 재귀 알고리즘 - 기초
(Recursive Algorithms)

재귀 함수란? <br>
하나의 함수에서 자신을 다시 호출하여 작업을 수행하는 것<br>
ex) 이진 트리(binary trees)<br>
* 간단한 예 - 자연수의 합 구하기 <br>
1부터 n까지 모든 자연수의 합 구하기 <br>
```python
# 재귀를 쓴 코드 (Recursive version)
def sum(num):
    if num <= 1:
        return num
    else:
        return num + sum(num-1)

a = int(input('number : '))
print(sum(a))
# 재귀함수에서는 종결 조건이 매우 중요하다


# 재귀를 안쓴 코드 (Iterative version)
def a(n):
    s = 0
    while n>=0:
        s += n
        n -= 1
    return s
    
# 추가 예제 (펙토리얼)
def what(n):
    if n <= 1:
        return 1
    else:
        return n * what(n-1)

```
연습 문제 <br>
-Fibonacci 순열 <br>
F(0) = 0 <br>
F(1) = 1 <br>
F(n) = F(n-1)+F(n-2), n >= 2<br>

0,1,1,2,3,5,8,12 <br>

Iterative version / Recursive version 으로 작성 해보기 <br>
*****
#### 재귀함수 -응용-

재귀함수가 어쩔땐 비효율적이나 꼭 재귀를 써야하는 상황에서는 interative한 함수보다 성능이 더 좋다.<br>
재귀적인 방법의 문제<br>
문제 : n개의 서로 다른 원소에서 m개를 택하는 경우의 수 <br>

```python
#[연습문제]
#* 재귀적 이진 탐색
# L->원소가 담겨있는 List
# x -> 찾을 원소의 값
# lower -> 왼쪽값
# upper -> 오른쪽값

def function(L, x, lower, upper):
    if lower > upper:
        return -1
    mid = (lower + upper) // 2
    if x == L[mid]:
        return mid
    # 재귀적 함수로 구현
    elif x < L[mid]:
        return function(L,x,lower,mid-1)
    else:
        return function(L,x,mid+1,upper)
# 풀이

# 첫번째 if는 값이 없을경우 반환하는 구문이다.
# lower와 upper중 upper는 항상 lower보다 커야하는데, 내가 찾는 값이 없을경우
# upper가 lower보다 낮아지므로 lower > upper가 되면 반환이 되게 하는것이 맞다.
# 또한 시간적으로도 단축되는 효율성이 있는 부분이다.

# 두번째 위 문제는 이진트리이지만 재귀함수를 넣어서 풀었으므로 기본적인 방식으로 구현해볼 수 있다.
```
*****
#### 알고리즘의 복잡도

* 시간 복잡도(Time Complexity)
  * 문제의 크기와 이를 해결하는데 걸리는 시간 사이의 관계
* 공간 복잡도(Space Complexity)
  * 문제의 크기와 이를 해결하는데 필요한 메모리 공간 사이의 관계 

```text도
시간 복잡도에서는..
평균 시간 복잡도 - 임의의 입력 패턴을 가정했을 때 소요되는 시간의 평균

최악 시간 복잡도 - 가장 긴 시간을 소요하게 만드는 입력에 따라 소요되는 시간
```
* Big-O Notation
  * 점근 표기법(asymptotic notation)의 하나
  * 어떤 함수의 증가 양상을 다른 함수와의 비교로 표현(알고리즘의 복잡도를 표현하때 쓰인다.)
O(logn), O(n), O(n^2), O(2^n)등으로 표기할수 있다. <br>

* 선형 시간 알고리즘 - O(n)
ex) n개의 무작위로 나열된 수에서 최댓값을 찾기 위해 선형 탐색 알고리즘을 적용<br>
최댓값 - 끝까지 다 살펴 보기 전까지는 알 수 없다.<br>

* 로그 시간 알고리즘 - O(logn)
ex) n개의 크기 순으로 정렬된 수에서 특정 값을 찾기위해 이진 탐색 알고리즘을 적용<br>

* 이차 시간 알고리즘 - O(n^2)
  * 삽입 정렬(insertion sort)
  * 정렬 알고리즘이다.
  
* 낮은 복잡도를 가지는 정렬 알고리즘
  * 병합 정렬(merge sort) - O(n logn)
  * 정렬할 데이터를 반씩 나누어 각각을 정렬시킨다.(divide & conquer) -> O(logn)

*****
#### 연결리스트(Linked Lists)
* 추상적 자료구조 (Abstract Data Structures)
  * 내부적으로 숨겨둔 데이터
  * Data
    * ex) 정수, 문자열, 레코드
  * A set of operations
  * A set of operations
    * 삽입, 삭제, 순회
    * 정렬, 탐색, ...
    
```text
Node
- Data
- Link(next)

제일 처음 데이터를 Head / 제일 마지막 데이터를 Tail 이라고 한다.
```