



def twoPtForwardDiff(x,y):
    """
    Takes arrays x and y, and takes the derivative of adjacent elemnts. We use the forward differentiating method, which is the standard
    (yfinal - yinital)/(xfinal-xinital). For the last element we use the backwards differentiating method to find the value, 
    since there are no more elements after it. After we make these calculations, we store the derivatives in an array of the same size 
    as our input arrays.
    """
    
    dydx = np.zeros(y.shape,float)
    dydx[0:-1] = np.diff(y)/np.diff(x)
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx







def twoPtCenteredDiff(x,y):
    """
    Takes arrays x and y, and takes the derivative of adjacent elements. We take advantage of array slicing in order to accomplish
    the task of finding the center difference. We must subtract the cooresponding opposite elements of the perspective arrays and then 
    divide by the result in order to find the center difference. After we make the calculations, we store the result in an array of
    the same length as the input variables, and return it.
    """
    
    
    dydxc = np.zeros(y.shape,float)
    dydxc[0:-1] = (y[1:] - y[:-1])/(x[1:] - x[:-1])
    return dydxc



def fourPtCenteredDiff(x,y):
    """
    Takes arrays x and y, and finds the centered difference by taking four points instead of two. We use a complicated algorithm
    in order to find the numbers for the majority of the array, but cannot use them on four special points. These four points just
    happen to be the outermost points in the array, so we cannot take a centered difference by taking two elements on each side.
    Thus, we just take the centered difference of the innermost outside elements, take the backward difference of the last element, and
    take the forward difference of the first element. After we store all these results, we return the array.
    """
    
    
    dydx = np.zeros(y.shape,float)
    dycenter = twoPtCenteredDiff(x,y)
    dyforward = twoPtForwardDiff(x,y)
    dydx[2:-2] = (y[0:-4] - 8*y[1:-3] + 8*y[3:-1] - y[4:])
    dydx[0]= dyforward[1]
    dydx[1]= dycenter[1]
    dydx[-1]= (y[-1] - y[-2])/(x[-1] - x[-2])
    dydx[-2]= dycenter[-2]
    return dydx