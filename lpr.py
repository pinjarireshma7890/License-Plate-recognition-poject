
import cv2
import easyocr

reader = easyocr.Reader(['en'])

image = cv2.imread('car.jpeg')

if image is None:
    print("Error: car.jpeg not found!")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)

    edges = cv2.Canny(gray, 30, 200)

    contours, _ = cv2.findContours(
        edges.copy(),
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    contours = sorted(
        contours,
        key=cv2.contourArea,
        reverse=True
    )[:30]

    plate_found = False

    for contour in contours:
        perimeter = cv2.arcLength(contour, True)

        approx = cv2.approxPolyDP(
            contour, 0.02 * perimeter, True
        )

        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)

            if w > 80 and h > 20 and w / h > 2:
                plate = gray[y:y+h, x:x+w]

                plate = cv2.resize(
                    plate,
                    None,
                    fx=3,
                    fy=3,
                    interpolation=cv2.INTER_CUBIC
                )

                plate = cv2.threshold(
                    plate,
                    0,
                    255,
                    cv2.THRESH_BINARY + cv2.THRESH_OTSU
                )[1]

         
                original_plate = gray[y:y+h, x:x+w]

                result1 = reader.readtext(
                    original_plate,
                    detail=1,
                    allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                )

                result2 = reader.readtext(
                    plate,
                    detail=1,
                    allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                )

                print("Original crop:", result1)
                print("Enhanced crop:", result2)

                plate_found = True
                break


    if not plate_found:
        print("Plate not detected. Try a clear, front-facing car image.")
