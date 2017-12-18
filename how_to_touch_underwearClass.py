#참좋은 예제입니다

'''

이닛 스트럭쳐 속에 있는 애는 비록 셀프가 달려도 터치가 가능해 거참
이닛과 클래쓰는 한 몸이다. 곧 삼위일체가 되나니,
클래쓰와 클래스 속 내부변수, 그리고 이닛에 심어진 셀프변수는 곧 한 몸이다

'''



class UnderWear():
    totalClothes = 0
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def whatyousee(self, utop, ubottom):
        self.inside_of_top = utop
        self.inside_of_bottom = ubottom
        return self.inside_of_top, self.inside_of_bottom

cloth = UnderWear('Tshirt', 'Skirt')

#이닛의 셀프뺀 꼬다리도 그냥 바로 써버릴수있다는 사실사실
print(cloth.top, cloth.bottom)

#속옷을 만지기 위해선 그냥은 안되지 리턴접근이 필요한 거라구
print(cloth.whatyousee('bra', 'short-pants'))
