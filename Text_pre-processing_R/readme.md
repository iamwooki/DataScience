# R로 하는 텍스트 데이터 전처리

from https://mrchypark.github.io/RKoText101/#1

## tidyverse
- 파이프 연산자(%>%)
```R
x %>% f(y)
becomes f(x,y)

#ex
#before
plot(diff(log(sample(rnorm(10000, mean = 10. sd = 1), size = 100, replace = FALSE))), col = "red", type = "1")
#after
rnorm(10000,mean=10,sd=1) %>%
  sample(size-199,replace=FALSE) %>%
  log() %>%
  diff() %>%
  plot(col="red", type="1")

```
## dplyr
-  열 방향 : 선택 - select()
```R
select(데이터명,컬럼명1, 컬럼명2, ... )
```
-  열 방향 : 계산 - mutate()
```R
#기존 컬럼을 이용해 새 컬럼을 만들 수 있음
mutate(데이터명,
    새컬럼 = 기존컬럼1 + 기존컬럼2
    )
```
-  행 방향 : 조건 - filter()
```R
#기존 컬럼에 조건을 이용해서 출력
filter(컬럼명, 컬럼==1)
```
-  행 방향 : 추가 - bind_rows()
```R
feb <- filter(데이터명, 컬럼==2)
dec <= filter(데이터명, 컬럼==12)
nrow(feb)+nrow(dec)
```
-  행 방향 : 정렬 - arrange()
```R
#컬럼 기준으로 오름차순 정렬
arrange(데이터명, 컬럼)
```
-  그룹 계산 - group_by() + summarise()
```R
#데이터를 요약하여 특성을 파악하는 방식으로 동작
summarise(데이터명, mean = mean(컬럼, na.rm=T), n=n())
#지정한 컬럼별이라는 추가 조건을 지정하는 기능
변수 = group_by(데이터, 컬럼명)
```
-  열 결합 - left_join()

## 단정한 데이터(tidy data)
1.1 Each variable forms a column.
1.2 각 변수는 개별의 열(column)으로 존재한다.
1.3 각 열에는 개별 속성이 들어간다.

2.1 Each observation forms a row.
2.2 각 관측치는 행(row)를 구성한다.
2.3 각 행에는 개별 관찰 항목이 들어간다.

3.1 Each type of observational unit forms a table.
3.2 각 테이블은 단 하나의 관측기준에 의해서 조직된 데이터를 저장한다.
3.3 각 테이블에는 단일 유형의 데이터가 들어간다.

## N2H4
from https://github.com/forkonlp/N2H4
- 네이버 뉴스 크롤링 수집도구

## RmecabKo
- 일본어 형태소 분석기 mecab 기반
- C++로 작성
- 일본어, 중국어도 사용 가능
- 형태소 분석 함수를 제공
- 띄어쓰기에 덜 민감

## KoNLP
- java로 작성된 한나눔 분석기 기반
- NIADic() 등 자체 사전
- 텍스트 분석을 위한 기능들 제공
- 친절한 설명서
