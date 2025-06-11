$(document).ready(function () {
    const data = JSON.parse(document.getElementById("data").textContent);

    function displayPopularItems() {
        const popularItemsContainer = document.getElementById("popular-items");
        const popularItems = data.slice(0, 3);

        popularItems.forEach(item => {
            const itemCard = document.createElement("div");
            itemCard.classList.add("col-md-4", "mb-4");

            itemCard.innerHTML = `
                <button class="btn p-0" onclick="window.location.href='/view/${item.id}'">
                    <div class="card">
                        <img src="${item.image}" class="card-img-top" alt="${item.title}">
                        <div class="card-body">
                            <h5 class="card-title">${item.title}</h5>
                        </div>
                    </div>
                </button>
            `;
            popularItemsContainer.appendChild(itemCard);
        });
    }

    displayPopularItems();
});