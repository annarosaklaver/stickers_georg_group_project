library(tidyverse)
library(ggplot2)
library(dplyr)

data <- read_csv('output_data/grouped_billboard_data.csv') |>
  transform(Date = as.numeric(Date)) 
generations <- read_csv('output_data/generations.csv')

#not necessary right now, but might be for other plots
genre_counts_per_year <- data |>
#  transform(
   # Date = as.numeric(Date),
   # period = round(Birthyear / 5) * 5
 # ) |>
  group_by(Date, Genre) |>
  summarise(n = n()) |>
  group_by(Date) |>
  mutate(percentage = n/sum(n) * 100) |>
  ungroup()

print(genre_counts_per_year)

ggplot(data = data) +
  aes(x = Date, color = Genre) +
  xlim(1958,2021) + 
  labs(x = 'Year', y = "Number of Hot 100 songs") +
  geom_line(stat = "bin", binwidth = 5) +
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 5, label= generation), y=80000, hjust = 1, colour="red", angle=90, data = generations)

ggsave('genre_hot100_line.pdf', width = 20, height = 15, units = c('cm'))

ggplot(data = genre_counts_per_year) + 
  aes(x = Date, y = percentage) + 
  xlim(1958,2021) + 
  labs(x = 'Year', y = "Percentage of Hot 100 songs") +
  geom_area(aes(fill = Genre), alpha = 0.6, size = 0.5, colour = "black", stat = "identity")+ 
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 3, label= generation), y=2, hjust = 0, colour="white", angle=90, data = generations)

ggsave('genre_hot100_stacked.pdf', width = 20, height = 15, units = c('cm'))

ggplot(data = data) +
  aes(x = Date, color = Genre) +
  xlim(1958,2000) + 
  labs(x = 'Year', y = "Number of Hot 100 songs") +
  geom_line(stat = "bin", binwidth = 5) +
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 1, label= generation), y=80000, hjust = 1, colour="red", angle=90, data = generations)

ggsave('genre_hot100_line_compare.pdf', width = 20, height = 15, units = c('cm'))

ggplot(data = genre_counts_per_year) + 
  aes(x = Date, y = percentage) + 
  xlim(1958,2000) + 
  labs(x = 'Year', y = "Percentage of Hot 100 songs") +
  geom_area(aes(fill = Genre), alpha = 0.6, size = 0.5, colour = "black", stat = "identity")+ 
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 1, label= generation), y=2, hjust = 0, colour="white", angle=90, data = generations)

ggsave('genre_hot100_stacked_compare.pdf', width = 20, height = 15, units = c('cm'))
