window.addEventListener('load', async function (event) {
    let responseCategory = await this.fetch('http://localhost:8000/api/categories/')
    let resDataCategory = await responseCategory.json()
    let categoryList = this.document.getElementById('category-list')
    for (category of resDataCategory) {
        categoryList.innerHTML += `
                    <option value="${category.id}">${category.title}</option>
        `
    }

    let responseTags = await this.fetch('http://localhost:8000/api/tags/')
    let resDataTags = await responseTags.json()
    let tagsList = document.getElementById('tags-list')
    for (tag of resDataTags) {
        tagsList.innerHTML += `
                    <option value="${tag.id}">${tag.title}</option>
        `
    }
})

let token = localStorage.getItem('token')
let creationForm = document.getElementById('creation-form')
creationForm.addEventListener('submit', function (event) {
    event.preventDefault()
    let formData = new FormData(creationForm)
    fetch('http://localhost:8000/api/recipes/', {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${token}`
        },
        body: formData
    })
})