# Widgets
from libqtile.widget import Net, NetGraph, Battery, BatteryIcon, CPUGraph, ClipBoard, Clock, CurrentLayout, CurrentScreen, LaunchBar, Memory, MemoryGrap, Volume, Wallpaper, Wlan

from libqtile.config import Screen
from libqtile import bar, widget

# screens
screens = [
    Screen(
        bottom=bar.Bar([
            widget.GroupBox(),
            widget.WindowName()
            ], 30),
        ),
    Screen(
        bottom=bar.Bar([
            widget.GroupBox(),
            widget.WindowName()
            ], 30),
        )
    ]
    

# lazy objects: http://docs.qtile.org/en/latest/manual/config/lazy.html
from libqtile.config import Key
from libqtile.command import lazy

keys = [
    Key(
        ["mod1"], "k",
        lazy.layout.down()
    ),
    Key(
        ["mod1"], "j",
        lazy.layout.up()
    )
]


# groups
from libqtile.config import Group, Match
groups = [
    Group("a"),
    Group("b"),
    Group("c", matches=[Match(wm_class=["Firefox"])]),
]

# allow mod3+1 through mod3+0 to bind to groups; if you bind your groups
# by hand in your config, you don't need to do this.
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod3")


# Layouts: http://docs.qtile.org/en/latest/manual/ref/layouts.html
from libqtile import layout
layouts = [
    layout.Max(),
    layout.Stack(stacks=2)
]

# Client-Server Scripting Model
from libqtile.command import Client
c = Client()
print c.screen.info()["index"]



