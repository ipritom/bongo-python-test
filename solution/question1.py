def print_depth(data,depth=0):
    ''' 
    Input: dictionary
    Print Dictionary Keys and Depths
    '''
    #raise TypeError
    if isinstance(data,dict)==False:
         raise TypeError("Input data type must be dictionary")

    #measure depth
    for key,value in data.items():
        print(key,depth+1)
        if isinstance(value,dict):
            print_depth(value,depth=depth+1)

     


if __name__=='__main__':
     a = {
          "key1": 1,
          "key2": {
          "key3": 1,
          "key4": {
          "key5": 4
          }
          }
          }
     b = {
          "key1": 1,
          "key2": {
          "key3": 1,
          "key4": {
          "key5": 4,
          "key6":{"key7":6}
          }
          }
          }          
     print_depth(a)
     print_depth(b)