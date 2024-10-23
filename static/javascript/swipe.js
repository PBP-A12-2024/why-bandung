const Swipe = document.querySelector('.swipe');
const Like = document.querySelector('.containerLike');
const Dislike = document.querySelector('.containerDislike');

// Dummy data
const data = [
    'https://images.unsplash.com/photo-1729273793467-7b40e05d1bbd?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw0fHx8ZW58MHx8fHx8',
    'https://plus.unsplash.com/premium_photo-1729594514498-e232ee4ca3b9?q=80&w=2529&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://plus.unsplash.com/premium_photo-1728069876111-db576d47754d?q=80&w=2574&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://plus.unsplash.com/premium_photo-1685798807393-0d843f6b6a3a?q=80&w=2574&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://plus.unsplash.com/premium_photo-1686606891168-8d9632e190fa?q=80&w=2452&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    'https://images.unsplash.com/photo-1729626739316-c9dd3c61683b?q=80&w=2515&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
];

let counterCard = 0;

// Update existing cards position
function updateCardPositions() {
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.setProperty('--i', index); 
    });
}

function addCard() {
    const card = document.createElement('div');
    card.classList.add('card');
    const img = document.createElement('img');
    img.src = data[counterCard % data.length]; // Use data.length to avoid index error
    card.appendChild(img);
    card.style.setProperty('--i', counterCard);

    card.addEventListener('mousedown', (e) => listenToMouseEvent(e, card));
    Swipe.appendChild(card);
    counterCard++;
}

function listenToMouseEvent(e, card) {
    const startX = e.clientX;
    const startY = e.clientY;
    let currentX = startX;
    let currentY = startY;

    const handleMouseDown = (e) => {
        currentX = e.clientX;
        currentY = e.clientY;
        const offsetX = currentX - startX;
        const offsetY = currentY - startY;

        card.style.transition = 'transform 0s';
        card.style.transform = `translate(${offsetX}px, ${offsetY}px) rotate(${offsetX * 0.1}deg)`;

        card.addEventListener('dragstart', (e) => {
            e.preventDefault();
        });

        if (Math.abs(offsetX) > card.clientWidth * 0.7) {
            dismissCard(offsetX > 0 ? 1 : -1, card, offsetX, offsetY);
        }
    };

    const handleMouseUp = () => {
        card.style.transition = 'transform 0.7s';
        card.style.transform = 'none';

        document.removeEventListener('mousemove', handleMouseDown);
        document.removeEventListener('mouseup', handleMouseUp);
    };

    const dismissCard = (direction, card, offsetX, offsetY) => {
        document.removeEventListener('mousemove', handleMouseDown);
        document.removeEventListener('mouseup', handleMouseUp);
        card.style.transition = 'transform 1.2s';
        card.style.transform = `translate(${direction * window.innerWidth}px, ${offsetY}px) rotate(${90 * direction}deg)`;

        setTimeout(() => {
            card.remove();
            addCard(); 
            updateCardPositions();

        }, 500); 
        
            // Reset the animation to allow it to play again
        if (direction === 1) {
            Like.style.animationPlayState = 'running';
            Dislike.style.animationPlayState = 'paused'; // Reset to paused
        } else {
            Dislike.style.animationPlayState = 'running';
            Like.style.animationPlayState = 'paused'; // Reset to paused
        }

        // Trigger reflow to restart the animation
        Like.offsetHeight; // This forces a reflow
        Dislike.offsetHeight; // This forces a reflow
    };

    document.addEventListener('mousemove', handleMouseDown);
    document.addEventListener('mouseup', handleMouseUp);
}

// Add initial 5 cards
for (let i = 0; i < 5; i++) {
    addCard();
}

