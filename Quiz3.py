url = 'http://naver.com'
s = url.replace("http://","")
s = s[:s.find(".")]
pw = s[:3] + str(len(s))+str(s.count('e'))+ '!'

print("{0}의 비밀번호는 {1} 입니다.".format(url,pw))


