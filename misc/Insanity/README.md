# Insanity

Total Solves - 14

Final Points - 473

## Description
Cause sanity was tough

## Writeup

> Came across this challenge in [AmateursCTF 2023](https://ctftime.org/writeup/37577)

If you copy the rules in rules channel in discord using discord's copy text, and paste it somewhere, you will see something like this

```
1. The CTF starts on 25th January, 2025 at 6 PM and lasts exactly 36 hours.
67111100101102. A team size of a maximum of 3 is allowed.
1011151166784. The flag format is `CodefestCTF{}` unless otherwise stated.
7012349110535211049. The organizers of this event reserve the right to refuse the eligibility of prizes if any situation of malpractice arises.
55121959910452. Please refrain from discussing strategy and solutions during the contest.
10810895545754. CTF organizers' decisions are final.
575457125. The person could have an unlimited number of submissions in most cases, but brute-forcing a server would be penalized and would result in an IP ban and discarding the team from the contest.
- Attacking, DoSing, or otherwise deliberately harming the event infrastructure is strictly prohibited and will result in an immediate ban and block from the event.
```
As you can see the, there are extra numbers. Upon inspection, its easy to realize that these are ascii encoded flag characters.

## Flag
`CodefestCTF{1n54n17y_ch4ll_696969}`