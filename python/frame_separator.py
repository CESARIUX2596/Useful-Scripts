import cv2


def video_frame_separation(video_path, output_path, file_name, frame_gap):
    capture = cv2.VideoCapture(video_path)
    count = 0
    while True:
        ret, frame = capture.read()
        if ret == False:
            capture.release()
            break
        if count == 0:
            cv2.imwrite(f'{output_path+file_name}{count}.jpg', frame)
        else:
            if count % frame_gap == 0:
                cv2.imwrite(f'{output_path+file_name}{count}.jpg', frame)
        count += 1
    print('Done')



def main():

    video_path = 'Input folder path'
    output_path = 'output folder path'
    file_name = 'frame_'
    frame_gap = 4
    video_frame_separation(video_path, output_path, file_name, frame_gap)


if __name__ == '__main__':
    main()
