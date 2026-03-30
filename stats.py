from statistics import mean, median, multimode

def summarise(data):
    """Function that accepts list of numbers and returns a dictionary with min, max, mean, median,
    count, and mode values of the list.
    """
    summary = {
        'min': min(data),
        'max': max(data),
        'count': len(data),
        'mean': mean(data)
       
    }
    return summary


if __name__ == "__main__":
    data = [10, 20, 100, 80, 50, 30, 60, 50, 40]
    stats = summarise(data)
    print(stats)