from pythonping import ping

ip_check = input('ip :')

print('-'*60)

ping(ip_check, verbose=True)

print('-'*60)
