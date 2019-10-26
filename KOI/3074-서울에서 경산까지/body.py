import tools
from time import time

class Main():
    def __init__(self, data):
        self.value = data
        self.makeValue()

    def makeValue(self):
        self.loop, self.maxTime = self.value[:2]
        self.data = {}
        self.iterTable = ['walk','bike']
        temp = self.value[2]

        for n in range(self.loop):
            self.data[n] = {}
            self.data[n]['walk'] = temp[n][0:2]
            self.data[n]['bike'] = temp[n][2:4]

        '''
        self.loop       구간 개수
        self.maxTime    걸리는 시간 제한
        self.data       데이터 딕셔너리
            [key]['walk']
            [key]['bike']
        '''

        return  # 빈 값 반환

    def seek(self):
        make = {}
        table = tools.get(self.loop) # 경우의 수를 모두 구하여 키를 만듬

        for val in table: # 여기서 모든 경우의 수를 다 구한다
            make[val] = {"time":0, "money":0}
            for n in range(len(val)):
                make[val]["time"] += self.data[n][self.iterTable[int(val[n])]][0]
                make[val]["money"] += self.data[n][self.iterTable[int(val[n])]][1]

        temp = []
        for key in make.keys():
            #print(n, "OVER" if make[n]['time'] > self.maxTime else make[n]['time'])
            if make[key]['time'] <= self.maxTime:
                temp.append([key, make[key]["money"]])

        return max(temp, key=lambda x: x[1])[1]



# TODO: 입력값수동지정 가능

count, maxValue = [ int(x) for x in input().split(" ") ]
temp = [ [ int(x) for x in input().split(" ")] for n in range(count) ]


start = time()
_d = Main([count, maxValue, temp ])
'''
# 테스트케이스를 직접 입력
_d = Main([3, 1650, [[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]]])
'''
data = _d.seek()
end = time() - start
print(data, end)