#키워드를 통해 전달하면 매개변수 순서가 바뀌어도 가능하다.
def profile(name,age,main_lang):
    print(name,age,main_lang)


profile(name="유재석",main_lang="파이썬",age=20)
profile(main_lang="자바",age=20,name="김태호")
