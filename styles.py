css = """
        <style>
        .expandable-image {
            max-width: 25%; /* 1/8 экрана */
            max-height: 120px;
            cursor: pointer;
            box-sizing: border-box; /* Учитывать padding и border внутри flex-basis */
            padding: 5px; /* Отступы между фотографиями */
        }
        .expanded-image-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.7);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .expanded-image {
                            max-width: 85%; /* Полноэкранное изображение */
                            max-height: 85%;
        }

        .map {
                position: fixed;
                bottom: 0;
                left: 0;
                max-width: 25%;
                min-width: 460px;
                cursor: pointer;
        }
        .preview {
                display: flex;
                overflow-x: auto;
                max-width: auto; /* Максимальная ширина превью контейнера */
                margin: 2px auto; /* Центрирование контейнера на странице */
                box-sizing: border-box; /* Учитывать padding и border внутри flex-basis */
                padding: 5px; /* Отступы между фотографиями */
                border: 2px solid #ccc; /* Толщина и цвет рамки */
                }
        .preview::-webkit-scrollbar {
              width: 10px; /* Ширина полосы прокрутки */
                }

        .preview::-webkit-scrollbar-track {
                                            background-color: #f1f1f1; /* Цвет фона трека */
        }

        .preview::-webkit-scrollbar-thumb {
                                            background-color: #888; /* Цвет полосы прокрутки */
                                            border-radius: 5px; /* Закругление углов полосы прокрутки */
        }
    </style>
"""
