import glob
import doctest

result = doctest.testfile('__grade__.txt', report = True, verbose = True)
a,b = result
print('\n>>>>  ', result, ' <<<<\n')
open('__grade__', 'w').write(str(round(float(b-a) / float(b) * 5.0 , 1)))




