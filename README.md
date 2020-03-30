# chinese_id_checker  中国公民身份证校验模块

[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)     [![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)

[github](https://github.com/BruceWW/chinese_id_checker)

### 安装  installation
经过测试，支持python3.6+
python 3.6+ is supported
```sh
$ pip install chinese_id_checker
```

### 基础使用使用  basic usage
```python
from chinese_id_checker import ChineseIdChecker
# 实例化身份证校验对象
chinses_id_obj = ChinsesIdChecker('110101199511114295')
# 判断传入身份证是否正确
chinese_id_obj.check()
>>> True
# 获取传入身份证的生日
chinese_id_obj.get_birthday()
>>> '1995-11-11'
# 获取传入身份证的所属区域，结果:[省],[市],[区]
chinese_id_obj.get_location()
>>> '北京市,北京市,东城区'
# 获取传入身份证所属省份
chinese_id_obj.get_location()
>>> '北京市'
# 获取传入身份证所属城市
chinese_id_obj.get_location()
>>> '北京市'
# 获取传入身份证所属区县
chinese_id_obj.get_location()
>>> '东城区'
# 为已实例化的对象设置新的身份证号
chinese_id_obj.id_str = '110101199511116098'
```

### 行政区配置文件说明 district instruction
行政区配置文件格式说明
默认目录：data_source
默认文件：location.json
默认备份目录：data_source/bak
默认备份文件：location.json.bak
数据格式
```json
{
    "id_code": ["privince","city","district"],
    "110101": ["北京市", "北京市", "东城区"]
}
```

行政区模块使用
```python
from chinese_id_checker impoer Location
location_obj = Location()
# 备份文件
location_obj.bak_file()
>>> True
# 回滚文件
location_obj.roll_back()
>>> True
# 添加新的数据（如果id_code已存在会返回False）
location_obj.add_info(id_code='999999', province='xxx', city='xxx', district='xxx')
>>> True
# 添加或更新新的数据（如果id_code已存在，会覆盖原始数据）
location_obj.add_info(id_code='999999', province='xxx', city='xxx', district='xxx', update_id_exist=False)
>>> True
# 删除已存在的数据（如果id_code不存在，则返回False)
location_obj.remove_info('999999')
>>> True
# 使用csv生成json文件
# 输入文件为参数csv_path: data_source/data_source_200327.csv
# 输出文件为参数output_path: 如果为None，则放到默认目录下
# with_head参数用于判断csv文件是否有标题行
# columns参数为数据处理列，接受可迭代对象，长度为4，第一个值为id_code的列，第二个值为省名称，第三个值为市名称，第四个值为区县名称
location_obj.output_json_file_from_csv(csv_path='data_source/data_source_200327.csv',output_path=None,with_head=True,columns=(4,1,2,3)
```


# 维护者 maintainers

[Lin Luo / Bruce Liu](15869600264@163.com
)