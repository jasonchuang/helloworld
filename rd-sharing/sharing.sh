#!/bin/bash
MNIST_IMAGE="6"
MULTIPLY_FLOAT_LIST="1.0, 3.0, 5.0, 7.0"
STR_LEN_STRING="picaas"
NLDF_IMAGE="direwolf"
IMAGE_RESIZE_FILE="jason_avatar"

echo ""
echo "0. Select which mlengine demo you want to see:"
echo "-------------------------------------------------------"
echo "0. MNIST"
echo "1. multiply"
echo "2. string length"
echo "3. image resize"
echo "4. nldf"
echo "-------------------------------------------------------"
echo -n ">>>> "
read choise

case $choise in
    "")
    echo "ERROR input"
    exit -1
    ;;
    *[!0-4]*)
    echo "ERROR input"
    exit -1
    ;;
    "0")
    time python mnist.py --input_image "${MNIST_IMAGE}.png"
    ;;

    "1")
    time python multiply.py --input_float_list "${MULTIPLY_FLOAT_LIST}"
    echo $MULTIPLY_FLOAT_LIST
    ;;

    "2")
    time python str_len.py --input_string $STR_LEN_STRING
    echo $STR_LEN_STRING
    ;;

    "3")
    time python image_resize.py --input_image "${IMAGE_RESIZE_FILE}.jpg"
    open "${IMAGE_RESIZE_FILE}_grid.jpg"
    ;;

    "4")
    time python nldf.py --input_image "${NLDF_IMAGE}.jpg"
    open "${NLDF_IMAGE}_grid.jpg"
    ;;

    *)
    echo "No define!!"
    exit -1
    ;;
esac

