"""
功能：读取测试数据；将读取到的测试数据处理成 "[{},{}]" 形式；
一、读Excel文件
 1.1、使用第三方库：xlrd操作excel
 1.2、1、获取测试数据文件路径 -->2、打开并读取测试文件，创建文件对象 -->3、获取指定sheet页内容-->
     4、获取第一行的值，作为字典的key -->5、获取sheet存在内容的最大行数 -->6定义一个储存结果的列表res_liset=[]
     7、循环sheet的所有行，进行处理-->
     8、将每行值和第一行值，组装成一个字典-->
     9、最后将组装的字典添加到定义好的结果列表中

二、读json文件
三、读yaml文件
"""
# 导包
import xlrd, os


class ReadData:
    def __init__(self, filename):
        """
        :param filename: 数据文件名，带后缀.xls/.json/.yaml
        """
        # 获取测试文件路径
        self.path = os.path.dirname(os.path.dirname(__file__)) + r"/testData/" + filename

    def read_excel(self, sheets):
        """
        :param sheets: sheet页名称/id-->str/int类型
        :return:结果列表-->[{},{}]
        """
        # 读取数据文件
        workbook = xlrd.open_workbook(self.path)
        # 获取指定sheet页
        if type(sheets) == int:
            sheet = workbook.sheet_by_index(sheets)
        elif type(sheets) == str:
            sheet = workbook.sheet_by_name(sheets)
        else:
            sheet = None
            print('参数错误，必须时 int / str 类型')
        # 获取sheet的第一行内容
        first_row = sheet.row_values(0)
        # 获取sheet内容最大行数、列数
        max_row = sheet.nrows
        # 定义一个结果列表
        res_list = []

        # 遍历sheet的所有内容，进行处理
        for line in range(1, max_row):
            # 获取每一行的内容
            row_value = sheet.row_values(line)
            # 将每行的值 与 第一行的值组装成一个字典
            data_dic = dict(zip(first_row, row_value))
            # 添加到结果列表中
            res_list.append(data_dic)
        # 返回结果数据，供外部调用
        return res_list

    def read_json(self):
        pass

    def read_yaml(self):
        pass


if __name__ == '__main__':
    # 实例化对象类
    rd = ReadData('data.xls')
    # 调用实例方法，读取Excel数据
    excel = rd.read_excel(0)
    print(excel)
