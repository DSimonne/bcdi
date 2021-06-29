# Contributing

Hi there! We're thrilled that you'd like to contribute to this project. Your help is 
essential for keeping it great.

Please note that this project is released with a [Contributor Code of Conduct]
[code-of-conduct]. By participating in this project you agree to abide by its terms.

## Never push modifications directly to do master branch, even if you have permissions

- Several continuous integration workflows are configured for the repository, they 
  need to pass successfully before considering merging modifications into the master 
  branch.

## Submitting a pull request

1. [Fork][fork] and clone the repository
1. Install the dependencies
1. Make sure the tests pass on your machine
1. Create a new branch: `git checkout -b my-branch-name`
1. Make your change, add tests, and make sure the tests still pass
1. Push to your fork and [submit a pull request][pr]
1. Pat your self on the back and wait for your pull request to be reviewed and merged.

Here are a few things you can do that will increase the likelihood of your pull 
request being accepted:

- Follow the [style guide][style] which is using PEP 8 reommandations.
- Run [black] [blck] against your code.
- Write and update tests.
- Keep your change as focused as possible. If there are multiple changes you would 
  like to make that are not dependent upon each other, consider submitting them as 
  separate pull requests.
- Write a [good commit message][gcm].

Work in Progress pull requests are also welcome to get feedback early on, or if 
there is something that blocked you.

## Resources

- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [Using Pull Requests](https://help.github.com/articles/about-pull-requests/)
- [GitHub Help](https://help.github.com)

[fork]: https://github.com/carnisj/bcdi/fork
[pr]: https://docs.github.com/en/github/collaborating-with-pull-requests/
[style]: https://www.python.org/dev/peps/pep-0008/
[blck]: https://pypi.org/project/black/
[gcm]: http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
[code-of-conduct]: CODE_OF_CONDUCT.md