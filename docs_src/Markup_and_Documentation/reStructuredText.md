---
title: reStructuredText Cheatsheet
category: markup
tags: python
---

# [reStructuredText](http://docutils.sourceforge.net/rst.html)

[reStructuredText Quick Ref](http://docutils.sourceforge.net/docs/user/rst/quickref.html)

[reStructuredText Cheat Sheet](http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt)  (see below)

## reST Short Overview

All reST files use an indentation of 3 spaces; no tabs are allowed. 
The maximum line length is 80 characters for normal text, but tables, 
deeply indented code samples and long links may extend beyond that. 
Code example bodies should use normal Python 4-space indentation.
Paragraphs are simply chunks of text separated by one or more blank lines. 
As in Python, indentation is significant in reST, so all lines of the same
paragraph must be left-aligned to the same level of indentation.

Section headers are created by underlining (and optionally overlining)
the section title with a punctuation character, at least as long as the text:

	=================
	This is a heading
	=================
	# with overline, for parts
	* with overline, for chapters
	= for sections
	- for subsections
	^ for subsubsections
	" for paragraphs

	one asterisk: *text* for emphasis (italics),
	two asterisks: **text** for strong emphasis (boldface), and
	backquotes: ``text`` for code samples.
	escape with a backslash \

	* This is a bulleted list.
	* It has two items, the second
	  item uses two lines.

	1. This is a numbered list.
	2. It has two items too.

	. This is a numbered list.
	. It has two items too.

Nested lists are possible, but be aware that they must be separated from the 
parent list items by blank lines

## Source Code Double Colon

```
This is a normal text paragraph. The next paragraph is a code sample::

	   It is not processed in any way, except
	   that the indentation is removed.

	   It can span multiple lines.

This is a normal text paragraph again.
```

## Links

	`Link text <http://target>`_ for inline web links.


## Definitions

	term (up to a line of text)
	   Definition of the term, which must be indented and 
	   can even consist of multiple paragraphs

	next term
	   Description.

### Footnotes 
 
	Lorem ipsum [#]_ dolor sit amet ... [#]_


## Use of reStructuredText in Python docstrings

See http://infinitemonkeycorps.net/docs/pph/

```
	# Typical function documentation: 
	
	:param volume_id: The ID of the EBS volume to be attached.
	:type volume_id: str

	:param instance_id: The ID of the EC2 instance 
	:type instance_id: str
		
	:return: `Reverse geocoder return value`_ dictionary giving closest
		address(es) to `(lat, lng)`
	:rtype: dict
	:raises GoogleMapsError: If the coordinates could not be reverse geocoded.

	Keyword arguments and return value are identical to those of :meth:`geocode()`.

	.. _`Reverse geocoder return value`:
		http://code.google.com/apis/maps/documentation/geocoding/index.html#ReverseGeocoding
```
	
- Normal docstring formatting conventions apply: see PEP 257.
- Identifier references go in \`backticks\`.
- `:param lat: some text`  _documents parameters_
- `:type lat: float` _documents parameter types_
- `:return:` dictionary giving some info... _documents return values_
- `:rtype: dict` _documents return type_
- `:raises SomeError:` sometext...  _documents exceptions raised_
- `>>>` _starts a doctest and is automatically formatted as code_
- Code can also be indicated by indenting four spaces or preceding with `::` and a blank line
- Link to other methods, functions, classes, modules with :meth:`mymethod`, 
- :func:`myfunc`, :class:`myclass`, and :mod:`mymodule`.
- Hyperlink names go in backticks with a trailing underscore: `Google`_
- Targets can be defined anywhere with: `.. _Google: http://www.google.com/`


## Explicit Markup

An explicit markup block begins with a line starting with .. followed by
whitespace and is terminated by the next paragraph at the same level of 
indentation. (There needs to be a blank line between explicit markup
and normal paragraphs.

	.. sectionauthor:: Guido van Rossum <guido@python.org>

	.. rubric:: Footnotes

	.. [#] Text of the first footnote.
	.. [#] Text of the second footnote. 


	:mod:`parrot` -- Dead parrot access
	===================================

	.. module:: parrot
	   :platform: Unix, Windows
	   :synopsis: Analyze and reanimate dead parrots.
	.. moduleauthor:: Eric Cleese <eric@python.invalid>
	.. moduleauthor:: John Idle <john@python.invalid>

	.. function:: repeat([repeat=3[, number=1000000]])
				  repeat(y, z)
	   :bar: no

	   Return a line of text input from the user.
	 

	.. class:: Spam

		  Description of the class.

		  .. data:: ham

			 Description of the attribute.



## Inline markup

	:rolename:`content`  or  :role:`title <target>`  
		   
	:meth:`~Queue.Queue.get` will refer to Queue.Queue.get but only display get as the link text.

The following roles refer to objects in modules and are possibly hyperlinked 
if a matching identifier is found:

**mod**

The name of a module; a dotted name may be used. This should also be used for package names.

**func**

The name of a Python function; dotted names may be used. The role text should not include trailing parentheses to enhance readability. The parentheses are stripped when searching for identifiers.

**data**

The name of a module-level variable or constant.

**const**

The name of a “defined” constant. This may be a C-language #define or a Python variable that is not intended to be changed.

**class**

A class name; a dotted name may be used.

**meth**

The name of a method of an object. The role text should include the type name and the method name. A dotted name may be used.

**attr**

The name of a data attribute of an object.

**exc**

The name of an exception. A dotted name may be used.


# Official reStructuredText Cheatsheet	

	=====================================================
	 The reStructuredText_ Cheat Sheet: Syntax Reminders
	=====================================================
	:Info: See <http://docutils.sf.net/rst.html> for introductory docs.
	:Author: David Goodger <goodger@python.org>
	:Date: $Date: 2013-02-20 01:10:53 +0000 (Wed, 20 Feb 2013) $
	:Revision: $Revision: 7612 $
	:Description: This is a "docinfo block", or bibliographic field list

	.. NOTE:: If you are reading this as HTML, please read
	   `<cheatsheet.txt>`_ instead to see the input syntax examples!

	Section Structure
	=================
	Section titles are underlined or overlined & underlined.

	Body Elements
	=============
	Grid table:

	+--------------------------------+-----------------------------------+
	| Paragraphs are flush-left,     | Literal block, preceded by "::":: |
	| separated by blank lines.      |                                   |
	|                                |     Indented                      |
	|     Block quotes are indented. |                                   |
	+--------------------------------+ or::                              |
	| >>> print 'Doctest block'      |                                   |
	| Doctest block                  | > Quoted                          |
	+--------------------------------+-----------------------------------+
	| | Line blocks preserve line breaks & indents. [new in 0.3.6]       |
	| |     Useful for addresses, verse, and adornment-free lists; long  |
	|       lines can be wrapped with continuation lines.                |
	+--------------------------------------------------------------------+

	Simple tables:

	================  ============================================================
	List Type         Examples (syntax in the `text source <cheatsheet.txt>`_)
	================  ============================================================
	Bullet list       * items begin with "-", "+", or "*"
	Enumerated list   1. items use any variation of "1.", "A)", and "(i)"
					  #. also auto-enumerated
	Definition list   Term is flush-left : optional classifier
						  Definition is indented, no blank line between
	Field list        :field name: field body
	Option list       -o  at least 2 spaces between option & description
	================  ============================================================

	================  ============================================================
	Explicit Markup   Examples (visible in the `text source`_)
	================  ============================================================
	Footnote          .. [1] Manually numbered or [#] auto-numbered
						 (even [#labelled]) or [*] auto-symbol
	Citation          .. [CIT2002] A citation.
	Hyperlink Target  .. _reStructuredText: http://docutils.sf.net/rst.html
					  .. _indirect target: reStructuredText_
					  .. _internal target:
	Anonymous Target  __ http://docutils.sf.net/docs/ref/rst/restructuredtext.html
	Directive ("::")  .. image:: images/biohazard.png
	Substitution Def  .. |substitution| replace:: like an inline directive
	Comment           .. is anything else
	Empty Comment     (".." on a line by itself, with blank lines before & after,
					  used to separate indentation contexts)
	================  ============================================================

	Inline Markup
	=============
	*emphasis*; **strong emphasis**; `interpreted text`; `interpreted text
	with role`:emphasis:; ``inline literal text``; standalone hyperlink,
	http://docutils.sourceforge.net; named reference, reStructuredText_;
	`anonymous reference`__; footnote reference, [1]_; citation reference,
	[CIT2002]_; |substitution|; _`inline internal target`.
	
	Directive Quick Reference
	=========================
	See <http://docutils.sf.net/docs/ref/rst/directives.html> for full info.

	================  ============================================================
	Directive Name    Description (Docutils version added to, in [brackets])
	================  ============================================================
	attention         Specific admonition; also "caution", "danger",
					  "error", "hint", "important", "note", "tip", "warning"
	admonition        Generic titled admonition: ``.. admonition:: By The Way``
	image             ``.. image:: picture.png``; many options possible
	figure            Like "image", but with optional caption and legend
	topic             ``.. topic:: Title``; like a mini section
	sidebar           ``.. sidebar:: Title``; like a mini parallel document
	parsed-literal    A literal block with parsed inline markup
	rubric            ``.. rubric:: Informal Heading``
	epigraph          Block quote with class="epigraph"
	highlights        Block quote with class="highlights"
	pull-quote        Block quote with class="pull-quote"
	compound          Compound paragraphs [0.3.6]
	container         Generic block-level container element [0.3.10]
	table             Create a titled table [0.3.1]
	list-table        Create a table from a uniform two-level bullet list [0.3.8]
	csv-table         Create a table from CSV data [0.3.4]
	contents          Generate a table of contents
	sectnum           Automatically number sections, subsections, etc.
	header, footer    Create document decorations [0.3.8]
	target-notes      Create an explicit footnote for each external target
	math              Mathematical notation (input in LaTeX format)
	meta              HTML-specific metadata
	include           Read an external reST file as if it were inline
	raw               Non-reST data passed untouched to the Writer
	replace           Replacement text for substitution definitions
	unicode           Unicode character code conversion for substitution defs
	date              Generates today's date; for substitution defs
	class             Set a "class" attribute on the next element
	role              Create a custom interpreted text role [0.3.2]
	default-role      Set the default interpreted text role [0.3.10]
	title             Set the metadata document title [0.3.10]
	================  ============================================================

	Interpreted Text Role Quick Reference
	=====================================
	See <http://docutils.sf.net/docs/ref/rst/roles.html> for full info.

	================  ============================================================
	Role Name         Description
	================  ============================================================
	emphasis          Equivalent to *emphasis*
	literal           Equivalent to ``literal`` but processes backslash escapes
	math              Mathematical notation (input in LaTeX format)
	PEP               Reference to a numbered Python Enhancement Proposal
	RFC               Reference to a numbered Internet Request For Comments
	raw               For non-reST data; cannot be used directly (see docs) [0.3.6]
	strong            Equivalent to **strong**
	sub               Subscript
	sup               Superscript
	title             Title reference (book, etc.); standard default role
	================  ============================================================
	

	
