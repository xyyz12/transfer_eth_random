# transfer_eth_random
一个比较麻烦的就是免验证功能，ok一次可以手动添加20个白名单，之后就可以放心提取，现在
ok的web3功能也很强大，多对多转账等等

批量创建钱包、从okx上批量转发金额到eth主网上

utils是钱包一些功能

01是批量创建钱包

02是从okx转移固定金额eth

03是从okx转移随机金额eth

04是从okx转移随机金额eth,随机间隔几秒，再发送

05检查单个地址eth余额+infrul

06检查批量地址eth余额+infrul

上传.env文件被隐藏，所以自己将env.txt  -->  .env

参考https://github.com/mixbe/zksync2_script，内有从eth主网跨zk

![1705220769031](https://github.com/xyyz12/transfer_eth_random/assets/91812763/28ee60d8-7590-463e-be03-d2d1aac478bc)


2、遇到的问题
![image](https://github.com/xyyz12/transfer_eth_random/assets/91812763/7b5d3599-0b8b-4941-bc30-6d06697d3d19)
解决方案：在 python 文件中添加了设置网络代理的代码
当你打开代理时，输入下面两行代码
![image](https://github.com/xyyz12/transfer_eth_random/assets/91812763/74d75d7b-7cd7-4492-8a8b-69204dac2e19)

返回内容
![image](https://github.com/xyyz12/transfer_eth_random/assets/91812763/da79f10a-a17a-4299-b5c7-2e0e2138731e)











