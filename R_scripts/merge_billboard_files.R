
library (tidyverse)
song_year<- read_csv("Hot_Stuff.csv")
song_genre <- read_csv("Hot 100 Audio Features.csv")

song_year_genre <- song_year |>
  inner_join(song_genre)

write_csv(song_year_genre, "merged_billboard_data.csv")