// Select the theme toggle button
const themeToggle = document.getElementById("theme-toggle");
const body = document.body;

// Add event listener to toggle button
themeToggle.addEventListener("click", () => {
    body.classList.toggle("dark-mode");
    
    // Update button text
    if (body.classList.contains("dark-mode")) {
        themeToggle.textContent = "Light Mode";
    } else {
        themeToggle.textContent = "Dark Mode";
    }
});
