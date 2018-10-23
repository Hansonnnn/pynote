

'''rename file'''
def get_file_list():
    pacs_list = list()
    with open("/Users/hanzhao/Downloads/pacs.txt", encoding='utf-8') as file:
        pacs_file = file.readlines()
        for pacs_line in pacs_file:
            pacs = {}
            array = pacs_line.split(',')
            num = array[0]
            tmp = array[1]
            name = ''.join(tmp).strip('\n')
            pacs['num'] = num
            pacs['name'] = name
            pacs_list.append(pacs)
    sort_pacs_list(pacs_list)


def rename_file(pacs_list):
    new_pacs_list = sorted(pacs_list, key=lambda item: int(item['num']))
    for i in range(len(new_pacs_list)):
        src = os.path.join(os.path.abspath(path), new_pacs_list[i]['name'])
        dst = os.path.join(os.path.abspath(new_path), 'pacs_' + format(str(i), '0>3s') + '.dcm')
        os.rename(src, dst)