x=['rock','paper','scissor',
   'quit']
us1=0
us2=0
while True:
    ui1=str(input('User1, Please enter your weapon'))
    ui2=str(input('User2, Please enter your weapon'))
    if ui1== 'quit':
      break
    if ui2== 'quit':
      break
    elif (ui1=='rock' and ui2=='scissors')or(ui1=='scissors' and ui2=='paper')or(ui1=='paper' and ui2=='rock'):
        print('User1 you have won against the uer2')
        us1=us1+1
    elif (ui1=='scissors' and ui2=='rock')or( ui1=='rock' and ui2=='paper')or(ui1=='paper' and ui2=='scissors'):
        print('User1 you have lost against the user2')
        us2=us2+1
    elif(ui1=='rock' and ui2=='rock')or(ui1=='paper' and ui2=='paper')or(ui1=='scissors' and ui2=='scissors'):
        print('User and the computer got the same weapon so it is a tie')
    else:
        print('Not in the list')
                   
