# xontrib-readable-traceback
Make traceback easier to see for xonsh.

Python work very often with large libraries like pandas, or matplotlib. This means that exceptions often produce long stack traces. Since we don't need to see the library detail in the vast majority of cases. Especially with a shell like xonsh.

This xontrib making readable and short traceback.

example:
Simple division by zero error.

<img src='https://github.com/6syun9/xontrib-readable-traceback/blob/master/img/division.png?raw=true'>

example:
This simple pandas error produces a stacktrace containing 28 lines. But xontrib load...

<img src='https://github.com/6syun9/xontrib-readable-traceback/blob/master/img/pandas.png?raw=true' width='450px'>

# Install
Install using pip

```
pip install xontrib-readable-traceback
```

Write .xonshrc
```
xontrib load readable-traceback
```

# Usage

This xontrib use [backtrace package](https://github.com/nir0s/backtrace).

For the main usage, please refer to the following.

https://github.com/nir0s/backtrace#usage

## Example xonshrc

xonshrc sample.
```
~~~
xontrib load readable-traceback
$READABLE_TRACE_STRIP_PATH_ENV=True
$READABLE_TRACE_REVERSE=True
~~~
```

## Setting backtrace

The correspondence with the variable of [backtrace](https://github.com/nir0s/backtrace) is as follows.

| backtrace | xontrib-readable-traceback | Type |
----|----|----|
| reverse | $READABLE_TRACE_REVERSE | bool |
| align | $READABLE_TRACE_ALIGN | bool |
| strip_path | $READABLE_TRACE_STRIP_PATH_ENV | bool |
| enable_on_envvar_only | $READABLE_TRACE_ENVVAR_ONLY | bool |
| on_tty | $READABLE_TRACE_ON_TTY | bool |
| conservative | $READABLE_TRACE_CONSERVATIVE | bool |
| style | $READABLE_TRACE_STYLES | dict |

For details of `style` please refer to [backtrace#style](https://github.com/nir0s/backtrace#styles) and [colorama](https://github.com/tartley/colorama).

## Switching readable-traceback

If we want to turn trace off, we can use:
```
$XONSH_READABLE_TRACEBACK=False
```

If so, the notation of traceback follows xonsh_env(`$XONSH_SHOW_TRACEBACK`).

## Xonsh traceback log

Xonsh can keep a log of traceback.<br>
To keep the log, write `"ABSOLUTE PATH TO TRACEBACK LOG"` below.
```
$XONSH_TRACEBACK_LOGFILE="PATH"
```
If it is None, no log is kept.
Default is None.

# Thanks

Thanks
 - https://github.com/xonsh/xonsh 
 - https://github.com/nir0s/backtrace
 - https://github.com/laerus/cookiecutter-xontrib

I appreciate all Python's assets and xonsh.<br>
If there is something problem, up to github issue.<br>
[@vaaaaanquish](https://twitter.com/vaaaaanquish)

