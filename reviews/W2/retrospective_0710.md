## 정리
AWS EC2에서는 OS를 ubuntu보다 Amazon Linux를 사용하면 좋을 것 같다.
Amazon끼리 호환이 잘 되는것 같다.
다만 Amazon Linux 2023와 Amazon Linux 2 두개중에 기호에 맞게 선택하자

Docker 이미지 생성하기
- 어떤 OS를 선택해야 할까요?
  - amazonlinux:2를 선택한 이유
    - 처음에 ubuntu를 썼는데 이미지 빌드하는데 너무 오랜 시간이 걸림
    - Alpine Linux가 빠르다고 해서 교체
    - Alpine Linux가 호환이 안된다고 해서 amazonlinux:2로 다시 교체
- 어떤 소프트웨어를 설치해야 할까요?
  - psutil과 cffi 라이브러리가 빌드하는 동안 필요한 헤더 파일들이 부족
    - bash gcc g++ musl-dev linux-headers libffi-dev python3-dev openssl-dev 등 설치
- 어떤 화일을 담아야 할까요?
  - RUN pip3 install --no-cache notebook (실행 시 노트북 실행하도록)
  - EXPOSE 8888 (포트번호 설정)
  
<br>
<br>

## keep
W2M6를 진행하면서 'AWS EC2에 배포된 후에 서버 주소로 들어가면 JupyterLab 인터페이스가 실행' 요구사항대로 작성한 것 같다.
무수히 많은 에러를 마주쳤다. 처음 User-Data를 사용해서 Docker를 설치하는데 몇시간 걸린것 같다.
하지만 결국에는 에러를 해결하고 요구사항대로 만들게 되었다.
에러를 통해 배운다는것을 하루종일 느꼈다.
오류가 생겼던 부분과 오늘 진행했던 부분을 노션에 잘 정리해서 나중에도 쓸 수 있을 것 같다.
<br>
<br>

## problem
Ubuntu에서 User-Data를 사용해서 Docker를 설치하는것을 해결하지 못하고 OS를 Amazon Linux 2로 바꿨다.
왜 안되는지 찾아보지 못했는데 집가서 찾아봐야겠다.
<br>
<br>

## try
미션을 해결해야한다는 생각이 강해서 왜?에 대한 생각이 부족했다.
다음엔 조금더 '왜 이걸 사용할까?'등 왜?에 대한 생각을 해봐야겠다.
<br>
<br>
