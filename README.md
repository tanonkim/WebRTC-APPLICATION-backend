# Puzzle AI VOIDOC MVP
<img width="234" src="https://user-images.githubusercontent.com/60570733/186329742-3f21ff74-c897-453a-9d9e-58eecc150304.png">
PuzzleAI와 기업협업 간 진행한 프로젝트로 비대면 진료 솔루션 VOIDOC의 주요 기능 API 구현 및 배포를 하였습니다.</br>

<br><br>


### 🚀 개발 인원 및 기간
* 개발 기간 : 2022/3/28 ~ 2022/4/22 (4주간)
* 프론트엔드 1명, 백엔드 1명
    * Back-end   
        * 김기현 - Modeling, SignIn API, SignUp API, 화상통화 기능을 위한 Signaling Server 구축


# 📍 데모 영상
![1](https://user-images.githubusercontent.com/60570733/186332691-6626aa10-3c58-4250-bf9c-d3bd60891551.gif)
![2](https://user-images.githubusercontent.com/60570733/186332731-48f73df1-9dc1-4c74-94f8-50a7c9d9114e.gif)
![3](https://user-images.githubusercontent.com/60570733/186332752-92a5c2c0-f4d1-4287-8688-c9a3cfd750cd.gif)




<br><br>


# 🌷 Target Application

<img width="1154" alt="스크린샷 2022-08-24 오후 2 03 06" src="https://user-images.githubusercontent.com/60570733/186333119-2c5b5997-deb7-4a43-ac55-faac6a27263f.png">

* ## 어플리케이션 소개  
    <a href="https://https://voidoc.io//">VOIDOC</a> </br>
    모바일 어플리케이션 기반으로 언제 어디서든 상담을 받을 수 있는 환경을 제공

* ## 어플리케이션 특징

    * 원격의료 플랫폼
    * 음성 보안 시스템으로 안전한 기록보관
    * 장소와 시간에 구애받지 않고 상담할 수 있는 특징이 있음



<br><br>


# 💡 초기기획 

## User flow

<img width="1185" alt="스크린샷 2022-08-26 오전 12 38 22" src="https://user-images.githubusercontent.com/60570733/186709163-5be251c9-4bbf-463b-a194-9187aebdf35f.png">




## 필수기능
* Django User model을 사용한 유저관리
  * 회원가입
  * 로그인
  
* 영상연결
   * WebRTC 
   * WebSocket


<br><br>

## 추가기능
* Unit Test
* Docker
* HTTPS 적용

<br><br>

# 📝 적용 기술 및 구현 기능

* ## 기술 스택
    * ### Front-end  
        <a href="#"><img src="https://img.shields.io/badge/HTML-DD4B25?style=plastic&logo=html&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/SASS-254BDD?style=plastic&logo=sass&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/javascript-EFD81D?style=plastic&logo=javascript&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/typescript-3073BF?style=plastic&logo=typescript&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/ReactNative-68D5F3?style=plastic&logo=react&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/Redux-7F42C3?style=plastic&logo=redux&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/styled components-f2af9b?style=plastic&logo=styled-components &logoColor=white"/></a>
    * ### Back-end  
        <a href="#"><img src="https://img.shields.io/badge/python-3873A9?style=plastic&logo=python&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/DjangoRestFramework-0B4B33?style=plastic&logo=django&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/Django Channels-0B4B33?style=plastic&logo=&logoColor=white"/></a> <br/>
    <a href="#"><img src="https://img.shields.io/badge/MySQL-005E85?style=plastic&logo=mysql&logoColor=white"/></a> 
    <a href="#"><img src="https://img.shields.io/badge/bcrypt-525252?style=plastic&logo=bcrypt&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/postman-F76934?style=plastic&logo=postman&logoColor=white"/></a> <br/>
    <a href="#"><img src="https://img.shields.io/badge/AWS RDS-FF9701?style=plastic&logo=aws&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/AWS S3-FF9701?style=plastic&logo=aws&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/AWS EC2-FF9701?style=plastic&logo=aws&logoColor=white"/></a> 
    <a href="#"><img src="https://img.shields.io/badge/docker-0040FF?style=plastic&logo=docker&logoColor=white"/></a> <br/>
    <a href="#"><img src="https://img.shields.io/badge/AWS ABL-FF9701?style=plastic&logo=aws&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/AWS ACM-FF9701?style=plastic&logo=aws&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/AWS Route53-FF9701?style=plastic&logo=aws&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/ Nginx-049800?style=plastic&logo=Nginx&logoColor=white"/></a>


    * ### Common  
        <a href="#"><img src="https://img.shields.io/badge/git-E84E32?style=plastic&logo=git&logoColor=white"/></a>
        <a href="#"><img src="https://img.shields.io/badge/RESTful API-415296?style=plastic&logoColor=white"/></a>
    * ### Communication  
        <a href="#"><img src="https://img.shields.io/badge/github-1B1E23?style=plastic&logo=github&logoColor=white"/></a>
        <a href="#"><img src="https://img.shields.io/badge/Slack-D91D57?style=plastic&logo=slack&logoColor=white"/></a>
        <a href="#"><img src="https://img.shields.io/badge/Trello-2580F7?style=plastic&logo=trello&logoColor=white"/></a>
        <a href="#"><img src="https://img.shields.io/badge/Notion-F7F7F7?style=plastic&logo=notion&logoColor=black"/></a>
* ## 구현기능
    * 회원가입
        - Django Rest Framework를 활용한 유저 관리
        - UserSerializer로 데이터 생성
        - DRF를 활용한 서버 유효성 처리
        - Unit Test 완료
        
    * 로그인
        - Django Rest Framework를 활용한 유저 관리
        - password 암호화 및 Meta 속성을 활용한 read only 제어
        - Unit Test 완료
        
    * WebSocket 연결
        - Django-Channels 활용 
        - Coturn을 활용한 Turn Server 배포
        - SSL이 적용된 webSocket(WSS) 설정
        - channels가 Web Socket의 요청을 받은 후 라우팅 설정 확인
        - 라우팅 설정을 확인 후 대응하는 Consumer을 찾고 요청 처리
        - Redis를 저장소로 하는 채널 레이어를 사용
        
    * HTTPS 적용
        - AWS Route 53 도메인 등록
        - ABL, ACM에서 SSL인증서 발급 후 HTTP 요청을 HTTPS 로 받도록 처리
        
    * 파이썬 배포 및 웹서버 배포 
        - uWSGI, Daphne을 통한 파이썬 배포
        - Nginx를 통한 웹서버 배포

    
<br><br>


## API 문서화
![image](https://user-images.githubusercontent.com/60570733/186714336-814559b3-7707-4e8f-9f9b-2b08037d4f3a.png)

* 포스트맨을 이용해 API 문서화를 진행
* 프론트엔드와 소통 시 문서를 통해 1차적으로 커뮤니케이션 비용을 줄임
<br><br>

<br>

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0F6975&height=100&section=footer)


