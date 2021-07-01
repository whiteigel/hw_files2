import os

file1 = '1.txt'
file2 = '2.txt'
file3 = '3.txt'
output_file = 'result.txt'
file1_path = os.path.join(os.getcwd(), file1)
file2_path = os.path.join(os.getcwd(), file2)
file3_path = os.path.join(os.getcwd(), file3)
output_path = os.path.join(os.getcwd(), output_file)

with open(file1_path, 'r', encoding='utf-8') as f1:
    read1 = f1.readlines()
with open(file2_path, 'r', encoding='utf-8') as f2:
    read2 = f2.readlines()
with open(file3_path, 'r', encoding='utf-8') as f3:
    read3 = f3.readlines()

output_data1 = [file1_path + '\n', str(len(read1)), '\n'+ str(read1) + '\n']
output_data2 = [file2_path + '\n', str(len(read2)), '\n'+ str(read2) + '\n']
output_data3 = [file3_path + '\n', str(len(read3)), '\n'+ str(read3) + '\n']

sort_len = len([output_data1, output_data2, output_data3])
# print(sort_len)
# sort_len = sorted(sort_len)
# print(sort_len)
output = []
output_list = [output_data1, output_data2, output_data3]
# print(output_list)
for ind, elm in enumerate(output_list):
    output.append(elm)
    # output.sort(key = elm[1])
# print(output)

def write_output(output_list, output_path):
    write_to_file = open(output_path, "w")
    for elm in output_list:
        write_to_file.writelines(elm)
    write_to_file.close()

write_output(output_list, output_file)
