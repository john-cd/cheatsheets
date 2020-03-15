# jQuery

## Links

- [jQuery API documentation]( http://api.jquery.com/ )
- [Learn jQuery]( http://learn.jquery.com/ )

The jQuery library exposes its methods and properties via two properties of the window object called jQuery and $. $ is simply an alias for jQuery and it's often employed because it's shorter and faster to write.

## Embed JQuery

Either directly

```html
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Demo</title>
</head>
<body>
<a href="http://jquery.com/">jQuery</a>
<script src="jquery.js"></script>
<script>
// Your code goes here.
</script>
</body>
```

or via a CDN

```html
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
</head>
```

## Launching Code on Document Ready

```js
$( document ).ready(function() {
// Your code here.
});

// Shorthand for $( document ).ready()
$(function() {
console.log( "ready!" );
});
```

## Selecting elements

```js
$( "#myId" ); // Note IDs must be unique per page.
$( ".myClass" );
$( "input[name='first_name']" );
$( "#contents ul.people li" );
$( "div.myClass, ul.people" );
```

If you have a variable containing a DOM element, and want to select elements related to that DOM element, simply wrap it in a jQuery object.

```js
var myDomElement = document.getElementById( "foo" ); // A plain DOM element.
$( myDomElement ).find( "a" ); // Finds all anchors inside the DOM element.
```

## Pull a native DOM element from a jQuery object

A jQuery object is an array-like wrapper around one or more DOM elements.

```js
$( "#foo" )[ 0 ]; // Equivalent to document.getElementById( "foo" )
$( "#foo" ).get( 0 );
```

// Testing whether a selection contains elements.

```js
if ( $( "div.foo" ).length ) {
...
}
```

## Refining selections.

```js
$( "div.foo" ).has( "p" ); // div.foo elements that contain <p> tags
$( "h1" ).not( ".bar" ); // h1 elements that don't have a class of bar
$( "ul li" ).filter( ".current" ); // unordered list items with class of current
$( "ul li" ).first(); // just the first unordered list item
$( "ul li" ).eq( 5 ); // the sixth

$( "form :checked" ); //  :checked targets checked checkboxes
```

## DOM Traversal and Manipulation

Get the ``<button>`` element with the class 'continue' and change its HTML to 'Next Step...'

```js
$( "button.continue" ).html( "Next Step..." )
$( "h1" ).html(); // returns the html
```

## Chaining

```js
$( "#content" ).find( "h3" ).eq( 2 ).html( "new text for the third h3!" ); 
$( "#content" )
.find( "h3" )
.eq( 2 )
.html( "new text for the third h3!" )
.end() // Restores the selection to all h3s in #content
.eq( 0 )
.html( "new text for the first h3!" );
```

## Manipulation

* .html() – Get or set the HTML contents.
* .text() – Get or set the text contents; HTML will be stripped.
* .attr() – Get or set the value of the provided attribute.
* .width() – Get or set the width in pixels of the first element in the selection as an integer.
* .height() – Get or set the height in pixels of the first element in the selection as an integer.
* .position() – Get an object with position information for the first element in the selection, relative to its first positioned ancestor. This is a getter only.
* .val() – Get or set the value of form elements.


Many jQuery methods implicitly iterate over the entire collection, applying their behavior to each matched element. In most cases, the "getter" signature returns the result from the first element in a jQuery collection while the setter acts over the entire collection of matched elements.

```js
$( "li" ).addClass( "newClass" ); // Each <li> in the document will have the class "newClass" added.
```

## Add / remove class

```js
$( "a" ).addClass( "test" );
$( "a" ).removeClass( "test" );

$( "div" ).click(function() {
if ( $( this ).hasClass( "protected" ) ) {
$( this )
.animate({ left: -10 })
.animate({ left: 10 })
.animate({ left: -10 })
.animate({ left: 10 })
.animate({ left: 0 });
}
});

if ( $( "#myDiv" ).is( ".pretty.awesome" ) ) {
$( "#myDiv" ).show();
}
var isVisible = $( "#myDiv" ).is( ":visible" );
if ( $( "#myDiv" ).is( ":hidden" ) ) {
$( "#myDiv" ).show();
}
```

## Set / get element attributes

```js
$( "a" ).attr( "href", "allMyHrefsAreTheSameNow.html" );
$( "a" ).attr({
title: "all titles are the same too!",
href: "somethingNew.html"
});
```

## CSS

Getting CSS properties.

```js
$( "h1" ).css( "fontSize" ); // Returns a string such as "19px".$( "h1" ).css( "font-size" ); // Also works.
```

Setting CSS properties.

```js
$( "h1" ).css( "fontSize", "100px" ); // Setting an individual property.// Setting multiple properties.$( "h1" ).css({fontSize: "100px",color: "red"});
```

## Data

Storing and retrieving data related to an element.

```js
$( "#myDiv" ).data( "keyName", { foo: "bar" } );
$( "#myDiv" ).data( "keyName" ); // Returns { foo: "bar" }
```

Storing a relationship between elements using .data()

```js
$( "#myList li" ).each(function() {
var li = $( this );
var div = li.find( "div.content" );
li.data( "contentDiv", div );
});
```

Later, we don't have to find the div again; we can just read it from the list item's data

```js
var firstLi = $( "#myList li:first" );
firstLi.data( "contentDiv" ).html( "new content" );
```

## Utility functions

.trim, .each, .map, inArray, isArray, isFunction, isNumeric, .type

Returns "lots of extra whitespace"

```js
$.trim( " lots of extra whitespace " );
```

### Iterate over an JS array or object

```js
$.each([ "foo", "bar", "baz" ], function( idx, val ) {
console.log( "element " + idx + " is " + val );
});
$.each({ foo: "bar", baz: "bim" }, function( k, v ) {
console.log( k + " : " + v );
});
```

HOWEVER, use this form for jQuery objects

```js
$( "li" ).each( function( index, element ){
console.log( $( this ).text() );
});

var myArray = [ 1, 2, 3, 5 ];
if ( $.inArray( 4, myArray ) !== -1 ) {
console.log( "found it!" );
}
```

```js
$.isArray([]); // true
$.isFunction(function() {}); // true
$.isNumeric(3.14); // true

$.type( true ); // "boolean"
$.type( 3 ); // "number"
$.type( "test" ); // "string"
$.type( function() {} ); // "function"
$.type( new Boolean() ); // "boolean"
$.type( new Number(3) ); // "number"
$.type( new String('test') ); // "string"
$.type( new Function() ); // "function"
$.type( [] ); // "array"
$.type( null ); // "null"
$.type( /test/ ); // "regexp"
$.type( new Date() ); // "date"
```

## $.map and .map

```js
<li id="a"></li>
<li id="b"></li>
<li id="c"></li>
<script>
var arr = [{
id: "a",
tagName: "li"
}, {
id: "b",
tagName: "li"
}, {
id: "c",
tagName: "li"
}];

// Returns [ "a", "b", "c" ]
$( "li" ).map( function( index, element ) {
return element.id;
}).get();

// Also returns [ "a", "b", "c" ]
// Note that the value comes first with $.map
$.map( arr, function( value, index ) {
return value.id;
});
```

## Event Handling

```js
var hiddenBox = $( "#banner-message" );
$( "#button-container button" ).on( "click", function( event ) {
hiddenBox.show();
});
```

The `on` method is useful for binding the same handler function to multiple events, when you want to provide data to the event handler, when you are working with custom events, or when you want to pass an object of multiple events and handlers.

### Event setup using a convenience method like  .click(), .focus(), .blur(), .change()

```js
$( "p" ).click(function() {
console.log( "You clicked a paragraph!" );
});
```

### The hover helper function

```js
$( "#menu li" ).hover(function() {
$( this ).toggleClass( "hover" );
});
```

The event object is most commonly used to prevent the default action of the event via the `.preventDefault()` method. However, the event object contains a number of other useful properties and methods, including:

    pageX, pageY, type, which, data

Use this code to inspect it in your browser console 

```js
$( "div" ).on( "click", function( event ) {
console.log( "event object:" );
console.dir( event );
});
```

### Preventing a link from being followed

```js
$( "a" ).click(function( eventObject ) {
var elem = $( this );
if ( elem.attr( "href" ).match( /evil/ ) ) {
eventObject.preventDefault();
elem.addClass( "evil" );
}
});
```

## Event setup using the `.on()` method with data

```js
$( "input" ).on(
"change",
{ foo: "bar" }, // Associate data with event binding
function( eventObject ) {
console.log("An input value has changed! ", eventObject.data.foo);
}
);
```

// Binding multiple events with different handlers

```js
$( "p" ).on({
"click": function() { console.log( "clicked!" ); },
"mouseover": function() { console.log( "hovered!" ); }
});
```

// Tearing down all click handlers on a selection

```js
$( "p" ).off( "click" );
```

// As of jQuery 1.7, attach an event handler to the `body` element that
// is listening for clicks, and will respond whenever *any* button is
// clicked on the page.

```js
$( "body" ).on({
click: function( event ) {
alert( "Hello." );
}
}, "button" );
```

// An alternative to the previous example, using slightly different syntax.

```js
$( "body" ).on( "click", "button", function( event ) {
alert( "Hello." );
});
```

// Attach a delegated event handler with a more refined selector

```js
$( "#list" ).on( "click", "a[href^='http']", function( event ) {
$( this ).attr( "target", "_blank" );
});
```

## Effects

Instantaneously hide all paragraphs

```js
$( "p" ).hide();

// slowly
$( "p" ).hide( "slow" ); 
```

Instantaneously show all divs that have the hidden style class

```js
$( "div.hidden" ).show();
```

Instantaneously toggle the display of all paragraphs

```js
$( "p" ).toggle();
```

Fade in all hidden paragraphs; then add a style class to them (correct with animation callback)

```js
$( "p.hidden" ).fadeIn( 750, function() {
// this = DOM element which has just finished being animated
$( this ).addClass( "lookAtMe" );
});
```


## Ajax

```js
$.ajax({
url: "/api/getWeather",
data: {
zipcode: 97201
},
success: function( result ) {
$( "#weather-temp" ).html( "<strong>" + result + "</strong> degrees" );
}
});
```

Using the core $.ajax() method

```js
$.ajax({
// The URL for the request
url: "post.php",
// The data to send (will be converted to a query string)
data: {
id: 123
},
// Whether this is a POST or GET request
type: "GET",
// The type of data we expect back
dataType : "json",
})
// Code to run if the request succeeds (is done);
// The response is passed to the function
.done(function( json ) {
$( "<h1>" ).text( json.title ).appendTo( "body" );
$( "<div class=\"content\">").html( json.html ).appendTo( "body" );
})
// Code to run if the request fails; the raw request and
// status codes are passed to the function
.fail(function( xhr, status, errorThrown ) {
alert( "Sorry, there was a problem!" );
console.log( "Error: " + errorThrown );
console.log( "Status: " + status );
console.dir( xhr );
})
```

Code to run regardless of success or failure;

```js
.always(function( xhr, status ) {
alert( "The request is complete!" );
});
```

Simple convenience methods such as $.get(), $.getScript(), $.getJSON(), $.post(), and $().load().

```js
$.get( "myhtmlpage.html", myCallBack );  // myCallback needs to be a parameterless function
# with parameters
$.get( "myhtmlpage.html", function() {
myCallBack( param1, param2 );
});
```
## Load

```js
$(selector).load(URL,data,callback);
```

Using .load() to populate an element

```js
$( "#newContent" ).load( "/foo.html" );
```

Using .load() to populate an element based on a selector

```js
$( "#newContent" ).load( "/foo.html #myDiv h1:first", function( html ) {
alert( "Content updated!" );
});
```

## Forms

Turning form data into a query string

```js
$( "#myForm" ).serialize();
```

// Creates a query string like this:
// field_1=something&field2=somethingElse


Create an array of objects containing form data

```js
$( "#myForm" ).serializeArray();
```

Use validation to check for the presence of an input

```js
$( "#form" ).submit(function( event ) {
// If .required's value's length is zero
if ( $( ".required" ).val().length === 0 ) {
// Usually show some kind of error message here
// Prevent the form from submitting
event.preventDefault();
} else {
// Run $.ajax() here
}
});
```

Validate a phone number field

```js
$( "#form" ).submit(function( event ) {
var inputtedPhoneNumber = $( "#phone" ).val();
// Match only numbers
var phoneNumberRegex = /^\d*$/;
// If the phone number doesn't match the regex
if ( !phoneNumberRegex.test( inputtedPhoneNumber ) ) {
// Usually show some kind of error message here
// Prevent the form from submitting
event.preventDefault();
} else {
// Run $.ajax() here
}
});
```

## Feature testing

Helper libraries (like Modernizr) that provide a simple, high-level API for determining if a browser has a specific feature available or not.

```js
if ( Modernizr.canvas ) {
showGraphWithCanvas();
} else {
showTable();
}
```