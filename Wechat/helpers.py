# -*- coding: utf-8 -*-
import pylibmc

mc = pylibmc.Client(
    ["127.0.0.1"],
    binary=True,
    behaviors={"tcp_nodelay": True, "ketama": True})
