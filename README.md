# caesar_solver
# Caesar Solver written by Denartha
# The Caesar cipher is a very simple substitution cipher.
# I wrote this tool to assist in CTF competitions where the Caesar cipher is a regular component. While there is a myriad of solvers online, I had difficulty finding one which would show all possible shift patterns.
# 
# Lets say you have the following block of ciphertext:
#
# Cqn zdrlt rln lanjv bjwmfrlq jwmaxrm cjkunc sdvynm xena cqn ujih frwmxfb wrwnch oren JCV vjlqrwn 
#
# To use caesar solver, select a word from the ciphertext and issue the command:
# python caesar_solver.py -b bjwmfrlq
#
# It will print the following output:
# 0: bjwmfrlq
# 1: ckxngsmr
# 2: dlyohtns
# 3: emzpiuot
# 4: fnaqjvpu
# 5: gobrkwqv
# 6: hpcslxrw
# 7: iqdtmysx
# 8: jreunzty
# 9: ksfvoauz
# 10: ltgwpbva
# 11: muhxqcwb
# 12: nviyrdxc
# 13: owjzseyd
# 14: pxkatfze
# 15: qylbugaf
# 16: rzmcvhbg
# 17: sandwich
# 18: tboexjdi
# 19: ucpfykej
# 20: vdqgzlfk
# 21: werhamgl
# 22: xfsibnhm
# 23: ygtjcoin
# 24: zhukdpjo
# 25: aivleqkp
#
# Looking down the list the only word which looks like english is number 17 which is sandwich. To decode the rest of the ciphertext, paste it into a text file and run the following command:
# python caesar.py -f filename.txt 17
# 
# The output should look like the following:
# 
# The quick ice cream sandwich android tablet jumped over the lazy windows ninety five ATM machine 
