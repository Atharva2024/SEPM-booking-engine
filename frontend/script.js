const API = "http://127.0.0.1:8000";

async function createResource() {

    const resource = {
        name: document.getElementById("name").value,
        category: document.getElementById("category").value,
        price_per_hour: parseFloat(document.getElementById("price").value),
        total_inventory: parseInt(document.getElementById("inventory").value)
    };

    const response = await fetch(`${API}/resources`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(resource)
    });

    alert("Resource Created");
}

async function loadResources() {

    const response = await fetch(`${API}/resources`);
    const data = await response.json();

    const list = document.getElementById("resourceList");
    list.innerHTML = "";

    data.forEach(resource => {

        const item = document.createElement("li");
        item.className = "list-group-item";

        item.innerText =
            `${resource.name} | ₹${resource.price_per_hour}/hr | inventory: ${resource.total_inventory}`;

        list.appendChild(item);
    });
}