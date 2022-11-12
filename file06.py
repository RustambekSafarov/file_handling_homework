def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    y = []
    for i in data.split("\n"):
        y.append(len(i))
    return y
# Read data from file
print(main(open('txt_file/data06.txt').read()))