import pywhatkit as kt

import getpass as gp

p_num = gp.getpass(prompt='phoneNumber: ', stream=None)

msg = input('Enter the text you want to send \n')
hour = int(input('Enter the time in hour \n'))
minute = int(input('Enter the time in minutes \n'))
kt.sendwhatmsg(p_num,msg,hour,minute)