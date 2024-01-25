library(tidyverse)
library(ggplot2)

data <- read_csv('output_data/grouped_billboard_data.csv') |>
  transform(Date = as.numeric(Date)) |> 
  mutate(
    Genre = case_when(
      Genre == "Easy_Listening" ~ "Easy Listening",
      Genre == "Hip_Hop" ~ "Hip Hop",
      Genre == "Soul_and_R&B" ~ "Soul and R&B",
      Genre == "Blues" ~ "Blues", 
      Genre == "Rock" ~ "Rock", 
      Genre == "Country" ~ "Country", 
      Genre == "Electronic" ~ "Electronic", 
      Genre == "Folk" ~ "Folk", 
      Genre == "Jazz" ~ "Jazz", 
      Genre == "Pop" ~ "Pop", 
      Genre == "Metal" ~ "Metal", 
    )
  )
generations <- read_csv('output_data/generations.csv')

#not necessary right now, but might be for other plots
genre_counts_per_year <- data |>
  group_by(Date, Genre) |>
  summarise(n = n()) |>
  group_by(Date) |>
  mutate(percentage = n/sum(n) * 100) |>
  ungroup()

print(genre_counts_per_year)

ggplot(data = data) +
  aes(x = Date, color = Genre) +
  xlim(1958,2021) + 
  theme_light() + 
  labs(x = 'Year', y = "Number of Hot 100 songs", title = "Number of Billboard Hot 100 songs per genre") +
  geom_line(stat = "bin", binwidth = 5) +
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 5, label= generation), y=80000, hjust = 1, colour="red", angle=90, data = generations)

ggsave('output_data/genre_hot100_line.pdf', width = 20, height = 15, units = c('cm'))
ggsave('output_data/genre_hot100_line.png', width = 20, height = 15, units = c('cm'))

ggplot(data = genre_counts_per_year) + 
  aes(x = Date, y = percentage) + 
  xlim(1958,2021) + 
  theme_light() + 
  labs(x = 'Year', y = "Percentage of Hot 100 songs", title = "Proportion of Billboard Hot 100 songs in each genre") +
  geom_area(aes(fill = Genre), alpha = 0.8, size = 0.5, colour = "black", stat = "identity")+ 
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 3, label= generation), y=2, hjust = 0, colour="white", angle=90, data = generations)

ggsave('output_data/genre_hot100_stacked.pdf', width = 20, height = 15, units = c('cm'))
ggsave('output_data/genre_hot100_stacked.png', width = 20, height = 15, units = c('cm'))

ggplot(data = data) +
  aes(x = Date, color = Genre) +
  xlim(1958,2000) + 
  theme_light() + 
  labs(x = 'Year', y = "Number of Hot 100 songs", title = "Number of Billboard Hot 100 songs per genre") +
  geom_line(stat = "bin", binwidth = 5) +
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 1, label= generation), y=80000, hjust = 1, colour="red", angle=90, data = generations)

ggsave('output_data/genre_hot100_line_compare.pdf', width = 20, height = 15, units = c('cm'))
ggsave('output_data/genre_hot100_line_compare.png', width = 20, height = 15, units = c('cm'))

ggplot(data = genre_counts_per_year) + 
  aes(x = Date, y = percentage) + 
  xlim(1958,2000) + 
  theme_light() + 
  labs(x = 'Year', y = "Percentage of Hot 100 songs", title = "Proportion of Billboard Hot 100 songs in each genre") +
  geom_area(aes(fill = Genre), alpha = 0.8, size = 0.5, colour = "black", stat = "identity")+ 
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 1, label= generation), y=2, hjust = 0, colour="white", angle=90, data = generations)

ggsave('output_data/genre_hot100_stacked_compare.pdf', width = 20, height = 15, units = c('cm'))
ggsave('output_data/genre_hot100_stacked_compare.png', width = 20, height = 15, units = c('cm'))
