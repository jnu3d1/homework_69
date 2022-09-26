function getButtons() {
    let buttons = document.getElementsByTagName('button');
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', buttonClick);
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function buttonClick(event) {
    event.preventDefault();
    const csrftoken = getCookie('csrftoken');
    let url = event.target.dataset.url;
    let inputA = document.getElementById('A');
    let inputB = document.getElementById('B');
    const request = new Request(url, {
            method: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            body: JSON.stringify({
                'A': inputA.value,
                'B': inputB.value
            })
        }
    );
    let response = await fetch(request);
    let value = await response.json();
    let div = document.getElementById('answer');
    if (response.ok) {
        div.style.color = 'green';
        div.innerText = `Ответ: ${value.answer}`;
    } else {
        div.style.color = 'red';
        div.innerText = value.error;
    }

}

window.addEventListener('load', getButtons);
