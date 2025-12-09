X, Y = input().split()
def mapping(X, Y):
    A = list(X)
    B = list(Y)

    n = len(A)
    M = [True]*n

    for i in range (n):
        temp = A[i]
        for j in range (i, n):
            if M[j] and A[j] == temp:
                A[j] = B[i]
                M[j] = False
    return A == B
if mapping(X, Y) and mapping(Y, X):
    print("true")
else:
    print("false")

            


