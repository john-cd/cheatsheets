---
title: Jekyll
category: documentation
tags: static-site-generator ruby github-pages
---

# Jekyll

Jekyll is a static site generator powered by Ruby. It is natively supported by GitHub Pages.

## Modern Compatibility

Ensure you have a recent version of Ruby (3.x) installed via `rbenv` or `rvm`.

```shell
# Install Jekyll and Bundler
gem install jekyll bundler

# Create a new site
jekyll new myblog
cd myblog

# Serve locally
bundle exec jekyll serve
```

GitHub Pages uses specific versions of Jekyll and its plugins. Reference the [GitHub Pages Dependency versions](https://pages.github.com/versions/) to align your `Gemfile`.
