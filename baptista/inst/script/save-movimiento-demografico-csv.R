library(tidyverse)
setwd("~/ProyectoGit/baptista")
data <- read_csv("inst/extdata/movimiento-demografico.csv")

save(data, file="data/movimiento_demografico.rda", compress="xz")
