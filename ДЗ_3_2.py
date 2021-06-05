import hashlib as h


salt = 'clear_sky'
password = input('Введите пароль: ')
hash_obj = h.sha256(salt.encode() + password.encode())
print(hash_obj.hexdigest())
with open('text.txt', 'w') as f:
    f.write(hash_obj.hexdigest())
pass_2 = input('Введите пароль еще раз: ')
# hash_obj_2 = h.sha256(pass_2.encode() + salt.encode()) при изменении порядка вложения хеши получаются разные
hash_obj_2 = h.sha256(salt.encode() + pass_2.encode())
print(hash_obj_2.hexdigest())
with open('text.txt') as f:
    hash_line = f.read()
    if hash_line == hash_obj_2.hexdigest():
        print('Пароль верный')
    else:
        print('Пароли отличаются')
