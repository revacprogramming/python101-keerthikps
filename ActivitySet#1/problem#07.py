# Strings
text = "X-DSPAM-Confidence:    0.8475"
pos=text.find(":")
peice=text[pos+1:] #string slicing
convert=float(peice)
print(convert)

