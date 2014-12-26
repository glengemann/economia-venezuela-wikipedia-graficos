# glengemann v0.1
# wxt
#set terminal wxt size 350,262 enhanced font 'Verdana,10' persist
# png
set terminal pngcairo size 350,262 enhanced font 'Verdana,10'
set output 'empleados_pdvsa.png'
# svg
#set terminal svg size 350,262 fname 'Verdana, Helvetica, Arial, sans-serif' \
#fsize '10'
#set output 'battery.svg'

set xlabel 'Anos'
set ylabel 'Miles'

set style line 1 lc rgb '#dd181f' lt 1 lw 2 pt 5 ps 1   # --- red
plot 'empleados_pdvsa.dat' index 0 with linespoints ls 1 title 'Empleados'