from django.db import models


"""
    @id : 3
    @name : Host
    @author : 刘旭阳
    @date : 2018.3.14
    @attribute : id(主机id),name(主机名),ip(主机ip地址),port(主机端口号),business(主机隶属部门)
"""
class Host(models.Model):
    host_id = models.AutoField(primary_key=True)
    host_name = models.CharField(max_length=64,db_index=True,verbose_name="主机名")
    host_ip = models.GenericIPAddressField(protocol="both",db_index=True,verbose_name="主机ip")
    host_port = models.IntegerField(verbose_name="主机端口")
    class Meta:
        verbose_name = '主机'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.host_name