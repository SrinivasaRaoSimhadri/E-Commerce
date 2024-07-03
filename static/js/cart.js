var updateBtns = document.getElementsByClassName("update-cart");
for(var  i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click" , function() {
        var productId = this.dataset.productid;
        var action = this.dataset.action;
        if (user === "AnonymousUser") {
            console.log("user is not authenticated");
        }
        else {
            updateUserOrder(productId ,action);
        }
    });
}

function updateUserOrder(productId , action ) {
    var url ='/cart/'
    fetch(url , {
        method:"POST",
        headers:{
            "Content-type" : "application/json",
            "X-CSRFToken" :csrftoken,
        },
        body: JSON.stringify({"productId": productId, "action": action})
    })
    .then((responce) => { 
        responce.json();
    })
    .then((data) => {
        location.reload();
    })
}