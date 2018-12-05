print("\n\n\t\t<<<CALCULATOR>>>");
def add(a,b):
    return a+b;
def mul(a,b):
    return a*b;
def sub(a,b):
    return a-b;
def mod(a,b):
    return a%b;
def div(a,b):
    return a/b;

ch='y';
while ch=='y' or ch=='Y':
    a=int(input("ENTER A  :"));
    b=int(input("ENTER B  :"));
    c=input("\n\nenter operation (+,-,*,%,/)  :");
    if c=='+':
        print("\n",a,"+",b,"=",add(a,b));
    
    elif c=='-':
        print("\n",a,"-",b,"=",sub(a,b));
    
    elif c=='*':
        print("\n",a,"*",b,"=",mul(a,b));
    
    elif c=='%':
        print("\n",a,"%",b,"=",mod(a,b));
    
    elif c=='/':
        print("\n",a,"/",b,"=",div(a,b));

    else:
        print("\n\n!!!INVALID OPERATOR!!!");
    print("_______________________________________________")
    ch=input("\n\nDO YOU WANT TO CONTINUE (y/n) :")

