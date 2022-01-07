library(tidyverse)
x = tribble(
      ~name,~name2,
      "Josh","Steinbecker",
      "Suck","it"
)
x = rbind(x,c("boo","loo"))
y = mutate(x,)

m = c("Josh","Steinbecker")
n = c("Frank","Sinatra")
o = cbind(m,n)
o
com = rbind(o,x)
