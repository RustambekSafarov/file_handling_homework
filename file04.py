def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    x = []
    for i in data:
        if not i.isdigit():
            x.append(i)
    return x
    
# Read data from file
print(main(open('txt_file/data04.txt','r+').read()))
