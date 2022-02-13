# 依赖包安装 python3环境

```bash
yum -y install gcc-c++
yum -y install krb5-devel
yum -y install python3
yum -y install python3-devel
yum -y install cyrus-sasl cyrus-sasl-plain cyrus-sasl-devel cyrus-sasl-gssapi cyrus-sasl-lib

pip3 install -U pip
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

pip3 install sasl
pip3 install impyla==0.17.0
pip3 install krbcontext==0.9
pip3 install thrift==0.11.0
pip3 install thrift-sasl==0.4.3
pip3 install pykerberos==1.2.1
pip3 install pyhive
pip3 install happybase
```
