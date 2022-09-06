import pyinputplus as pyip
import random , time

numberOfQuestions = 10
correctAnswers = 0 

for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = '#%s: %s x %s ='%(questionNumber,num1,num2)
    
    try:
        #Right answers are handled by allowRegexes
        #Wrong answers are handled by blockRegexes,with a custom message.
        pyip.inputStr(prompt,allowRegexes=['^%s$' %(num1 * num2)],blockRegexes=[('.*','Incorrect')],timeout=8,limit=3)

        # ('.*') - Matches every possible strings 
    
    except pyip.TimeoutException:
        print('Out of Time!')

    except pyip.RetryLimitException:
        print('Out of tries')

    else:
        #this block runs if no exceptions were raised in the try block
        print('Correct!')
        correctAnswers+=1
        time.sleep(1)#Brief Pause to let user see result

print('Score:%s / %s' %(correctAnswers,numberOfQuestions))

