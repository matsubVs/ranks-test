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
    console.log(itemId)
    return fetch(`/buy/${+itemId}/`)
        .then(result => result.json())
        .then(data => data.sessionId)
}

const get_order_session_id = async (orderId) => {
    return fetch(`/order_buy/${+orderId}/`)
        .then(result => result.json())
        .then(data => data.sessionId)
}

submitBtn = document.querySelector("#submitBtn");
dataId = submitBtn.dataset.id;
dataType = submitBtn.dataset.type
submitBtn.addEventListener("click",async () => {
    const stripe = await configStripe(dataId)
    if (dataType === 'item') {
        get_item_session_id(dataId)
            .then(sessionId => stripe.redirectToCheckout({ sessionId: sessionId }))
    }
    else {
        get_order_session_id(dataId)
            .then(sessionId => stripe.redirectToCheckout({ sessionId: sessionId }))
    }
})