# glengemann v0.1
# INPC, 25 de diciembre de 2014
# Boletin Indicadores Semanales, semana #52
# www.bcv.org.ve
# wxt
#set terminal wxt size 850,462 enhanced font 'Verdana,10' persist
# png
set terminal pngcairo size 850,362 enhanced font 'Verdana,10'
set output 'inpc_venezuela_2008_2014.png'
# svg
set terminal svg size 850,262 fname 'Verdana, Helvetica, Arial, sans-serif' \
fsize '10'
set output 'inpc_venezuela_2008_2014.svg'

set key top left
set xlabel 'Años'
set ylabel 'Porcentajes'

set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 5 ps 1   # --- blue
plot 'inpc_venezuela_2008_2014.dat' index 0 with linespoints ls 1 title 'INPC'