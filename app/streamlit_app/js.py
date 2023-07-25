js = """
<script>
        let currentImageIndex = -1;
        let expandedImageContainer = null;

        function expandImage(image, currentIndex) {
            if (expandedImageContainer) {
                expandedImageContainer.remove();
            }

            expandedImageContainer = document.createElement('div');
            expandedImageContainer.classList.add('expanded-image-container');

            const slideshowButtons = `
                <div class="slideshow-buttons">
                    <div class="slideshow-button" onclick="showPrevImage()">&lt;</div>
                    <div class="slideshow-button" onclick="showNextImage()">&gt;</div>
                </div>
            `;

            expandedImageContainer.innerHTML = `
                ${slideshowButtons}
                <img class="expanded-image" src="${image.src}" alt="${image.alt}">
            `;

            expandedImageContainer.addEventListener('click', () => {
                expandedImageContainer.remove();
            });

            document.body.appendChild(expandedImageContainer);
            currentImageIndex = currentIndex;
        }

        function showNextImage() {
            const previewImages = document.querySelectorAll('.expandable-image');
            currentImageIndex = (currentImageIndex + 1) % previewImages.length;
            const image = previewImages[currentImageIndex];
            expandImage(image, currentImageIndex);
        }

        function showPrevImage() {
            const previewImages = document.querySelectorAll('.expandable-image');
            currentImageIndex = (currentImageIndex - 1 + previewImages.length) % previewImages.length;
            const image = previewImages[currentImageIndex];
            expandImage(image, currentImageIndex);
        }

        // JavaScript для увеличения превьюшек при клике
        const previewImages = document.querySelectorAll('.expandable-image');
        previewImages.forEach((previewImage, index) => {
            previewImage.addEventListener('click', () => {
                expandImage(previewImage, index);
            });
        });


        // JavaScript для обработки клавиш "вправо" и "влево" на компьютере
        document.addEventListener('keydown', handleKeyPress, false);

        function handleKeyPress(event) {
            if (expandedImageContainer) {
                if (event.key === 'ArrowRight') {
                    showNextImage();
                } else if (event.key === 'ArrowLeft') {
                    showPrevImage();
                }
            }
        }

        // JavaScript для обработки свайпов на телефоне
        let xDown = null;

        document.addEventListener('touchstart', handleTouchStart, false);
        document.addEventListener('touchmove', handleTouchMove, false);

        function handleTouchStart(event) {
            xDown = event.touches[0].clientX;
        }

        function handleTouchMove(event) {
            if (!xDown) {
                return;
            }

            const xUp = event.touches[0].clientX;
            const xDiff = xDown - xUp;

            if (xDiff > 0) {
                showNextImage();
            } else {
                showPrevImage();
            }

            xDown = null;
        }
</script>
"""