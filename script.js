document.getElementById("myDiv").addEventListener("click", function() {
    fetch("/hello")
        .then(response => response.text())
        .then(data => {
            console.log(data);
        });
});