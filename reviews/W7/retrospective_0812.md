# 정리
- Monitoring and Optimizing Spark Job

<br>
<br>

## keep
딱히 없는것 같다.

<br>
<br>

## problem
크리티컬한 이슈의 수가 너무 없는것 같다는 피드백을 받았다.<br>
다시 크리티컬한 데이터를 많이 수집해 오는게 목표다.

<br>
<br>

## try
dc에서는 크롤링하는데 다른 사이트에 비해서 오래걸린다.<br>
많은 요청을 하면 로딩시간이 길어지는것 같다.<br>
하나의 람다는 최대 15분까지 사용할 수 있는데, 하나의 람다로는 dc에서 크롤링하기는 어렵다고 판단했다.<br>
Step Function을 사용해서 람다를 이어붙였다.<br>
쓸 수 있는 람다의 수만 많으면 이론상 3분 이내에 원하는 내용의 데이터를 수집할 수 있을 것 같다.<br>
그러면 iteration도 빨라지고, 시간도 절약되고, 더 좋아진다?<br>
Step Function 마지막 부분에 오류로 다시 해봐야 되겠지만 괜찮은것 같다.

<br>
<br>
