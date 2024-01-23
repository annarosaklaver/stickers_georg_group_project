library(tidyverse)
library(ggplot2)
library(dplyr)

data <- read_csv('output_data/grouped_genre_and_birthyear.csv') |>
  transform(Birthyear = as.numeric(Birthyear)) |>
  filter(Birthyear >= 1850) |>
  distinct()
generations <- read_csv('output_data/generations.csv')

#not necessary right now, but might be for other plots
musicians_per_year <- data |>
  transform(
    Birthyear = as.numeric(Birthyear),
    period = round(Birthyear / 5) * 5
  ) |>
  filter(Birthyear >= 1900 & Birthyear <= 2000) |>
  group_by(period, Genre) |>
  summarise(n = n()) |>
  group_by(period) |>
  mutate(percentage = n/sum(n)) |>
  ungroup()

print(musicians_per_year)

ggplot(data = data) +
  aes(x = Birthyear, color = Genre) +
  geom_line(stat = "bin", binwidth = 5) +
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 5, label= generation), y=600, colour="red", angle=90, data = generations)

ggsave('first_plot.pdf', width = 20, height = 15, units = c('cm'))

ggplot(data = musicians_per_year) + 
  aes(x = period, y = percentage) + 
  xlim(1900,2000) + 
  geom_area(aes(fill = Genre), alpha = 0.6, size = 0.5, colour = "black", stat = "identity")+ 
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 3, label= generation), y=0.02, hjust = 0, colour="white", angle=90, data = generations)

ggsave('hopefully_better_plot.pdf', width = 20, height = 15, units = c('cm'))
