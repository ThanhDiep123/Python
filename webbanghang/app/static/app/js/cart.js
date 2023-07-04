var updataBtns = document.getElementsByClassName('updata-cart')

for (i=0;i < updataBtns.length;i++){
    updataBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId',productId,'action',action)
        console.log('user: ',user)
        if (user === "AnonymousUser"){
           console.log('user not logged')
        } else{
            updataUserOrder(productId,action)
        }
    })
}

function updataUserOrder(productId,action){
    console.log('user logged in, success add')
    var url = '/updata_item/'
    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken ,
        },
        body: JSON.stringify({'productId':productId,'action':action})
    })
    .then((response) =>{
    return response.json()
    })
    .then((data) =>{
        console.log('data',data)
        location.reload()
    })
}