
def sleep_in(weekday,vacation):
    if not weekday or vacation:
        return True
    else:
        return False

answer = sleep_in(True,False)
print 'It is a weekday: ' +str(answer)
print 'It is a weekday, but vacation: '+str(sleep_in(True,True))
print 'It is neither weekday, nor vacation: '+str(sleep_in(False,False))
