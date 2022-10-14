import bcrypt

passwd = b'nick_baker_etc'

salt_1 = bcrypt.gensalt()
salt_2 = bcrypt.gensalt()

hashed_1 = bcrypt.hashpw(passwd, salt_1)
hashed_2 = bcrypt.hashpw(passwd, salt_2)

print(salt_1)
print(salt_2)

print()

print(hashed_1)
print(hashed_2)

print()

result_1 = bcrypt.checkpw(b'secret', hashed_1)
result_2 = bcrypt.checkpw(b'secret', hashed_2)

print(result_1)
print(result_2)

