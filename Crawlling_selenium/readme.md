# Selenium Crawlling
- from https://tacademy.skplanet.com/live/player/onlineLectureDetail.action?seq=133
- ref: https://beomi.github.io/2017/09/28/HowToMakeWebCrawler-Headless-Chrome/

```python
#웹에 내용 입력
driver.find_element_by_id('HTML ID').send_keys('입력내용')
#클릭 효과
driver.find_element_by_css_selector('.search-btn').click()

#명시적 대기
from selenium.webdriver.support.ui import WebDriverWait
WebDriverWait(driver, 10).until(
        #지정한 한개 요소가 오면 웨이트 종료
        EC.presence_of_element_located(By.ID,'HTML ID')
    )

#묵시적 대기
driver.implicitly_wait(10)
#절대적 대기
import time
time.sleep(1)

#자바스크립트 구동하기
driver.execute_script("search.SetCategoryList(%s, '')" % page)

```
