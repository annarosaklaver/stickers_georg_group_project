library(tidyverse)
library(ggplot2)

data <- read_csv('output_data/grouped_genre_and_birthyear.csv') |>
  transform(Birthyear = as.numeric(Birthyear)) |>
  filter(Birthyear >= 1850) |>
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
  ) |> 
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

percentage_musicians <- data |>
  transform(Birthyear = as.numeric(Birthyear)) |>
  filter(Birthyear >= 1900) |>
  group_by(Birthyear, Genre) |>
  summarise(n = n()) |>
  group_by(Birthyear) |>
  mutate(percentage_per_year = n/sum(n) * 100) |>
  ungroup()

ggplot(data = data) +
  aes(x = Birthyear, color = Genre) +
  labs(x = 'Birth year', y = "Number of artists", title = "Number of artists making music in each genre") +
  geom_line(stat = "bin", binwidth = 5) +
  theme_light() + 
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 5, label= generation), y=750, hjust = 1, colour="red", angle=90, data = generations)

ggsave('output_data/genre_birthyear_line.pdf', width = 20, height = 15, units = c('cm'))
ggsave('output_data/genre_birthyear_line.png', width = 20, height = 15, units = c('cm'))

ggplot(data = musicians_per_year) + 
  aes(x = period, y = percentage) + 
  xlim(1900,2000) + 
  theme_light() + 
  labs(x = 'Birth year', y = "Percentage of artists", title = "Percentage of artists making music in each genre") +
  geom_area(aes(fill = Genre), alpha = 0.8, size = 0.5, colour = "black", stat = "identity")+ 
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 1, label= generation), y=2, hjust = 0, colour="white", angle=90, data = generations)

ggsave('output_data/genre_birthyear_stacked.pdf', width = 20, height = 15, units = c('cm'))
ggsave('output_data/genre_birthyear_stacked.png', width = 20, height = 15, units = c('cm'))

ggplot(data = data) +
  aes(x = Birthyear, color = Genre) +
  labs(x = 'Birth year', y = "Number of artists", title = "Number of artists making music in each genre") +
  xlim(1938,1980) + 
  theme_light() + 
  geom_line(stat = "bin", binwidth = 5) +
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 1, label= generation), y=750, hjust = 1, colour="red", angle=90, data = generations)

ggsave('output_data/genre_birthyear_line_compare.pdf', width = 20, height = 15, units = c('cm'))
ggsave('output_data/genre_birthyear_line_compare.png', width = 20, height = 15, units = c('cm'))

ggplot(data = percentage_musicians) + 
  aes(x = Birthyear, y = percentage_per_year) + 
  xlim(1938,1980) + 
  theme_light() + 
  labs(x = 'Birth year', y = "Percentage of artists", title = "Percentage of artists making music in each genre") +
  geom_area(aes(fill = Genre), alpha = 0.8, size = 0.5, colour = "black", stat = "identity")+ 
  geom_vline(aes(xintercept = start_date), linetype = 'dashed', data = generations) +
  geom_text(aes(x= start_date + 1, label= generation), y=2, hjust = 0, colour="white", angle=90, data = generations)

ggsave('output_data/genre_birthyear_stacked_compare.pdf', width = 20, height = 15, units = c('cm'))
ggsave('output_data/genre_birthyear_stacked_compare.png', width = 20, height = 15, units = c('cm'))
