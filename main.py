import os

file1 = '1.txt'
file2 = '2.txt'
file3 = '3.txt'
output_file = 'result.txt'
file1_path = os.path.join(os.getcwd(), file1)
file2_path = os.path.join(os.getcwd(), file2)
file3_path = os.path.join(os.getcwd(), file3)
output_path = os.path.join(os.getcwd(), output_file)

read1 = open(file1_path, 'r', encoding='utf-8' )
read1_list = []
for line in read1:
    read1_list.append(line)
read2 = open(file2_path, 'r', encoding='utf-8' )
read2_list = []
for line in read2:
    read2_list.append(line)
read3 = open(file3_path, 'r', encoding='utf-8' )
read3_list = []
for line in read3:
    read3_list.append(line)

output_data1 = ['\n', file1_path +'\n', str(len(read1_list)) +'\n', (read1_list)]
output_data2 = ['\n', file2_path +'\n', str(len(read2_list)) +'\n', (read2_list)]
output_data3 = ['\n', file3_path +'\n', str(len(read3_list)) +'\n', (read3_list)]

output_list = [output_data1, output_data2, output_data3]
output = []
for ind, elm in enumerate(output_list):
    output.append(elm)
output.sort(key=len) # как отсортировать список по

def write_output(output_data, output_path):
    write_to_file = open(output_path, "w")
    for elm in output_data:
        # print(elm)
        for part in elm:
            write_to_file.writelines(part)
    write_to_file.close()

write_output(output, output_file)
