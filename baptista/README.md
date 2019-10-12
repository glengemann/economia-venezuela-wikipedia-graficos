## Example Rural Urban Population

```r
library(baptista)
data(rural_urban_population)

tidy_data %>% 
  mutate(population = population/100000) %>%
  ggplot(aes(year, population, color = `Tipo de Población`)) + 
    geom_point()
```

## Example 

```r
library(baptista)
library(ggplot2)

data(movimiento_demografico)

ggplot(data) + 
  geom_point(aes(`Año`, `Nacimientos`)) + 
  geom_point(aes(`Año`, `Defunciones`))
```

## Example Movimiento Urbanizatorio

```r
data %>% 
  mutate("Población rural" = `Población censal` - `Población urbana`) %>% 
  ggplot(aes(year, `Población urbana`)) + 
    geom_point()
```
