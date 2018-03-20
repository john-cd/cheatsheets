
[Scaladoc](https://docs.scala-lang.org/overviews/scaladoc/for-library-authors.html)
[Scaladoc Style Guide](https://docs.scala-lang.org/style/scaladoc.html)


	/** Start the comment here
	  * and use the left star followed by a
	  * white space on every line.
	  *
	  * Even on empty paragraph-break lines.
	  *
	  * Note that the * on each line is aligned
	  * with the second * in /** so that the
	  * left margin is on the same column on the
	  * first line and on subsequent ones.
	  *
	  * The closing Scaladoc tag goes on its own,
	  * separate line. E.g.
	  *
	  * Calculate the square of the given number
	  *
	  * @param d the Double to square
	  * @return the result of squaring d
	  */
	 def square(d: Double): Double = d * d

## Tags

### Class specific tags

``@constructor`` placed in the class comment will describe the primary constructor.
Method specific tags

``@return`` detail the return value from a method (one per method).
Method, Constructor and/or Class tags

``@throws`` what exceptions (if any) the method or constructor may throw.

``@param`` detail a value parameter for a method or constructor, provide one per parameter to the method/constructor.

``@tparam`` detail a type parameter for a method, constructor or class. Provide one per type parameter.

### Usage tags

``@see`` reference other sources of information like external document links or related entities in the documentation.

``@note`` add a note for pre or post conditions, or any other notable restrictions or expectations.

``@example`` for providing example code or related example documentation.

``@usecase`` provide a simplified method definition for when the full method definition is too complex or noisy. An example is (in the collections API), providing documentation for methods that omit the implicit canBuildFrom.

### Member grouping tags

``@group <group>`` - mark the entity as a member of the <group> group.

``@groupname <group> <name>`` - provide an optional name for the group. <name> is displayed as the group header
before the group description.

``@groupdesc <group> <description>`` - add optional descriptive text to display under the group name. Supports multiline formatted text.

``@groupprio`` - control the order of the group on the page. Defaults to 0. Ungrouped elements have an implicit priority of 1000. Use a value between 0 and 999 to set a relative position to other groups. Low values will appear before high values.

### Diagram tags

``@contentDiagram`` - use with traits and classes to include a content hierarchy diagram showing included types. The diagram content can be fine tuned with additional specifiers taken from hideNodes, hideOutgoingImplicits, hideSubclasses, hideEdges, hideIncomingImplicits, hideSuperclasses and hideInheritedNode. hideDiagram can be supplied to prevent a diagram from being created if it would be created by default. Packages and objects have content diagrams by default.

``@inheritanceDiagram``

### Other tags

``@author`` provide author information for the following entity

``@version`` the version of the system or API that this entity is a part of.

``@since`` like ``@version`` but defines the system or API that this entity was first defined in.

``@todo`` for documenting unimplemented features or unimplemented aspects of an entity.

``@deprecated`` marks the entity as deprecated, providing both the replacement implementation that should be used and the version/date at which this entity was deprecated.

``@migration`` like deprecated but provides advanced warning of planned changes ahead of deprecation. Same fields as ``@deprecated``.

``@inheritdoc`` take comments from a superclass as defaults if comments are not provided locally.

``@documentable`` Expand a type alias and abstract type into a full template page. - TODO: Test the “abstract type” claim - no examples of this in the Scala code base

### Macros

``@define <name> <definition>`` allows use of $name in other Scaladoc comments within the same source file which will be expanded to the contents of <definition>.

 
## Markup

	`monospace`
	''italic text''
	'''bold text'''
	__underline__
	^superscript^
	,,subscript,,
	[[entity link]], e.g. [[scala.collection.Seq]]
	[[http://external.link External Link]],
	  e.g. [[http://scala-lang.org Scala Language Site]]
	  
## Other formatting notes

Paragraphs are started with one (or more) blank lines. 

``*`` in the margin for the comment is valid (and should be included) but the line should be blank otherwise.

Code blocks are contained within {{{ this }}} and may be multi-line. 

Indentation is relative to the starting * for the comment.

Headings are defined with surrounding = characters, with more = denoting subheadings. E.g. =Heading=, ==Sub-Heading==, etc.

List blocks are a sequence of list items with the same style and level, with no interruptions from other block styles. Unordered lists can be bulleted using -, while numbered lists can be denoted using 1., i., I., a. for the various numbering styles.