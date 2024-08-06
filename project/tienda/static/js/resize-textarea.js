// resize-textarea.js

document.addEventListener('DOMContentLoaded', function() {
    const textareas = document.querySelectorAll('textarea');

    textareas.forEach(textarea => {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto'; // Reset height
            this.style.height = `${this.scrollHeight}px`; // Set height to match content
        });
    });
});
