# glengemann v0.1
# wxt
#set terminal wxt size 350,262 enhanced font 'Verdana,10' persist
# png
set terminal pngcairo size 350,262 enhanced font 'Verdana,10'
set output 'battery.png'
# svg
#set terminal svg size 350,262 fname 'Verdana, Helvetica, Arial, sans-serif' \
#fsize '10'
#set output 'battery.svg'

set xlabel 'Anos'
set ylabel 'Millones $'

set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 ps 2.5   # --- blue
set style line 2 lc rgb '#dd181f' lt 1 lw 2 pt 5 ps 1   # --- red
set style line 3 lc rgb '#ff0000' lt 1 lw 2 pt 5 ps 1   # --- red
plot 'deuda_publica_venezuela.dat' index 0 with linespoints ls 1 title 'Deuda Total', \
     '' index 1 with linespoints ls 2 title 'Deuda Interna', \
     '' index 2 with linespoints ls 3 title 'Deuda Externa'
#set terminal wxt size 350,262 enhanced font 'Verdana,10' persist
#set terminal svg size 350,262 fname 'Verdana' fsize 10
#set output "deuda_publica_venezuela.svg"
#set output "deuda_publica_venezuela.png"