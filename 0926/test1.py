temp = 'R_emaildomain_id_18'

print(temp.split('_',2))
print(temp.split('_',2)[0])
feature = temp.split('_',2)[0] + '_' + temp.split('_',2)[1] + '__' + temp.split('_',2)[2]
print(feature)