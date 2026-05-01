let input = document.querySelector('input')
let btn = document.querySelector('button')
let li = document.querySelector('li')

btn.addEventListener("click",function(){
    let item = document.createElement('li')
    item.innerText= input.value;

    let delbtn = document.createElement('button')
    delbtn.innerText= "Delete"
    delbtn.classList.add('delete')

    item.appendChild(delbtn)
    li.appendChild(item);

})
