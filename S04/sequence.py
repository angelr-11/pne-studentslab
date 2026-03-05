from pathlib import Path

ADA = "./sequences/ADA.txt"
cont = Path(ADA).read_text()

split_cont = cont.split("\n",1)
body = split_cont[1]
single_line_body = body.replace("\n", "")

print ("Number of bases in ADA:", len(single_line_body))