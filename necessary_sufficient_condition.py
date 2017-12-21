

"""
necessary condition and sufficient condition::
calculate which condition is necessary for, and sufficient for
디베이트의 영역인 것이지 --왜 그렇게 생각하는지가 중요한거야, 딱 딱 이게 그거고 이게 그거고 그런게 아니라
테크닉은
자체만으로도 되는지(아니면 다른 조건이필요한지 -1)
없으도 가능한지-2

"""



A = input("\n관계를 알고 싶은 첫번째 단어를 입력해\n")
B = input("\n그리고 두번째 단어를 입력해\n")

fset = [ A, B ]


C = input("\n""'"+str(A)+"'""이거 자체만으로도 ""'"+str(B)+"'""이(가) 될까(=*be/has) 생각해봐""\n "" 혹시 또 다른 extra 조건(*혹은 가능한 case)이 필요해?(*=존재해?)\n")

if C == 'no':
    print("'"+str(A)+"'"+"(은)는 ""'"+str(B)+"'""의 sufficient condition")
    print("'"+str(A)+"'""--->""'"+str(B)+"'")

elif C == 'yes':
    fset.reverse()
    # print(fset)
    D = input(  "\n""'"+str(fset[1])+"'""없이도""'"+str(fset[0])+"'""가능해?""\n")
    if D == 'no':
        print("\n"+str(fset[1])+"is necessary condition for "+str(fset[0]))
        print("'" + str(fset[0]) + "'""--->""'" + str(fset[1]) + "'")
        print("잘 이해 안되면 has로 생각해")

    elif D == 'yes':
        print("이런! ""'" + str(fset[0]) + "'""과  ""'" + str(fset[1]) + "'""은 관계가 없구나")



