from dolfin import dot, grad, div, inner, outer, sqrt, tr, as_vector, le, conditional, acos
from ufl import Identity as identity, atan_2



#shape identities
def dn(n,V):
    return -dot(grad(V).T,n)
    
def ddn(n, V, W):
    return dot(grad(V).T, dot(grad(W).T, n)) + dot(grad(W).T, dot(grad(V).T, n)) - n*inner( dot(grad(V).T, n), dot(grad(W).T, n))

def dtE(tE, V):
    return dot(grad(V), tE) - tE*inner(tE, dot(grad(V),tE))
    
def dmu(mu, tE, V):
    return dot(grad(V), mu) - mu*inner(mu, dot(grad(V), mu)) -  tE*inner(mu, dot(grad(V)+grad(V).T, tE))

def divE(tE, V):
    return inner(tE, dot(grad(V), tE))('+')

def Hedge(tE,V,W):
    return (-divE(tE,V)*divE(tE,W)+inner(dot(grad(W), tE), dot(grad(V), tE))('+'))

def Hsurf(n,V,W):
    return (div(V)*div(W) - tr(dot(grad(V), grad(W))) + inner(dot(grad(V).T, n), dot(grad(W).T, n)))




def max(a,b):
    return conditional( le(a, b), b, a)

def norm(v):
    return sqrt(inner(v,v))

def sign(a):
    return conditional(le(a , -a), -1, 1)

def angle(a,b):
    return acos(conditional(le(inner(a,b), 1), inner(a,b), 1))

def angle2(a,b):
    return 2*atan_2(sqrt(inner(a-b, a-b)), sqrt(inner(a+b, a+b)))

def logmu(n, mu):
    return sign(inner(n('-'), mu('+')))*angle2(n('+'), n('-'))

def dlogmu(n, mu, V):
    return -inner(dn(n, V)('+'), mu('+')) - inner(dn(n, V)('-'), mu('-'))

def Hlogmu(n,mu,tE,V, W):
    #res = -inner(dmu(mu, tE, W)('+'), dn(n,V)('+')) - inner(dmu(mu, tE, W)('-'), dn(n,V)('-'))
    res = -inner(dot(grad(W), tE)('+'), dot( outer(mu('+'), n('+'))+outer(mu('-'), n('-')), dot(grad(V), tE)('+')))
    res += -inner(mu('+'), ddn(n, V, W)('+'))-inner(mu('-'), ddn(n, V, W)('-'))
    return res
    
    
def log(n, mu):
    return logmu(n, mu)*mu('+')
    
def dlog(n, mu, tE, V):
    return dlogmu(n, mu, V)*mu('+') + logmu(n,mu)*dmu(mu, tE, V)('+')
    
