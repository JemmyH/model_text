# coding:utf-8
import requests
import json
from random import sample

header = {
    'Accept':
        'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':
        'gzip, deflate',
    'Accept-Language':
        'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection':
        'keep-alive',
    'Content-Type':
        'application/x-www-form-urlencoded; charset=utf-8',
    'Cookie':
        'www91upcom$$BDRCVFRU=nd; NTKF_T2D_CLIENTID=guest6ED517B6-BF9F-49F1-D6A2-572CF8BB18A5; Hm_lvt_bf25d2c507f127f66be27a6e237cc090=1539060858; ASP.NET_SessionId=j2blzw0txtmb0zcfur1wefaj; learning_help_first=true; www91upcom$$BDRCVFRU=nd; bdshare_firstime=1539064146824; 101UP-SESSIONID=ACA63826A5523BA215A3E780D3982043; dsy_sdhghbjb_hgsjahd=b12b213bb213hsahebhb223bhagh; nTalk_CACHE_DATA={uid:kf_9162_ISME9754_202075177376,tid:1539060857018021}; Hm_lpvt_bf25d2c507f127f66be27a6e237cc090=1539064264',
    'Host':
        'www.91up.com',
    'Referer':
        'http://www.91up.com/course/3265/chapter/learn?bankId=502106&catalogId=142588&resultMode=0',
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'X-Requested-With':
        'XMLHttpRequest',
}


def get_big_area():
    data = {'unitId': '2476', 'catalogId': '142588', 'bankId': '502106'}
    res = requests.post(
        'http://www.91up.com/Practice/chapter/GetCatalog',
        headers=header,
        data=data)
    tem = json.loads(res.text)['UserCatalogs'][2:]
    a = []
    for i in tem:
        a.append([i['Id'], i['Title']])
    print(a)
    return a  # [[142589, '华北'], [142595, '东北'], [142599, '华东'], [142607, '华中'], [142611, '华南'], [142615, '西南'], [142621, '西北'], [145165, '中国著名景观']]


def get_city(big_area):
    city_data = []
    for i in big_area:
        data = {'unitId': '2476', 'catalogId': str(i[0]), 'bankId': '502106'}
        res = json.loads(
            requests.post(
                'http://www.91up.com/Practice/chapter/GetCatalog',
                headers=header,
                data=data).text)['UserCatalogs'][2:]
        a = []
        for i in res:
            a.append([i['Id'], i['Title'], i['TotalCount']])
        city_data.append(a)
    print(city_data)
    return city_data  # [[[142590, '北京'], [142591, '天津'], [142592, '河北'], [142593, '山西'], [142594, '内蒙古']], [[142596, '辽宁'], [142597, '吉林'], [142598, '黑龙江']], [[142600, '上海'], [142601, '江苏'], [142602, '浙江'], [142603, '安徽'], [142604, '福建'], [142605, '江西'], [142606, '山东']], [[142608, '河南'], [142609, '湖北'], [142610, '湖南']], [[142612, '广东'], [142613, '广西'], [142614, '海南']], [[142616, '重庆'], [142617, '四川'], [142618, '贵州'], [142619, '云南'], [142620, '西藏']], [[142622, '陕西'], [142623, '甘肃'], [142624, '青海'], [142625, '宁夏'], [142626, '新疆']], [[142401, '中国的世界遗产'], [145168, '中国的世界地质公园及其他']]]


def get_total_id(city_data):
    total_id = []
    for i in city_data:
        # i = [[142590, '北京',40], [142591, '天津',32], [142592, '河北'], [142593, '山西'], [142594, '内蒙古']]
        for j in i:
            # j = [142590, '北京',40]
            res = requests.get(
                'http://www.91up.com/course/3265/chapter/chapter?unitId=2476&bankId=502106&catalogId={0}&userCount={1}&questionTypeId=0&resultMode=2&answerMode=0&jectiveMode=1&count={2}'
                    .format(j[0], j[2], j[2]),
                headers=header)
            a = [i['Id'] for i in json.loads(res.text)['Cells']]
            print(a)
            total_id.append(a)
    print(total_id)
    return total_id  # [[1493223, 1494185, 1501087, 1501212, 1462623, 1495298, 1497751, 1497763, 1495064, 1495192, 1464949, 1494979, 1464951, 1495238, 1495137, 1497738, 1495146, 1427344, 1495119, 1497778, 1464962, 1501220, 1636715, 1464952, 1495279, 1462622, 1497989, 1495091, 1497781, 1495179, 1497923, 1494187, 1493175, 1501224, 1495314, 1464971, 1464950, 1497732, 1501234, 1496797], [1501181, 1464972, 1464945, 1495222, 1464973, 1497952, 1501131, 1495184, 1494059, 1495008, 1464947, 1464946, 1495299, 1497948, 1464960, 1497978, 1494988, 1495120, 1464948, 1501129, 1466674, 1497993, 1497894, 1501098, 1501116, 1497943, 1495141, 1501146, 1462674, 1497902, 1497956, 1497753]]


def get_detail(total_id):
    result = []
    for i in total_id:
        # i = [1493223, 1494185, 1501087, 1501212, 1462623, 1495298]
        # 将id以20个为单位进行分组
        tem = []
        devi = (len(i) // 20) if (len(i) / 20) == (
                len(i) // 20) else ((len(i) // 20) + 1)
        if (len(i) / 20) != (len(i) // 20):
            for j in range(devi - 1):
                ah = []
                for k in range(j * 20, (j + 1) * 20 - 1):
                    ah.append(i[k])
                tem.append(ah)
            ah = []
            for j in range((devi - 1) * 20, len(i)):
                ah.append(i[j])
            tem.append(ah)
        else:
            for j in range(devi):
                ah = []
                for k in range(j * 20, (j + 1) * 20 - 1):
                    ah.append(i[k])
                tem.append(ah)
        # 将20一组的id换成str
        for j in tem:
            s = ''
            for k in j:
                s += "&ids={}".format(k)
            res = requests.get(
                'http://www.91up.com/course/3265/chapter/getquestions?unitId=2476{0}'
                    .format(s),
                headers=header)
            result.append(json.loads(res.text))
    print(result)
    return result


def get_json(result):
    fir = ['华北', '东北', '华东']
    # sec = ['华中','华南','西南','西北']
    judge = []
    singal = []
    multi = []
    firs = [[], [], []]
    secs = [[], [], []]
    for i in result:
        for j in i:
            if j['Question']['QuestionType'] == 10:
                # 单选题
                tmp = {}
                tmp['id'] = j['Question']['Id']
                tmp['subject'] = j['Question']['Catalogs'][0]['Title']
                tmp['area'] = j['Question']['Catalogs'][1]['Title']
                tmp['city'] = j['Question']['Catalogs'][2]['Title']
                tmp['title'] = j['Question']['SubItems'][0]['Body']
                tmp['answer'] = j['Question']['SubItems'][0]['Answer']
                tmp['explation'] = j['Question']['SubItems'][0]['Explanation']
                tmp['options'] = j['Question']['SubItems'][0]['Options']
                singal.append(tmp)
                if tmp['area'] in fir:
                    firs[0].append(tmp)
                else:
                    secs[0].append(tmp)


            elif j['Question']['QuestionType'] == 30:
                # 判断题
                tmp = {}
                tmp['id'] = j['Question']['Id']
                tmp['subject'] = j['Question']['Catalogs'][0]['Title']
                tmp['area'] = j['Question']['Catalogs'][1]['Title']
                tmp['city'] = j['Question']['Catalogs'][2]['Title']
                tmp['title'] = j['Question']['SubItems'][0]['Body']
                tmp['answer'] = j['Question']['SubItems'][0]['Answer']
                tmp['explation'] = j['Question']['SubItems'][0]['Explanation']
                # tmp['options'] = j['Question']['SubItems'][0]['Options']  # 选择题没有选项
                judge.append(tmp)
                if tmp['area'] in fir:
                    firs[1].append(tmp)
                else:
                    secs[1].append(tmp)
            else:
                # 多选题
                tmp = {}
                tmp['id'] = j['Question']['Id']
                tmp['subject'] = j['Question']['Catalogs'][0]['Title']
                tmp['area'] = j['Question']['Catalogs'][1]['Title']
                tmp['city'] = j['Question']['Catalogs'][2]['Title']  # tag
                tmp['title'] = j['Question']['SubItems'][0]['Body']
                tmp['answer'] = j['Question']['SubItems'][0]['Answer']
                tmp['explation'] = j['Question']['SubItems'][0]['Explanation']
                tmp['options'] = j['Question']['SubItems'][0]['Options']
                multi.append(tmp)
                if tmp['area'] in fir:
                    firs[2].append(tmp)
                else:
                    secs[2].append(tmp)
    # a = sample(singal, 80)
    # b = sample(judge, 40)
    # c = sample(multi, 40)
    write_to_file(singal, '单选')
    write_to_file(judge, '判断')
    write_to_file(multi, '多选')

    a_fir = sample(firs[0], 80)
    b_fir = sample(firs[1], 40)
    c_fir = sample(firs[2], 40)
    create_file(a_fir, b_fir, c_fir, 1, '试卷一')  # 1代表给学生
    a_sec = sample(secs[0], 80)
    b_sec = sample(secs[1], 40)
    c_sec = sample(secs[2], 40)
    create_file(a_sec, b_sec, c_sec, 2, '试卷一（带答案）')  # 2代表给老师

    a_fir = sample(firs[0], 80)
    b_fir = sample(firs[1], 40)
    c_fir = sample(firs[2], 40)
    create_file(a_fir, b_fir, c_fir, 1, '试卷二')  # 1代表给学生
    a_sec = sample(secs[0], 80)
    b_sec = sample(secs[1], 40)
    c_sec = sample(secs[2], 40)
    create_file(a_sec, b_sec, c_sec, 2, '试卷二（带答案）')  # 2代表给老师


def create_file(singal, judge, multi, flag, filename):
    option_dict = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E'
    }
    with open('/home/hujiaming/文档/{0}.csv'.format(filename), 'w') as f:
        f.write("{}\n".format(filename))
        f.write("一、单选(每题0.5分，80题共40分)\n")
        text_num = 1
        for i in singal:
            f.write("{}. {}\n".format(text_num, i['title']))
            text_num += 1
            for j, k in enumerate(i['options']):
                f.write("{}. {}\n".format(option_dict[j+1], k))
            # 在这里添加正确答案以及解析
            if flag == 2:
                f.write("【答案】{}\n".format(i['answer']))
                f.write(("【解析】{}\n".format(i['explation'])))
        f.write("\n")
        f.write("二、多项选择题（每题1分，共40分）\n")
        text_num = 1
        for i in multi:
            f.write("{}. {}\n".format(text_num, i['title']))
            text_num += 1
            for j, k in enumerate(i['options']):
                f.write("{}. {}\n".format(option_dict[j+1], k))
            if flag == 2:
                f.write("【答案】{}\n".format(i['answer']))
                f.write(("【解析】{}\n".format(i['explation'])))
        f.write("\n")
        f.write("三.判断题（每题0.5分，40题共20分）\n")
        text_num = 1
        for i in judge:
            f.write("(    ) {}. {}\n".format(text_num, i['title']))
            text_num += 1
            if flag == 2:
                f.write("【答案】{}\n".format(i['answer']))
                f.write(("【解析】{}\n".format(i['explation'])))


def write_to_file(alist, name):
       with open("/home/hujiaming/文档/{}.json".format(name), 'w') as f1:
        for i in alist:
            json.dump(i, f1, ensure_ascii=False)
            f1.write(',\n')


if __name__ == '__main__':
    get_json(get_detail(get_total_id(get_city(get_big_area()))))
