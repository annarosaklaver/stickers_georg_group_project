library(tidyverse)
library(ggplot2)

data <- read_csv('grouped_genre_and_birthyear.csv') |>
  transform(Birthyear = as.numeric(Birthyear)) |>
  filter(Birthyear >= 1850) |>
  distinct()
generations <- read_csv('generations.csv')

#not necessary right now, but might be for other plots
musicians_per_year <- data |>
  transform(Birthyear = as.numeric(Birthyear)) |>
  group_by(Birthyear) |>
  summarise(n = n()) |>
  filter(Birthyear >= 1850)

ggplot(data = data) +
  aes(x = Birthyear, color = Genre) +
  geom_line(stat = "bin", binwidth = 5) +
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date - 5, label= generation), y=600, colour="red", angle=90, data = generations)

ggsave('first_plot.pdf', width = 20, height = 15, units = c('cm'))
