import numpy as np

# Algorithm 2 with possible projection (BC) for variables that are not optimized.
def truncatedCG(b, A_action, M_solve, bc = None):
    
    r = -b.copy()
   
    w = 0*b.copy()

    M_inv_r = r.copy()
    M_solve(M_inv_r,r)    
    if bc != None:
        bc.apply(M_inv_r)

    p = -M_inv_r.copy()
    r_M_inv_r = r.inner(M_inv_r)
    
    tol = min(0.5,np.sqrt(np.sqrt(r_M_inv_r)))*np.sqrt(r_M_inv_r)
    k = 1
    while np.sqrt(r_M_inv_r) >= tol:
      Ap = A_action(p)
      if bc != None:
          bc.apply(Ap)

      gamma = p.inner(Ap)
            
      if gamma <= 0:
        if k == 1:
          return p, False
        else:
          return w, True
      alpha = r_M_inv_r / gamma

      w.axpy(alpha, p)


      r.axpy(alpha, Ap)

      r_M_inv_r_old = r_M_inv_r
      M_solve(M_inv_r, r)
      if bc != None:
          bc.apply(M_inv_r)

      r_M_inv_r = r.inner(M_inv_r)
      beta = r_M_inv_r / r_M_inv_r_old

      p *= beta
      p.axpy(-1, M_inv_r)
      k += 1 
    
    return w, True





