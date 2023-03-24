import cv2

# Get the default camera
video_capture = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    if ret:
        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Write the frame into the file 'output.avi'
        out.write(frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the camera and the file
video_capture.release()
out.release()
cv2.destroyAllWindows()
