
a = input('입력')
b = input()

#음 num 얘는 로컬 배리어블인데,,,
#이것을 어떻게 만져야 하는것인가....



# num =1

def num_test():

    if a == 'a':
        print("증답")
        if b == 'b':
            # num+= 20
            print("참콤보")
        else:
            print("오십점!")

    elif a != 'a':
        print('이런쓰!')



        if b !='b':
            print("또또틀림")

        elif b == 'b':
            print("이상한 오십점")

        # num +=100
       # return num

        # print(num)
        # return num

# def __str__():
#     return num_test()


print(num_test())

'''
논리박스로 파악해보면
     a    b
     t    f :11
     f    t :None
     f    f :None
     t    t :31


'''

