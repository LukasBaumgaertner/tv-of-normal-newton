from dolfin import *
set_log_level(30)

import numpy as np
import time

def ADMM(AL, smooth_step, cb = None, max_outer_iter=1000, max_inner_iter=10, stepsize = 1e-4, verbose=False):
    AL.log([max_inner_iter, 0])
    for i in range(max_outer_iter): 
        if verbose:
            print("i outer = ", i)
        
        if AL.shape_first:
            stepsize, inner_iterations = smooth_step(AL, max_iter=max_inner_iter, stepsize=stepsize)
            
            AL.update_nonsmooth()
        
        else:
            AL.update_nonsmooth()
        
            stepsize, inner_iterations = smooth_step(AL, max_iter=max_inner_iter, stepsize=stepsize)
        
        AL.update_multipliers()
        
        if i % 20 == 0:
            AL.log([inner_iterations, i+1])
        
        
        AL.update_penalty_param()
        
        AL.finish_iteration()
        
        if cb != None:
            cb(AL, i)
            
        
    
    
    history_array = np.array(AL.history)
    history_array[:, 5] -= history_array[0,5]
    time_per_iteration = np.hstack([np.nan, history_array[1:,5]  - history_array[:-1, 5]])
    history_array = np.hstack( [history_array[:, :6], time_per_iteration[:, np.newaxis], history_array[:, 6:]])
    
    np.savetxt("history.txt", history_array)
