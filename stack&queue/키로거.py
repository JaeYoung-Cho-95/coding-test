"""
문제
창영이는 강산이의 비밀번호를 훔치기 위해서 강산이가 사용하는 컴퓨터에 키로거를 설치했다. 며칠을 기다린 끝에 창영이는 강산이가 비밀번호 창에 입력하는 글자를 얻어냈다.

키로거는 사용자가 키보드를 누른 명령을 모두 기록한다. 따라서, 강산이가 비밀번호를 입력할 때, 화살표나 백스페이스를 입력해도 정확한 비밀번호를 알아낼 수 있다. 

강산이가 비밀번호 창에서 입력한 키가 주어졌을 때, 강산이의 비밀번호를 알아내는 프로그램을 작성하시오. 강산이는 키보드로 입력한 키는 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표이다.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한줄로 이루어져 있고, 강산이가 입력한 순서대로 길이가 L인 문자열이 주어진다. (1 ≤ L ≤ 1,000,000) 강산이가 백스페이스를 입력했다면, '-'가 주어진다. 이때 커서의 바로 앞에 글자가 존재한다면, 그 글자를 지운다. 화살표의 입력은 '<'와 '>'로 주어진다. 이때는 커서의 위치를 움직일 수 있다면, 왼쪽 또는 오른쪽으로 1만큼 움직인다. 나머지 문자는 비밀번호의 일부이다. 물론, 나중에 백스페이스를 통해서 지울 수는 있다. 만약 커서의 위치가 줄의 마지막이 아니라면, 커서 및 커서 오른쪽에 있는 모든 문자는 오른쪽으로 한 칸 이동한다.

출력
각 테스트 케이스에 대해서, 강산이의 비밀번호를 출력한다. 비밀번호의 길이는 항상 0보다 크다.
"""


# 두 개의 큐를 생성한다.
# index 를 관리한다.
# index 를 중심으로 left_data 에 담을지, right_data 에 담을지 정해놓는다.
# > 가 나오면 index 를 기준으로 left_data 에 있는 데이터에서 하나를 right_data 로 담는다.
# < 가 나오면 index 를 기준으로 right_data 에 있는 데이터에서 하나를 left_data 로 담는다.
# - 가 나오면 left_data 에서 Pop 을 해준다.


from collections import deque
import sys

input = sys.stdin.readline


for _ in range(int(input().strip())):
    data = input().strip()
    
    left_data = deque()
    right_data = deque()
    
    for i in data:
        if i == "<":
            if len(left_data) > 0: 
                right_data.appendleft(left_data.pop())
        
        elif i == ">":
            if len(right_data) > 0:
                left_data.append(right_data.popleft())
        
        elif i == "-":
            if len(left_data) != 0:
                left_data.pop()
            
        else:
            left_data.append(i)
    
    print("".join(left_data + right_data))