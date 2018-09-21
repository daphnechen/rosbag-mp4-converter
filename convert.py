# import rosbag2video
import os
import sys

def get_files(path):
    directory = os.fsencode(path)

    for root, dirs, files in os.walk(directory):
        print('ROOT: ' + str(root))
        for name in files:
            filename = os.fsdecode(name)
            # print(filename)
            if filename.endswith(".bag"):
                # print(name.decode("UTF-8"))
                prefix = filename.split(".")
                # print(prefix)
                # print(dirs)
                # print('current directory: ' + str(os.getcwd()))
                relative_path_to_file = root.decode("UTF-8") + "/" + name.decode("UTF-8")
                path_to_file = "/".join(relative_path_to_file.strip("/").split('/')[3:])
                task = path_to_file.split('/')[1]
                user_number = path_to_file.split('/')[2]
                # print(path_to_file)
                # print("python rosbag2video.py --fps 30 -s -o " + prefix[0]
                #     + "-view2.mp4 -t /usb_cam_2/image_raw " + path_to_file)

                # print(task)
                # print(user_number)

                new_path = "videos/" + task + "/" + user_number + "/"
                if not os.path.exists(new_path):
                    try:
                        os.makedirs(new_path)
                    except OSError as e:
                        if e.errno != errno.EEXIST:
                            raise

                os.system("python rosbag2video.py --fps 30 -s -o " + new_path + prefix[0]
                    + "-view1.mp4 -t /usb_cam_1/image_raw " + path_to_file)
            else:
                continue


if __name__ == "__main__":
    path = sys.argv[1]
    get_files(path)