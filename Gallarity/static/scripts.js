document.addEventListener('DOMContentLoaded', () => {
    console.log("✅ JavaScript file loaded successfully!");

    // Get elements
    const loginBtn = document.getElementById('login-btn');
    const signInBtn = document.getElementById('sign-in-btn');
    const authForm = document.getElementById('auth-form');
    const submitBtn = document.getElementById('submit-btn');
    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');
    const fileUploadInput = document.getElementById("file_upload");
    const profileDpInput = document.getElementById("profile_dp");
    const wallpapers = document.querySelectorAll('.wallpaper');
    

    // Handle Login Button
    if (loginBtn && authForm && submitBtn) {
        loginBtn.addEventListener('click', () => {
            authForm.classList.remove('hidden');
            submitBtn.textContent = 'Login';
        });
    }

    // Handle Sign-In Button
    if (signInBtn && authForm && submitBtn) {
        signInBtn.addEventListener('click', () => {
            authForm.classList.remove('hidden');
            submitBtn.textContent = 'Sign In';
        });
    }

    // Search Function
    function performSearch() {
        if (!searchInput) {
            console.error("🚨 Search input not found!");
            return;
        }
        
        const query = searchInput.value.toLowerCase().trim();
        console.log("🔍 Searching for:", query);

        wallpapers.forEach(wallpaper => {
            const name = wallpaper.getAttribute('data-name')?.toLowerCase() || "";
            const description = wallpaper.getAttribute('data-description')?.toLowerCase() || "";

            if (name.includes(query) || description.includes(query)) {
                wallpaper.style.display = 'block'; // Show if it matches
            } else {
                wallpaper.style.display = 'none'; // Hide if it doesn't match
            }
        });
    }

    // Attach event listeners if elements exist
    if (searchInput && searchButton) {
        searchButton.addEventListener('click', performSearch);
        searchInput.addEventListener('input', performSearch); // Live search
        searchInput.addEventListener('keypress', (event) => {
            if (event.key === 'Enter') {
                event.preventDefault();
                performSearch();
            }
        });
    } else {
        console.error("🚨 Search elements not found!");
    }

    // Profile Picture Preview
    if (profileDpInput) {
        profileDpInput.addEventListener("change", (event) => {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    alert("Profile Picture Selected:" + file.name);
                };
                reader.readAsDataURL(file);
            }
        });
    }

    // File Upload Size Validation
    if (fileUploadInput) {
        fileUploadInput.addEventListener("change", (event) => {
            const file = event.target.files[0];
            if (file && file.size > 5 * 1024 * 1024) { // 5 MB limit
                alert("File size exceeds 5 MB!");
                fileUploadInput.value = ""; // Clear the input
            }
        });
    }
});