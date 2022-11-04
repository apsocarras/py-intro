# _py-intro_

#### By _**Alejandro Socarras**_

#### _Week 1 Code Review_

## Description

_`list_sayer()`_

A function called list_sayer() that takes a list as an argument
* If the list isn't empty (i.e. there's one or more items in it):
      print a string for each item saying the name of the item and its index
      return the Boolean True
*  If the list is empty:
      print a string saying that the list is empty
      return the Boolean False

_`dict_sayer()`_

A function called dict_sayer() that takes a dictionary as an argument
* If the dictionary isn't empty (i.e. there's one or more items in it):
    print a string for each item saying the name of each key and its value
    return the Boolean True
* If the dictionary is empty:
    print a string saying that the dictionary is empty
    return the Boolean False

_`greatest()`_

A function called greatest() that takes as an argument a dictionary that has strings as keys and integers as values
* Find the greatest value
* Return a tuple with the greatest value and its key

_`zipper()`_

A function called zipper() that takes two lists as arguments
* If the lists are the same length:
    return a dictionary that has the items of the first list as keys, and each item in the same index in the second list as the value > For instance, the lists ["vanilla", "cherry"] and ["cake", "ice_cream"] would return {"vanilla": "cake", "cherry": "ice_cream"}
* If the lists are different lengths:
    return a tuple with each list and its length > For instance, the lists ["vanilla", "cherry", "pistachio"] and ["cake", "ice_cream"] would return (["vanilla", "cherry", "pistachio"], 3, ["cake", "ice_cream"], 4)

## Setup/Installation Requirements

_To run the project from your local system:_

1. Make a directory on your disk where you would like to clone the repo.

2. Copy the repo link: https://github.com/apsocarras/language-suggest.git (available if you click the green "Code" dropdown button on this page).

3. Open your terminal and change into the directory you made (`cd /path/to/new/directory`).

4. Type `git clone ` and paste the URL.

5. Copy and paste the path to `index.html` into your browser's URL bar to open the page.

## Known Bugs

_No known bugs._

## License

_[MIT License](https://opensource.org/licenses/MIT)_

Copyright (c) _11.4.22_ Alejandro Socarras

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
