def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    x = []
    for i in data:
        if i.isdigit():
            x.append(i)

    
    return x
    

print(main(open('txt_file/data03.txt','r+').read()))
