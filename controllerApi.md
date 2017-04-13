### Web Controller Rest API Document (ver 1.0.1) ###
<pre>该接口文档用于说明与web server之间通过的api及参数、返回值等</pre>
#### 1. 初始化连接
* 接口说明：APP启动后，首先通过此接口请求获取必要的信息
* 接口地址：http://192.168.1.101/connect
* 接口类型：POST
* 接口参数：
  <pre>
  * frequency : （int）向小车发送脉冲信号的频率，单位毫秒ms
  </pre>
* 接口返回值：
  <pre>
  {
    "status" : "true",
    "response" : "connect to server successful",
    "frequency" : 20,
    "mode" : [
        { 
            "name" : "free",
            "description" : "自由控制模式",
            "code" : "1"
        },
        {
            "name" : "preset",
            "description" : "预设模式",
            "code" : "2"
        },
        {
            "name" : "orbit",
            "description" : "轨迹模式",
            "code" : "3"
        }
    ]
  }
  </pre>

#### 2.即时指令发送
* 接口说明：APP连接成功后，即时性的向服务端发送控制指令
* 接口地址：http://192.168.1.101/action
* 接口类型：POST
* 接口参数：
  <pre>
  * mode ： (int) 标识控制模式，根据mode值判定，取值范围[1,2,3]
  * param : (json) 具体的控制指令的json obj
  </pre>
* 接口示例：
  <pre>
  example [mode = 1]:
    {
        "direction" : "front", // [front、behind、left、right、up、down] = [前、后、左、右、上、下]
        "speed" : "10" // 10cm per second
    }
    
  example [mode = 2]:(预设模式下，运动时长和距离不能同时存在)
    {
        "list" : [
            {
                "direction" : "front",
                "speed" : "10",
                "duration" : "20",// 运动时长，毫秒
            },
            {
                "direction" : "left",
                "speed" : "10",
                "distance" : "300"// 运动距离，毫米
            },
            {
                "direction" : "right",
                "speed" : "10",
                "distance" : "400"// 运动距离，毫米
            }
        ]
    }
    
    example [mode = 3]:(轨迹模式下，发送json文件)
    {
        "fpscapture" : 120,//每秒的采集帧数
        "list" : [
            {
                "info" : "584.444,-40.6353,197.896" //单位毫米
            },
            {
                "info" : "584.444,-40.6353,197.896"
            },
            {
                "info" : "584.444,-40.6353,197.896"
            }
        ]
    }
    </pre>
* 接口返回值：
  <pre>
  {
    "mode" : 1,
    "taskid" : 10010, //标识正在进行的任务ID
    "status" : "true"
  }
  </pre>
  
#### 3.获取运行状态
* 接口说明：向服务端发送完指令并成功后，通过接口返回的taskid获取相应任务的运行状态
* 接口地址：http://192.168.1.101/getstatus
* 接口类型：POST
* 接口参数：
  <pre>
  * mode ： (int) 标识控制模式，根据mode值判定，取值范围[1,2,3]
  * taskid : 任务ID
  </pre>
* 接口示例：
  <pre>
  {
    "mode" : 1,
    "taskid" : 10010, //标识正在进行的任务ID
    "code" : 10001, //当前运行状态码
    "error" : "出错相关信息"
  }
  运行状态码声明：
  [10001] : 正在运行中
  [10002] : 运行完成
  [10003] : 轨迹出错
  </pre>
  
#### 4.停止运行
* 接口说明：向服务端发送完指令并成功后，通过接口返回的taskid停止相应任务的运行状态
* 接口地址：http://192.168.1.101/stop
* 接口类型：POST
* 接口参数：
  <pre>
  * mode ： (int) 标识控制模式，根据mode值判定，取值范围[1,2,3]
  * taskid : 任务ID
  </pre>
* 接口示例：
  <pre>
  {
    "mode" : 1,
    "taskid" : 10010, //标识正在进行的任务ID
    "code" : 10001, //当前运行状态码
    "error" : "出错相关信息"
  }
  运行状态码声明：
  [10001] : 停止完成
  </pre>