
import argparse

def function() -> None:

    parser=argparse.ArgumentParser()

    parser.add_argument(help='Enter a string',dest='string',type=str)   
    parser.add_argument(help='Enter a integer',dest='number',type=int)   
    parser.add_argument(help='Enter a float',dest='float',type=float)   

    args = parser.parse_args()

    strname= args.string
    numbers= args.number  
    floatnum = args.float	

    print("string is: ", strname) 	
    print("number is: ",numbers)
    print("float number is: ",floatnum)

if __name__=='__main__': 	
    function()