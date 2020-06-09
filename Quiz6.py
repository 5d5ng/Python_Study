def getStandard(height,gender):
    if(gender=="남자"):
        return height*height*22
    elif(gender=="여자"):
        return height*height*21
    else:
        print("Error")

h = 175
gen = '남자'

res = round(getStandard(h/100,gen),2)
#round는 소숫점 n번쨰 자리까지 표현
print('키 {} {}의 표준 체중은 {}입니다.'.format(h,gen,res))