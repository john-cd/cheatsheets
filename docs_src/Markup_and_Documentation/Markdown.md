---
title: Markdown Essentials
category: markup
tags: github
---

# Markdown Essentials

[Markdown main site](http://daringfireball.net/projects/markdown/)

[GitHub Flavored Markdown Guide](https://guides.github.com/features/mastering-markdown/)


## Basics

A paragraph is one or more consecutive lines of text separated by one or more blank lines. A blank line contains nothing but spaces or tabs. 

Do not indent normal paragraphs with spaces or tabs. Indent at least 4 spaces or a tab for code blocks.

```markdown
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

	*single asterisks*
	_single underscores_
	**double asterisks**
	__double underscores__

	Emphasis can be used in the mi\*dd\*le of a word.



## Headers

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

## Links and Images 

	[ Text for the link ](URL)

	This is [an example][id] reference-style link.
	[id]: http://example.com/  "Optional Title Here"
	
	![Alt text](/path/to/img.jpg "Optional title")

## Code

	`span of code`


	```python

	def wiki_rocks(text):
		formatter = lambda t: "funky"+t
		return formatter(text)
	```

will be displayed as

```python
def wiki_rocks(text):
	formatter = lambda t: "funky"+t
	return formatter(text)
```

## Blockquotes

	> This is a blockquote with two paragraphs. 
	> 
	> Second paragraph.


## GitHub Pages

[GitHub Pages documentation](https://help.github.com/categories/github-pages-basics/) 

GitHub Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/john-cd/john-cd.github.io/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.



## Bitbucket 

Bitbucket doesn't support arbitrary HTML in Markdown, it instead uses safe mode. 
[Safe mode](http://pythonhosted.org/Markdown/reference.html#safe_mode) requires that you replace, remove, or escape HTML tags appropriately.
 	
Code highlighting to bitbucket README.md written in Python Markdown 

	:::python
        friends = ['john', 'pat', 'gary', 'michael']
        for i, name in enumerate(friends):
            print "iteration {iteration} is {name}".format(iteration=i, name=name)

[Python markdown main site](http://pythonhosted.org//Markdown/)	


#### [Cloning your Bitbucket Wiki](https://confluence.atlassian.com/display/BITBUCKET/View+and+edit+pages)

	$ git clone http://bitbucket.org/MY_USER/MY_REPO/wiki