# REST_API
## REST API(Representational API)

### 프로그래머의 소통방법

1. API: 어플리케이션과 프로그래밍으로 소통하는 방법

2. CLI(명령줄, git bash)
3. GUI(아이콘, git desktop)

개발을 할때 본인이 다 구현하는 게 아니라 기존의 API들로 효율적으로 만들자


### REST API란?
웹설계상 장점을 최대한 사용할 수 있는 방법론으로 두 가지 조건을 충족
1. 자원(Data)을 정의
2. 자원의 주소를 지정

### REST 구성

자원: URI / 행위: HTTP Method / 표현: Representaion 3가지로 구성됨

```
자원(URI, URL, URN):
URI는 URL을 포함하는 상위개념으로 인터넷의 '자원을 나타내는' 유일한 주소임
URL은 '자원이 어디있는지 주소'를 알려주는 약속(웹주소)(WWW.NAVER.COM)
URN은 통합자원이름(유일한 이름역할 EX) ISBN(국제표준도서번호)

행위 HTTP method(Hypertext transfer protocol):
HTML같은 자원들을 가져올 수 있게 하는 프로토콜로 소통할 수 있게 해주는 도구
요청(request) <-> 응답(response)
클라이언트 <-> 서버 프로토콜
특징: 
1. 비연결지향(응답후접속끊음) 
2. 무상태(접속이끊어지면 상태저장x)
이런 특징들을 보완하기 위해 쿠키 & 세션이 있는거임

대표적인 HTTP 메서드: 
1. GET 오직 데이터 받기만하기 (네이버로 GET 보내면 네이버 문서를 받게됨)
2. POST 서버로 데이터 전송
3. PUT 요청한 주소의 자원 수정
4. DELETE 지정한 자원 삭제

행위(Representations):
json 객체로 표현함
json은 자바스크립트 객체 문법을 따르며 구조화된 데이터를 표현하기 위한 문자 기번 데이터 포맷이며
일반적으로 클라이언트한테 데이터를 전송할 때 사용함
JSON은 기계가 파싱(해석&분석)해서 만들어 내기 쉬움
파싱: 문자열같은건 쓸 수 있는 json객체로 바꾸는 과정
HTML이 아니라 json객체로 클라이언트한테 주면 노트북, 핸드폰 등 다양한데서 바로 적용 가능
django에서 json파일로 넘겨주기 위해 직접 json파일을 만들거나 json라이브러리를 사용하거나 다양한 방법이 있는데 DRF(django restful framework)이 가장 좋음
```



정리: 내가 만든걸 배포하려면 

DJANGO에서 server(백앤드)로 json객체를 배포하는 서버를 통해 JSON 객체를 주고 vue에서 Front 역할로 template을 줄 수 있음

쟝고에서 RESTful한 방식으로 json을 응답하는 서버 만드는게 1차 목표



## Django REST Framework

web API 구축에 용이함

Serialization(직렬화): 데이터 구조나 객체 상태를 다른 컴퓨터에 저장하고 다시

재구성할 수 있는 포맷으로 변환하느 과정

Model Serialization 제공 Model자체를 Serialization 가능함

기존의 Forms.py -> serializations.py 로 바뀜



## POSTMAN

C, U, D를 편하게 하기 위해 PostMan 사용





## 유교수님강의

restapi는 주소를 통해서 어떤 행동을 하는지도 예측가능하게 CRUD에서 HTTP Method로 변경시킨 것

R - GET

C - POST

U - PATCH/PUT

D - DELETE



기존의 form에서 serializer로 변경

1. model의 데이터 html 검증 -> model의 데이터 json 검증
2. html 생성 -> json 생성