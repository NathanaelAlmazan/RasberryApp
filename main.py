import cv2
from datetime import datetime


def main():
    cap = cv2.VideoCapture('./footage/footage2.mp4')

    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    output_name = str(datetime.timestamp(datetime.now())).split(".")[0]
    output_path = './outputs/' + output_name + '.mp4'
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    current_video = int(1)
    frame_num = 0
    current_video_name = output_name
    current_video_path = output_path
    saved = False
    frame_per_clip = fps * 90

    print(str(fps))

    while True:
        ret, frame = cap.read()

        if ret:
            frame_num += 1
        else:
            if frame_num > 1:
                out.release()
                print(current_video_name)
                print(current_video_path)
            break

        out.write(frame)
        cv2.imshow('frame', frame)

        if frame_num >= frame_per_clip:
            if saved is False:
                out.release()
                print(current_video_name)
                print(current_video_path)
                saved = True

                current_video_name = str(datetime.timestamp(datetime.now())).split(".")[0]
                current_video_path = './outputs/' + current_video_name + '.mp4'
                out = cv2.VideoWriter(current_video_path, fourcc, fps, (width, height))

                frame_num = 0
                current_video += 1
        else:
            saved = False

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


try:
    main()
except Exception as e:
    print(e)
