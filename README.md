## Prerequisites

- Remote power switch IP power 9258 https://www.aviosys.com/products/9258.php
- Linux device running Python 3 on the same network as the router.

## How to to run

- Change the variables in the top of the file to match your environment
- Add this to your crontab: @reboot sudo python /<PATH_TO_FILE>/devicewachter.py &
