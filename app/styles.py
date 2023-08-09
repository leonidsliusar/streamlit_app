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
        .whatsapp-button {
                            position: fixed;
                            right: 13px;
                            bottom: 90px;
                            transform: translate(-50%, -50%);
                            background: #25D366; /*цвет кнопки*/
                            border-radius: 50%;
                            width: 55px; /*ширина кнопки*/
                            height: 55px; /*высота кнопки*/
                            color: #fff;
                            text-align: center;
                            line-height: 53px; /*центровка иконки в кнопке*/
                            font-size: 50px; /*размер иконки*/
                            z-index: 9999;
                        }
.whatsapp-button a {
                        color: #fff;
                    }
.whatsapp-button:before,
.whatsapp-button:after {
    content: " ";
    display: block;
    position: absolute;
    border: 50%;
    border: 1px solid #25D366; /*цвет анимированных волн от кнопки*/
    left: -20px;
    right: -20px;
    top: -20px;
    bottom: -20px;
    border-radius: 50%;
    animation: animate 1.5s linear infinite;
    opacity: 0;
    backface-visibility: hidden;
}

.whatsapp-button:after{
    animation-delay: .5s;
}

@keyframes animate
{
    0%
    {
        transform: scale(0.5);
        opacity: 0;
    }
    50%
    {
        opacity: 1;
    }
    100%
    {
        transform: scale(1.2);
        opacity: 0;
    }
}
    .css-189oqrx {
    width: 20px;
    position: relative;
    display: flex;
    flex: 1 1 0%;
    flex-direction: column;
    gap: 1rem;
}   
    .css-1w58vtp {
    width: 140px;
    position: grid;
}
.attr-table {
  width: 400px;
  display: flex;
  justify-content: space-between;
  align-items: baseline; /* Чтобы ключи и значения выровнялись по базовой линии текста */
  margin-bottom: 5px; /* Пространство между парами ключ-значение */
}


.attr-value {
    display: flex;
  text-align: left;
}
}
"""
