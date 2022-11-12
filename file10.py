def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    y = []
    l = 0
    for i in data.split("\n"):
        y.append(len(i))
    for i in y:
        if i > l:
            l = i
    return l
# Read data from file
print(main(open('txt_file/data10.txt').read()))