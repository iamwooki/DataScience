#install.packages("tidyverse")
#install.packages("N2H4")
#install.packages("tidytext")
#install.packages("remotes")
#remotes::install_github("mrchypark/multilinguer")
#multilinguer::install_java()
#install.packages("https://cran.r-project.org/src/contrib/Archive/KoNLP/KoNLP_0.80.2.tar.gz", repos = NULL, type="source")
library(KoNLP)
library(tidyverse)
library(N2H4)
library(dplyr)
library(tidytext)


url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=005&aid=0001236313"
getAllComment(url) %>%
  select(userName,contents)
comment = getAllComment(url)
getAllComment(url) %>%
  select(userName, contents) %>%
  unnest_tokens(ws,contents, "words")  # ws :white space 



