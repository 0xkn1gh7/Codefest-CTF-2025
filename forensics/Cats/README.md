# Cats

Total Solves - 162

Final Points - 100

## Description
Because Events Head said "NO CATS"

## Attachment
![chall.jpg](./attachments/chall.jpg)

## Writeup

The image has been treated with [steghide](https://steghide.sourceforge.net/). This can be verified using 

```bash
stegseek --seed chall.jpeg
```

Then you can easily crack the password using [stegseek](https://github.com/RickdeJager/stegseek) and [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt).

```bash
stegseek --crack -sf chall.jpeg -wl rockyou.txt
```

## Flag
`CodefestCTF{573gh1de_ch4ll_m30w}`
