set terminal postscript landscape color enhanced "Helvetica" 12
set output "temperature.eps"
#set title ""
set datafile separator ";"
set datafile missing "NaN"

set timefmt "%s"
set xdata time

set ylabel "temperature [{/Symbol \260}C]"
set xlabel "time"
set yrange [0:40]

plot \
"0.dat" using 1:($2) t "sensor 1" with lines, \
"1.dat" using 1:($2) t "sensor 2" with lines, \
"2.dat" using 1:($2) t "sensor 3" with lines, \
"3.dat" using 1:($2) t "sensor 4" with lines, \
"4.dat" using 1:($2) t "sensor 5" with lines, \
"5.dat" using 1:($2) t "sensor 6" with lines, \
"6.dat" using 1:($2) t "sensor 7" with lines, \
"7.dat" using 1:($2) t "sensor 8" with lines, \
"8.dat" using 1:($2) t "kombi" with lines

