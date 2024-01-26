library(tidyverse)
library(ggplot2)
library(ggpubr)

data_billboard <- read_csv('output_data/grouped_billboard_data.csv') |>
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

#not necessary right now, but might be for other plots
genre_counts_per_year_artists <- data_billboard |>
  group_by(Date, Genre, Artist) |>
  summarise(n = n()) |>
  group_by(Date, Genre) |> 
  summarise(n = n()) |> 
  group_by(Date) |>
  mutate(percentage = n/sum(n) * 100) |>
  ungroup()

billboard_artists <- ggplot(data = genre_counts_per_year_artists) + 
  aes(x = Date, y = percentage) + 
  xlim(1958,2000) + 
  theme_light() + 
  labs(x = 'Year', y = "Percentage of Hot 100 songs", title = "Percentage of Billboard Hot 100 artists in each genre") +
  geom_area(aes(fill = Genre), alpha = 0.8, size = 0.5, colour = "black", stat = "identity")

data_wikipedia <- read_csv('output_data/grouped_genre_and_career_start.csv') |>
  transform(Career_Start = as.numeric(Career_Start)) |>
  filter(Career_Start >= 1850) |>
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

percentage_musicians <- data_wikipedia |>
  transform(Career_Start = as.numeric(Career_Start)) |>
  filter(Career_Start >= 1900) |>
  group_by(Career_Start, Genre) |>
  summarise(n = n()) |>
  group_by(Career_Start) |>
  mutate(percentage_per_year = n/sum(n) * 100) |>
  ungroup()

wikipedia <- ggplot(data = percentage_musicians) + 
  aes(x = Career_Start, y = percentage_per_year) + 
  xlim(1958,2000) + 
  theme_light() + 
  theme(legend.position = "none") +
  labs(x = 'Start of career (year)', y = "Percentage of artists", title = "Percentage of artists making music in each genre") +
  geom_area(aes(fill = Genre), alpha = 0.8, size = 0.5, colour = "black", stat = "identity") 

#not necessary right now, but might be for other plots
genre_counts_per_year <- data_billboard |>
  group_by(Date, Genre) |>
  summarise(n = n()) |>
  group_by(Date) |>
  mutate(percentage = n/sum(n) * 100) |>
  ungroup()

billboard <- ggplot(data = genre_counts_per_year) + 
  aes(x = Date, y = percentage) + 
  xlim(1958,2000) + 
  theme_light() + 
  theme(legend.position = "none") +
  labs(x = 'Year', y = "Percentage of Hot 100 songs", title = "Percentage of Billboard Hot 100 songs in each genre") +
  geom_area(aes(fill = Genre), alpha = 0.8, size = 0.5, colour = "black", stat = "identity")

ggarrange(wikipedia, billboard_artists, widths = c(4,5), ncol = 2)
ggsave('output_data/comparison.pdf', width = 28, height = 10, units = c('cm'))
ggsave('output_data/comparison.png', width = 28, height = 10, units = c('cm'))
