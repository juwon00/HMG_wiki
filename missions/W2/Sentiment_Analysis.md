# Main

---

# Sentiment Analysis(Team) : Blind

## **문제정의**

**현대자동차 입사를 희망하여 재직자&퇴사자들이 현대차에 대해 어떤 리뷰를 남겼는지 보고 싶었고,**

**현대차 인사 담당자는 인사 운영을 위해 재직자&퇴사자 혹은 신규 입사자들이 무엇을 원하고 만족하고 있는지를 알고 싶어 할 것이다.** 

---

## 창출 할 수 있을 비지니스 가치

핵심 고객 : 현대자동차 인사팀에서 **HRD, 기획 / 제도**를 관리하는 책임자

**채용공고 마케팅 전략에 활용**

- **복지 & 문화 강조** → 우수 인재 유치

**리뷰 제목 단어 분석 (Word Cloud)**

- **이미지 파악**:
    - 긍정적 단어 유지, 부정적 단어 개선

**채용시 직무별 제목 강조**

- **우수 인재 확보 도움**

**부정적 리뷰 분석**

- **일의 만족도 향상**:
    - 부정적 키워드 개선

**항목별 평점 분석**

- **사내 문화**:
    - 평점 낮은 리뷰 개선
- **커리어 향상**:
    - 개선 및 인재 유지

→ **비즈니스 가치**: 인재 양성, 직원 만족도 증가, 생산성 향상

---

## **데이터수집**

https://www.teamblind.com/kr/company/현대자동차/reviews?page=1

<img width="764" alt="Untitled" src="https://github.com/juwon00/HMG_wiki/assets/99171610/75f90315-5d25-4772-93d5-ed44a9a2f094">

1. selenium을 이용해 크롤링 작업을 하였음.

<img width="874" alt="Untitled 1" src="https://github.com/juwon00/HMG_wiki/assets/99171610/f4fd7984-2857-4782-935c-9887c92bb02f">

<img width="308" alt="Untitled 2" src="https://github.com/juwon00/HMG_wiki/assets/99171610/d83fa7d9-ae5e-40cd-bef4-ab3917c38ec9">

| 커리어 향상 | 업무와 삶의 균형 | 급여 및 복지 | 사내 문화	 | 경영진 |
| --- | --- | --- | --- | --- |
| 총점	 | 제목	 | 장점 | 단점 | 직무 |

| career | work_life_balance | salary_and_benefits | culture | management |
| --- | --- | --- | --- | --- |
| total_score | title | pros | cons | job_role |
1. 워드클라우드를 진행하기 위해 str로 이루어진 “제목”, “장점”, “단점” 을 형태소 분석기를 통해 명사만 추출
2. 해당 단어들의 빈도 Counter를 통해 데이터셋 구축 하였음.

<img width="198" alt="Untitled 3" src="https://github.com/juwon00/HMG_wiki/assets/99171610/e05f9dc0-d750-4998-b84c-b965b2080965">

---

## **프로토타입**

- 처음 1000개 데이터셋만 크롤링 하여 EDA 및 워드클라우드를 진행함.
- 속도와 비용을 절약하기위해 샘플링 하여 먼저 작업 하였음.
- 샘플링 한 데이터를 가지고 EDA 와 형태소 분석기, 워드클라우드를 먼저 만드는 과정을 진행함.
- 이 과정을 하며 전체 데이터셋 (약 7천여개)를 크롤링을 다시 진행 하였음.
- 샘플 데이터를 통해 기본적인 데이터 특성을 파악하고, 분석 방법론을 검증. 이 과정에서 유의미한 패턴이나 문제점을 발견하여 이후 전체 데이터 분석에 반영함.

![Untitled 4](https://github.com/juwon00/HMG_wiki/assets/99171610/369090c9-af7d-4767-b615-6320b928fd80)

---

## EDA → 가설 → 평가

*가정 : 총점이 1~2점일 때 부정적, 4~5점일 때 긍정적인 리뷰라고 가정하였음*

## 1.‘업무와 삶의 균형’

### EDA

<img width="302" alt="Untitled 5" src="https://github.com/juwon00/HMG_wiki/assets/99171610/8f9aa97e-68c4-4f56-b509-6b526ee64a56">


- ‘업무와 삶의 균형’의 평점이 다른 항목에 비해 높다

### 목표설계

- ‘업무와 삶의 균형’과 관련된 단어가 많이 나올 것이다.

### 결론

- **전체 제목**

![Untitled 6](https://github.com/juwon00/HMG_wiki/assets/99171610/8e63f881-b6a8-4ca8-951c-696e716841e5)

- 가설에 맞게 제목에 워라벨에 대한 빈도수가 가장 높다.
    - 장점 역시 워라벨에 대한 빈도수가 많으므로 현대자동차 인사 담당자는 직원들의 워라벨은 지금과 동일하게 유지하는 쪽으로 가면 좋을 것 같다
    

## 2. 총점에 따른 키워드 분포

### EDA

<img width="289" alt="Untitled 7" src="https://github.com/juwon00/HMG_wiki/assets/99171610/f36ec8cf-5680-4e05-902e-06d4b66fed48">

- 총점이 전체적으로 고른 편이긴 하나 **1점**의 빈도가 높은것을 볼 수 있다
- 총점이 1~2점일 때 부정, 4~5점일 때 긍정으로 생각

### 목표설계

- 총점에 따라 키워드 분포가 다를 것이다.

### 결론

- **총점이 1점, 5점일 때 제목**

![Untitled 8](https://github.com/juwon00/HMG_wiki/assets/99171610/1582155a-dd44-45b1-96de-42aae0e8db70)

![Untitled 9](https://github.com/juwon00/HMG_wiki/assets/99171610/fae8f792-ba80-4b6d-844c-5f3a4778deda)

- 단점에는 연봉에 대한 빈도수가 가장 많이 나왔다.
    - 현대자동차 인사 담당자는 직원들의 연봉(성과금)을 올림으로써 인재 유지에 힘쓸 수 있다.
- 부정적인 키워드로 ‘연봉’에 대한 빈도수가 가장 많이 나왔다.
    - 부정적인 키워드인 ‘연봉’을 인사팀이 확인하여 해당 사항을 신속히 개선할 수 있다.
- 긍정적인 키워드로 ‘워라벨’에 대한 빈도수가 가장 많이 나왔다.
    - ‘워라벨’을 통해 복지 & 조직 문화를 강조할 수 있음
    

## 3. 연구개발 (R&D) 직무의 분포

### EDA

<img width="583" alt="Untitled 10" src="https://github.com/juwon00/HMG_wiki/assets/99171610/8e8cc989-9719-4190-8f85-d6f36a367f37">

<img width="475" alt="Untitled 11" src="https://github.com/juwon00/HMG_wiki/assets/99171610/302d1405-c055-4187-a096-fffa20593c63">

- 연구개발 (R&D)의 비중이 절반정도 차지하고 있는것을 볼 수 있다.
- 연구개발 (R&D)의 평균 점수가 다른직무의 평균점수보다 0.6점정도 낮은 것을 볼 수 있다.

### 목표설계

- ‘연구개발 (R&D)’ 직무가 전체 직무의 절반
    - ‘연구개발 (R&D)’과 다른 직무 간의 차이가 있을 것이다.

### 결론

![Untitled 12](https://github.com/juwon00/HMG_wiki/assets/99171610/e521c624-e298-4f4e-9a10-cfb099747b9d)

![Untitled 13](https://github.com/juwon00/HMG_wiki/assets/99171610/6bcc79ab-ea26-44e7-bac3-a45a5278799d)

- 연구개발(R&D)와 그 외 직무(생산 엔지니어) 비교
    - 다른 직무에서의 단점에서는 나오지 않았지만 연구개발(R&D) 직무에서의 단점에서 많은 빈도수가 나온 ‘출퇴근’ 문제를 통근버스, 기숙사 제공 등의 복지를 이용해 해결하면 전체적인 직원 만족도가 증가할 수 있다.

---

## 개선사항

![Untitled 14](https://github.com/juwon00/HMG_wiki/assets/99171610/a2bc8fbf-a9e4-4242-8a96-b7e7fbe7207a)

쿠팡 전용페이지

- 블라인드에서 현대자동차 전용페이지를 조회할 수 있다면 현재 직원들이 어떤 주제로 이야기를 하는지 파악 후 그에 대한 개선이 가능 할 것 같다.
- 잡플래닛과 같은 기업리뷰를 남기는 타 사이트를 함께 분석해봐도 좋은 결과가 나올 것 같다.
- 몇년차인지 데이터를 구할 수 있다면 어떤 계층에서 어떤 분야에 대해 좋게 생각하고 안좋게 생각하는지 파악가능 할 것 같다.
