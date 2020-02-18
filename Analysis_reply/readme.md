# Inflearn new year event 2020
from https://github.com/corazzon/inflearn-new-year-event-2020

### 0. 크롤링(Crawlling)
> beautifulSoup4
> requests
### 1. 키워드 빈도수 계산
```python
from sklearn.feature_extraction.text import CountVectorizer
```
```CountVectorizer```는 문서를 토큰리스트로 변환하고 토큰의 출현 빈도를 세아려 Bag of Words(BOG) 인코딩 벡터로 변환한다.
- stop_words : 문자열 {‘english’}, 리스트 또는 None (디폴트) <br>
stop words 목록.‘english’이면 영어용 스탑 워드 사용, Stop Words 는 문서에서 단어장을 생성할 때 무시할 수 있는 단어를 말한다. 보통 영어의 관사나 접속사, 한국어의 조사 등이 여기에 해당한다. stop_words 인수로 조절할 수 있다.

- analyzer : 문자열 {‘word’, ‘char’, ‘char_wb’} 또는 함수 <br>
단어 n-그램, 문자 n-그램, 단어 내의 문자 n-그램

- token_pattern : string : 토큰 정의용 정규 표현식

- tokenizer : 함수 또는 None (디폴트) : 토큰 생성 함수

- ngram_range : (min_n, max_n) 튜플 <br>
n-그램 범위, n-그램은 단어장 생성에 사용할 토큰의 크기를 결정한다. 모노그램(1-그램)은 토큰 하나만 단어로 사용하며 바이그램(2-그램)은 두 개의 연결된 토큰을 하나의 단어로 사용한다.

- max_df : 정수 또는 [0.0, 1.0] 사이의 실수. 디폴트 1<br>
단어장에 포함되기 위한 최대 빈도

- min_df : 정수 또는 [0.0, 1.0] 사이의 실수. 디폴트 1<br>
 단어장에 포함되기 위한 최소 빈도 <br>
max_df, min_df 인수를 사용하여 문서에서 토큰이 나타난 횟수를 기준으로 단어장을 구성할 수도 있다. 토큰의 빈도가 max_df로 지정한 값을 초과 하거나 min_df로 지정한 값보다 작은 경우에는 무시한다. 인수 값은 정수인 경우 횟수, 부동소수점인 경우 비중을 뜻한다.


### 2. Bag of Words(BOW), TF-IDF
```python
from sklearn.feature_extraction.text import TfidfTransformer
```
TF-IDF(Term Frequency – Inverse Document Frequency) 인코딩은 단어를 갯수 그대로 카운트하지 않고 모든 문서에 공통적으로 들어있는 단어의 경우 문서 구별 능력이 떨어진다고 보아 가중치를 축소하는 방법이다.

구제적으로는 문서  𝑑 (document)와 단어  𝑡  에 대해 다음과 같이 계산한다.
```
tf-idf(𝑑,𝑡)=tf(𝑑,𝑡)⋅idf(𝑡)
```
여기에서

tf(𝑑,𝑡) : term frequency. 특정한 단어의 빈도수
idf(𝑡)  : inverse document frequency. 특정한 단어가 들어 있는 문서의 수에 반비례하는 수
```
idf(𝑑,𝑡)=log𝑛 / 1+df(𝑡)
```
𝑛  : 전체 문서의 수
df(𝑡) : 단어  𝑡 를 가진 문서의 수 <br>
참고 : [데이터사이언스스쿨](https://datascienceschool.net/view-notebook/3e7aadbf88ed4f0d87a76f9ddc925d69/)
### 3. 군집화(KMeans)

### 4. 워드클라우드
