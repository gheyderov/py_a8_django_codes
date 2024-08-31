let subscribeForm = document.getElementById('subscribe-form')
subscribeForm.addEventListener('submit', function(event){
    let email = document.getElementById('subscribe-email')
    event.preventDefault()
    fetch('http://localhost:8000/api/subscriber/', {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : subscribeForm.csrfmiddlewaretoken.value
        },
        body: JSON.stringify({'email' : email.value})
    }).then(response => {
        if (response.ok){
            subscribeForm.innerHTML = 'Thanks for your subscribing!'
        }
})
})