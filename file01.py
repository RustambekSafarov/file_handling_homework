def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    x = data.split(',') 
    y = []
    for i in x:
        y.append(int(i))
    return y


print(main(open('txt_file/data01.txt').read()))