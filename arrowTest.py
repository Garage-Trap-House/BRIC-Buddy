import arrow as arrow

def currentTime():
    currentTime = arrow.now('US/Pacific').for_json()
    return currentTime