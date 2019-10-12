library(tidyverse)
setwd("~/ProyectoGit/baptista")
data <- read_csv("inst/extdata/f-4-movimiento-urbanizatorio.csv")

save(data, file="data/f_4_movimiento_urbanizatorio.rda", compress="xz")
