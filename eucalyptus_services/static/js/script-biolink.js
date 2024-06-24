const expandList = document.querySelectorAll(".expand");
expandList.forEach(element => {
    element.addEventListener("click", toggleExpanded);
});

document.getElementById("collapseAll").addEventListener("click", collapseAll);

function toggleExpanded(event) {
    const card = event.target.closest(".link-item");
    if (card) {
        const icons = card.querySelector(".platform-icons");
        card.classList.toggle("expanded");
        icons.style.display = card.classList.contains("expanded")? "flex" : "none";
    }
}

function collapseAll() {
    const expandedCards = document.querySelectorAll(".link-item.expanded");
    expandedCards.forEach(card => {
        card.classList.remove("expanded");
        const icons = card.querySelector(".platform-icons");
        icons.style.display = "none";
    });
}