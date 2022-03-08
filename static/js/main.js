
let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

if (searchForm) {
    for (let i=0; pageLinks.length > i; i++ ) {
        pageLinks[i].addEventListener('click',  function(e) {
            e.preventDefault()
            
            // get the data attribute
            let page = this.dataset.page
            console.log(page)

            // add hidden search input to form
            searchForm.innerHTML += `<input value=${page} name="page" hidden />`

            // submit form
            searchForm.submit()
        })
    }
}


// Removing tags from projects
let tags = document.getElementsByClassName('project-tag')

    for (let i=0; tags.length > i; i++) {
        tags[i].addEventListener('click', (e) => {
            let tagId = e.target.dataset.tag
            let projectId = e.target.dataset.project

            fetch('http://localhost:8000/api/remove-tag/', {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({'project':projectId, 'tag': tagId})
            })
            .then(res => res.json())
            .then(data => {
                e.target.remove()
            })
        })
    }