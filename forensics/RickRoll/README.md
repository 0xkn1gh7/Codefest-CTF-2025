# RickRoll

Total Solves - 60

Final Points - 100

## Description
This song is actually pretty good. Anyways while giving CTFs I came across a rare tool I had never heard of. Pretty sure I would have documented this somewhere.

## Attachment

 - [chall.zip]('./attachment/chall.zip')
    
    - [chall.mp3](./files/chall.mp3)
    - ![cover.jpg](./files/cover.jpg)

## Writeup

On running exiftool on cover.jpeg file, you will find find an unusual artist.

```
exiftool cvoer.jpeg

...
Artist  : giveupplease
...
```

For finding the tool, you have to do a bit of OSINT about the author `0xkn1gh7`. A simple google search would lead to you to the [blog](https://0xkn1gh7.com/2024/06/20/Bitguard-Cybersecurity-Hackathon-2024-Writeups/#Challenge-14-GPay-or-OpSec). Going through the writeups you will come across [stegonaut](https://www.stegonaut.com/). Use the string from exiftool as password and you get the flag.

## Flag
`CodefestCTF{1e55_kn0wn_573g0_700l?}`
