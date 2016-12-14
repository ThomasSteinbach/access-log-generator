# thomass/access-log-generator

This python script is creating a fake access log file with accesses in the past.
This is useful, if you need an example access log for scientific research.

## usage

Run

    ./alg.py

Thiss will output a new access_log.log file in the workspace.

## configuration

You can run the script with preceeding environment variables like:

    MIN_MOD_LINEAR='+3600' MAX_MOD_LINEAR='+3600' ./alg.py

Following variables are available

| variable | default | description |
|----------|---------|-------------|
| FIRST_ACCESS | 1462060800 (Sun, 01 May 2016 00:00:00 GMT) | The seconds since epoch of the first access. |
| LAST_ACCESS | 1477958399 (Mon, 31 Oct 2016 23:59:59 GMT) | The seconds since of the last access. |
| MIN_SHIFT | 10 | The initial minimum distance between two acesses. |
| MAX_SHIFT | 86400 (1 day) | The initial maximum distance between two accesses. |
| MIN_MOD_LINEAR | '+0' | The seconds added (+) or removed (-) to/from MIN_SHIFT after every access. |
| MAX_MOD_LINEAR | '+0' | The seconds added (+) or removed (-) to/from MAX_SHIFT after every access. |
| MIN_MOD_FACTOR | 1 | The factor MIN_SHIFT is modified after every access. |
| MAX_MOD_FACTOR | 1 | The factor Max_SHIFT is modified after every access. |

## Licence

MIT License

Copyright (c) 2016 Thomas Steinbach

This script is based on https://gist.github.com/gwenshap/11390102

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
