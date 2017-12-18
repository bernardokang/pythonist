'''

나의 욕심은
함수 구조에서
함수의 어떤 내부 펑션만 쓰고 싶다는 것이었다 그런데 그런건
예를 들어)) my_pretty_waiter.main 이런 욕심이었으나
부질없었다
차라리 리턴을 활용해서 리턴튜플에서 요거를 딱 핀셋처럼 찝어주는거야
핀셋리턴이라고 하자

'''


class Diner():
    def my_pretty_waiter(self, nudl, str, drk):
        self.main = nudl
        self.dissert = str
        self.drink = drk
        return self.main, self.dissert, self.drink

menu = Diner()


db = menu.my_pretty_waiter('spaghetti', 'choco_pie', 'cappucino')
print(db) ##리턴값 모두를 보여줌 즉, 셀프변수를 모두 연산한 거
print(db[0]) ##셀프변수 중에서 메인(맨 첨 리턴에 적어준 거 리턴)
print(db[1]) ##셀프변수 중에서 중간거
print(db[2]) ##셀프변수 중에서 마지막거만 리턴한다!!

'''
i know waitress
'''