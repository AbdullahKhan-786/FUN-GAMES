import random
x=['rock','paper','scissor']
us=0
cs=0
while True:
    ci=random.choice(x)
    ui=str(input('Please enter your weapon'))
    if ui== 'q':
      break
    elif (ui=='rock' and ci=='scissors')or(ui=='scissors' and ci=='paper')or(ui=='paper' and ci=='rock'):
        print('User you have won against the computer')
        us=us+1
    elif (ui=='scissors' and ci=='rock')or( ui=='rock' and ci=='paper')or(ui=='paper' and ci=='scissors'):
        print('User you have lost against the computer')
        cs=cs+1
    elif(ui=='rock' and ci=='rock')or(ui=='paper' and ci=='paper')or(ui=='scissors' and ci=='scissors'):
        print('User and the computer got the same weapon so it is a tie')
    else:
        print('Not in the list')
                   
