#-*- coding:utf-8 -*-

import ushuffle

class Shuffle:
	def __init__(self):
		pass

	def readFasta(self, file):
		chr = "temp"
		chrseq = ""
		f = open(file, "r")
		for line in f:
			if line == "": break
			elif line[0] == ">":
				chr = line[1:].rstrip("\n")
			else:
				chrseq = chrseq+line.rstrip("\n")
		f.close()
		return chr, chrseq
	def sep(self, line, val = 50):
		count = 0
		while count < len(line):
			count = min(count+val, len(line))
			line = line[0:count]+"\n"+line[count:]
			count = count+1
		return line

	def simpleShuffleFasta(self, file):
		chrom, chrseq = self.readFasta(file)
		chrseq = chrseq.upper()
		out = ""
		while len(chrseq) > 0:
			if chrseq[0:4] == "N"*4:
				for i in range(0, len(chrseq)):
					if chrseq[i] == "N": continue
					else:
						out = out+chrseq[0:i]
						chrseq = chrseq[i:]
						break
			if chrseq.find("NNNN"):
				index = chrseq.index("NNNN")
				out = out+ushuffle.shuffle(chrseq[0: (index)], index+4, 3)
				chrseq = chrseq[(index):]
			else:
				out = out+ushuffle.shuffle(chrseq[0:], len(chrseq), 3)
				chrseq = ""
				break
		out = self.sep(out)
		f = open(dir+chrom+"_shuffle_3.fa", "w")
		f.write(">"+chrom+"\n")
		f.write(out)
		f.close()

def shuffleCrm(file):
	sh = Shuffle()
	sh.simpleShuffleFasta(chrfile, DIR)


if __name__=="__main__":
	argvs = sys.argv
	if len(argvs) >= 2:
		shuffleCrm(argvs[1])

