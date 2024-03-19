n = 40;

sum = 0;
sum_even = 0;

for i in  range(1, n) :
    print(i, end=' ');
    sum += i;
    if i % 2 == 0:
        sum_even += i;

print(sum);
print(sum_even);