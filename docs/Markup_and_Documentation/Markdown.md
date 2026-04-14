---
title: Markdown Essentials
category: markup
tags: github
---

# Markdown Essentials

Markdown is a lightweight markup language for creating formatted text using a plain-text editor. It is widely used in blogging, instant messaging, online forums, and collaborative software.

[Markdown main site](https://daringfireball.net/projects/markdown/)

[GitHub Flavored Markdown Guide](https://guides.github.com/features/mastering-markdown/)

## Basics

A paragraph is one or more consecutive lines of text separated by one or more blank lines. A blank line contains nothing but spaces or tabs.

Do not indent normal paragraphs with spaces or tabs. Indent at least 4 spaces or a tab for code blocks.

```txt
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

## Emphasis

```txt
 *single asterisks*
 _single underscores_
 **double asterisks**
 __double underscores__
```

Emphasis can be used in the `mi\*dd\*le of a word`.

## Headers

```txt
 # H1
 ## H2
 ### H3
 #### H4
 ##### H5
 ###### H6

 Alt-H1
 ======

 Alt-H2
 ------
```

## Links and Images

```txt
 [Text for the link](URL)

 This is [an example][id] reference-style link.
 [id]: https://example.com/  "Optional Title Here"

 ![Alt text](/path/to/img.jpg "Optional title")
```

## Code

 `span of code`

~~~txt
```python

 def wiki_rocks(text):
  formatter = lambda t: "funky"+t
  return formatter(text)
```
~~~

will be displayed as

```python
def wiki_rocks(text):
 formatter = lambda t: "funky"+t
 return formatter(text)
```

## Blockquotes

```txt
 > This is a blockquote with two paragraphs.
 >
 > Second paragraph.
```

## GitHub Pages

[GitHub Pages documentation](https://help.github.com/categories/github-pages-basics/)

GitHub Pages site will use the layout and styles from the Jekyll theme you have selected in your repository settings. The name of this theme is saved in the Jekyll `_config.yml` configuration file.

## Bitbucket

Bitbucket doesn't support arbitrary HTML in Markdown, it instead uses safe mode.
Safe mode requires that you replace, remove, or escape HTML tags appropriately.

Code highlighting to bitbucket README.md written in Python Markdown

 :::python
        friends = ['john', 'pat', 'gary', 'michael']
        for i, name in enumerate(friends):
            print "iteration {iteration} is {name}".format(iteration=i, name=name)

[Python markdown main site](https://pythonhosted.org//Markdown/)

#### [Cloning your Bitbucket Wiki](https://confluence.atlassian.com/display/BITBUCKET/View+and+edit+pages)

```bash
git clone https://bitbucket.org/MY_USER/MY_REPO/wiki
```

## Modern CommonMark

Current standards heavily follow [CommonMark](https://commonmark.org/).

### Syntax Examples

**Bold** and *Italic*

### Lists
- Item 1
- Item 2
  - Nested Item

### Links and Images
[CommonMark](https://commonmark.org/)
![Alt Text](https://via.placeholder.com/150)

### Code Blocks
```python
def hello():
    print("Hello CommonMark")
```

### Tables
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
