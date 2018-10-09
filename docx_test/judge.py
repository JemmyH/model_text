# coding:utf-8
from docx import Document


def get_resource(path):
    d = Document(path)
    t = [i.text for i in d.paragraphs]
    s = []
    for i in t:
        if i.find("\n") > -1:
            tem = i.split("\n")
            for j in tem:
                s.append(j)
        else:
            s.append(i)
    s = [i for i in s if len(i) > 0]
    return s


def make_list(s):
    num = [str(i) for i in range(10)]  # ['1','2',.......'9']
    num_index = []
    for i in s:
        if i[0] in num:
            num_index.append(s.index(i))  # 获得了标题索引
    singal_text = []
    for i in range(len(num_index) - 1):
        a = [s[j] for j in range(num_index[i], num_index[i + 1])]
        singal_text.append(a)
    a = [s[j] for j in range(num_index[-1], len(s))]
    singal_text.append(a)
    return singal_text


def pre_check(singal_text):
    # 标签跑到上一行中了
    for i in singal_text:
        for j, k in enumerate(i):
            if k.count('【') > 1:
                pass



def partion(singal_text):
    for i in singal_text:
        for j, k in enumerate(i):
            if k[0] in num:
                print('标题：', end='')
                print(j, k)
            if k[:2] == '答案':
                print('答案：', end='')
                print(j, k)
            if k[:4] == '【解析】':
                print('解析：', end='')
                print(j, k)
            if k[:5] == '【知识点】':
                print('知识点：', end='')
                print(j, k)


if __name__ == '__main__':
    path = '/home/hujiaming/文档/judge_dongbei_heilongjiang.docx'
