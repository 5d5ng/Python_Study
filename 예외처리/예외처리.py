

try:
    print('나누기 전용 계산기')
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 :")))
    nums.append(int(input("첫번째 숫자를 입력하세요 :")))
    nums.append(int(nums[0]/nums[1]))
    print("{0}/{1} = {2}".format(nums[0],nums[1],nums[2]))

except ValueError:
    print('에러! 잘못된 값을 입력하였습니다.')
except ZeroDivisionError as err:
    print(err)
except Exception as err: #위 두 에러를 제외한 나머지 에러의 경우
    print("알 수 없는 에러가 발생했습니다.")
    print(err)