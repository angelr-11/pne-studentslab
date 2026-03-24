from pathlib import Path

FILENAME = "./sequences/RNU6_269P.txt"
from pathlib import Path

FILENAME = "./sequences/RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()

split_contents = file_contents.split("\n")

header = split_contents[0]

print(header)