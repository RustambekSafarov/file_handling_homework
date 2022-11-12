def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    x = data.read()
    # for i in data.split():
        
    return data.write(x)

# Read data from file
print(main(open('txt_file/data02.txt','r+')))
