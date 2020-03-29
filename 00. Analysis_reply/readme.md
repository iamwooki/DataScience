# Inflearn new year event 2020
from https://github.com/corazzon/inflearn-new-year-event-2020

doc : https://www.crummy.com/software/BeautifulSoup/bs4/doc/

### 0. 크롤링(Crawlling)
> beautifulSoup4
> requests
> trange

### 1. 키워드 빈도수 계산
> si-kit learn
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
idf(𝑑,𝑡)=log(𝑛 / 1+df(𝑡))
```
𝑛  : 전체 문서의 수
df(𝑡) : 단어  𝑡 를 가진 문서의 수 <br>
참고 : [데이터사이언스스쿨](https://datascienceschool.net/view-notebook/3e7aadbf88ed4f0d87a76f9ddc925d69/)
### 3. 군집화(KMeans)
```python
from sklearn.cluster import KMeans
```
#### K-평균 군집화 방법
은 가장 단순하고 빠른 군집화 방법의 하나이다. 다음과 같은 목적함수 값이 최소화될 때까지 군집의 중심위치와 각 데이터가 소속될 군집를 반복해서 찾는다. 이 값을 관성(inertia)이라 한다.
```
𝐽=∑_𝑘=1^𝐾 ∑_𝑖∈𝐶𝑘 𝑑(𝑥𝑖,𝜇𝑘)
 ```
이 식에서  𝐾 는 군집의 갯수이고  𝐶𝑘 는  𝑘 번째 군집에 속하는 데이터의 집합,  𝜇𝑘 는  𝑘 번째 군집의 중심위치(centroid),  𝑑 는  𝑥𝑖,𝜇𝑘  두 데이터 사이의 거리 혹은 비유사도(dissimilarity)로 정의한다. 만약 유클리드 거리를 사용한다면 다음과 같다.
```
𝑑(𝑥𝑖,𝜇𝑘)=||𝑥𝑖−𝜇𝑘||^2
 ```
위 식은 다음처럼 표현할 수도 있다.
```
𝐽=∑_𝑖=1^𝑁 min_𝜇_𝑗∈𝐶 (||𝑥𝑖−𝜇𝑗||^2)
 ```
세부 알고리즘은 다음과 같다.

임의의 중심위치  𝜇𝑘(𝑘=1,…,𝐾) 를 고른다. 보통 데이터 표본 중에서  𝐾 개를 선택한다.
모든 데이터  𝑥𝑖(𝑖=1,…,𝑁) 에서 각각의 중심위치  𝜇𝑘 까지의 거리를 계산한다.
각 데이터에서 가장 가까운 중심위치를 선택하여 각 데이터가 속하는 군집을 정한다.
각 군집에 대해 중심위치  𝜇𝑘 를 다시 계산한다.
2 ~ 4를 반복한다.
K-평균 군집화란 명칭은 각 군집의 중심위치를 구할 때 해당 군집에 속하는 데이터의 평균(mean)값을 사용하는데서 유래하였다. 만약 평균 대신 중앙값(median)을 사용하면 K-중앙값(K-Median) 군집화라 한다.

scikit-learn의 cluster 서브패키지는 K-평균 군집화를 위한 KMeans 클래스를 제공한다. 다음과 같은 인수를 받을 수 있다.

- n_clusters: 군집의 갯수
- init: 초기화 방법. "random"이면 무작위, "k-means++"이면 K-평균++ 방법. 또는 각 데이터의 군집 라벨.
- n_init: 초기 중심위치 시도 횟수. 디폴트는 10이고 10개의 무작위 중심위치 목록 중 가장 좋은 값을 선택한다.
- max_iter: 최대 반복 횟수.
- random_state: 시드값.

#### 미니배치 K-평균 군집화
K-평균 방법에서는 중심위치와 모든 데이터 사이의 거리를 계산해야 하기 때문에 데이터의 갯수가 많아지면 계산량도 늘어단다. 데이터의 수가 너무 많을 때는 미니배치 K-평균(Mini-batch) 군집화 방법을 사용하면 계산량을 줄일 수 있다. 미니배치 K-평균 군집화는 데이터를 미니배치 크기만큼 무작위로 분리하여 K-평균 군집화를 한다. 모든 데이터를 한꺼번에 썼을 때와 결과가 다를 수는 있지만 큰 차이가 없다.

사이킷런의 cluster 서브패키지는 미니배치 K-평균 군집화를 위한 MiniBatchKMeans 클래스를 제공한다. 미니배치 크기 batch_size 인수를 추가로 받는다.
<br>참고 : [데이터사이언스스쿨](https://datascienceschool.net/view-notebook/2205ad8f0c5947c08696e8927b466341/)

### 4. 워드클라우드
from https://github.com/conda-forge/wordcloud-feedstock
