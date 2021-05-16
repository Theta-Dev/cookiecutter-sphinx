#############################################################################################################
Cookiecutter Sphinx template
#############################################################################################################

Setup
#####

Install the following packages via pip:

cookiecutter
  Cookiecutter is a python application that can create project directories from premade templates dubbed
  "Cookiecutters".

tox
  Python venv manager. Used to build yor docs with one command.

Generate your documentation directory
======================================
Open a command line in the folder you want your documentation directory to be.
Then create your documentation with this command (change path of template if necessary).

.. code-block:: sh

    cookiecutter gh:Theta-Dev/cookiecutter-sphinx

Cookiecutter asks you to enter all the information about your project (Author, Title, Subtitle) and
then generates your documentation in the specified folder (``docs`` by default).

Write the docs
===============
After you have set up Sphinx, you can write your documentation as a set of .rst files that you put in the
main directory.

Dont forget to insert the filenames into the table of contents located in the ``index.rst`` file.
Otherwise your documentation wont show up on the final page.

You can write your documentation with any text editor you like. If you're using VSCode there is
an extension available (``lextudio.restructuredtext``) that enables syntax highlighting
and autocompletion.

Build the docs
===============
Once you have written your documentation, you have to build it. Sphinx will take your RST files,
parse them and generate production-ready output data in html and docx format.

To to this, simply run the ``tox`` command from your documentation directory.
Your build documentation will be located in the ``_build/<TYPE>`` folder.

Auto-build
===========
If you want to preview your documentation while you're working on it, you can use the autobuild
feature. Run ``tox -e live`` file and wait a few seconds. It will open your browser
showing the documentation in html format. When it detects changes in your source files, it
automatically rebuilds the html file and refreshes the browser window.

This is exceptionally useful if you are using a text editor like VSCode
which automatically saves your files (click :guilabel:`File` > :guilabel:`Auto Save` to enable).
