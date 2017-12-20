
"""
군대 입영과 탈영으로 살펴보는 내 클래쓰 마을
입영하면 한명이 추가되고 집도 하나 준다(개꿀)
근데도 탈영하기 시작했다


이 경우, my = self가 되는데
그렇지 않을 경우는 뭐가 있을까

"""


class MyCastle():

#이 애들은 내가 프로그램을 종료할때까지만 살아있고 프로그램을 다시키면 리셋된다(램 메모리에 저장되는 듯! 휘발..)


#클래쓰변수 : 얘들을 다루는 법은 그냥 무턱대고 soldier!이렇게 부르면 안온다
#누구 부대인지 알아야온다고 그건 내 부대니까 my.soldier 이렇게 부르면 된다(인스턴스 솔져)
#혹은 self를 써도 됨 오나전똑같음 self.soldier 셀프솔져 이리온ㅋㅋ 좀 이상하긴 함 아무튼 이렇게 부르면 옴
#명령으로 써줄 땐 반드시 my.soldier이렇게 써야하고 서술격으로 쓸 땐 둘이 암꺼나 써두 되는 것 같다.

    soldier = 100
    archer = 1
    elf = 20
    housing  = 1000


    def newSoldier(self):
        my.soldier += 1
        print("한 녀석이 입영 했습니당")

    def runSoldier(self):
        self.soldier -= 1
        print("근데도 한 녀석이 탈영 했습니당")

    def showHouses(self):
        print(my.housing)
        print(self.housing)

    def rooms(self):
        room = my.housing - (my.elf + my.archer + self.soldier)
        print(str(room)+"하우징이 남았읍니다")
        return room

    def girlcrush(self):
        while my.soldier-self.elf >1:
            my.soldier -= 10
            print("쏠져 열명이 탈영합니다 여자에게 차였읍니다")
            print("남은 쏠져는"+str(my.soldier))
        else:
            print("happy end!")


my = MyCastle()
my.girlcrush()
my.rooms()
my.runSoldier()
print(my.soldier)
