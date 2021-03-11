library(ggplot2)
library(dplyr)


df <- mpg



df <- df %>% 
  select(hwy)

df$x = 1

df


p = ggplot(df, aes(x, hwy)) + geom_boxplot()


ggplot_build(p)$data %>% data.frame()


library(ggplot2)
boxplot(mpg$hwy, plot = F)$stats
q1 <- boxplot(mpg$hwy, plot = F)$stats[2]
q1

q3 <- boxplot(mpg$hwy, plot = F)$stats[4]
q3


iqr15 <- (q3-q1)*1.5
iqr15

upper <- q3 + iqr15
upper

lower <- q1 - iqr15 
lower

# upper보다 작은 것 중 가장 큰 값이 위쪽 수염
df %>% 
  filter(hwy < upper) %>% 
  arrange(desc(hwy)) %>% 
  head(1)
  
# lower보다 큰 것중 가장 작은 값이 아랫쪽 수염
df %>% 
  filter(hwy > lower) %>% 
  arrange(hwy) %>% 
  head(1)
  







