# hivediff
Diff viewer for hive posts was inspired by [pydiff](https://github.com/yebrahim/pydiff).
hivediff can be used to view the edit history of posts and to do a diff of locally stored markdown posts with the
published version on the hive blockchain


## Requirements
hivediff needs python 3 and the following packages:

* tkinter
* beem
* diff_match_patch

On Ubuntu, you need to install tkinter:
```
sudo apt-get install python3-tk
```
On windows, using anaconda is the easiest way. More information about installing Tk can be found in the [docs](https://tkdocs.com/tutorial/install.html).

You need also beem which installs also diff_match_patch:

```
pip install beem
```
or
```
conda install beem
```
when using anaconda.

## Install

`git clone https://github.com/holgern/hivediff.git`


## Usage

`python hivediff.py`