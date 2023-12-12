class A(): #Base class
    #1.1  Property
    bloodGroup = 'A+ve'
    #1.2  Constructor
    #1.3  Method
    pass

class B(A): #Base class
    #1.1  Propert
    #1.2  Constructor
    #1.3  Method
    pass

class C(B): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class D(C): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class E(D): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class F(E): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class G(F): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class H(G): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class I(H): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class J(I): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class K(J): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class L(K): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class M(L): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class N(M): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class O(N): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class P(O): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class Q(P): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class R(Q): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class S(R): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class T(S): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class U(T): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class V(U): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class W(V): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class X(W): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class Y(X): #Base class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    pass

class Z(H): # derived class
    #1.1  Property
    #1.2  Constructor
    #1.3  Method
    def getMyBloodGroup(self):
        print(f"My Blood Group is {self.bloodGroup}")
    pass
# Create Class Object
# We always Create object of child class
co = Z()
co.getMyBloodGroup() # classObject.method
