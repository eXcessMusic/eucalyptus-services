const expandList = document.querySelectorAll(".expand");
expandList.forEach(element => {
    element.addEventListener("click", toggleExpanded);
});

function toggleExpanded(event) {
    const card = event.target.closest(".link-item");
    if (card) {
        const icons = card.querySelector(".platform-icons");
        card.classList.toggle("expanded");
        icons.style.display = card.classList.contains("expanded")? "flex" : "none";
    }
}
/* toggleExpanded(index: number): void {
    if (index >= 0 && index < this.linkItems.length) {
      this.linkItems[index].expanded = !this.linkItems[index].expanded;
    } else {
      console.error('Invalid index:', index);
    }
  }  
} */

/* Toggle between showing and hiding the navigation menu links when the user clicks on the hamburger menu / bar icon */
function myFunction() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}