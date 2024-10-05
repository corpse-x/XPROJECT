document.getElementById('signup-link').addEventListener('click', function () {
    document.querySelector('.login-container').style.display = 'none';
    document.querySelector('.signup-container').style.display = 'block';
});

document.getElementById('login-link').addEventListener('click', function () {
    document.querySelector('.login-container').style.display = 'block';
    document.querySelector('.signup-container').style.display = 'none';
});

// Handle form submissions (dummy for now)
document.getElementById('login-form').addEventListener('submit', function (e) {
    e.preventDefault();
    alert('Logging in...');
    // Redirect to dashboard.html
    window.location.href = "dashboard.html";
});

document.getElementById('signup-form').addEventListener('submit', function (e) {
    e.preventDefault();
    alert('Signing up...');
    // Redirect to dashboard.html
    window.location.href = "dashboard.html";
});