import os
import tqdm


def write_to_file(data_dir, f):
    for dir, dirs, files in tqdm.tqdm(os.walk(data_dir)):
        for index, file in enumerate(files):
            filepath = os.path.join(dir, file)

            if filepath.endswith(".jpg") or filepath.endswith(".JPG") or filepath.endswith(".png"):
                f.write("%s %s\n" % (os.path.join(filepath.split('/')[-2]
                                , filepath.split('/')[-1]), filepath.split('/')[-2]))
                # print(filepath)


if __name__ == "__main__":
    # generate dataset for unnormal data
    print('generate dataset for training data')
    new_dir = './data_list'
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)

    f = open(os.path.join(new_dir, 'train_list.txt'), 'w')

    data_dir = '../face_dataset/ms1m_align_112'
    write_to_file(data_dir, f)

    f.close()

