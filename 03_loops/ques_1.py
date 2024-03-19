numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10];

cnt = 0;

for num in numbers :
    print(num,end="-");
    if num > 0 :
        cnt += 1;

print("pos nums are : ", cnt);