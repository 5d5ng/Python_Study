# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print('이름:{0}\t 나이: {1}\t'.format(name,age),end=" ") #end =" "를 이용하여 개행문자 삭제 가능
#     print(lang1,lang2,lang3,lang4,lang5)

# profile('유재석',20,"python","Java","C","C++","C#")
# profile('김태호',25,"Kotlin","Java","Swift","","")

#계속 ""을 인자로 넣는 비효율을 막기 위해 가변인자를 사용한다.

def profile(name,age,*language):
    print('이름:{0}\t 나이: {1}\t'.format(name,age),end=" ") #end =" "를 이용하여 개행문자 삭제 가능
    for lang in language:
        print(lang,end=" ")
    print()

profile('유재석',20,"python","Java","C","C++","C#")
profile('김태호',25,"Kotlin","Java","Swift")\

# 서로다른 개수의 값을 넣어줄때는 가변인자(*test)를 이용하여 문제를 해결할 수 있다.