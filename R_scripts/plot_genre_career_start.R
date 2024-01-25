library(tidyverse)
library(ggplot2)

data <- read_csv('output_data/grouped_genre_and_career_start.csv') |>
  transform(Career_Start = as.numeric(Career_Start)) |>
  filter(Career_Start >= 1850) |>
  distinct()
generations <- read_csv('output_data/generations.csv')

#not necessary right now, but might be for other plots
musicians_per_year <- data |>
  transform(
    Career_Start = as.numeric(Career_Start),
    period = round(Career_Start / 5) * 5
  ) |>
  filter(Career_Start >= 1900) |>
  group_by(period, Genre) |>
  summarise(n = n()) |>
  group_by(period) |>
  mutate(percentage = n/sum(n) * 100) |>
  ungroup()

percentage_musicians <- data |>
  transform(Career_Start = as.numeric(Career_Start)) |>
  filter(Career_Start >= 1900) |>
  group_by(Career_Start, Genre) |>
  summarise(n = n()) |>
  group_by(Career_Start) |>
  mutate(percentage_per_year = n/sum(n) * 100) |>
  ungroup()

ggplot(data = data) +
  aes(x = Career_Start, color = Genre) +
  geom_line(stat = "bin", binwidth = 5) +
  theme_light() + 
  labs(x = 'Start of career (year)', y = "Number of artists") +
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 5, label= generation), y=1165, hjust = 1, colour="red", angle=90, data = generations)

ggsave('output_data/career_start_line.pdf', width = 20, height = 15, units = c('cm'))

ggplot(data = musicians_per_year) + 
  aes(x = period, y = percentage) + 
  xlim(1920,2015) + 
  theme_light() + 
  labs(x = 'Start of career (year)', y = "Percentage of artists") +
  geom_area(aes(fill = Genre), alpha = 0.8, size = 0.5, colour = "black", stat = "identity")+ 
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 3, label= generation), y=2, hjust = 0, colour="white", angle=90, data = generations)

ggsave('output_data/career_start_stacked.pdf', width = 20, height = 15, units = c('cm'))

ggplot(data = data) +
  aes(x = Career_Start, color = Genre) +
  geom_line(stat = "bin", binwidth = 5) +
  xlim(1958,2000) + 
  theme_light() + 
  labs(x = 'Start of career (year)', y = "Number of artists") +
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 1, label= generation), y=1165, hjust = 1, colour="red", angle=90, data = generations)

ggsave('output_data/career_start_line_compare.pdf', width = 20, height = 15, units = c('cm'))

ggplot(data = percentage_musicians) + 
  aes(x = Career_Start, y = percentage_per_year) + 
  xlim(1958,2000) + 
  theme_light() + 
  labs(x = 'Start of career (year)', y = "Percentage of artists") +
  geom_area(aes(fill = Genre), alpha = 0.8, size = 0.5, colour = "black", stat = "identity")+ 
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 1, label= generation), y=2, hjust = 0, colour="white", angle=90, data = generations)

ggsave('output_data/career_start_stacked_compare.pdf', width = 20, height = 15, units = c('cm'))
