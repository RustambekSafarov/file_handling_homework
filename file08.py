def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    l = 0
    print(data.split())
    for i in data.split():

        if i.isdigit():
            if float(i) > l:
                l = float(i)
    return l
print(main(open('txt_file/data08.txt').read()))
