password = 'slfklsfj';
pass_len = len(password);

if pass_len < 6:
    strength = 'weak';
elif pass_len < 9:
    strength = 'normal';
else :
    strength = 'strong';

print('strength of pass is :', strength);