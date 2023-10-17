function visitorCount(){
    fetch("https://9278f0hyme.execute-api.eu-west-1.amazonaws.com/default/visitors-function")
        .then(response => response.json())
        .then(data => {
            const countElement = document.getElementById('count');
            countElement.textContent = data.visitor_count;
        })
        .catch(error => {
            console.error("Error fetching visitor count:", error);
        });
}

// Fetch visitor count when the page loads
window.addEventListener('load', visitorCount);