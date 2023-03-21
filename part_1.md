### Data Source: Wikipedia

Wikipedia is another valuable source of data that can be easily accessed and parsed using the [mediawiki library](https://github.com/barrust/mediawiki) which is a python wrapper and parser for the **MediaWiki API**. To install the library, you can use the following command in the Command Prompt or Terminal:

```shell
> python -m pip install pymediawiki
> python3 -m pip install pymediawiki # on MacOS Terminal
```

Once you have installed the library, you can use it to search Wikipedia, get article summaries, and extract data like links and images from a page. To fetch a particular article and print out its sections, you can use the following Python code:

```python
from mediawiki import MediaWiki

wikipedia = MediaWiki()
babson = wikipedia.page("Babson College")
print(babson.title)
print(babson.content)

```

This code will fetch the article with the given title and print its title and content. The output will look like this:

```txt
Babson College 


Babson College is a private business school in Wellesley, Massachusetts. Established in 1919, its central focus is on entrepreneurship education. It was founded by Roger W. Babson as an all-male business institute but is now coeducational.
...
```

You can also access other properties of a page, such as its categories, sections, and links. See the mediawiki package [documentation](https://pymediawiki.readthedocs.io/en/latest/quickstart.html#other-properties) for more information on available properties and methods.