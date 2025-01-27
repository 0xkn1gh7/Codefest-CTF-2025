# Background Check

You have been asked by Sprinklr to do a background check on an intern candidate. The candidate's name is `Arnav Kumar Sinha` and he's from IIT(BHU), Varanasi, India.
Help the company!

*There are 7 challenges in this OSINT investigation.*

## JEE (Advanced)

Total Solves - 380

Final Score - 100

### Description
Find the candidate's rank in JEE Advanced and year appeared.

FLAG FORMAT - `CodefestCTF{year_rank}`

### Writeup
Search google for `Arnav Kumar Sinha IIT BHU` and the first [linkedin profile](https://in.linkedin.com/in/iedfa) will lead you to the answer. 

### Flag
`CodefestCTF{2022_858}`

---
## Present Sir!

Total Solves - 359

Final Score - 100

### Description

Find the candidate's institute roll number

FLAG FORMAT - `CodefestCTF{rollno}`

### Writeup
The google search for `Arnav Kumar Sinha IIT BHU` will give a [pdf document](https://prev.iitbhu.ac.in/contents/cse/doc/btech_students_cse_2021-22.pdf) on the first page of results.

### Flag
`CodefestCTF{22075013}`

---
## Alias

Total Solves - 318

Final Points - 100

### Description
The candidate's known to use a certain 5 digit username on many online platforms. Find that username.

FLAG FORMAT - `CodefestCTF{username}`

### Writeup
The linkedin username gives a hint. To confirm, the initital google search would lead you to [this](https://iitbhucybersec.in/members/) website.

### Flag
`CodefestCTF{iedfa}`

---
## CP

Total Solves - 264

Final Points - 100

### Description
The candidate is a Competitive Programming enthusiast. Can you find his current and max rating on Codeforces and current rating on CodeChef.

FLAG FORMAT - `CodefestCTF{currentCF_maxCF_currentCC}`

### Writeup
The IIT(BHU)CyberSec link in previous challenge has the Codeforces Handle of the candidate. The same username - iedfa. Checking the same on CodeChef will give you the flag.

### Flag
`CodefestCTF{1687_1769_2018}`

---
## Github

Total Solves - 306

Final Points - 100

### Description
Can you find the candidate's github username?

FLAG FORMAT - `CodefestCTF{username}`

### Writeup
The IIT(BHU)CyberSec link will lead you to correct answer.

### Flag
`CodefestCTF{JustAnAverageGuy}`

---
## JEE Main

Total Solves - 337

Final Points - 100

### Description
Can you find the candidate's percentile in JEE Main?

FLAG FORMAT - `CodefestCTF{XX.XX}`

### Writeup
Searching `Arnav Kumar Sinha jee main` gives a [youtube video](https://www.youtube.com/watch?v=V4a5fzL33t0). The answer is in the title.

### Flag
`CodefestCTF{99.72}`

---
## Why do they even need this?

Total Solves - 50

Final Points - 100

### Description
Can you find the candidate's laptop's user and hostname?

FLAG FORMAT - `CodefestCTF{username_hostname}`

### Writeup

Use [sherlock](https://github.com/sherlock-project/sherlock) on `idefa`. Will reach [here](https://asciinema.org/~iedfa).

There are other methods like searching github or finding a workshop video where iedfa shared laptop screen.

### Flag
`CodefestCTF{aks_aks-Inspiron-3505}`
