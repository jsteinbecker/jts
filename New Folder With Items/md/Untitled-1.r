

# install.packages("tidyverse")
library(tidyverse)

#DF with Flu Data
df <- read.csv("/Users/joshsteinbecker/jts_project/csv/US Flu Data from 2012.csv")
summary(df) #, digits = digits, maxsum = maxsum)
s <- sort(df,decreasing = decreasing)

#DF Filtered for Colorado Records
co <- filter(df, State == "Colorado")
summary(co)

head(co,7)
#co <- co %>% select(State,Deaths.from.pneumonia.and.influenza,All.Deaths)
co %>% head(7)
co %>% tail(7)
plot (co$Deaths.from.pneumonia.and.influenza,co$All.Deaths)

nat <- df %>% filter(geoid == "National")
nat
summary(nat)