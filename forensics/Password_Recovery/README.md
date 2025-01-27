# Password Recovery

Total Solves - 57

Final Points - 100

## Description
Back in 2019, I wrote a secret and encrypted it using a password on Republic Day of India. Now I forgot the password :(

I only have the passgen utility I used and the encrypted file. Can you help me?

## Attachment
- [encrypted.zip](./attachment/encrypted.zip)
- [passgen]('./attachment/passgen')

## Writeup

> The challenge was inspired from [this](https://youtu.be/o5IySpAkThg) video.

On reverse engineering passgen utlity using any reverse engineering tool you will come across an output like this

```C
// ghidra generated output

local_58 = 0x6867666564636261; //abcdefgh
local_50 = 0x716f6e6d6c6b6a69; //ijklmnoq
local_48 = 0x7977767574737270; //prstuvwy
local_40 = 0x464544434241787a; //zxABCDEF 
local_38 = 0x4e4d4c4b4a494847; //GHIJKLMN
local_30 = 0x5554535250514f; //OQPRSTU
uStack_29 = 0x59; //Y
uStack_28 = 0x323130585a5657; //WVZX012
local_21 = 0x39383736353433; //3456789
tVar2 = time((time_t *)0x0); // Current time is taken
srand((uint)tVar2); // Passed into srand
for (local_6c = 0; local_6c < 0xf; local_6c = local_6c + 1) { // Loop of 15 characters
iVar1 = rand(); // rand is used
local_68[local_6c] = *(undefined *)((long)&local_58 + (long)(iVar1 % 0x3e)); // Offset of generated value mod 62
}
local_59 = 0;
printf("[*] HERE IS YOUR SECURELY GENERATED PASSWORD: %s\n",local_68);
if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                /* WARNING: Subroutine does not return */
__stack_chk_fail();
}
return 0;
```

It becomes clear that from a custom character list, random characters were chosen to generate the password. However its important to note that the implementation is not secure as same srand values will give same outputs.

Description states that the password was generated on 26th January, 2019. The time was chosen such that both IST and UTC timezones give a answer. For this PoC I will work with IST.

First generate a duplicate of passgen using same login to generate the wordlist.

```C
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    char characters[] = "abcdefghijklmnoqprstuvwyzxABCDEFGHIJKLMNOQPRSTUYWVZX0123456789";
    FILE *fptr = fopen("wordlist.txt", "w");
    long long t = 1548441000;
    for(int i = 0; i <= 86400; i++) {
        t += 1;
        srand(t);
        char password[16];
        for(int i = 0; i < 15; i++) {
            password[i] = characters[rand()%62];
        }
        password[15] = '\n';
        fwrite(password, sizeof(char), 16, fptr);
    }
    fclose(fptr);
    return 0;
}
```

Now we can use something like [John the Ripper](https://github.com/openwall/john) to get the password from the wordlist.

```bash
zip2john encrypted.zip > hash
```

```bash
john --wordlist=wordlist.txt hash

Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 16 OpenMP threads
Note: Passwords longer than 21 [worst case UTF-8] to 63 [ASCII] rejected
Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
kFEbD1Pzxyu69Yw  (encrypted.zip/flag.txt)     
1g 0:00:00:00 DONE (2025-01-27 09:28) 100.0g/s 8640Kp/s 8640Kc/s 8640KC/s AWaEU6xHEZpLkig..eZDDocGu1TL0b6h
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

We get the password as `kFEbD1Pzxyu69Yw`.

## Flag
`CodefestCTF{rand_15_n07_4c7ua11y_r4nd0m}`