function uploadAudio() {
    const input = document.getElementById('audio-file');
    const file = input.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('audio', file);

        fetch('/upload', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.transcription) {
                document.getElementById('transcription').innerText = data.transcription;
            } else {
                document.getElementById('transcription').innerText = data.error;
            }
        })
        .catch(error => {
            document.getElementById('transcription').innerText = 'Error: ' + error;
        });
    }
}

function setBackgroundImage() {
    const input = document.getElementById('background-image');
    const file = input.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            document.body.style.backgroundImage = `url('${e.target.result}')`;
        };
        reader.readAsDataURL(file);
    }
}
