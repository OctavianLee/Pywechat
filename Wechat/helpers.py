# -*- coding: utf-8 -*-
import pylibmc
from config import server_ips

mc = pylibmc.Client(
    server_ips,
    binary=True,
    behaviors={"tcp_nodelay": True, "ketama": True})
