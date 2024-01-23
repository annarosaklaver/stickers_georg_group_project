library(tidyverse)
library(ggplot2)

data <- read_csv('jazz_birthyears.csv') |>
  filter(birthyear >= 1700)

#not necessary right now, but might be for other plots
musicians_per_year <- data |>
  transform(birthyear = as.numeric(birthyear)) |>
  group_by(birthyear) |>
  summarise(n = n()) |>
  filter(birthyear >= 1700)

ggplot(data = data) +
  aes(x = as.numeric(birthyear)) +
  geom_line(stat = "bin", binwidth = 5)