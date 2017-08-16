
def dategenerator(start, end):
    """Simple data range iterator that takes two datetime dates and acts an iterator"""
    current = start
    while current <= end:
        if current < end:
            yield current
            current += timedelta(days=1)
        else:
            yield current
            break