library(tidyverse)
library(ggplot2)

data <- read_csv('jazz_birthyears.csv') |>
  filter(birthyear >= 1700)
generations <- read_csv('generations.csv')

#not necessary right now, but might be for other plots
musicians_per_year <- data |>
  transform(birthyear = as.numeric(birthyear)) |>
  group_by(birthyear) |>
  summarise(n = n()) |>
  filter(birthyear >= 1700)

ggplot(data = generations) +
  aes(x = as.numeric(birthyear)) +
  geom_line(stat = "bin", binwidth = 5, data = data) +
  geom_vline(aes(xintercept = start_date), linetype = 'dashed') +
  geom_text(aes(x= start_date - 5, label= generation), y=180, colour="red", angle=90)
  
  
 # for(i in 1:ncol(generations)) {
  #  geom_vline(xintercept = 'start_date') + 
   # geom_text(aes(x= int('start_date'), label= 'generation', y=9), colour="red", angle=90) 
#  } 
