
"""
이쁜여자로 보는 로직연습
    pretty    mind
    T         T      : marry me
    T         F      : just kiss me
    F         F      : 당장 도락가!!
    F         T      : 너는 내 뻐끔이


else는 일단 어렵고 하니 elif로 일단 쓴다
elif로 다 구성해보고, 그리고 else로 간결화 작업을 하는 것이군!!
그리고 리턴은 함부로 달면 큰일나, 터미네이터란말이지 터미네이터는 가능한 멀리 집어던져야 한다!!
리턴은 프린트(함수()) 에 하면 나타나기 때문이기 야끼야끼

"""



girl = input("첫인상이 어떤가")
mind = input("마음씨는??")



def whatgirl():
    if girl == 'pretty':
        if mind == 'good':
            return "결혼해여"
        elif mind != 'good':
            return "just kiss me"



    elif girl != 'pretty':
        if mind == 'good':
            return "너는 내 뻐끔이"
        elif mind != 'good':
            return "당장 도락가!!!"

    return "누구냐 넌, 진짜 누구냐 넌"

if __name__ == '__main__':
    print(whatgirl())


#일단 엘리프로 꾸민다으메
#간지나보이게 나중에 else로 바꿔버린다

