from pathlib import Path

U5 = "./sequences/U5.txt"
contents = Path(U5).read_text()

split_c = contents.split("\n",1)
body = split_c[1]
print ("Body of the U5.txt file:\n"+body)
