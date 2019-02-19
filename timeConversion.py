def timeConversion(s):
    z = s.split(':')
    if '' in z[2]:
        print("Hello")
        z[0] = str(int(z[0]) + 12)
        z[2] = z[2][:-2]
        t = (':'.join(str(i) for i in z))
        return(t)
    if 'a' in z[2]:
        z[2] = z[2][:-2]
        t = (':'.join(str(i) for i in z))
        return(t)
if __name__ == '__main__':
    d = timeConversion('07:05:45PM')
    print(d)
