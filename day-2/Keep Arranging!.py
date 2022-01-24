def Harm(n):
    if(n==1):
        return 1
    else:
        return Harm(n-1) + 1/n

n = int(input())
four_harm = "{:.4f}".format(Harm(n))
print("Harmonic sum upto 4 decimal places:",four_harm)
