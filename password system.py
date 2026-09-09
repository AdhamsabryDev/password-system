tries=4

thecorrectpassword='Adhamsabry1712'

theinputpassword=input('enter the password  ')

while thecorrectpassword != theinputpassword:
    tries -= 1

    if tries==0:
      print('pls try later')

      break

    print(f"wrong password { 'last' if tries == 1 else tries } chanses later")
    theinputpassword=input('enter the password  ')

else:
    print('correct password')






































