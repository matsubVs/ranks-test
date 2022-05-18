

    document.querySelector("#submitBtn").addEventListener("click", () => {
        fetch("/buy/")
            .then((result) => result.json())
            .then((data) => {
              console.log(data);
              return stripe.redirectToCheckout({sessionId: data.sessionId})
            })
            .then((res) => {
              console.log(res);
            });
        });

const configStripe = async () => {
    return fetch("/config/")
        .then(result => result.json())
        .then(data => {
            const stripe = Stripe(data.publicKey);
            console.log('Stripe initialized');
            return stripe
        });
}

const get_item_session_id = async (itemId) => {
    return fetch(`/buy/${itemId}/`)
        .then(result => result.json())
        .then(data => data.sessionId)
}

const get_order_session_id = async (orderId) => {
    return fetch(`/order_buy/${orderId}/`)
        .then(result => result.json())
        .then(data => data.sessionId)
}

submitBtn = document.querySelector('#sButton');
dataId = submitBtn.data.id;
submitBtn.addEventListener("click",async () => {
    const stripe = await configStripe(dataId)
    get_item_session_id(dataId)
         .then(sessionId => stripe.redirectToCheckout({ sessionId: session.id }))
})