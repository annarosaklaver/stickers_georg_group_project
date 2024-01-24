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
  mutate(percentage = n/sum(n) * 100) |>
  ungroup()

print(musicians_per_year)

ggplot(data = data) +
  aes(x = Birthyear, color = Genre) +
  labs(x = 'Birth year', y = "Number of artists") +
  geom_line(stat = "bin", binwidth = 5) +
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 5, label= generation), y=750, hjust = 1, colour="red", angle=90, data = generations)

ggsave('genre_birthyear_line.pdf', width = 20, height = 15, units = c('cm'))

ggplot(data = musicians_per_year) + 
  aes(x = period, y = percentage) + 
  xlim(1900,2000) + 
  labs(x = 'Birth year', y = "Percentage of artists") +
  geom_area(aes(fill = Genre), alpha = 0.6, size = 0.5, colour = "black", stat = "identity")+ 
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 1, label= generation), y=2, hjust = 0, colour="white", angle=90, data = generations)

ggsave('genre_birthyear_stacked.pdf', width = 20, height = 15, units = c('cm'))

ggplot(data = data) +
  aes(x = Birthyear, color = Genre) +
  labs(x = 'Birth year', y = "Number of artists") +
  xlim(1938,1980) + 
  geom_line(stat = "bin", binwidth = 5) +
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 1, label= generation), y=750, hjust = 1, colour="red", angle=90, data = generations)

ggsave('genre_birthyear_line_compare.pdf', width = 20, height = 15, units = c('cm'))

ggplot(data = musicians_per_year) + 
  aes(x = period, y = percentage) + 
  xlim(1938,1980) + 
  labs(x = 'Birth year', y = "Percentage of artists") +
  geom_area(aes(fill = Genre), alpha = 0.6, size = 0.5, colour = "black", stat = "identity")+ 
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 1, label= generation), y=2, hjust = 0, colour="white", angle=90, data = generations)

ggsave('genre_birthyear_stacked_compare.pdf', width = 20, height = 15, units = c('cm'))
