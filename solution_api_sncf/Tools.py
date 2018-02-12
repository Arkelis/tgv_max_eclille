def total_seconds(duration, format):
    if format == "h%m":
        return int(duration[3:])*60+int(duration[:2])*3600

def time_difference(t1,t2,format):
    """
    Calculate the duration between two dates.
    :param t1: string as "14:02" for example
    :param t2: string
    :param format: format of the date
    :return: duration in string
    """
    if format == "h%m":
        if len(t1)==4:
            t1="0"+t1
        if len(t2)==4:
            t2="0"+t2
        t1=total_seconds(t1,format)
        t2=total_seconds(t2,format)
        d=t2-t1
        h=int(d/3600)
        m=int((d/3600-h)*60)+1
        return str(h)+":"+str(m)
