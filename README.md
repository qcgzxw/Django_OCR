# Django_OCR
接口练习，调用腾讯云OCR接口实现各种图片的识别。

## 配置说明：
Python 3.7

Django 2.1a1

## 使用说明：
下载所有代码后，更改 ==/apps/txystsb/== 目录下的conf.py配置文件。

进入到虚拟环境，在根目录下执行 ==python manager.py runserver [端口]==

访问 ==127.0.0.1:[端口]== 即可看到初始界面，直接上传图片，选择对应的识别方式开始图片识别。


## 返回json数据
以下图片数据均来自 百度搜图 ，隐私部位已打码，侵删。
1. 身份证识别（正面）：

```
{
    "result_list": [
        {
            "code": 0,
            "message": "OK",
            "filename": "sfz1.jpg.JPG",
            "data": {
                "name": "小文博客",
                "sex": "男",
                "nation": "汉",
                "birth": "2018/9/13",
                "address": "安徽省安庆市大观区",
                "id": "3408032018091366666",
                "name_confidence_all": [
                    100
                ],
                "sex_confidence_all": [
                    69
                ],
                "nation_confidence_all": [
                    64
                ],
                "birth_confidence_all": [
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100
                ],
                "address_confidence_all": [
                    88,
                    99,
                    51,
                    97,
                    77,
                    31,
                    70,
                    93,
                    51,
                    99,
                    99,
                    98,
                    51,
                    52,
                    59,
                    99
                ],
                "id_confidence_all": [
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100
                ]
            }
        }
    ]
}
```

2. 身份证识别（反面）：

```
{
    "result_list": [
        {
            "code": 0,
            "message": "OK",
            "filename": "sfz2.JPG",
            "data": {
                "authority": "中国公安局",
                "valid_date": "2018.9.13-2118.9.13",
                "authority_confidence_all": [
                    100
                ],
                "valid_date_confidence_all": [
                    85,
                    79,
                    65,
                    98,
                    86,
                    81,
                    57,
                    56,
                    83,
                    83,
                    34,
                    52,
                    40,
                    49
                ]
            }
        }
    ]
}
```

3. 名片识别：

```
{
    "result_list": [
        {
            "code": 0,
            "message": "OK",
            "filename": "mp.jpg",
            "data": [
                {
                    "item": "公司",
                    "value": "小文博客",
                    "confidence": 0.9868298172950744
                },
                {
                    "item": "地址",
                    "value": "中国",
                    "confidence": 0.9981801509857178
                },
                {
                    "item": "手机",
                    "value": "13000000000",
                    "confidence": 0.998361885547638
                },
                {
                    "item": "电话",
                    "value": "010-1234567",
                    "confidence": 0.9968294501304628
                },
                {
                    "item": "传真",
                    "value": "010-1234567",
                    "confidence": 0.6805435419082642
                },
                {
                    "item": "公司账号",
                    "value": "9559900000000000000",
                    "confidence": 1.0
                }
            ]
        }
    ]
}
```

4. 行驶证识别：

```
{
	"code": 0,
	"message": "OK",
	"data": {
		"session_id": "1252089729-776801086",
		"items": [{
			"item": "所有人",
			"itemcoord": {
				"x": 111,
				"y": 142,
				"width": 84,
				"height": 36
			},
			"itemconf": 0.5837883949279785,
			"itemstring": "入徐峥"
		}, {
			"item": "住址",
			"itemcoord": {
				"x": 107,
				"y": 195,
				"width": 390,
				"height": 30
			},
			"itemconf": 0.4140888750553131,
			"itemstring": "广东省深圳市福田南路9号皇御苑4栋302室"
		}, {
			"item": "品牌型号",
			"itemcoord": {
				"x": 303,
				"y": 235,
				"width": 227,
				"height": 35
			},
			"itemconf": 0.4373725950717926,
			"itemstring": "宝马WBSG1618"
		}, {
			"item": "使用性质",
			"itemcoord": {
				"x": 126,
				"y": 240,
				"width": 72,
				"height": 28
			},
			"itemconf": 1.0,
			"itemstring": "非营运"
		}, {
			"item": "识别代码",
			"itemcoord": {
				"x": 274,
				"y": 285,
				"width": 136,
				"height": 40
			},
			"itemconf": 0.9991225600242616,
			"itemstring": "12312321"
		}, {
			"item": "发动机号",
			"itemcoord": {
				"x": 301,
				"y": 327,
				"width": 181,
				"height": 40
			},
			"itemconf": 0.8825730681419373,
			"itemstring": "WBSG1618"
		}, {
			"item": "注册日期",
			"itemcoord": {
				"x": 258,
				"y": 377,
				"width": 156,
				"height": 38
			},
			"itemconf": 0.4257842600345612,
			"itemstring": " "
		}, {
			"item": "发证日期",
			"itemcoord": {
				"x": 461,
				"y": 379,
				"width": 143,
				"height": 30
			},
			"itemconf": 0.7899119853973389,
			"itemstring": "2014-10-29"
		}]
	}
}
```

5. 驾驶证识别：

```
{
	"code": 0,
	"message": "OK",
	"data": {
		"session_id": "12520897292100492157",
		"items": [{
			"item": "证号",
			"itemcoord": {
				"x": 165,
				"y": 49,
				"width": 146,
				"height": 23
			},
			"itemconf": 0.6305853724479675,
			"itemstring": "440204199104284722"
		}, {
			"item": "性别",
			"itemcoord": {
				"x": 216,
				"y": 74,
				"width": 19,
				"height": 21
			},
			"itemconf": 0.9996992945671082,
			"itemstring": "女"
		}, {
			"item": "姓名",
			"itemcoord": {
				"x": 63,
				"y": 76,
				"width": 99,
				"height": 21
			},
			"itemconf": 0.9860403537750244,
			"itemstring": "叶真志"
		}, {
			"item": "国籍",
			"itemcoord": {
				"x": 284,
				"y": 75,
				"width": 34,
				"height": 20
			},
			"itemconf": 0.9999998211860656,
			"itemstring": "中国"
		}, {
			"item": "住址",
			"itemcoord": {
				"x": 64,
				"y": 96,
				"width": 287,
				"height": 22
			},
			"itemconf": 0.36578431725502016,
			"itemstring": "广东省江门市新会汉会城帝临南路6号403"
		}, {
			"item": "出生日期",
			"itemcoord": {
				"x": 167,
				"y": 141,
				"width": 81,
				"height": 20
			},
			"itemconf": 0.9912522435188294,
			"itemstring": "1991-04-28"
		}, {
			"item": "领证日期",
			"itemcoord": {
				"x": 187,
				"y": 163,
				"width": 81,
				"height": 21
			},
			"itemconf": 0.6987147331237793,
			"itemstring": "2014-04-17"
		}, {
			"item": "准驾车型",
			"itemcoord": {
				"x": 196,
				"y": 187,
				"width": 43,
				"height": 23
			},
			"itemconf": 0.4786324203014374,
			"itemstring": "A1"
		}, {
			"item": "起始日期",
			"itemcoord": {
				"x": 93,
				"y": 212,
				"width": 90,
				"height": 22
			},
			"itemconf": 0.7346487045288086,
			"itemstring": "2014-04-17"
		}, {
			"item": "有效日期",
			"itemcoord": {
				"x": 198,
				"y": 212,
				"width": 85,
				"height": 21
			},
			"itemconf": 0.8567164540290833,
			"itemstring": "2020-04-17"
		}, {
			"item": "发证单位",
			"itemcoord": {
				"x": 36,
				"y": 142,
				"width": 83,
				"height": 75
			},
			"itemconf": 0.9711614847183228,
			"itemstring": "广东省江门市公安局交通警察支队"
		}, {
			"item": "红章",
			"itemcoord": {
				"x": 36,
				"y": 142,
				"width": 83,
				"height": 75
			},
			"itemconf": 0.9711614847183228,
			"itemstring": "广东省江门市公安局交通警察支队"
		}]
	}
}
```

6. 驾驶证识别（副页）：

```
{
	"code": 0,
	"message": "OK",
	"data": {
		"session_id": "1252089729-1330448932",
		"items": [{
			"item": "号牌号码",
			"itemcoord": {
				"x": 174,
				"y": 133,
				"width": 173,
				"height": 49
			},
			"itemconf": 0.6521227955818176,
			"itemstring": "鲁AY883"
		}, {
			"item": "",
			"itemcoord": {
				"x": 0,
				"y": 0,
				"width": 0,
				"height": 0
			},
			"itemconf": 0.0,
			"itemstring": ""
		}, {
			"item": "准牵引总质量",
			"itemcoord": {
				"x": 445,
				"y": 501,
				"width": 179,
				"height": 41
			},
			"itemconf": 1.0,
			"itemstring": "--"
		}, {
			"item": "",
			"itemcoord": {
				"x": 0,
				"y": 0,
				"width": 0,
				"height": 0
			},
			"itemconf": 0.0,
			"itemstring": ""
		}, {
			"item": "档案编号",
			"itemcoord": {
				"x": 587,
				"y": 658,
				"width": 248,
				"height": 49
			},
			"itemconf": 0.02100922167301178,
			"itemstring": "370101037339"
		}, {
			"item": "总质量",
			"itemcoord": {
				"x": 754,
				"y": 728,
				"width": 125,
				"height": 47
			},
			"itemconf": 0.5430548787117004,
			"itemstring": "2025kg"
		}, {
			"item": "核定载人数",
			"itemcoord": {
				"x": 201,
				"y": 747,
				"width": 71,
				"height": 44
			},
			"itemconf": 0.9934362769126892,
			"itemstring": "5人"
		}, {
			"item": "整备质量",
			"itemcoord": {
				"x": 210,
				"y": 819,
				"width": 120,
				"height": 47
			},
			"itemconf": 0.9999564290046692,
			"itemstring": "1615kg"
		}, {
			"item": "外廓尺寸",
			"itemcoord": {
				"x": 218,
				"y": 881,
				"width": 350,
				"height": 59
			},
			"itemconf": 0.9943339824676514,
			"itemstring": "4760×1811×1455mm"
		}, {
			"item": "检验记录",
			"itemcoord": {
				"x": 155,
				"y": 253,
				"width": 787,
				"height": 908
			},
			"itemconf": 0.0,
			"itemstring": "检验有效期至2018-09-07汽油"
		}, {
			"item": "核定载质量",
			"itemcoord": {
				"x": 10,
				"y": 10,
				"width": 10,
				"height": 10
			},
			"itemconf": 1.0,
			"itemstring": "--"
		}]
	}
}
```

7. 车牌识别：

```
{
	"code": 0,
	"message": "OK",
	"data": {
		"items": [{
			"item": "车牌",
			"itemcoord": {
				"x": 242,
				"y": 253,
				"width": 198,
				"height": 64
			},
			"itemconf": 0.9997475743293762,
			"itemstring": "鄂B74110"
		}]
	}
}
```

8. 银行卡识别：

```
{
	"code": 0,
	"message": "OK",
	"data": {
		"recognize_warn_msg": [],
		"recognize_warn_code": [],
		"items": [{
			"item": "卡号",
			"itemcoord": {
				"x": 53,
				"y": 153,
				"width": 329,
				"height": 27
			},
			"itemconf": 0.9791542887687684,
			"itemstring": "6217003810026896707",
			"coords": [],
			"words": [],
			"candword": [],
			"wordcoordpoint": []
		}, {
			"item": "卡类型",
			"itemcoord": {
				"x": 10,
				"y": 10,
				"width": 10,
				"height": 10
			},
			"itemconf": 0.9791542887687684,
			"itemstring": "借记卡",
			"coords": [],
			"words": [],
			"candword": [],
			"wordcoordpoint": []
		}, {
			"item": "卡名字",
			"itemcoord": {
				"x": 10,
				"y": 30,
				"width": 10,
				"height": 10
			},
			"itemconf": 0.9791542887687684,
			"itemstring": "龙卡通",
			"coords": [],
			"words": [],
			"candword": [],
			"wordcoordpoint": []
		}, {
			"item": "银行信息",
			"itemcoord": {
				"x": 10,
				"y": 50,
				"width": 10,
				"height": 10
			},
			"itemconf": 0.9791542887687684,
			"itemstring": "建设银行(01050000)",
			"coords": [],
			"words": [],
			"candword": [],
			"wordcoordpoint": []
		}, {
			"item": " 有效期",
			"itemcoord": {
				"x": 201,
				"y": 186,
				"width": 58,
				"height": 21
			},
			"itemconf": 0.999996781349182,
			"itemstring": "07/2024",
			"coords": [],
			"words": [],
			"candword": [],
			"wordcoordpoint": []
		}],
		"session_id": "1252089729-1506607680",
		"class": []
	}
}
```

9. 营业执照识别：

```
{
	"code": 0,
	"message": "OK",
	"data": {
		"session_id": "1252089729296943063",
		"items": [{
			"item": "注册号",
			"itemcoord": {
				"x": 341,
				"y": 328,
				"width": 112,
				"height": 16
			},
			"itemconf": 0.9978125095367432,
			"itemstring": "371526200019332",
			"coords": [],
			"words": [],
			"candword": []
		}, {
			"item": "法定代表人",
			"itemcoord": {
				"x": 187,
				"y": 450,
				"width": 55,
				"height": 19
			},
			"itemconf": 0.9986087679862976,
			"itemstring": "高友帅",
			"coords": [],
			"words": [],
			"candword": []
		}, {
			"item": "注册资本",
			"itemcoord": {
				"x": 186,
				"y": 479,
				"width": 84,
				"height": 19
			},
			"itemconf": 0.9974791407585144,
			"itemstring": "贰仟万元整",
			"coords": [],
			"words": [],
			"candword": []
		}, {
			"item": "公司名称",
			"itemcoord": {
				"x": 184,
				"y": 360,
				"width": 183,
				"height": 19
			},
			"itemconf": 0.9995620250701904,
			"itemstring": "山东高仕过滤技术有限公司",
			"coords": [],
			"words": [],
			"candword": []
		}, {
			"item": "地址",
			"itemcoord": {
				"x": 186,
				"y": 419,
				"width": 291,
				"height": 18
			},
			"itemconf": 0.9905643463134766,
			"itemstring": "高唐县人和办事处308国道东转盘东2公里路北",
			"coords": [],
			"words": [],
			"candword": []
		}, {
			"item": "营业期限",
			"itemcoord": {
				"x": 178,
				"y": 536,
				"width": 255,
				"height": 19
			},
			"itemconf": 0.997233271598816,
			"itemstring": "2014年08月01 日至长期",
			"coords": [],
			"words": [],
			"candword": []
		}, {
			"item": "经营范围",
			"itemcoord": {
				"x": 183,
				"y": 567,
				"width": 314,
				"height": 42
			},
			"itemconf": 0.9924321174621582,
			"itemstring": "提供过滤技术交流、咨询、推广服务;生产、销售:过滤设备及配件,并提供以上产品的安装及维修服务(依法须经批准的项目,经相关部门批准后方可开展经营活动)",
			"coords": [],
			"words": [],
			"candword": []
		}, {
			"item": "主体类型",
			"itemcoord": {
				"x": 188,
				"y": 390,
				"width": 237,
				"height": 20
			},
			"itemconf": 0.999891459941864,
			"itemstring": "有限责任公司(自然人投资或控股)",
			"coords": [],
			"words": [],
			"candword": []
		}]
	}
}
```

10. 通用印刷体识别：

```
{
	"code": 0,
	"message": "OK",
	"data": {
		"class": [],
		"angle": 0.0,
		"items": [{
			"itemcoord": {
				"x": 8,
				"y": 8,
				"width": 295,
				"height": 55
			},
			"words": [{
				"character": "图",
				"confidence": 0.9999860525131226
			}, {
				"character": "片",
				"confidence": 0.9988077878952026
			}, {
				"character": "来",
				"confidence": 0.99984610080719
			}, {
				"character": "自",
				"confidence": 0.999526023864746
			}, {
				"character": "小",
				"confidence": 0.9999170303344728
			}, {
				"character": "文",
				"confidence": 0.9996131062507628
			}, {
				"character": "’",
				"confidence": 0.6718323230743408
			}],
			"itemstring": "图片来自小文’"
		}, {
			"itemcoord": {
				"x": 326,
				"y": 17,
				"width": 116,
				"height": 47
			},
			"words": [{
				"character": "s",
				"confidence": 0.6071960926055908
			}, {
				"character": "",
				"confidence": 1.0
			}, {
				"character": "b",
				"confidence": 0.99984872341156
			}, {
				"character": "l",
				"confidence": 0.993683695793152
			}, {
				"character": "o",
				"confidence": 0.9966122508049012
			}, {
				"character": "g",
				"confidence": 0.999716818332672
			}],
			"itemstring": "s blog"
		}, {
			"itemcoord": {
				"x": 57,
				"y": 70,
				"width": 296,
				"height": 40
			},
			"words": [{
				"character": "转",
				"confidence": 0.9998407363891602
			}, {
				"character": "载",
				"confidence": 0.999666690826416
			}, {
				"character": "请",
				"confidence": 0.9987756609916688
			}, {
				"character": "注",
				"confidence": 0.9994645714759828
			}, {
				"character": "明",
				"confidence": 0.9996492862701416
			}, {
				"character": "出",
				"confidence": 0.9999841451644898
			}, {
				"character": "处",
				"confidence": 0.999714195728302
			}],
			"itemstring": "转载请注明出处"
		}],
		"session_id": "1252089729405993189"
	}
}
```

11. 手写体识别：

```
{
	"code": 0,
	"message": "OK",
	"data": {
		"recognize_warn_msg": [],
		"recognize_warn_code": [],
		"items": [{
			"itemcoord": {
				"x": 0,
				"y": 8,
				"width": 309,
				"height": 52
			},
			"itemconf": 0.9999167323112488,
			"itemstring": "图片来自小文",
			"coords": [],
			"words": [{
				"character": "图",
				"confidence": 0.9999890327453612
			}, {
				"character": "片",
				"confidence": 0.999902606010437
			}, {
				"character": "来",
				"confidence": 0.9999804496765136
			}, {
				"character": "自",
				"confidence": 0.9999884366989136
			}, {
				"character": "小",
				"confidence": 0.9999948740005492
			}, {
				"character": "文",
				"confidence": 0.9996446371078492
			}],
			"candword": [],
			"parag": {
				"word_size": 38,
				"parag_no": 0
			},
			"coordpoint": {
				"x": [0, 8, 308, 8, 308, 59, 0, 59]
			},
			"wordcoordpoint": []
		}, {
			"itemcoord": {
				"x": 345,
				"y": 16,
				"width": 97,
				"height": 45
			},
			"itemconf": 0.7773940563201904,
			"itemstring": "; blog",
			"coords": [],
			"words": [{
				"character": ";",
				"confidence": 0.6663510203361511
			}, {
				"character": "",
				"confidence": 1.0
			}, {
				"character": "b",
				"confidence": 0.9999924898147584
			}, {
				"character": "l",
				"confidence": 0.9981441497802734
			}, {
				"character": "o",
				"confidence": 0.9999104738235474
			}, {
				"character": "g",
				"confidence": 0.9999662637710572
			}],
			"candword": [],
			"parag": {
				"word_size": 38,
				"parag_no": 0
			},
			"coordpoint": {
				"x": [345, 16, 441, 16, 441, 60, 345, 60]
			},
			"wordcoordpoint": []
		}, {
			"itemcoord": {
				"x": 58,
				"y": 70,
				"width": 295,
				"height": 40
			},
			"itemconf": 0.999867856502533,
			"itemstring": "转载请注明出处",
			"coords": [],
			"words": [{
				"character": "转",
				"confidence": 0.9997584223747252
			}, {
				"character": "载",
				"confidence": 0.9999712705612184
			}, {
				"character": "请",
				"confidence": 0.999437153339386
			}, {
				"character": "注",
				"confidence": 0.9999452829360962
			}, {
				"character": "明",
				"confidence": 0.9999878406524658
			}, {
				"character": "出",
				"confidence": 0.9999885559082032
			}, {
				"character": "处",
				"confidence": 0.9999864101409912
			}],
			"candword": [],
			"parag": {
				"word_size": 38,
				"parag_no": 0
			},
			"coordpoint": {
				"x": [58, 70, 352, 70, 352, 109, 58, 109]
			},
			"wordcoordpoint": []
		}],
		"session_id": "1252089729959642468",
		"angle": 0.0,
		"class": []
	}
}
```
