def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    d = 0
    nd = 0
    x = []
    for i in data:
        if not i.isdigit():
            nd += 1
        if i.isdigit():
            d += 1
    x.append(d)   
    x.append(nd)
    return x


    
# Read data from file
print(main(open('txt_file/data05.txt').read()))