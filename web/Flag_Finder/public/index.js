document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    const uploadBtn = document.getElementById('uploadBtn');
    const statusText = document.getElementById('status');
    
    if (file && file.type === 'application/zip') {
        uploadBtn.disabled = false;
    } else {
        uploadBtn.disabled = true;
        statusText.textContent = 'Please select a valid ZIP file.';
    }
});

document.getElementById('uploadBtn').addEventListener('click', async function() {
    const file = document.getElementById('fileInput').files[0];
    const toFind = document.getElementById('toFindInput').value.trim();
    const statusText = document.getElementById('status');
    const uploadBtn = document.getElementById('uploadBtn');

    if (!file) {
        statusText.textContent = 'Please select a ZIP file.';
        return;
    }

    if (!toFind) {
        statusText.textContent = 'Please enter a search string.';
        return;
    }

    statusText.textContent = 'Uploading...';
    uploadBtn.disabled = true;

    try {
        const arrayBuffer = await file.arrayBuffer();
        const rawBytes = new Uint8Array(arrayBuffer);

        const queryParams = new URLSearchParams();
        queryParams.append('toFind', toFind);

        const response = await fetch(`/upload?${queryParams.toString()}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/octet-stream',
            },
            body: rawBytes,
        });

        if (response.ok) {
            statusText.textContent = 'Response: '+(await response.text());
        } else {
            statusText.textContent = 'Upload failed. Try again.';
        }
    } catch (error) {
        statusText.textContent = 'Error during upload: ' + error.message;
    } finally {
        uploadBtn.disabled = false;
    }
});
