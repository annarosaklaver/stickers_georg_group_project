library(tidyverse)
library(ggplot2)

data <- read_csv('jazz_birthyears.csv')

#musicians_per_year <- data |>
 # group_by(birthyear) |>
  #summarise(n = n())

print(data)
  

#ggplot(data = data) +
 # aes(x = year, y = genre) +
  #geom_line