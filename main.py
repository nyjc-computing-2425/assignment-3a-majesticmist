nric = input('Enter an NRIC number: ')

# Type your code below
validity = 1
if nric[0] not in "STPG" :
  validity *= 0 

if not(nric[-1].isalpha):
  validity *= 0



weight = [0,2,7,6,5,4,3,2]
digit_check_ST = 'JZIHGFEDCBA'
digit_check_FG = 'XWUTRQPNMLK'

digits = nric[1:8]
if digits.isdecimal():
  sum = 0
  sum = sum + int(nric[1])*weight[1]
  sum = sum + int(nric[2])*weight[2]
  sum = sum + int(nric[3])*weight[3]
  sum = sum + int(nric[4])*weight[4]
  sum = sum + int(nric[5])*weight[5]
  sum = sum + int(nric[6])*weight[6]
  sum = sum + int(nric[7])*weight[7]
  sum = sum + 4*(nric[0]in"TG")
  sum = sum%11
  if nric[0] in "ST":
    if digit_check_ST[sum] != nric[-1]:
      validity *= 0

  if nric[0] in "FG":
    if digit_check_FG[sum] != nric[-1]:
      validity *= 0
else:
  validity *=0



if validity == 0:
  print("NRIC is invalid.")
else:
  print("NRIC is valid.")


