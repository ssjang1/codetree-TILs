secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class mission:
    def __init__(self, secret_code, meeting_point, time):
        self.s= secret_code
        self.m= meeting_point
        self.t= time

    def detail(self):
        print(f'secret code : {self.s}')
        print(f'meeting point : {self.m}')
        print(f'time : {self.t}')

today = mission(secret_code,meeting_point,time)
today.detail()