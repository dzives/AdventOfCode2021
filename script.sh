for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
do
	mkdir "Day$i"
	cd "Day$i"
	echo "f = open('input.txt')
x = f.readlines()
f.close()" > "app1.py"
	echo "f = open('input.txt')
x = f.readlines()
f.close()" > "app2.py"
	type nul > "input.txt"
	cd ..
done