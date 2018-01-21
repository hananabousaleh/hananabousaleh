# How many lines in the text?
wc -l shakespeare-macbeth-46.txt

# How many lines contain the string LADY MACBETH?
grep -c 'LADY MACBETH' shakespeare-macbeth-46.txt

# How many lines contain both strings LADY MACBETH and must?
grep -c 'LADYMACBETH|must' shakespeare-macbeth-46.txt

# What is the 8th word in the line containing strings LADY MACBETH and blood?
