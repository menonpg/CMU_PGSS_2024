---
title: "myFirstRMarkdown"
author: "Prahlad Menon"
date: '2024-06-25'
output: html_document
---

# My First Python script generated using Github Copilot

```python
# Write a python function to add two numbers
def add_numbers(a, b):
    return a + b    

def main():
    print(add_numbers(2, 3))

```

# R script that performs analysis on a CSV file 

```r
knitr::opts_chunk$set(echo = TRUE)
```

## My first R Markdown

```r

library(readr)
iris <- read_csv("iris.csv", col_names = F)
colnames(iris) <- c('Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Class')

sapply(iris, class)

iris$Class <- as.factor(iris$Class)
sapply(iris, class)

# install.packages("dplyr")
library(dplyr)

iris %>% group_by(Class) %>% summarize( Min.Sepal.Length = min(Sepal.Length, na.rm=T),
                                        Max.Sepal.Length = max(Sepal.Length, na.rm=T),
                                        Mean.Sepal.Length = mean(Sepal.Length, na.rm=T),
                                        SD.Sepal.Length = sd(Sepal.Length, na.rm=T))  %>% as.data.frame()

```

```r
boxplot(Sepal.Length ~ Class, data = iris)

```

```r

boxplot(Sepal.Width ~ Class, data = iris)
```

