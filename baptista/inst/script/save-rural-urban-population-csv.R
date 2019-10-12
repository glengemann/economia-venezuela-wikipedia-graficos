library(tidyverse)
setwd("~/ProyectoGit/baptista")
wide_data <- read_csv("inst/extdata/rural-urban-population.csv")
tidy_data <- wide_data %>% 
  gather(year, population, -`Tipo de Población`)

save(tidy_data, file="data/rural_urban_population.rda", compress="xz")
