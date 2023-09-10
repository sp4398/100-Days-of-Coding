def kthChildNthGeneration(n, k):
    # Write your code here
    if n==1 or k==1:
        return "Male"

    parent=(k+1)//2
    parent_gender= kthChildNthGeneration(n-1,parent)
    if k==(2*parent)-1:
        return parent_gender
    else:
        if parent_gender=="Male":
            return "Female"
        else:
            return "Male"
