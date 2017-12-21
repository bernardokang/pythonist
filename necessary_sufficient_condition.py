

"""
necessary condition and sufficient condition::
calculate which condition is necessary for, and sufficient for

"""



A = input("\n관계를 알고 싶은 첫번째 단어를 입력하세염\n")
B = input("\n그리고 두번째 단어를 입력하세염\n")

fset = [ A, B ]


C = input("\n""'"+str(A)+"'""이거 자체만으로도 ""'"+str(B)+"'""이(가) 될까 생각해봐"" "" 혹시 또 다른 extra 조건이 필요해?\n")

if C == 'no':
    print("'"+str(A)+"'"+"(은)는 ""'"+str(B)+"'""의 sufficient condition")
    print("'"+str(A)+"'""--->""'"+str(B)+"'")

elif C == 'yes':
    fset.reverse()
    # print(fset)
    D = input("\n ""'"+str(fset[0])+"'""인 것이 가능해?\n" ""+str(fset[1])+"(이)가 없어도??")
    if D == 'no':
        print("\n"+str(fset[1])+"is necessary condition for "+str(fset[0]))
        print("'" + str(fset[0]) + "'""--->""'" + str(fset[1]) + "'")



