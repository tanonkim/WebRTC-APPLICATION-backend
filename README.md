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


# 💡 초기기획 & ERD

## ERD

<img width="1400" alt="스크린샷 2022-03-25 오후 5 02 20" src="https://user-images.githubusercontent.com/60570733/160079346-672ac8a8-5314-4167-adb9-bc433ada24c3.png">
<a href="https://www.erdcloud.com/p/ubQyfGJ5FLKhYbRAy">Site Link</a>

<br><br>

## User flow

<img width="924" alt="스크린샷 2022-03-27 오전 12 41 14" src="https://user-images.githubusercontent.com/60570733/160246837-e87b4a41-f758-4d53-a715-345eb299babd.png">


## 초기기획 및 구현 목표
* 짧은 기간동안 service flow에 해당하는 기능 구현을 목표
* 개발은 초기세팅부터 전부 직접 구현
* 사이트 카테고리 중 숙소 예약 기능만 구현
* 필수 구현 사항을 (소셜) 로그인, 숙소 조회, 숙소 상세페이지, 예약으로 설정 
* 한 상품에 여러 옵션(숙소 종류, 인원, 기간)이 적용될 수 있게 기획
* 예약 된 일정을 제외한 예약 가능일만 예약할 수 있는 로직 구현
* 리뷰 CRUD

<br><br>



# 📝 적용 기술 및 구현 기능

* ## 기술 스택
    * ### Front-end  
        <a href="#"><img src="https://img.shields.io/badge/HTML-DD4B25?style=plastic&logo=html&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/SASS-254BDD?style=plastic&logo=sass&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/javascript-EFD81D?style=plastic&logo=javascript&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/typescript-3073BF?style=plastic&logo=typescript&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/React-68D5F3?style=plastic&logo=react&logoColor=white"/></a>
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
    * 회원가입 / 로그인
        - 카카오톡 소셜 로그인
        - OAuth2에 맞는 로직 구현
        - 일치하는 user가 없으면 Create, user가 있으면 Get하는 로직 적용
        - Unit Test 완료
    * Room List API
        - Q를 활용해 판매 상품의 분류에 따른 filtering 적용
        - 가격, 기간, 인원, 카테고리, amenity에 따른 filtering 적용
        - pagination
        - Unit Test 완료
    * Room Detail API
        - 숙소 상세페이지에 필요한 데이터를 필터링 하여 프론트엔드로 전달
        - path parameter 경로 적용
        - ORM 최적화
        - Unit Test 완료
    * Wishlist API
        - 해당 room_id를 가져온 후 Wishlist를 생성
        - 성공할 시 WishlistRoom 테이블의 항목 생성
        - adding and deleting 기능 구현
        - wishlist추가 시 중간테이블도 생성되는 로직 구현
        - Unit Test 완료
    * Reservation API
        - 예약 CRUD 기능 구현
        - 일련의 과정에 원자성을 부여하기 위해 transaction 사용
        - 기존 예약이 존재할 때, 예약가능일자 검증 조건 확인
     * Review API
        - 리뷰 CRUD 구현
        - AWS S3 활용하여 이미지 저장
    
<br><br>


## API 문서화
<img width="1144" alt="스크린샷 2022-03-25 오후 5 32 57" src="https://user-images.githubusercontent.com/60570733/160084208-f227cb40-12cb-44cc-84ff-8ec766a7a8bb.png">

* 포스트맨을 이용해 API 문서화를 진행
* 이번 프로젝트에서 쿼리파라미터(category, check_in&out, amenity, price, guest, options, page, booking 등)로 많은 값들을 받아야했기 때문에 API 문서화를 진행
* 프론트엔드와 소통 시 문서를 통해 1차적으로 커뮤니케이션 비용을 줄임
<br><br>

## Trello

<img width="1676" alt="스크린샷 2022-03-25 오후 5 31 52" src="https://user-images.githubusercontent.com/60570733/160083999-169baf7d-2f32-4543-8b84-d0d09e74b1c2.png">

* 트렐로를 이용해 모든 업무들을 세분화 시켜 하나의 티켓으로 제작
* 팀원들과 공유해야할 내용은 공지 탭을 통해 단일화
* 전체 프로세스를 네 가지 카테고리로 나눠서 각각의 티켓을 과정에 따라 하나씩 이동 시키며 프로젝트의 모든 일정과 업무를 관리
* 각자 데일리 스탠드업 미팅 로그를 작성하고 10~20분내로 짧게 진행상황 및 블로커를 점검
* 스프린트 주기를 지켜 한 스프린트가 끝나고 회고미팅을 해 발전방향을 모색

<br>

# Reference
* 이 프로젝트는 [Airbnb](https://airbnb.co.kr) 사이트를 참조하여 학습목적으로 만들었습니다.
* 실수수준의 프로젝트이지만 학습용으로 만들었기 떄문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
* 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
* 이 프로젝트에서 사용하고 있는 로고와 배너는 해당 프로젝트 팀원 소유이므로 해당 프로젝트 외부인이 사용할 수 없습니다.

![Footer](https://capsule-render.vercel.app/api?type=waving&color=ff385c&height=100&section=footer)


