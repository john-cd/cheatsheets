---
layout: inner
title: Jekyll How-To
date: 2017-02-20 11:41:26 -0800
category: frontend
tags: blog jekyll
---

# Jekyll Basics

Jekyll is a simple, blog-aware, static site generator. It takes your text written in your favorite markup language and uses layouts to create a static website. You can tweak the site's look and feel, URLs, the data displayed on the page, and more.

[Jekyll Home Page](https://jekyllrb.com)

Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll’s GitHub repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll Talk][jekyll-talk].

[Jekyll source code](https://github.com/jekyll/jekyll)

## Jekyll Install How-To

[Install Instructions](https://jekyllrb.com/docs/installation/)

- Install Ruby via [RubyInstaller](https://rubyinstaller.org/)

- Update RubyGems

```bash
gem update --system
```

- Install Jekyll

```bash
gem install jekyll
```

- Test Jekyll

```bash
jekyll --version
gem list jekyll
```

- Install bundler

```bash
gem install bundler
```

[Bundler](https://rubygems.org/gems/bundler) is a gem that manages other Ruby gems. It makes sure your gems and gem versions are compatible, and that you have all necessary dependencies each gem requires.

- Create a new site

```bash
# Create a new Jekyll site at ./myblog
~ $ jekyll new myblog

# Change into your new directory
~ $ cd myblog
```

Jekyll installs a site that uses a gem-based theme called Minima.

With gem-based themes, some of the site’s directories (such as the assets, \_layouts,\_includes, and \_sass directories) are stored in the theme’s gem, hidden from your immediate view. Yet all of the necessary directories will be read and processed during Jekyll’s build process.

- Build site locally

```bash
# Build the site on the preview server
~/myblog $ bundle exec jekyll serve
```

Now browse to [localhost:4000](https://localhost:4000)

[Jekyll Quickstart](https://jekyllrb.com/docs/quickstart/)

When you run bundle exec jekyll serve, Bundler uses the gems and versions as specified in Gemfile.lock to ensure your Jekyll site builds with no compatibility or dependency conflicts.

The Gemfile and Gemfile.lock files inform Bundler about the gem requirements in your site. If your site doesn’t have these Gemfiles, you can omit bundle exec and just run jekyll serve.

```bash
$ jekyll build
# => The current folder will be generated into ./_site

$ jekyll serve
# => A development server will run at https://localhost:4000/
# Auto-regeneration: enabled. Use `--no-watch` to disable.
```

## Plugins

```bash
$ gem install jekyll-sitemap
$ gem install jekyll-feed
etc...
```

Add to `_config.yml`

````yaml
gems:
  - jekyll-paginate
  - jekyll-feed
  - jekyll-sitemap
``


# Custom Search

[Adding a custom Google search](https://digitaldrummerj.me/blogging-on-github-part-7-adding-a-custom-google-search/)


# Themes

[Theme documentation](https://jekyllrb.com/docs/themes/)

To change theme, search for jekyll theme on [RubyGems](https://rubygems.org/search?utf8=%E2%9C%93&query=jekyll-theme) to find other gem-based themes.

Add the theme to your site’s Gemfile:

```bash
gem "jekyll-theme-tactile"
````

```bash
$ bundle install

# Check proper install.
$ bundle show jekyll-theme-tactile
```

Add the following to your site’s \_config.yml to activate the theme:

```yaml
theme: jekyll-theme-tactile
```

Build your site:

```bash
bundle exec jekyll serve
```

You can find out info about customizing your Jekyll theme, as well as basic Jekyll usage documentation at [jekyllrb.com](https://jekyllrb.com/)

You can find the source code for the Jekyll minima theme at:
[minima](https://github.com/jekyll/minima)

______________________________________________________________________

You’ll find this post in your `_posts` directory. Go ahead and edit it and re-build the site to see your changes. You can rebuild the site in many different ways, but the most common way is to run `jekyll serve`, which launches a web server and auto-regenerates your site when a file is updated.

To add new posts, simply add a file in the `_posts` directory that follows the convention `YYYY-MM-DD-name-of-post.ext` and includes the necessary front matter. Take a look at the source for this post to get an idea about how it works.

Jekyll also offers powerful support for code snippets:

```md
{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
## => prints 'Hi, Tom' to STDOUT.
{% endhighlight %}
```

## Modern Compatibility

Ensure you have a recent version of Ruby (3.x) installed via `rbenv` or `rvm`.

```shell
## Install Jekyll and Bundler
gem install jekyll bundler

## Create a new site
jekyll new myblog
cd myblog

## Serve locally
bundle exec jekyll serve
```

GitHub Pages uses specific versions of Jekyll and its plugins. Reference the [GitHub Pages Dependency versions](https://pages.github.com/versions/) to align your `Gemfile`.

[jekyll-docs]: https://jekyllrb.com/docs/home
[jekyll-gh]: https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/
