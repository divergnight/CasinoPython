const clickOnCardForReverse = thisCard => {
    let selectedCard = thisCard.getAttribute("data-card");
    let stateImg     = thisCard.getAttribute("src");

    stateImg === "/static/img/cards/back.jpg"
        ? stateImg = `/static/img/cards/${selectedCard}.jpg`
        : stateImg = `/static/img/cards/back.jpg`;

    thisCard.setAttribute("src", stateImg);
}