#magic dates
print('bienvenue chez le date du magique')
def magic_dates(year):
    '''
this function is created to check if a specific date is pecuilar(or special) in a sorts of way
    '''
    day = int(input('enter day: '))
    month = input('enter month: ')
    cal = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6,
           'July':7, 'August':8, 'September':9,
           'October':10, 'November':11, 'December':12}
    if month in cal:
        y = year % 100
    if cal[month]*(day) == y:
        return True
    else:
        return False

year = int(input('enter year: '))
print(magic_dates(year))
def count_magic(ycount):
    '''
this function is created on the basis of generate the total number of possible
magic dates in a year by passing the outer function into the inner function
    '''

    idn = {'January':(31,1), 'February':(28,2), 'March':(31,3), 'April':(30,4), 'May':(31,5), 'June':(30,6), 'July':(31,7),
          'August':(31,8), 'September':(30,9), 'October':(31,10), 'November':(30,11), 'December':(31,12)}
    lim = []
    for mo in idn.keys():
        for da in range(1, idn[mo][0] + 1):
              t = ycount % 100
              if idn[mo][1]*(da) == t:
                 v = mo + str(da) + ',' + str(count)
                 lim += v
        return lim

ycount = input('enter count: ')
print(count_magic(ycount))
print('hope we made it finally')
