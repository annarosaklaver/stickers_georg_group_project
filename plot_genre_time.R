library(tidyverse)
library(ggplot2)

data <- read_csv('test.csv') |>
  transform(Birthyear = as.numeric(Birthyear)) |>
  filter(Birthyear >= 1700)
generations <- read_csv('generations.csv')

#not necessary right now, but might be for other plots
musicians_per_year <- data |>
  transform(Birthyear = as.numeric(Birthyear)) |>
  group_by(Birthyear) |>
  summarise(n = n()) |>
  filter(Birthyear >= 1700)

ggplot(data = data) +
  aes(x = Birthyear, color = Genre) +
  geom_line(stat = "bin", binwidth = 5) +
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date - 5, label= generation), y=180, colour="red", angle=90, data = generations)
