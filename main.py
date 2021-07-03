import os

file1 = '1.txt'
file2 = '2.txt'
file3 = '3.txt'
output_file = 'result.txt'
file1_path = os.path.join(os.getcwd(), file1)
file2_path = os.path.join(os.getcwd(), file2)
file3_path = os.path.join(os.getcwd(), file3)
output_path = os.path.join(os.getcwd(), output_file)

paths = [file1_path, file2_path, file3_path]

def make_feed(path_file):
    read_dict = {}
    feed_list = []
    for ind, elm in enumerate(path_file):
        with open(elm, 'r', encoding='utf-8') as read:
            feed = []
            for line in read:
                feed.append(line)
        read_dict[int(ind)] = [elm + '\n', str(len(feed)) + '\n', feed, '\n']
    feed_list.append(read_dict)
    return feed_list

feed_list = make_feed(paths)

def feed_to_output(feed_list):
    output_feed = []
    with open(output_path, "w") as output:
        for ind, elm in enumerate(feed_list):
            for key, value in elm.items():
                output_feed.append(value)
    output_feed.sort(key=lambda item: len(item[2]))
    return output_feed

output_list = feed_to_output(feed_list)

def write_output(output_data, output_path):
    with open(output_path, "w") as output:
        for elm in output_data:
            for part in elm:
                output.writelines(part)

write_output(output_list, output_file)