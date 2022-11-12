def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    d = 0
    y = []
    for i in data:
        for x in i:
            if x != '\n':
                d += 1
        y.append(d)
        d = 0
            
    return y
# Read data from file
print(main(open('txt_file/data06.txt').readlines()))