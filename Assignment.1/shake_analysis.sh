# How many lines in the text?
w1=$(wc -l < shakespeare-macbeth-46.txt)
w2=$(($w1 + 1))
echo $w2

# How many lines contain the string LADY MACBETH?
x=$(grep -c 'LADY MACBETH' shakespeare-macbeth-46.txt)
echo $x

# How many lines contain both strings LADY MACBETH and must?
y=$(grep -c 'LADY MACBETH.*must\|must.*LADY MACBETH' shakespeare-macbeth-46.txt)
echo $y

# What is the 8th word in the line containing strings LADY MACBETH and blood?
z=$(grep 'LADY MACBETH.*blood\|blood.*LADY MACBETH' shakespeare-macbeth-46.txt)
echo $z
