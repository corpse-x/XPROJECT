document.getElementById('home-tab').addEventListener('click', function () {
    document.getElementById('home-content').style.display = 'block';
    document.getElementById('account-content').style.display = 'none';
    document.getElementById('game-content').style.display = 'none';
});

document.getElementById('account-tab').addEventListener('click', function () {
    document.getElementById('home-content').style.display = 'none';
    document.getElementById('account-content').style.display = 'block';
    document.getElementById('game-content').style.display = 'none';
});

document.getElementById('game-tab').addEventListener('click', function () {
    document.getElementById('home-content').style.display = 'none';
    document.getElementById('account-content').style.display = 'none';
    document.getElementById('game-content').style.display = 'block';
});