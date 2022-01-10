#221 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.

def print_reverse(name):
    print(name[::-1])

print_reverse("python")

#222 성적 리스트를 입력 받아 평균을 출력하는  print_score 함수를 정의하라.

list = [1,2,3]

def print_score(list):
    print(sum(list)/len(list))

print_score(list)

#223 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.

list2 = [1,3,2,10,12,11,15]

def print_even(list):
    for number in list2:
        if number % 2 == 0:
            print(number)

print_even(list2)

#224 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.

person =  {"이름": "김말똥", "나이": 30, "성별": 0}

def print_keys(person):
    for keys in person.keys():
        print(keys)

print_keys(person)

#225 my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼있다. my_dict와 날짜 키값을 입력받아 OHLC리스트를 출력하는 print_value_by_key 함수를 정의하라.

my_dict = {"10/26": [100, 130, 100, 100], "10/27": [10, 12, 10, 11]}

def print_value_by_key(my_dict,key):
    print(my_dict[key])

print_value_by_key(my_dict, "10/26")
print_value_by_key(my_dict, "10/27")

#226 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.

def print_5xn(sentence):
    five_letters = int(len(sentence)/5)  #몫을 구하는 것
    for i in range(five_letters + 1):    #반복문을 돌리는데 값만 넣으면 나머지 문자가 출력이 되지 않으므로 +1을 해주는 것
        print(sentence[i*5 : i*5 +5])    #다섯 글자씩 출력해야 하는데 정확한 글자수를 모른다는 가정하에 i=0부터 시작해서 *5 해주기 (슬라이싱 활용 )

print_5xn("아이엠어보이유알어걸")


#227 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string)함수를 작성하라.

def print_mxn(sentence, letter):
    random_letters = int(len(sentence) / letter)
    for i in range(random_letters + 1):
        print(sentence[i*letter : i*letter + letter])

print_mxn("아이엠어보이유알어걸", 3)

#228 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.

def calc_monthly_salary(annual_pay):
    monthly_pay = int(annual_pay / 12)
    print(monthly_pay)
    return monthly_pay

calc_monthly_salary(12000000)

#229 아래 코드의 실행 결과를 예측하라.

def my_print(a,b):
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)

#230 아래 코드의 실행 결과를 예측하라.

def my_print(a,b):
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)

#231 아래 코드를 실행한 결과를 예상하라. -> 에러 발생

#def n_plus_1 (n):
    #result = n + 1


#n_plus_1(3)
#print(result)

#232 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.

def make_url(internet):
    url = "www." + internet +  ".com"
    print(url)
    return url

make_url("naver")

#233 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.

def make_list(letters):
    list3 = []
    for i in letters:
        list3.append(i)
    print(list3)
    return list3

make_list("abcd")
            
#234 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.

def pickup_even(letters):
    result = []
    for letter in letters:
        if letter % 2 ==0:
            result.append(letter)
    print(result)
    return result

pickup_even([3,4,5,6,7,8])
    
#235 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.

def convert_int(str_number):
    result = ''                      #숫자들을 하나하나 더해서 나중에 반환처리
    for letter in str_number:
        if letter.isdigit():         #해당 문자가 숫자라면 (. isdigt() 사용 - 해당문자가 숫자면 true, 아니면 false 반환)
            result += letter         #result에 해당 문자를 더함
    print(int(result))
    return int(result)

convert_int("1,234,567")
    
#236 아래 코드의 실행 결과를 예측하라.

def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

#237 아래 코드의 실행 결과를 예측하라.

def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)

#238 아래 코드의 실행 결과를 예측하라.

def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

#239 아래 코드의 실행 결과를 예측하라.

def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)

#240 아래 코드의 실행 결과를 예측하라.

def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)

