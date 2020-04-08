import requests
import parsel

    #页数循环下载，请按需要修改页数
for page in range(1,10):
    print('===================正在抓取第{}页数据==================='.format(page))
    #图片列表网址，landscape修改成所需要的主题的英文，例如风景，抽象等
    base_url = 'http://wallls.com/tag/landscape/{}'.format(str(page))
    #头文件
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    #获取网页源代码
    response = requests.get(base_url, headers=headers)
    #下载网页源代码
    data = response.text
    #xpath取出目的位置
    html_data = parsel.Selector(data)
    data_list = html_data.xpath('//div[@class="col-sm-3 col-xs-12"]//a/@href').extract()


    #遍历取出得位置
    for alist in data_list:
    #整合成完整路径
        tu = "http://wallls.com" + alist
    #打开路径并解析源代码，第二层网页
        response_2 = requests.get(tu, headers=headers).text
    #xpath取出网页第三层位置，这里指最终图片路径
        html_2 = parsel.Selector(response_2)
        img_url = html_2.xpath('//div[@class="photo-info col-md-offset-1 col-md-3 col-sm-offset-0 col-sm-4 col-xs-offset-0 col-xs-12"]/a/@href').extract_first()
    #图片以content的二进制下载
        img_data = requests.get(img_url, headers=headers).content
    #图片以路径的最后一层命名，-1
        file_name = img_url.split('/')[-1]

    #保存的路径
        with open('img\\' + file_name, 'wb')as f:
            print('正在保存文件',file_name)
    #开始写入
            f.write(img_data)
            f.close()





