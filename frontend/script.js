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
    loadResources(); 
    alert("Resource Created");

document.getElementById("name").value = "";
document.getElementById("category").value = "";
document.getElementById("price").value = "";
document.getElementById("inventory").value = "";
    
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
    `ID: ${resource.id} | ${resource.name} | ₹${resource.price_per_hour}/hr | inventory: ${resource.total_inventory}`;

        list.appendChild(item);
    });
}
async function checkAvailability() {

    const resourceId = document.getElementById("resourceId").value;
    const start = document.getElementById("startTime").value;
    const end = document.getElementById("endTime").value;

    const response = await fetch(
        `${API}/availability?resource_id=${resourceId}&start_time=${start}&end_time=${end}`
    );

    const data = await response.json();

    const result = document.getElementById("availabilityResult");

    if (data.available) {
        result.innerText = " Slot Available";
        result.style.color = "green";
    } else {
        result.innerText = " Slot Not Available";
        result.style.color = "red";
    }
}

async function createBooking() {

    const booking = {
        user_email: document.getElementById("email").value,
        start_time: document.getElementById("startTime").value,
        end_time: document.getElementById("endTime").value,
        items: [
            {
                resource_id: parseInt(document.getElementById("resourceId").value),
                quantity: 1
            }
        ]
    };

    const response = await fetch(`${API}/bookings`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(booking)
    });

    const data = await response.json();

    if (response.ok) {
    alert("Booking created successfully!");

    document.getElementById("email").value = "";
    document.getElementById("resourceId").value = "";
    document.getElementById("startTime").value = "";
    document.getElementById("endTime").value = "";
    document.getElementById("availabilityResult").innerText = "";
} else {
    alert(data.detail);
}}