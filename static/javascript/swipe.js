const Like = document.querySelector('.containerLike');
const Dislike = document.querySelector('.containerDislike');
const Swipe = document.querySelector('.swipe');

let counterCard = 0;
let dismissedCards = [];
let dataProducts = [];

// Load data and add the initial 5 cards
function loadProducts() {
    fetch('get_products/')
    .then(response => response.json())
    .then(data => {
        dataProducts = data.sort(() => Math.random() - 0.5);;
        console.log(dataProducts); 
        for (let i = 0; i < Math.min(5, dataProducts.length); i++) {
            addCard(dataProducts[i]);
        }
    })
    .catch(error => console.error('Error:', error));

}

// update posisi kartu
function updateCardPositions() {
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.setProperty('--i', index);
    });
}

// Menambahkan kartu ke dalam swipe container
function addCard(product) {
    if (!product) return;  
    const card = document.createElement('div');
    card.classList.add('card', 'border-[15px]', 'border-[#FDF6E1ff]', 'p-3', 'flex', 'flex-col', 'justify-center', 'items-center', 'bg-[#c25450]');
    card.dataset.productId = product.id; 

    card.innerHTML = `
        <div class="name-box-actual flex justify-between items-center w-full p-4 my-4 overflow-hidden h-[45px]">
            <div class = "flex justify-center items-center flex-1">
                <strong class="text-[15px] font-bold">${product.name}</strong>
            </div>
            <div class="font-semibold text-[12px] mx-2">Rp ${product.price.toLocaleString()}</div>
        </div>

        <div class="img-actual bg-[#FDF6E1ff] size-[252px] flex justify-center items-center p-3 mb-5 rounded-sm">
            <img src="${product.image}" alt="Product Image" class="object-fit w-[110%] max-h-full object-center">
        </div>

        <div class="border-4 border-[FDF6E1ff] flex flex-col justify-center w-full p-1">
            <div class=" text-[#FDF6E1ff] text-center border-black py-2 border-t-1 font-bold">${product.toko_name}</div>
        </div>
    `;
    card.style.setProperty('--i', counterCard);
    card.addEventListener('mousedown', (e) => listenToMouseEvent(e, card));
    Swipe.appendChild(card);
    counterCard++;
}

// Event listener untuk mouse event
function listenToMouseEvent(e, card) {
    const startX = e.clientX;
    const startY = e.clientY;
    let currentX = startX;
    let currentY = startY;

    // Event listener untuk mousemove dan mouseup
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

    // Fungsi untuk menghapus kartu
    function dismissCard(direction, card, offsetX, offsetY) {
        // Menghapus event listener mouse
        document.removeEventListener('mousemove', handleMouseDown);
        document.removeEventListener('mouseup', handleMouseUp);
    
        // Animasi dismiss
        card.style.transition = 'transform 1.2s';
        card.style.transform = `translate(${direction * window.innerWidth}px, ${offsetY}px) rotate(${90 * direction}deg)`;
    
        // Mendapatkan ID produk dan menyimpan objek produk untuk dismissed card
        const productId = card.dataset.productId;
        const product = dataProducts.find(p => p.id == productId);
    
        if (direction === 1) {
            // Jika liked
            Like.style.opacity = 1;
            setTimeout(() => {
                Like.style.opacity = 0.2;
            }, 500);
            setTimeout(() => {
                window.location.href = `${window.location.origin}/product/product_page/${productId}/`;
            }, 1000);
        } else {
            // Jika disliked, tambahkan objek produk ke dismissedCards
            dismissedCards.push(product);
            Dislike.style.opacity = 1;
            setTimeout(() => {
                Dislike.style.opacity = 0.2;
            }, 500);
            drawDismissedCard();
        }
    
        setTimeout(() => {
            card.remove();
            const nextProduct = dataProducts[counterCard];
            if (nextProduct) {
                addCard(nextProduct); 
                updateCardPositions();
            }
        }, 500);
    }

    document.addEventListener('mousemove', handleMouseDown);
    document.addEventListener('mouseup', handleMouseUp);
}

// GSAP Timeline to draw dismissed cards
function drawDismissedCard() {
    if (dismissedCards.length > 0) {
        const table = document.getElementById('table');
        const product = dismissedCards[dismissedCards.length - 1]; // Mendapatkan produk terakhir yang di-dismiss
        const card = document.createElement('div');

        card.classList.add('cardDismissed'); // Gunakan kelas baru

        // Buat elemen untuk name-box
        const nameBox = document.createElement('div');
        nameBox.classList.add('name-box');
        
        const nameStrong = document.createElement('strong');
        nameStrong.innerText = product.name;
        nameStrong.style.fontSize = '7px'; // Ukuran font

        const priceDiv = document.createElement('div');
        priceDiv.classList.add('font-semibold');
        priceDiv.style.fontSize = '5px'; // Ukuran font
        priceDiv.innerText = `Rp ${product.price.toLocaleString()}`;

        nameBox.appendChild(nameStrong);
        nameBox.appendChild(priceDiv);
        card.appendChild(nameBox);

        // Buat elemen untuk gambar
        const imgContainer = document.createElement('div');
        imgContainer.classList.add('img-container');

        const img = document.createElement('img');
        img.src = product.image;
        img.alt = "Product Image";
        img.style.maxWidth = '80px'; 
        img.style.maxHeight = '80px'; 

        imgContainer.appendChild(img);
        card.appendChild(imgContainer);

        // Buat elemen untuk kotak toko
        const kotakDesk = document.createElement('div');
        kotakDesk.classList.add('kotakDesk');
        
        const tokoName = document.createElement('div');
        tokoName.style.color = '#FDF6E1ff';
        tokoName.style.fontWeight = 'bold';
        tokoName.innerText = product.toko_name;

        kotakDesk.appendChild(tokoName);
        card.appendChild(kotakDesk);

        // Tambahkan kartu ke dalam tabel
        table.appendChild(card);

        // Posisi acak untuk dismissed card menggunakan GSAP
        const tl = gsap.timeline();
        const position = getTableCenter();
        const offsetX = table.offsetWidth * 0.5;
        const offsetY = table.offsetHeight * 0.5;

        gsap.set(card, {
            y: -table.offsetHeight,
            x: table.offsetWidth / 2,
            zIndex: dismissedCards.length,
        });

        tl.addLabel('start')
            .to(card, {
                duration: 1.5,
                ease: "power2.out",
                x: position.x + getRandom(-offsetX, offsetX),
                y: position.y + getRandom(-offsetY, offsetY),
            }, 'start')
            .to(card, {
                duration: 1.4,
                ease: "power2.out",
                rotation: getRandom(360),
            }, 'start');
    }
}

function getTableCenter() {
    const table = document.getElementById('table');
    return {
        x: (table.offsetLeft + table.offsetWidth / 2) - (100 / 2),      
        y: (table.offsetTop + table.offsetHeight / 2) - (150 / 2),  
    };
}

function getRandom(min, max = null) {
    let realMax = (max === null ? min * 2 : max);
    return min + Math.random() * (realMax - min);
}

loadProducts();
