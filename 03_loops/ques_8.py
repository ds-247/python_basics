num = 17;

if num == 1 : 
    print("not prime"); 
    exit();

i = 2;
prime = True

while i*i < num :
    if num % i*i  == 0:
        prime = False
    i += 1;

if prime :
    print("prime");
else : 
    print('not prime')