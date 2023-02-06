# api: 두소프트웨어가 통신할수있도록 연결시켜주는 인터페이스 
# 서버마다 요청받는 방식이 다르면 요청하기가 쉽지 않아 통일된 대화 규측을 만들자 해서 나온것이 Rest api
# import requests


# url = 'https://api.agify.io/?name=sungjoon'
# response = requests.get(url).json()

# name = response.get('name')
# age = response.get('age')


# print(f'{name}의 나이는 {age}살')

# url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1021'
# response= requests.get(url).json()
# for i in range(1,7):
#     words = 'drwtNo'+str(i)
#     print(response.get(words))

# hoicha=input()
# # https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1001
# url='https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+hoicha
# result=requests.get(url).json()
# print(result)

# for i in range(1,7):
#     words="drwtNo"+str(i)
#     print(result.get(words))

# 컴퓨터      hw  cpu 메모리 저장 장치 (ssd(하드디스크))
#             sw system sw 운영체에 우리가 사용하는 앱들
#             application sw 
#             운영체제 - 리눅스 윈도우
#             리눅스 - pda mac
# 절대 경로- 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한것
# 상대 경로- 현재 작업하고 있는 위치에서 계산된 상대적 위치를 작성한것
# 텍스트기반의 언어 쉽게 쓰고 읽고 하는데 도움이 되는것 HTML로 변환이 가능함
# github(원격저장소)
# readme 파일!! = 이저장소는 어떠한 정보를 기록한 저장소이며 .. 자기소개.. 업로드한 자료에 대한 정보를 적는 파일
# .md

# git
#       add>     commit>        push>
#  woking> staging> git directory> Remote repo
#  (   내컴퓨터에서 이뤄지는 작업  ) (원격저장소)
#  새로생성된 파일 untracked file
#  한번이라도 add한 이력이 있으면 git의 관리 대상 tracked file
