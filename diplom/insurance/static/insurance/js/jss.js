function toggleAnswer(element) {
    const answer = element.nextElementSibling;
    const icon = element.querySelector('.plus-icon');
    if (answer.style.display === 'none' || !answer.style.display) {
        answer.style.display = 'block';
        icon.textContent = '-';
    } else {
        answer.style.display = 'none';
        icon.textContent = '+';
    }
}