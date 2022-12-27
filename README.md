# Automatic Netgear Orbi accesspoint rebooter

Also have a faulty Netgear Orbi RBR350 accesspoint that looses connectivity every 12 hours and Netgear support ignores its paying customers?
This might be the solution for you.

This script check if the router is still reachable and when it inevitably becomes unresponsive after exactly 12 hours it will run a power cycle using a remote power switch.

## Prerequisites

- Remote power switch IP power 9258 https://www.aviosys.com/products/9258.php
- Linux device running Python 3 on the same network as the router.

## How to to run

- Change the variables in the top of the file to match your environment
- Add this to your crontab: @reboot sudo python /<PATH_TO_FILE>/devicewachter.py &
