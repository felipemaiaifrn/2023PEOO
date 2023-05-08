ab=input().split()
a=int(ab[0])
b=int(ab[1])

if a>b :
  resto = a%b
  if resto == 0 :
    print('Sao multiplos')
  else :
    print('Nao sao multiplos')

if b>a :
  resto = b%a
  if resto == 0 :
    print('Sao multiplos')
  else :
    print('Nao sao multiplos')

if a==b :
  resto = b%a
  if resto == 0 :
    print('Sao multiplos')
  else :
    print('Nao sao multiplos')