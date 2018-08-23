# Author:Sunny Liu
from django.contrib import admin
import xadmin
# Register your models here.
from uradmin.models import Host


@xadmin.sites.register(Host)
class HostAdmin(object):
    list_display=('host_id', 'host_name', 'host_ip', 'host_port')
    list_display_links = ("host_name",)
    list_per_page = 50


