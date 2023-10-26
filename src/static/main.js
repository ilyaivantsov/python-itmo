const speechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition;

const recognition = new speechRecognition();
const rl = document.querySelector('#running-line');

recognition.continuous = true;
recognition.interimResults = true;
recognition.lang = 'ru-RU';

let gifTimeout = null;

recognition.onresult = (event) => {
    rl.textContent = '';
    rl.classList.remove('final');
    for (let i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
            rl.classList.add('final');
            rl.textContent = event.results[i][0].transcript;
            sendText(rl.textContent).then((data) => {
                console.log(data);
                if (data && data.length) {
                    setGif(data[0]);
                }
                toggleCad();
            }).catch((err) => {
                console.log(err);
            });
        } else {
            rl.textContent += event.results[i][0].transcript;
        }
    }
}

recognition.onerror = function (event) {
    if (event.error === 'no-speech') {
        console.log('no-speech');
        rl.textContent = '...';
        rl.classList.remove('final');
    }
    if (event.error === 'audio-capture') {
        console.log('audio-capture');
    }
    if (event.error === 'not-allowed') {
        console.log('not-allowed');
    }
    console.error(event.error);
}

recognition.onend = function () {
    console.error('recognition end!'.toUpperCase());
    recognition.start();
}

navigator.mediaDevices.getUserMedia({audio: true})
    .then(() => {
        recognition.start();
    }).catch(console.error)

async function sendText(text) {
    const params = new URLSearchParams({
        query: text,
        limit: 1,
        lang: 'ru',
    });
    const response = await fetch(`/search-gifs?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        }
    });

    return await response.json();
}

const setGif = (gifSrc) => {
    const gifElement = getHideCad().querySelector('img');
    gifElement.src = gifSrc;
}

const getHideCad = () => document.querySelector('#cad-1').classList.contains('hide') ?
    document.querySelector('#cad-1') : document.querySelector('#cad-2');

const toggleCad = () => {
    clearTimeout(gifTimeout);
    const cad1 = document.querySelector('#cad-1');
    const cad2 = document.querySelector('#cad-2');
    gifTimeout = setTimeout(() => {
        cad1.classList.toggle('hide');
        cad2.classList.toggle('hide');
    }, 100);
}
