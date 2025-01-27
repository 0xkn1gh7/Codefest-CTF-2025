# Vault

Total Solves - 124

Final Points - 100

## Description
Can you break the vault?

## Writeup
Initially you are given a jwt token

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZ3Vlc3QifQ.KimmF-GuaVVyqXUm4pqvFrnQFkxnin5qwkrtgQUX4iE
```

This toke corresponds to following data

```
{
  "user": "guest"
}
```
It becomes clear that changing user to something like "admin" would give the flag. However the jwt is signed using HS256 algorithm. After trying different attacks, one should realise the token is not vulnerable to implementation based attacks and the secret key is needed. To bruteforce the key, using [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) and [hashcat](https://github.com/hashcat/hashcat) is the best approach.

```
hashcat -a 0 -m 16500 eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZ3Vlc3QifQ.KimmF-GuaVVyqXUm4pqvFrnQFkxnin5qwkrtgQUX4iE rockyou.txt
```
This gives the key as `rafa2986`.

Now just change the user and sign the jwt token with the secret found.

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE3Mzc5NzQ3Mzl9.h2De8Ec5Fl7pjBth7SrEfJSrzMe0TqG-5AnqTSpyIJc
```

Using this token reveals the flag!

## Flag
`CodefestCTF{jwt_secr3t_brut3f0rce_\[0-9a-zA-Z\]{9}}`
