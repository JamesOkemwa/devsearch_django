
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